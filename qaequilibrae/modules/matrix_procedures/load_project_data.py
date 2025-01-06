import os
from os.path import join

import pandas as pd
import qgis
from aequilibrae.project.database_connection import database_connection
from aequilibrae.utils.db_utils import commit_and_close
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtWidgets import QAbstractItemView, QTabWidget
from qgis.core import QgsProject, QgsVectorLayerJoinInfo

from qaequilibrae.modules.common_tools import PandasModel
from qaequilibrae.modules.matrix_procedures.display_aequilibrae_formats_dialog import DisplayAequilibraEFormatsDialog
from qaequilibrae.modules.matrix_procedures.load_result_table import load_result_table
from qaequilibrae.modules.matrix_procedures.matrix_lister import list_matrices
from qaequilibrae.modules.matrix_procedures.results_lister import list_results

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), "forms/ui_project_data.ui"))


class LoadProjectDataDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, qgs_proj, proj=True):
        QtWidgets.QDialog.__init__(self)
        self.iface = qgs_proj.iface
        self.setupUi(self)
        self.data_to_show = None
        self.error = None
        self.qgs_proj = qgs_proj
        self.from_proj = proj
        self.project = qgs_proj.project if self.from_proj else None

        if self.from_proj:
            self.matrices: pd.DataFrame = None
            self.matrices_model: PandasModel = None

            self.results: pd.DataFrame = None
            self.results_model: PandasModel = None

            for table in [self.list_matrices, self.list_results]:
                table.setSelectionBehavior(QAbstractItemView.SelectRows)
                table.setSelectionMode(QAbstractItemView.SingleSelection)

            self.load_matrices()
            self.load_results()

            self.but_update_matrices.clicked.connect(self.update_matrix_table)
            self.but_load_Results.clicked.connect(self.load_result_table)
            self.but_load_matrix.clicked.connect(self.display_matrix)
        else:
            QTabWidget.removeTab(self.tabs, 0)
            QTabWidget.removeTab(self.tabs, 0)

        self.but_load_data.clicked.connect(self.display_external_data)

    def display_matrix(self):
        idx = [x.row() for x in list(self.list_matrices.selectionModel().selectedRows())]
        if not idx:
            return
        if self.matrices["WARNINGS"][idx[0]] != "":
            return

        file_name = self.matrices["file_name"][idx[0]]

        dlg2 = DisplayAequilibraEFormatsDialog(self.qgs_proj, join(self.project.matrices.fldr, file_name), proj=True)
        dlg2.show()
        dlg2.exec_()

    def load_matrices(self):
        self.matrices = list_matrices(self.project.matrices.fldr)

        self.matrices_model = PandasModel(self.matrices)
        self.list_matrices.setModel(self.matrices_model)

    def update_matrix_table(self):
        matrices = self.project.matrices
        matrices.update_database()
        with commit_and_close(database_connection("network")) as conn:
            qry = """UPDATE matrices SET name = substr(file_name, 1, length(file_name)-4) WHERE name like "b''%";"""
            conn.execute(qry)
        self.load_matrices()

    def load_results(self):
        self.results = list_results(self.project.project_base_path)

        self.results_model = PandasModel(self.results)
        self.list_results.setModel(self.results_model)

    def load_result_table(self):
        idx = [x.row() for x in list(self.list_results.selectionModel().selectedRows())]
        if not idx:
            return
        table_name = self.results["table_name"][idx[0]]
        if self.results["WARNINGS"][idx[0]] != "":
            return

        lyr = load_result_table(self.project.project_base_path, table_name)

        if self.chb_join.isChecked():
            procedure = self.results.loc[self.results["table_name"] == table_name]["procedure"].values[0]
            if procedure == "transit assignment":
                self.link_layer = self.qgs_proj.layers["transit_links"][0]
            else:
                self.link_layer = self.qgs_proj.layers["links"][0]
            rem = [lien.joinLayerId() for lien in self.link_layer.vectorJoins()]
            for lien_id in rem:
                self.link_layer.removeJoin(lien_id)
            QgsProject.instance().addMapLayer(self.link_layer)

            lien = QgsVectorLayerJoinInfo()
            lien.setJoinFieldName("link_id")
            lien.setTargetFieldName("link_id")
            lien.setJoinLayerId(lyr.id())
            lien.setUsingMemoryCache(True)
            lien.setJoinLayer(lyr)
            lien.setPrefix(f"{table_name}_")
            self.link_layer.addJoin(lien)

    def display_external_data(self):
        dlg2 = DisplayAequilibraEFormatsDialog(self.qgs_proj)
        dlg2.show()
        dlg2.exec_()

    def exit_with_error(self):
        qgis.utils.iface.messageBar().pushMessage("Error:", self.error, level=1)
        self.close()

    def exit_procedure(self):
        self.show()
        self.close()
        # sys.exit(app.exec_())
