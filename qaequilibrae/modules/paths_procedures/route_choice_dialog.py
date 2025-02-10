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

from qaequilibrae.modules.matrix_procedures import list_matrices


sys.modules["qgsmaplayercombobox"] = qgis.gui
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), "forms/ui_route_choice.ui"))
logger = logging.getLogger("AequilibraEGUI")


class RouteChoiceDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, qgis_project):
        QtWidgets.QDialog.__init__(self)
        self.iface = qgis_project.iface
        self.project = qgis_project.project
        self.matrices = self.project.matrices
        self.setupUi(self)
        self.error = None
        self.matrix = None
        self.cost_function = ""
        self.utility = []

        self.all_modes = {}
        self._pairs = []

        self.__populate_project_info()

        self.__project_nodes = self.project.network.nodes.data.node_id.tolist()
        self.proj_matrices = list_matrices(self.project.matrices.fldr)

        # Removes `Critical analysis` until it is set
        self.tabWidget.removeTab(1)

        self.cob_algo.addItems(["BFSLE", "Link Penalization"])

        self.list_matrices()
        self.set_matrix()

        self.cob_matrices.currentTextChanged.connect(self.set_matrix)
        self.but_add_to_cost.clicked.connect(self.add_cost_function)
        self.but_clear_cost.clicked.connect(self.clear_cost_function)

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

        if len(self.matrices.list()) == 0:
            self.matrix = None
        else:
            self.matrix = self.matrices.get_matrix(self.cob_matrices.currentText())

        self.cob_matrix_core.clear()
        
        if self.matrix is not None:
            self.cob_matrix_core.addItems(self.matrix.names)

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

        self.utility.extend((self.parameter, self.cob_net_field.currentText()))

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
            x += (par * self.graph.network[col].array)

        self.graph.network["utility"] = field.reshape(self.graph.network.shape[1], 1)

        if self.chb_chosen_links.isChecked():
            self.graph = self.project.network.graphs.pop(mode_id)
            idx = self.link_layer.dataProvider().fieldNameIndex("link_id")
            remove = [feat.attributes()[idx] for feat in self.link_layer.selectedFeatures()]
            self.graph.exclude_links(remove)
        
        self.graph.set_graph("utility")
        # self.graph.prepare_graph(nodes_of_interest)
        self.graph.set_blocked_centroid_flows(self.chb_check_centroids.isChecked())

    def matrix_config(self):
        self.matrix.computational_view([self.cob_matrix_core.currentText()])

    def route_choice(self):
        self.graph_config()
        self.matrix_config()

        rc = RouteChoice(self.graph)
        rc.add_demand(self.matrix)

        # Add a warning here
        rc.set_choice_set_generation("bfsle", max_routes=5)
