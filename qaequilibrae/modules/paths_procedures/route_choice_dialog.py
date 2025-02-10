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

        self.all_modes = {}
        self._pairs = []

        self.__populate_project_info()

        self.__project_nodes = self.project.network.nodes.data.node_id.tolist()
        self.proj_matrices = list_matrices(self.project.matrices.fldr)

        # We start with `Choice set generation`
        self.tabWidget.removeTab(1)

        self.cob_algo.addItems(["BFSLE", "Link Penalization"])

        self.list_matrices()
        self.set_matrix()

        self.cob_matrices.currentTextChanged.connect(self.set_matrix)
        self.but_add_to_cost.clicked.connect(self.add_cost_function)

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
        valid_params = self.__check_parameter_value(self.ln_parameter.text())

        if not valid_params:
            qgis.utils.iface.messageBar().pushMessage(self.tr("Input error"), self.error, level=1, duration=5)
            return
        
        # cost_function = ""
        # self.txt_cost_func.setText()

    def exit_procedure(self):
        self.close()

    def __check_parameter_value(self, par):
        # parameter cannot be null
        if par is None:
            self.error = "Check parameter value."
            return False

        # parameter needs to be numeric
        if not par.replace(".", "").isdigit():
            self.error = "Wrong value in parameter."
            return False
        
        self.parameter = float(par)
        return True
        