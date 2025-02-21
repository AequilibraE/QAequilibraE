import os
import sys
from dataclasses import dataclass
from functools import partial
from random import randint
from typing import Tuple, Literal, Dict, Union

import qgis
from PyQt5.QtGui import QColor
from qgis.PyQt import uic
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QPushButton, QTableWidgetItem, QTableWidget
from qgis.PyQt.QtWidgets import QToolButton, QHBoxLayout, QWidget, QDialog
from qgis._core import QgsLineSymbol, QgsVectorLayer, QgsSymbol, QgsProject
from qgis._core import QgsMapLayerProxyModel, QgsSimpleLineSymbolLayer, QgsExpressionContextUtils
from qgis._core import QgsSingleSymbolRenderer, QgsRuleBasedRenderer, QgsStyle

from qaequilibrae.modules.common_tools import get_parameter_chain
from .set_color_ramps_dialog import LoadColorRampSelector

sys.modules["qgsfieldcombobox"] = qgis.gui
sys.modules["qgscolorbutton"] = qgis.gui
sys.modules["qgsmaplayercombobox"] = qgis.gui
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), "forms/ui_bandwidths.ui"))


@dataclass
class BandAttributes:
    """Record type to hold stack bandwidth styling data."""

    label: str
    color: Union[QColor, Dict]
    color_ramp_style: bool
    # direction specific fields
    fieldnames: Tuple[str, str]
    direction: Tuple[Literal["ab", "ba"], Literal["ab", "ba"]]


class CreateBandwidthsDialog(QDialog, FORM_CLASS):
    def __init__(self, qgis_project):
        QDialog.__init__(self)
        self.iface = qgis_project.iface
        self.setupUi(self)

        self.tot_bands = 0

        self.scale = {"width": 10, "spacing": 0.001, "max_flow": -1}

        self.band_size = 10.0
        self.space_size = 0.01
        self.layer = None
        self.ramps = None
        self.drive_side = get_parameter_chain(["system", "driving side"])

        # layers and fields for adding skims
        self.mMapLayerComboBox.layerChanged.connect(self.add_fields_to_cboxes)
        self.mMapLayerComboBox.setFilters(QgsMapLayerProxyModel.LineLayer)
        self.mMapLayerComboBox.setLayer(self.iface.activeLayer())

        self.ab_FieldComboBox.currentIndexChanged.connect(partial(self.choose_a_field, "AB"))
        self.ba_FieldComboBox.currentIndexChanged.connect(partial(self.choose_a_field, "BA"))

        # List of bands
        self.bands_list.setColumnWidth(0, 210)
        self.bands_list.setColumnWidth(1, 210)
        self.bands_list.setColumnWidth(2, 110)
        self.bands_list.setColumnWidth(3, 110)

        # loading ramps
        self.but_load_ramp.setVisible(False)
        self.txt_ramp.setVisible(False)

        self.but_add_band.clicked.connect(self.add_to_bands_list)
        self.bands_list.setEditTriggers(QTableWidget.NoEditTriggers)

        self.rdo_color.toggled.connect(self.color_origins)

        self.rdo_ramp.toggled.connect(self.color_origins)
        self.but_run.clicked.connect(self.add_bands_to_map)
        self.but_run.setEnabled(False)

        self.but_load_ramp.clicked.connect(self.load_ramp_action)

        self.add_fields_to_cboxes()
        self.random_rgb()
        self.set_initial_value_if_available()
        self.but_load_ramp.setEnabled(False)

    def color_origins(self):
        self.mColorButton.setVisible(self.rdo_color.isChecked())
        self.but_load_ramp.setVisible(self.rdo_ramp.isChecked())
        self.txt_ramp.setVisible(self.rdo_ramp.isChecked())
        self.but_load_ramp.setEnabled(self.rdo_ramp.isChecked())

    def choose_a_field(self, modified):
        i, j = "AB", "BA"
        if self.layer is None:
            return

        if modified == i:
            text = self.ab_FieldComboBox.currentText().upper()
            if i in text:
                text = text.replace(i, j)
                index = self.ba_FieldComboBox.findText(text, Qt.MatchFixedString)
                if index >= 0:
                    self.ba_FieldComboBox.setCurrentIndex(index)

        if modified == j:
            text = self.ba_FieldComboBox.currentText().upper()
            if j in text:
                text = text.replace(j, i)
                index = self.ab_FieldComboBox.findText(text, Qt.MatchFixedString)
                if index >= 0:
                    self.ab_FieldComboBox.setCurrentIndex(index)

    def set_initial_value_if_available(self):
        all_items = [self.ab_FieldComboBox.itemText(i) for i in range(self.ab_FieldComboBox.count())]

        for i in all_items:
            if "AB" in i:
                index = self.ab_FieldComboBox.findText(i, Qt.MatchFixedString)
                if index >= 0:
                    self.ab_FieldComboBox.setCurrentIndex(index)
                break

    def add_fields_to_cboxes(self):
        self.layer = self.mMapLayerComboBox.currentLayer()
        if self.layer is not None:
            self.but_load_ramp.setEnabled(True)
            self.ab_FieldComboBox.setLayer(self.layer)
            self.ba_FieldComboBox.setLayer(self.layer)
        else:
            self.but_load_ramp.setEnabled(False)

    def add_to_bands_list(self):
        if self.ab_FieldComboBox.currentIndex() >= 0 and self.ba_FieldComboBox.currentIndex() >= 0:
            self.bands_list.setRowCount(self.tot_bands + 1)

            # Field names
            self.bands_list.setItem(self.tot_bands, 0, QTableWidgetItem(self.ab_FieldComboBox.currentText()))
            self.bands_list.setItem(self.tot_bands, 1, QTableWidgetItem(self.ba_FieldComboBox.currentText()))

            # color
            if self.ramps is None:
                self.bands_list.setItem(self.tot_bands, 2, QTableWidgetItem(""))
                self.bands_list.item(self.tot_bands, 2).setBackground(self.mColorButton.color())
            else:
                self.bands_list.setItem(self.tot_bands, 2, QTableWidgetItem(str(self.ramps)))
                self.ramps = None
                self.rdo_color.setChecked(True)

            # Up-Down buttons

            button_up = QToolButton()
            button_up.setArrowType(Qt.UpArrow)
            button_up.clicked.connect(self.click_button_inside_the_list)

            button_down = QToolButton()
            button_down.setArrowType(Qt.DownArrow)
            button_down.clicked.connect(self.click_button_inside_the_list)

            del_button = QPushButton("X")
            del_button.clicked.connect(self.click_button_inside_the_list)

            layout = QHBoxLayout()
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)
            layout.addWidget(button_down)
            layout.addWidget(button_up)
            layout.addWidget(del_button)

            cellWidget = QWidget()
            cellWidget.setLayout(layout)
            self.bands_list.setCellWidget(self.tot_bands, 3, cellWidget)

            # incrementing and moving on
            self.tot_bands += 1
            self.but_run.setEnabled(True)
            self.random_rgb()

    def click_button_inside_the_list(self):
        button = self.sender()
        parent = button.parent()

        for i in range(self.tot_bands):
            if self.bands_list.cellWidget(i, 3) is parent:
                row = i
                break

        column = 2
        for i, q in enumerate(button.parentWidget().findChildren(QToolButton)):
            if q is button:
                column = i

        # if we clicked the "down button"
        if column == 0 and row < self.tot_bands - 1:
            low_cl = self.bands_list.item(row + 1, 2).background()
            low_ab = self.bands_list.item(row + 1, 0).text()
            low_ba = self.bands_list.item(row + 1, 1).text()

            top_cl = self.bands_list.item(row, 2).background()
            top_ab = self.bands_list.item(row, 0).text()
            top_ba = self.bands_list.item(row, 1).text()

            self.bands_list.setItem(row, 0, QTableWidgetItem(low_ab))
            self.bands_list.setItem(row, 1, QTableWidgetItem(low_ba))
            self.bands_list.item(row, 2).setBackground(low_cl)

            self.bands_list.setItem(row + 1, 0, QTableWidgetItem(top_ab))
            self.bands_list.setItem(row + 1, 1, QTableWidgetItem(top_ba))
            self.bands_list.item(row + 1, 2).setBackground(top_cl)

        # if we clicked the "up button"
        elif column == 1 and row > 0:
            low_cl = self.bands_list.item(row, 2).background()
            low_ab = self.bands_list.item(row, 0).text()
            low_ba = self.bands_list.item(row, 1).text()

            top_cl = self.bands_list.item(row - 1, 2).background()
            top_ab = self.bands_list.item(row - 1, 0).text()
            top_ba = self.bands_list.item(row - 1, 1).text()

            self.bands_list.setItem(row, 0, QTableWidgetItem(top_ab))
            self.bands_list.setItem(row, 1, QTableWidgetItem(top_ba))
            self.bands_list.item(row, 2).setBackground(top_cl)

            self.bands_list.setItem(row - 1, 0, QTableWidgetItem(low_ab))
            self.bands_list.setItem(row - 1, 1, QTableWidgetItem(low_ba))
            self.bands_list.item(row - 1, 2).setBackground(low_cl)

        # if we clicked the "remove button"
        elif column == 2:
            self.bands_list.removeRow(row)
            self.tot_bands -= 1

            if self.tot_bands == 0:
                self.but_run.setEnabled(False)

    def random_rgb(self):
        rgb = []
        for i in range(3):
            rgb.append(randint(0, 255))
        a = QColor()
        a.setRgb(rgb[0], rgb[1], rgb[2])
        self.mColorButton.setColor(a)

    def load_ramp_action(self):
        if self.layer is not None:
            self.ramps = None
            dlg2 = LoadColorRampSelector(self.iface, self.layer)
            dlg2.show()
            dlg2.exec_()
            if dlg2.results is not None:
                self.ramps = dlg2.results
                self.txt_ramp.setText(str(self.ramps))

    def add_bands_to_map(self):
        for item in [
            self.but_run,
            self.mMapLayerComboBox,
            self.but_add_band,
            self.rdo_color,
            self.rdo_ramp,
        ]:
            item.setEnabled(False)

        band_size = self.scale["width"]  # TODO will changing this break something, seems like it should be a float/int
        space_size = self.scale["spacing"]
        max_value = self.scale["max_flow"]
        # define the side of the plotting based on the side of the road the system has defined
        ab = -1
        if self.drive_side == "right":
            ab = 1
        ba = -ab

        # Create new simple stype
        symbol = QgsLineSymbol.createSimple({"name": "square", "color": "red"})
        self.layer.setRenderer(QgsSingleSymbolRenderer(symbol))
        bands = []  # TODO consolidate new bands with old bands list?
        bands_ab = []
        bands_ba = []
        # go through all the fields that will be used to find the maximum value. This will be used
        # to limit the size of bandwidth for all layers of bands
        values = []
        all_fields = [x.name() for x in self.layer.fields()]
        for i in range(self.tot_bands):
            for j in range(2):
                if max_value < 0:
                    field = self.bands_list.item(i, j).text()
                    idx = all_fields.index(field)
                    values.append(self.layer.maximumValue(idx))

                # we also build a list of bands to construct
                # The function "(2 * j -1) * ba"  maps the index j {1,2} and the direction to the side of the
                # link the band needs to be. Try it out. it works!!
                # bands.append((field, (2 * j -1) * ba, self.bands_list.item(i, 2).background()))
            if len(self.bands_list.item(i, 2).text()) == 0:
                color_ramp_style = False
                cl = self.bands_list.item(i, 2).background().color()
            else:
                color_ramp_style = True
                cl = eval(self.bands_list.item(i, 2).text())
            text_ab = self.bands_list.item(i, 0).text()
            text_ba = self.bands_list.item(i, 1).text()
            bands_ab.append((text_ab, ab, cl, "ab"))
            bands_ba.append((text_ba, ba, cl, "ba"))
            if text_ab.upper().endswith("_AB") and text_ba.upper().endswith("_BA"):
                # remove directed suffix
                label = text_ab[:-3]
            else:
                label = f"{text_ab} - {text_ba}"
            bands.append(BandAttributes(label, cl, color_ramp_style, (text_ab, text_ba), ("ab", "ba")))

        if max_value < 0:
            values = [x for x in values if x is not None] + [0]
            max_value = max(values)

        QgsExpressionContextUtils.setProjectVariable(QgsProject.instance(), "aeq_band_max_value", max_value)
        QgsExpressionContextUtils.setProjectVariable(QgsProject.instance(), "aeq_band_spacer", float(space_size))
        QgsExpressionContextUtils.setProjectVariable(QgsProject.instance(), "aeq_band_width", band_size)
        max_value_aeq_var = "@aeq_band_max_value"
        space_size_aeq_var = "@aeq_band_spacer"
        band_size_aeq_var = "@aeq_band_width"

        for s in [bands_ab, bands_ba]:
            acc_offset = "0"
            for field, side, clr, direc in s:
                symbol_layer = QgsSimpleLineSymbolLayer.create({})
                props = symbol_layer.properties()
                width = (
                    '(coalesce(scale_linear("'
                    + field
                    + '", 0, '
                    + max_value_aeq_var
                    + ", 0, "
                    + band_size_aeq_var
                    + "), 0))"
                )
                props["width_dd_expression"] = width

                xpr = (
                    acc_offset
                    + "+"
                    + str(side)
                    + ' * (coalesce(scale_linear("'
                    + field
                    + '", 0, '
                    + str(max_value_aeq_var)
                    + ", 0, "
                    + band_size_aeq_var
                    + "), 0)/2 + "
                    + space_size_aeq_var
                    + ")"
                )
                props["offset_dd_expression"] = xpr
                props["line_style_expression"] = 'if (coalesce("' + field + '",0) = 0,' + "'no', 'solid')"

                if isinstance(clr, dict):
                    if direc == "ab":
                        xpr = (
                            "ramp_color('"
                            + clr["color ab"]
                            + "',scale_linear("
                            + '"'
                            + clr["ramp ab"]
                            + '", '
                            + str(clr["min ab"])
                            + ", "
                            + str(clr["max ab"])
                            + ", 0, 1))"
                        )
                        props["color_dd_expression"] = xpr

                    else:
                        xpr = (
                            "ramp_color('"
                            + clr["color ba"]
                            + "',scale_linear("
                            + '"'
                            + clr["ramp ba"]
                            + '", '
                            + str(clr["min ba"])
                            + ", "
                            + str(clr["max ba"])
                            + ", 0, 1))"
                        )
                        props["color_dd_expression"] = xpr
                else:
                    xpr = (
                        str(clr.getRgb()[0])
                        + ","
                        + str(clr.getRgb()[1])
                        + ","
                        + str(clr.getRgb()[2])
                        + ","
                        + str(clr.getRgb()[3])
                    )
                    props["line_color"] = xpr

                symbol_layer = QgsSimpleLineSymbolLayer.create(props)
                self.layer.renderer().symbol().appendSymbolLayer(symbol_layer)

                acc_offset = acc_offset + " + " + str(side) + "*(" + width + "+" + space_size_aeq_var + ")"

        self.build_width_legend(self.layer.name(), max_layer_value=max_value, max_band_value=band_size)
        self.build_color_legend(self.layer.name(), bands=bands)

        self.layer.renderer().symbol().deleteSymbolLayer(0)
        self.layer.triggerRepaint()
        self.exit_procedure()

    def exit_procedure(self):
        self.close()

    @classmethod
    def delete_existing_layers_with_same_name(cls, layer_name: str) -> None:
        layers_with_name = QgsProject.instance().mapLayersByName(layer_name)
        if len(layers_with_name) > 0:
            # delete existing layers with this name (i.e. previous legends)
            # TODO small chance this deletes user data, should this be behind a default ticked checkbox?
            for layer in layers_with_name:
                QgsProject.instance().removeMapLayer(layer.id())

    @classmethod
    def build_width_legend(cls, layer_name: str, max_layer_value: float, max_band_value: float) -> None:
        """Generate legend entry for stacked bandwidth line thickness."""
        width_legend_name = f"{layer_name} (Width)"
        cls.delete_existing_layers_with_same_name(width_legend_name)

        width_layer = QgsVectorLayer("LineString?crs=epsg:4326", width_legend_name, "memory")
        symbol = QgsSymbol.defaultSymbol(width_layer.geometryType())
        symbol.setWidth(0.001)
        symbol.setColor(QColor("#000000"))
        renderer = QgsRuleBasedRenderer(symbol)
        num_legend_steps = 5
        for interval in range(num_legend_steps + 1):
            pct = interval / num_legend_steps
            rule = renderer.rootRule().children()[0].clone()
            ub = cls.format_legend_number(pct * max_layer_value, max_layer_value)

            if interval > 0:
                pct_prev = (interval - 1) / num_legend_steps
                lb = cls.format_legend_number(pct_prev * max_layer_value + 1, max_layer_value)
                label = f"{lb} - {ub}"
            else:
                label = ub

            rule.setLabel(label)
            rule.symbol().setWidth(pct * max_band_value)  # scale width by @aeq_band_width
            renderer.rootRule().appendChild(rule)

        # remove first child (dummy entry we have been cloning)
        renderer.rootRule().removeChildAt(0)

        width_layer.setRenderer(renderer)
        QgsProject.instance().addMapLayer(width_layer)
        width_layer.triggerRepaint()

    @classmethod
    def build_color_legend(cls, layer_name: str, bands: list[BandAttributes]) -> None:
        """Generate legend layer for stacked bandwidths colored categories."""
        color_legend_name = f"{layer_name} (Color)"
        cls.delete_existing_layers_with_same_name(color_legend_name)

        color_layer = QgsVectorLayer("LineString?crs=epsg:4326", color_legend_name, "memory")

        renderer = QgsRuleBasedRenderer(QgsLineSymbol.createSimple({"width": 2}))
        root_rule = renderer.rootRule()
        rule_to_clone = root_rule.children()[0]
        for band in bands:
            if band.color_ramp_style:
                ref_style = QgsStyle().defaultStyle()

                # Same colormap both directions
                if (band.color["max ba"] == band.color["max ab"]) and (
                    band.color["color ba"] == band.color["color ab"]
                ):
                    color_ramp = ref_style.colorRamp(band.color["color ba"])
                    band_max_value = band.color["max ba"]
                    cls.populate_graduated_rule_rendered(
                        root_rule, rule_to_clone, band.label, color_ramp, band_max_value
                    )

                else:  # split AB BA colormap
                    color_ramp = ref_style.colorRamp(band.color["color ba"])
                    band_max_value = band.color["max ba"]
                    band_label = f"{band.label} BA"
                    cls.populate_graduated_rule_rendered(
                        root_rule, rule_to_clone, band_label, color_ramp, band_max_value
                    )

                    color_ramp = ref_style.colorRamp(band.color["color ab"])
                    band_max_value = band.color["max ab"]
                    band_label = f"{band.label} AB"
                    cls.populate_graduated_rule_rendered(
                        root_rule, rule_to_clone, band_label, color_ramp, band_max_value
                    )

            else:
                rule = rule_to_clone.clone()
                rule.setLabel(band.label)
                rule.symbol().setColor(band.color)
                root_rule.appendChild(rule)

        # remove first child (dummy entry we have been cloning)
        renderer.rootRule().removeChildAt(0)
        color_layer.setRenderer(renderer)
        QgsProject.instance().addMapLayer(color_layer)
        color_layer.triggerRepaint()

    @staticmethod
    def format_legend_number(value: float, max_value: float) -> str:
        return f"{(value):,.2f}" if max_value < 100 else f"{int(value):,}"

    @classmethod
    def populate_graduated_rule_rendered(
        cls,
        parent_rule: QgsRuleBasedRenderer.Rule,
        rule_to_clone: QgsRuleBasedRenderer.Rule,
        band_label: str,
        color_ramp,
        max_val: float,
        num_legend_steps: int = 5,
    ):
        """Populate a new rule tier inside parent_rule displaying color ramp value ranges."""
        band_parent_rule = rule_to_clone.clone()
        band_parent_rule.setLabel(band_label)
        parent_rule.appendChild(band_parent_rule)
        for interval in range(num_legend_steps + 1):
            pct = interval / num_legend_steps
            rule = rule_to_clone.clone()
            ub = cls.format_legend_number(pct * max_val, max_val)

            if interval > 0:
                pct_prev = (interval - 1) / num_legend_steps
                lb = cls.format_legend_number(pct_prev * max_val + 1, max_val)
                label = f"{lb} - {ub}"
            else:
                label = ub

            rule.setLabel(label)
            rule.symbol().setColor(color_ramp.color(pct))
            band_parent_rule.appendChild(rule)
