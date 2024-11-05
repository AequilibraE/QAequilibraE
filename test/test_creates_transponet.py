import pytest
from uuid import uuid4
from os.path import join
from shutil import copytree

from qgis.core import QgsProject, QgsVectorLayer
from qgis.PyQt import QtWidgets
from qaequilibrae.modules.project_procedures.creates_transponet_dialog import CreatesTranspoNetDialog
from qaequilibrae.modules.project_procedures.creates_transponet_procedure import CreatesTranspoNetProcedure


def load_test_layer(path):
    for file_name in ["link", "node"]:
        csv_path = f"/{path}/{file_name}.csv"

        if file_name == "link":
            uri = "file://{}?delimiter=,&crs=epsg:4326&wktField={}".format(csv_path, "geometry")
        else:
            uri = "file://{}?delimiter=,&crs=epsg:4326&xField={}&yField={}".format(csv_path, "x", "y")

        layer = QgsVectorLayer(uri, file_name, "delimitedtext")

        if not layer.isValid():
            print(f"{file_name} layer failed to load!")
        else:
            QgsProject.instance().addMapLayer(layer)


def test_without_nodes(ae, tmp_path, qtbot, timeoutDetector):
    # path = join(tmp_path, uuid4().hex)
    folder = "/workspaces/drive_d/.OuterLoop/.QAequilibrae/.move to 1.1/debugging"
    path = join(folder, uuid4().hex)
    copytree("test/data/NetworkPreparation", path)

    load_test_layer(path)

    dialog = CreatesTranspoNetDialog(ae)
    dialog.project_destination.setText(path)

    columns = ["link_id", "a_node", "b_node", "direction", "distance", "modes", "link_type"]

    child = dialog.findChildren(QtWidgets.QComboBox)
    links_chd = []
    for chd in child:
        if chd.count() == 18:
            links_chd.append(chd)
    
    for idx, chd in enumerate(links_chd):
        print(idx, chd)
        # chd.setCurrentIndex(chd.findText(columns[idx]))
    # for idx, chd in enumerate(links_chd):
    #     chd.setCurrentIndex(columns[idx])
    #     if idx > 6:
    #         break
            
    # child = dialog.findChild(QtWidgets.QTableWidget, "table_link_fields")
    # child.item(1, 2).setSelected(True)
    # for idx in range(child.rowCount()):
    #     for col in range(child.columnCount()):
    #         print(idx, col, child.item(idx, col))
    #     print(idx, child.item(idx, 0).text())
    # print(child.rowCount(), child.columnCount())

    # all_layers = [layer.name() for layer in QgsProject.instance().mapLayers().values()]
    # print(all_layers)

    # path_links = qtbot.screenshot(dialog.tabs_list_widget.widget(0), suffix="tab_links")
    # path_nodes = qtbot.screenshot(dialog.tabs_list_widget.widget(1), suffix="tab_nodes")
    # print(path_links)

    QgsProject.instance().removeAllMapLayers()