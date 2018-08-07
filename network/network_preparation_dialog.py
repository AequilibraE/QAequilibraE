"""
 -----------------------------------------------------------------------------------------------------------
 Package:    AequilibraE

 Name:       Network preparation
 Purpose:    Loads GUI for preparing networks (extracting nodes A and B from links)

 Original Author:  Pedro Camargo (c@margo.co)
 Contributors:
 Last edited by: Pedro Camargo

 Website:    www.AequilibraE.com
 Repository:  https://github.com/AequilibraE/AequilibraE

 Created:    2014-03-19
 Updated:    21/12/2016
 Copyright:   (c) AequilibraE authors
 Licence:     See LICENSE.TXT
 -----------------------------------------------------------------------------------------------------------
 """

from qgis.core import *
import qgis
from qgis.PyQt.QtCore import *
from qgis.PyQt import QtWidgets, uic

import sys
from ..common_tools.global_parameters import *
from ..common_tools.auxiliary_functions import *
from ..common_tools import ReportDialog

from .Network_preparation_procedure import NetworkPreparationProcedure

sys.modules['qgsmaplayercombobox'] = qgis.gui
sys.modules['qgsfieldcombobox'] = qgis.gui
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'forms/ui_network_preparation.ui'))


class NetworkPreparationDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, iface):
        QtWidgets.QDialog.__init__(self)
        self.iface = iface
        self.setupUi(self)

        self.filename = False
        self.new_layer = False
        self.radioUseNodes.clicked.connect(self.uses_nodes)
        self.radioNewNodes.clicked.connect(self.uses_nodes)

        self.cbb_node_layer.currentIndexChanged.connect(self.set_columns_nodes)

        self.pushOK.clicked.connect(self.run)
        self.pushClose.clicked.connect(self.exit_procedure)

        # We load the line and node layers existing in our canvas
        self.cbb_line_layer.setFilters(QgsMapLayerProxyModel.LineLayer)
        self.cbb_node_layer.setFilters(QgsMapLayerProxyModel.PointLayer)

        # loads default path from parameters
        self.path = standard_path()
        self.uses_nodes()
        self.set_columns_nodes()

    def run_thread(self):
        self.worker_thread.ProgressValue.connect(self.progress_value_from_thread)
        self.worker_thread.ProgressText.connect(self.progress_text_from_thread)
        self.worker_thread.ProgressMaxValue.connect(self.progress_range_from_thread)
        self.worker_thread.jobFinished.connect(self.job_finished_from_thread)
        self.worker_thread.start()
        self.show()

    def progress_range_from_thread(self, val):
        self.progressbar.setRange(0, val)

    def progress_value_from_thread(self, value):
        self.progressbar.setValue(value)

    def progress_text_from_thread(self, value):
        self.progress_label.setText(value)

    def set_columns_nodes(self):
        self.cbb_node_fields.clear()
        if self.cbb_node_layer.currentIndex() >= 0:
            layer = get_vector_layer_by_name(self.cbb_node_layer.currentText())
            self.cbb_node_fields.setLayer(layer)

    def uses_nodes(self):
        for_creating_nodes = [self.OutNodes, self.label_9, self.np_node_start, self.label_3]
        for_using_existing_nodes = [self.cbb_node_layer, self.cbb_node_fields, self.label_2, self.label_4]

        if self.radioUseNodes.isChecked():
            for i in for_creating_nodes:
                i.setVisible(False)
            for i in for_using_existing_nodes:
                i.setVisible(True)

            self.cbb_node_layer.clear()
        else:
            for i in for_creating_nodes:
                i.setVisible(True)
            for i in for_using_existing_nodes:
                i.setVisible(False)

            self.cbb_node_layer.clear()
            self.cbb_node_layer.hideEvent
            self.np_node_start.setEnabled(True)

    def job_finished_from_thread(self, success):

        if self.worker_thread.error is not None:
            qgis.utils.iface.messageBar().pushMessage("Node layer error: ", self.worker_thread.error, level=3)
        else:
            QgsProject.instance().addMapLayer(self.worker_thread.new_line_layer)
            if self.worker_thread.new_node_layer:
                QgsProject.instance().addMapLayer(self.worker_thread.new_node_layer)
        self.exit_procedure()
        if self.worker_thread.report:
            dlg2 = ReportDialog(self.iface, self.worker_thread.report)
            dlg2.show()
            dlg2.exec_()

    def run(self):
        if self.radioUseNodes.isChecked():
            self.pushOK.setEnabled(False)
            self.worker_thread = NetworkPreparationProcedure(qgis.utils.iface.mainWindow(), self.cbb_line_layer.currentText(),
                                                             self.OutLinks.text(), self.cbb_node_layer.currentText(),
                                                             self.cbb_node_fields.currentText())
            self.run_thread()

        else:
            self.pushOK.setEnabled(False)
            self.worker_thread = NetworkPreparationProcedure(qgis.utils.iface.mainWindow(), self.cbb_line_layer.currentText(),
                                                             self.OutLinks.text(), new_node_layer=self.OutNodes.text(),
                                                             node_start = int(self.np_node_start.text()))
            self.run_thread()

    def exit_procedure(self):
        self.close()

