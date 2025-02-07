import logging
import os
import sys
from tempfile import gettempdir

import qgis
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtWidgets import QTableWidgetItem, QLineEdit, QComboBox, QCheckBox, QPushButton, QAbstractItemView

from qaequilibrae.modules.common_tools import PandasModel, ReportDialog, standard_path

sys.modules["qgsmaplayercombobox"] = qgis.gui
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), "forms/ui_route_choice_v2.ui"))
logger = logging.getLogger("AequilibraEGUI")
    

class RouteChoiceDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, qgis_project):
        QtWidgets.QDialog.__init__(self)
        self.iface = qgis_project.iface
        self.project = qgis_project.project
        self.setupUi(self)
        
        self.tabWidget.removeTab(2)
        self.tabWidget.removeTab(1)

        pass

