import logging
import os
import sys

import numpy as np
import qgis
from aequilibrae.paths.route_choice import RouteChoice
from aequilibrae.project.database_connection import database_connection
from aequilibrae.utils.db_utils import read_and_close
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtWidgets import QTableWidgetItem


sys.modules["qgsmaplayercombobox"] = qgis.gui
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), "forms/ui_route_choice.ui"))
logger = logging.getLogger("AequilibraEGUI")


class RouteChoiceDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, qgis_project):
        QtWidgets.QDialog.__init__(self)
        self.iface = qgis_project.iface
        self.project = qgis_project.project
        self.setupUi(self)
        self.error = None

        self.all_modes = {}
        self._pairs = []

        self.__populate_project_info()

        self.__project_nodes = self.project.network.nodes.data.node_id.tolist()

        # We start with `Choice set generation`
        self.tabWidget.removeTab(2)
        self.tabWidget.removeTab(1)

        self.cob_algo.addItems(["BFSLE", "Link Penalization"])

        self.but_add_node.clicked.connect(self.add_nodes)
        self.tbl_selected_nodes.cellDoubleClicked.connect(self.__remove_nodes)
        self.but_add_graph.clicked.connect(self.add_graph)
        self.but_execute.clicked.connect(self.config_route_choice)

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
        self.cob_graph_cost.clear()
        self.cob_graph_cost.addItems(flds)

    def __validate_node_id(self, node_id: str):
        # Check if we have only numbers
        if not node_id.isdigit():
            self.error = self.tr("Wrong input value for node ID")
            qgis.utils.iface.messageBar().pushMessage(self.tr("Input error"), self.error, level=1, duration=5)
            return

        # Check if node_id exists
        node_id = int(node_id)
        if node_id not in self.__project_nodes:
            self.error = self.tr("Node ID doesn't exist in project")
            qgis.utils.iface.messageBar().pushMessage(self.tr("Input error"), self.error, level=1, duration=5)
            return

        return node_id

    def add_nodes(self):
        from_node = self.__validate_node_id(self.node_from.text())
        to_node = self.__validate_node_id(self.node_to.text())

        if self.error:
            return

        self._pairs.extend([(from_node, to_node)])

        self.tbl_selected_nodes.clearContents()
        self.tbl_selected_nodes.setRowCount(len(self._pairs))

        for i, (origin, dest) in enumerate(self._pairs):
            self.tbl_selected_nodes.setItem(i, 0, QTableWidgetItem(str(origin)))
            self.tbl_selected_nodes.setItem(i, 1, QTableWidgetItem(str(dest)))

    def __remove_nodes(self, line):
        self.tbl_selected_nodes.removeRow(line)
        self._pairs.pop(line - 1)

    def add_graph(self):
        mode = self.cob_mode.currentText()
        mode_id = self.all_modes[mode]
        if mode_id not in self.project.network.graphs:
            self.project.network.build_graphs(modes=[mode_id])

        self.graph = self.project.network.graphs[mode_id]

        if self.chb_chosen_links.isChecked():
            self.graph = self.project.network.graphs.pop(mode_id)
            idx = self.link_layer.dataProvider().fieldNameIndex("link_id")
            remove = [feat.attributes()[idx] for feat in self.link_layer.selectedFeatures()]
            self.graph.exclude_links(remove)

        nodes_of_interest = np.array(list(set(sum(self._pairs, ()))))
        self.graph.set_graph(self.cob_graph_cost.currentText())
        self.graph.prepare_graph(nodes_of_interest)
        self.graph.set_blocked_centroid_flows(self.chb_check_centroids.isChecked())

    def config_route_choice(self):
        self.__validade_rc_inputs()

        if self.error:
            return

        max_routes = int(self.max_routes.text())
        max_depth = int(self.max_depth.text())
        penalty = float(self.penalty.text())

        rc = RouteChoice(self.graph)

        algorithm = "bfsle" if self.cob_algo.currentText().lower() == "bflse" else "link-penalisation"

        rc.set_choice_set_generation(algorithm, max_routes=max_routes, penalty=penalty, max_depth=max_depth)
        if self.chb_save_results.isChecked():
            rc.set_save_routes(self.project.project_base_path)
        rc.prepare(self._pairs)
        rc.execute(self.chb_assignment.isChecked())

        self.exit_procedure()

    def __validade_rc_inputs(self):

        rt = self.max_routes.text()
        dp = self.max_depth.text()
        pen = self.penalty.text()

        if not rt and not dp:
            self.error = "One must set at least one of max. routes or max. depth"
            qgis.utils.iface.messageBar().pushMessage(self.tr("Input error"), self.error, level=1, duration=5)
            return

        if not rt.isdigit():
            self.error = self.tr("Wrong value for max. routes")
            qgis.utils.iface.messageBar().pushMessage(self.tr("Input error"), self.error, level=1, duration=5)
            return

        if not dp.isdigit():
            self.error = self.tr("Wrong value for max. depth")
            qgis.utils.iface.messageBar().pushMessage(self.tr("Input error"), self.error, level=1, duration=5)
            return

        if not pen.replace(".", "").isdigit():
            self.error = self.tr("Wrong value for penalty.")
            qgis.utils.iface.messageBar().pushMessage(self.tr("Input error"), self.error, level=1, duration=5)
            return

    def exit_procedure(self):
        self.close()
