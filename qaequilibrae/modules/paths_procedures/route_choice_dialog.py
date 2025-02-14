import logging
import os
import sys

import numpy as np
import qgis
from aequilibrae.paths.route_choice import RouteChoice
from aequilibrae.paths import SubAreaAnalysis
from aequilibrae.project.database_connection import database_connection
from aequilibrae.utils.db_utils import read_and_close
from qgis.PyQt import uic
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QTableWidgetItem, QWidget, QHBoxLayout, QCheckBox, QDialog

from qaequilibrae.modules.matrix_procedures import list_matrices
from qaequilibrae.modules.paths_procedures.execute_single_dialog import VisualizeSingle
from qaequilibrae.modules.paths_procedures.route_choice_plot import plot_results

sys.modules["qgsmaplayercombobox"] = qgis.gui
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), "forms/ui_route_choice.ui"))
logger = logging.getLogger("AequilibraEGUI")


class RouteChoiceDialog(QDialog, FORM_CLASS):
    def __init__(self, qgis_project):
        QDialog.__init__(self)
        self.iface = qgis_project.iface
        self.project = qgis_project.project
        self.qgis_project = qgis_project
        self.matrices = self.project.matrices
        self.setupUi(self)
        self.error = None
        self.matrix = None
        self.cost_function = ""
        self.utility = []

        self.all_modes = {}
        self._pairs = []
        self.link_layer = qgis_project.layers["links"][0]
        self.zones_layer = qgis_project.layers["zones"][0]
        self.zones = self.project.zoning.all_zones()
        self.__kwargs = {}

        self.__populate_project_info()

        self.__project_nodes = self.project.network.nodes.data.node_id.tolist()
        self.proj_matrices = list_matrices(self.project.matrices.fldr)

        self.cob_algo.addItems(["BFSLE", "Link Penalization"])

        self.cob_matrices.currentTextChanged.connect(self.set_show_matrices)
        self.chb_use_all_matrices.toggled.connect(self.set_show_matrices)
        self.but_add_to_cost.clicked.connect(self.add_cost_function)
        self.but_clear_cost.clicked.connect(self.clear_cost_function)
        self.but_perform_assig.clicked.connect(lambda: self.assign_and_save(arg="assign"))
        self.but_build_and_save.clicked.connect(lambda: self.assign_and_save(arg="build"))
        self.but_visualize.clicked.connect(self.execute_single)
        self.chb_set_sub_area.toggled.connect(self.set_sub_area_use)
        self.rdo_selected_zones.toggled.connect(self.set_show_zones)
        self.rdo_zones_from_layer.toggled.connect(self.use_selected_zones)

        self.list_matrices()
        self.set_show_matrices()
        self.set_sub_area_use()

    def __populate_project_info(self):
        with read_and_close(database_connection("network")) as conn:
            res = conn.execute("""select mode_name, mode_id from modes""")

            modes = []
            for x in res.fetchall():
                modes.append(f"{x[0]} ({x[1]})")
                self.all_modes[f"{x[0]} ({x[1]})"] = x[1]

        self.cob_mode.clear()
        for m in modes:
            self.cob_mode.addItem(m)

        flds = self.project.network.skimmable_fields()
        self.cob_net_field.clear()
        self.cob_net_field.addItems(flds)

    def list_matrices(self):
        for _, rec in self.proj_matrices.iterrows():
            if len(rec.WARNINGS) == 0:
                self.cob_matrices.addItem(rec["name"])

    def set_matrix(self):
        if self.cob_matrices.currentIndex() < 0:
            self.matrix = None
            return

        if self.cob_matrices.currentText() in self.qgis_project.matrices:
            self.matrix = self.qgis_project.matrices[self.cob_matrices.currentText()]
            return
        self.matrix = self.qgis_project.project.matrices.get_matrix(self.cob_matrices.currentText())

    def set_show_matrices(self):
        self.tbl_array_cores.setVisible(not self.chb_use_all_matrices.isChecked())
        self.tbl_array_cores.clear()

        self.set_matrix()

        self.tbl_array_cores.setColumnWidth(0, 200)
        self.tbl_array_cores.setColumnWidth(1, 80)
        self.tbl_array_cores.setHorizontalHeaderLabels(["Matrix", "Use?"])

        if self.matrix is not None:
            table = self.tbl_array_cores
            table.setRowCount(self.matrix.cores)
            for i, mat in enumerate(self.matrix.names):
                item1 = QTableWidgetItem(mat)
                item1.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                table.setItem(i, 0, item1)

                chb1 = QCheckBox()
                chb1.setChecked(True)
                chb1.setEnabled(True)
                table.setCellWidget(i, 1, self.centers_item(chb1))

    def centers_item(self, item):
        cell_widget = QWidget()
        lay_out = QHBoxLayout(cell_widget)
        lay_out.addWidget(item)
        lay_out.setAlignment(Qt.AlignCenter)
        lay_out.setContentsMargins(0, 0, 0, 0)
        cell_widget.setLayout(lay_out)
        return cell_widget

    def __check_matrices(self):
        self.set_matrix()
        if self.matrix is None:
            return False

        if self.chb_use_all_matrices.isChecked():
            matrix_cores_to_use = self.matrix.names
        else:
            matrix_cores_to_use = []
            for i, mat in enumerate(self.matrix.names):
                if self.tbl_array_cores.cellWidget(i, 1).findChildren(QCheckBox)[0].isChecked():
                    matrix_cores_to_use.append(mat)

        if len(matrix_cores_to_use) > 0:
            self.matrix.computational_view(matrix_cores_to_use)
        else:
            return False

        return True

    def add_cost_function(self):
        params = self.ln_parameter.text()
        valid_params = self.__check_parameter_value(params)

        if not valid_params:
            qgis.utils.iface.messageBar().pushMessage(self.tr("Input error"), self.error, level=1, duration=5)
            return

        if len(self.cost_function) > 0 and self.parameter >= 0:
            self.cost_function += " + "
        elif len(self.cost_function) > 0 and self.parameter < 0:
            params = params.replace("-", " - ")

        self.cost_function += f"{params} * {self.cob_net_field.currentText()}"
        self.txt_cost_func.setText(self.cost_function)

        self.utility.extend([(self.parameter, self.cob_net_field.currentText())])

    def clear_cost_function(self):
        self.txt_cost_func.clear()

        self.cost_function = ""

    def exit_procedure(self):
        self.close()

    def __check_parameter_value(self, par):
        # parameter cannot be null
        if len(par) == 0:
            self.error = "Check parameter value."
            return False

        # parameter needs to be numeric
        if not par.replace(".", "").replace("-", "").isdigit():
            self.error = "Wrong value in parameter."
            return False

        self.parameter = float(par)
        return True

    def graph_config(self):
        mode = self.cob_mode.currentText()
        mode_id = self.all_modes[mode]
        if mode_id not in self.project.network.graphs:
            self.project.network.build_graphs(modes=[mode_id])

        self.graph = self.project.network.graphs[mode_id]

        field = np.zeros((1, self.graph.network.shape[0]))
        for idx, (par, col) in enumerate(self.utility):
            field += par * self.graph.network[col].array

        self.graph.network = self.graph.network.assign(utility=0)
        self.graph.network["utility"] = field.reshape(self.graph.network.shape[0], 1)

        if self.chb_chosen_links.isChecked():
            self.graph = self.project.network.graphs.pop(mode_id)
            idx = self.link_layer.dataProvider().fieldNameIndex("link_id")
            remove = [feat.attributes()[idx] for feat in self.link_layer.selectedFeatures()]
            self.graph.exclude_links(remove)

        self.graph.set_blocked_centroid_flows(self.chb_check_centroids.isChecked())

    def __get_parameters(self):
        self.__check_route_choice_params()

        if self.error:
            qgis.utils.iface.messageBar().pushMessage(self.tr("Input error"), self.error, level=1, duration=5)
            return

        self.__kwargs = {
            "max_routes": self.num_routes,
            "max_depth": self.rc_depth,
            "penalty": float(self.penalty.text()),
            "cutoff_prob": self.cutoff,
            "beta": float(self.ln_psl.text()),
        }

        if self.cob_algo.currentText().lower() == "bfsle":
            self.__kwargs["algorithm"] = "bflse"
            self.__kwargs["store_results"] = True
        else:
            self.__kwargs["algorithm"] = "lp"
            self.__kwargs["store_results"] = False

    def __check_route_choice_params(self):
        # parameter needs to be numeric
        if not self.max_routes.text().isdigit():
            self.error = "Max. routes needs to be a numeric integer value"
            return False

        if not self.max_depth.text().isdigit():
            self.error = "Max. depth needs to be a numeric integer value"
            return False

        # Check cutoff
        if not self.ln_cutoff.text().replace(".", "").isdigit():
            self.error = "Probability cutoff needs to be a float number"
            return False

        self.cutoff = float(self.ln_cutoff.text())
        if self.cutoff < 0 or self.cutoff > 1:
            self.error = "Probability cutoff assumes values between 0 and 1"
            return False

        # TODO: Check penalty

        self.num_routes = int(self.max_routes.text())
        self.rc_depth = int(self.max_depth.text())

    def execute_single(self):
        self.from_node = self.__validate_node_id(self.node_from.text())
        self.to_node = self.__validate_node_id(self.node_to.text())

        demand = self.ln_demand.text()
        if not demand.replace(".", "").isdigit():
            self.error = "Wrong input value for demand"

        if self.error:
            qgis.utils.iface.messageBar().pushMessage(self.tr("Input error"), self.error, level=1, duration=5)
            return

        nodes_of_interest = np.array([self.from_node, self.to_node], dtype=np.int64)

        self.graph_config()
        self.graph.prepare_graph(nodes_of_interest)
        self.graph.set_graph("utility")

        rc = self.set_route_choice()

        _ = rc.execute_single(self.from_node, self.to_node, float(demand))

        plot_results(rc.get_results().to_pandas(), self.from_node, self.to_node, self.link_layer)

        self.dlg2 = VisualizeSingle(
            qgis.utils.iface.mainWindow(),
            self.graph,
            self.__kwargs,
            float(self.ln_demand.text()),
            self.link_layer,
        )
        self.dlg2.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.dlg2.show()
        self.dlg2.open()
        # see note in https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QDialog.html#PySide2.QtWidgets.PySide2.QtWidgets.QDialog.exec_

        self.exit_procedure()

    def __validate_node_id(self, node_id: str):
        # Check if we have only numbers
        if not node_id.isdigit():
            self.error = self.tr("Wrong input value for node ID")
            return

        # Check if node_id exists
        node_id = int(node_id)
        if node_id not in self.__project_nodes:
            self.error = self.tr("Node ID doesn't exist in project")
            return

        return node_id

    def assign_and_save(self, arg):
        valid_params = self.__check_matrices()
        if not valid_params:
            self.error = "Check matrices inputs"
            qgis.utils.iface.messageBar().pushMessage(self.tr("Input error"), self.error, level=1, duration=5)
            return

        if not self.__kwargs:
            self.__get_parameters()

        self.graph_config()
        self.graph.prepare_graph(self.graph.centroids)
        self.graph.set_graph("utility")

        if self.chb_set_sub_area.isChecked():
            demand = self.set_sub_area()

            # Rebuild graph for external ODs
            new_centroids = np.unique(demand.reset_index()[["origin id", "destination id"]].to_numpy().reshape(-1))
            self.graph.prepare_graph(new_centroids)
            self.graph.set_graph("utility")

        rc = RouteChoice(self.graph)
        rc.add_demand(demand)  # replace variable
        rc.set_choice_set_generation(**self.__kwargs)
        rc.prepare()

        if arg == "build":
            rc.set_save_routes(self.project.project_base_path)

        assig = True if arg == "assign" else False
        rc.execute(perform_assignment=assig)

        if self.chb_save_choice_set.isChecked() and assig:
            name = "route_choice_for_subarea" if self.chb_set_sub_area.isChecked() else "route_choice"
            rc.save_link_flows(name)

        self.exit_procedure()

    def set_sub_area(self):
        # Sub-area prep
        zones_of_interest = self.__get_zones_of_interest()  # Select zones of interest
        print(zones_of_interest)
        zones = self.project.zoning.data.set_index("zone_id")
        zones = zones.loc[zones_of_interest]

        self.__get_parameters()

        sub_area = SubAreaAnalysis(self.graph, zones, self.matrix)
        sub_area.rc.set_choice_set_generation(**self.__kwargs)
        sub_area.rc.execute(perform_assignment=True)

        return sub_area.post_process()

    def set_sub_area_use(self):
        for item in [self.rdo_selected_zones, self.rdo_zones_from_layer, self.tbl_zones]:
            item.setEnabled(self.chb_set_sub_area.isChecked())

    def __get_zones_of_interest(self):
        if self.error:
            qgis.utils.iface.messageBar().pushMessage(self.tr("Input error"), self.error, level=1, duration=5)
            return

        if self.rdo_zones_from_layer.isChecked():
            zones_to_use = [feat["zone_id"] for feat in self.zones_layer.selectedFeatures()]
        elif self.rdo_zones_from_layer.isChecked():
            zones_to_use = []
            for i, zone in enumerate(self.zones.keys()):
                if self.tbl_array_cores.cellWidget(i, 1).findChildren(QCheckBox)[0].isChecked():
                    zones_to_use.append(zone)

        return zones_to_use

    def set_show_zones(self):
        self.tbl_zones.setEnabled(self.rdo_selected_zones.isChecked())
        self.tbl_zones.clear()

        self.tbl_zones.setColumnWidth(0, 100)
        self.tbl_zones.setColumnWidth(1, 60)
        self.tbl_zones.setHorizontalHeaderLabels(["Zone ID", "Use?"])

        if self.zones is not None:
            table = self.tbl_zones
            table.setRowCount(len(self.zones))
            for i, zone in enumerate(self.zones.keys()):
                item1 = QTableWidgetItem(str(zone))
                item1.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                table.setItem(i, 0, item1)

                chb1 = QCheckBox()
                chb1.setChecked(False)
                chb1.setEnabled(True)
                table.setCellWidget(i, 1, self.centers_item(chb1))

    def use_selected_zones(self):
        self.tbl_zones.setEnabled(not self.rdo_zones_from_layer.isChecked())
        self.tbl_zones.clear()

        self.tbl_zones.setHorizontalHeaderLabels(["Zone ID", "Use?"])

        if self.zones_layer.selectedFeatureCount() == 0:
            self.error == "Select at least one zone to proceed with sub-area analysis"
