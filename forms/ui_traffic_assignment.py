# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_traffic_assignment.ui'
#
# Created: Mon Dec 12 09:22:03 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from qgis.gui import QgsMapLayerComboBox

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_traffic_assignment(object):
    def setupUi(self, traffic_assignment):
        traffic_assignment.setObjectName(_fromUtf8("traffic_assignment"))
        traffic_assignment.setWindowModality(QtCore.Qt.ApplicationModal)
        traffic_assignment.resize(662, 412)
        traffic_assignment.setModal(True)
        self.tabWidget = QtGui.QTabWidget(traffic_assignment)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 641, 391))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.widget = QtGui.QWidget()
        self.widget.setObjectName(_fromUtf8("widget"))
        self.but_load_new_matrix = QtGui.QPushButton(self.widget)
        self.but_load_new_matrix.setGeometry(QtCore.QRect(20, 13, 261, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.but_load_new_matrix.setFont(font)
        self.but_load_new_matrix.setObjectName(_fromUtf8("but_load_new_matrix"))
        self.display_matrix = QtGui.QCheckBox(self.widget)
        self.display_matrix.setGeometry(QtCore.QRect(300, 20, 121, 17))
        self.display_matrix.setObjectName(_fromUtf8("display_matrix"))
        self.matrix_viewer = QtGui.QTableView(self.widget)
        self.matrix_viewer.setGeometry(QtCore.QRect(20, 50, 591, 291))
        self.matrix_viewer.setObjectName(_fromUtf8("matrix_viewer"))
        self.tabWidget.addTab(self.widget, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.lblnodematch_11 = QtGui.QLabel(self.tab_2)
        self.lblnodematch_11.setGeometry(QtCore.QRect(50, 203, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblnodematch_11.setFont(font)
        self.lblnodematch_11.setObjectName(_fromUtf8("lblnodematch_11"))
        self.minimizing_field = QtGui.QComboBox(self.tab_2)
        self.minimizing_field.setGeometry(QtCore.QRect(150, 72, 391, 30))
        self.minimizing_field.setObjectName(_fromUtf8("minimizing_field"))
        self.ba_time_lbl = QtGui.QLabel(self.tab_2)
        self.ba_time_lbl.setGeometry(QtCore.QRect(50, 79, 151, 16))
        self.ba_time_lbl.setObjectName(_fromUtf8("ba_time_lbl"))
        self.no_connectors_in_graph = QtGui.QCheckBox(self.tab_2)
        self.no_connectors_in_graph.setGeometry(QtCore.QRect(151, 106, 341, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.no_connectors_in_graph.setFont(font)
        self.no_connectors_in_graph.setChecked(True)
        self.no_connectors_in_graph.setObjectName(_fromUtf8("no_connectors_in_graph"))
        self.load_graph_from_file = QtGui.QPushButton(self.tab_2)
        self.load_graph_from_file.setGeometry(QtCore.QRect(30, 30, 91, 30))
        self.load_graph_from_file.setObjectName(_fromUtf8("load_graph_from_file"))
        self.lbl_graphfile = QtGui.QLabel(self.tab_2)
        self.lbl_graphfile.setGeometry(QtCore.QRect(153, 35, 391, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_graphfile.setFont(font)
        self.lbl_graphfile.setObjectName(_fromUtf8("lbl_graphfile"))
        self.chb_check_consistency = QtGui.QCheckBox(self.tab_2)
        self.chb_check_consistency.setEnabled(False)
        self.chb_check_consistency.setGeometry(QtCore.QRect(410, 264, 131, 18))
        self.chb_check_consistency.setObjectName(_fromUtf8("chb_check_consistency"))
        self.lblnodematch_14 = QtGui.QLabel(self.tab_2)
        self.lblnodematch_14.setGeometry(QtCore.QRect(50, 236, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblnodematch_14.setFont(font)
        self.lblnodematch_14.setObjectName(_fromUtf8("lblnodematch_14"))
        self.network_layer = QgsMapLayerComboBox(self.tab_2)
        self.network_layer.setGeometry(QtCore.QRect(151, 196, 391, 30))
        self.network_layer.setObjectName(_fromUtf8("network_layer"))
        self.network_field = QtGui.QComboBox(self.tab_2)
        self.network_field.setGeometry(QtCore.QRect(150, 230, 391, 30))
        self.network_field.setObjectName(_fromUtf8("network_field"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.skim_list = QtGui.QTableWidget(self.tab_4)
        self.skim_list.setGeometry(QtCore.QRect(20, 80, 571, 261))
        self.skim_list.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.skim_list.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.skim_list.setRowCount(0)
        self.skim_list.setColumnCount(1)
        self.skim_list.setObjectName(_fromUtf8("skim_list"))
        item = QtGui.QTableWidgetItem()
        self.skim_list.setHorizontalHeaderItem(0, item)
        self.skim_list.verticalHeader().setDefaultSectionSize(27)
        self.add_skim = QtGui.QPushButton(self.tab_4)
        self.add_skim.setGeometry(QtCore.QRect(20, 49, 571, 24))
        self.add_skim.setObjectName(_fromUtf8("add_skim"))
        self.skim_field = QtGui.QComboBox(self.tab_4)
        self.skim_field.setGeometry(QtCore.QRect(60, 17, 531, 30))
        self.skim_field.setObjectName(_fromUtf8("skim_field"))
        self.lblnodematch_12 = QtGui.QLabel(self.tab_4)
        self.lblnodematch_12.setGeometry(QtCore.QRect(25, 24, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblnodematch_12.setFont(font)
        self.lblnodematch_12.setObjectName(_fromUtf8("lblnodematch_12"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.select_link_list = QtGui.QTableWidget(self.tab_3)
        self.select_link_list.setEnabled(False)
        self.select_link_list.setGeometry(QtCore.QRect(10, 50, 611, 291))
        self.select_link_list.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.select_link_list.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.select_link_list.setRowCount(0)
        self.select_link_list.setColumnCount(4)
        self.select_link_list.setObjectName(_fromUtf8("select_link_list"))
        item = QtGui.QTableWidgetItem()
        self.select_link_list.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.select_link_list.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.select_link_list.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.select_link_list.setHorizontalHeaderItem(3, item)
        self.select_link_list.verticalHeader().setDefaultSectionSize(27)
        self.do_select_link = QtGui.QCheckBox(self.tab_3)
        self.do_select_link.setEnabled(False)
        self.do_select_link.setGeometry(QtCore.QRect(10, 15, 141, 22))
        self.do_select_link.setObjectName(_fromUtf8("do_select_link"))
        self.but_build_query = QtGui.QPushButton(self.tab_3)
        self.but_build_query.setEnabled(False)
        self.but_build_query.setGeometry(QtCore.QRect(540, 11, 81, 30))
        self.but_build_query.setObjectName(_fromUtf8("but_build_query"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.list_link_extraction = QtGui.QTableWidget(self.tab_5)
        self.list_link_extraction.setEnabled(False)
        self.list_link_extraction.setGeometry(QtCore.QRect(10, 40, 311, 311))
        self.list_link_extraction.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.list_link_extraction.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.list_link_extraction.setRowCount(0)
        self.list_link_extraction.setColumnCount(2)
        self.list_link_extraction.setObjectName(_fromUtf8("list_link_extraction"))
        item = QtGui.QTableWidgetItem()
        self.list_link_extraction.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.list_link_extraction.setHorizontalHeaderItem(1, item)
        self.list_link_extraction.verticalHeader().setDefaultSectionSize(27)
        self.do_extract_link_flows = QtGui.QCheckBox(self.tab_5)
        self.do_extract_link_flows.setEnabled(False)
        self.do_extract_link_flows.setGeometry(QtCore.QRect(10, 10, 191, 22))
        self.do_extract_link_flows.setObjectName(_fromUtf8("do_extract_link_flows"))
        self.but_build_query_extract = QtGui.QPushButton(self.tab_5)
        self.but_build_query_extract.setEnabled(False)
        self.but_build_query_extract.setGeometry(QtCore.QRect(240, 5, 81, 30))
        self.but_build_query_extract.setObjectName(_fromUtf8("but_build_query_extract"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.do_assignment = QtGui.QPushButton(self.tab)
        self.do_assignment.setGeometry(QtCore.QRect(40, 290, 351, 30))
        self.do_assignment.setObjectName(_fromUtf8("do_assignment"))
        self.cancel_all = QtGui.QPushButton(self.tab)
        self.cancel_all.setGeometry(QtCore.QRect(410, 290, 131, 30))
        self.cancel_all.setObjectName(_fromUtf8("cancel_all"))
        self.cb_choose_algorithm = QtGui.QComboBox(self.tab)
        self.cb_choose_algorithm.setGeometry(QtCore.QRect(80, 18, 531, 30))
        self.cb_choose_algorithm.setMaxVisibleItems(10)
        self.cb_choose_algorithm.setObjectName(_fromUtf8("cb_choose_algorithm"))
        self.lblnodematch_13 = QtGui.QLabel(self.tab)
        self.lblnodematch_13.setGeometry(QtCore.QRect(10, 24, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblnodematch_13.setFont(font)
        self.lblnodematch_13.setObjectName(_fromUtf8("lblnodematch_13"))
        self.progress_label0 = QtGui.QLabel(self.tab)
        self.progress_label0.setGeometry(QtCore.QRect(250, 329, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.progress_label0.setFont(font)
        self.progress_label0.setObjectName(_fromUtf8("progress_label0"))
        self.progressbar0 = QtGui.QProgressBar(self.tab)
        self.progressbar0.setEnabled(True)
        self.progressbar0.setGeometry(QtCore.QRect(9, 327, 231, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 153, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.progressbar0.setPalette(palette)
        self.progressbar0.setProperty("value", 0)
        self.progressbar0.setTextVisible(True)
        self.progressbar0.setObjectName(_fromUtf8("progressbar0"))
        self.do_path_file = QtGui.QCheckBox(self.tab)
        self.do_path_file.setGeometry(QtCore.QRect(10, 60, 171, 22))
        self.do_path_file.setObjectName(_fromUtf8("do_path_file"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 90, 621, 181))
        self.groupBox.setAcceptDrops(False)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.critical_matrix_path = QtGui.QLabel(self.groupBox)
        self.critical_matrix_path.setEnabled(False)
        self.critical_matrix_path.setGeometry(QtCore.QRect(150, 108, 451, 17))
        self.critical_matrix_path.setObjectName(_fromUtf8("critical_matrix_path"))
        self.lbl_output = QtGui.QLabel(self.groupBox)
        self.lbl_output.setGeometry(QtCore.QRect(150, 35, 451, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl_output.setFont(font)
        self.lbl_output.setObjectName(_fromUtf8("lbl_output"))
        self.select_critical_analysis_output = QtGui.QPushButton(self.groupBox)
        self.select_critical_analysis_output.setEnabled(False)
        self.select_critical_analysis_output.setGeometry(QtCore.QRect(10, 103, 121, 27))
        self.select_critical_analysis_output.setObjectName(_fromUtf8("select_critical_analysis_output"))
        self.path_file_display = QtGui.QLabel(self.groupBox)
        self.path_file_display.setGeometry(QtCore.QRect(150, 72, 451, 17))
        self.path_file_display.setObjectName(_fromUtf8("path_file_display"))
        self.select_path_file_name = QtGui.QPushButton(self.groupBox)
        self.select_path_file_name.setGeometry(QtCore.QRect(11, 67, 121, 27))
        self.select_path_file_name.setObjectName(_fromUtf8("select_path_file_name"))
        self.select_result = QtGui.QPushButton(self.groupBox)
        self.select_result.setGeometry(QtCore.QRect(10, 34, 121, 24))
        self.select_result.setObjectName(_fromUtf8("select_result"))
        self.do_group_outputs = QtGui.QCheckBox(self.groupBox)
        self.do_group_outputs.setGeometry(QtCore.QRect(387, 8, 231, 22))
        self.do_group_outputs.setObjectName(_fromUtf8("do_group_outputs"))
        self.critical_matrix_path_2 = QtGui.QLabel(self.groupBox)
        self.critical_matrix_path_2.setEnabled(False)
        self.critical_matrix_path_2.setGeometry(QtCore.QRect(150, 146, 451, 17))
        self.critical_matrix_path_2.setObjectName(_fromUtf8("critical_matrix_path_2"))
        self.select_link_flow_extraction_output = QtGui.QPushButton(self.groupBox)
        self.select_link_flow_extraction_output.setEnabled(False)
        self.select_link_flow_extraction_output.setGeometry(QtCore.QRect(10, 141, 121, 27))
        self.select_link_flow_extraction_output.setObjectName(_fromUtf8("select_link_flow_extraction_output"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        self.retranslateUi(traffic_assignment)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(traffic_assignment)

    def retranslateUi(self, traffic_assignment):
        traffic_assignment.setWindowTitle(_translate("traffic_assignment", "Traffic Assignment toolbox - Provided by www.xl-optim.com", None))
        self.but_load_new_matrix.setText(_translate("traffic_assignment", "Load new matrix", None))
        self.display_matrix.setText(_translate("traffic_assignment", "Display Matrix", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("traffic_assignment", "Demand", None))
        self.lblnodematch_11.setText(_translate("traffic_assignment", "Line layer", None))
        self.ba_time_lbl.setText(_translate("traffic_assignment", "Minimizing field", None))
        self.no_connectors_in_graph.setText(_translate("traffic_assignment", "Prevent flows through centroid connectors", None))
        self.load_graph_from_file.setText(_translate("traffic_assignment", "Load Graph", None))
        self.lbl_graphfile.setText(_translate("traffic_assignment", "Load graph *.aeg", None))
        self.chb_check_consistency.setText(_translate("traffic_assignment", "Check consistency", None))
        self.lblnodematch_14.setText(_translate("traffic_assignment", "Link ID field", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("traffic_assignment", "Network", None))
        self.skim_list.setAccessibleName(_translate("traffic_assignment", "<html><head/><body><p>xcxc</p></body></html>", None))
        item = self.skim_list.horizontalHeaderItem(0)
        item.setText(_translate("traffic_assignment", "Skim name", None))
        self.add_skim.setText(_translate("traffic_assignment", "Add Skim", None))
        self.lblnodematch_12.setText(_translate("traffic_assignment", "Field", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("traffic_assignment", "Skims", None))
        self.select_link_list.setAccessibleName(_translate("traffic_assignment", "<html><head/><body><p>xcxc</p></body></html>", None))
        item = self.select_link_list.horizontalHeaderItem(0)
        item.setText(_translate("traffic_assignment", "Links", None))
        item = self.select_link_list.horizontalHeaderItem(1)
        item.setText(_translate("traffic_assignment", "Type", None))
        item = self.select_link_list.horizontalHeaderItem(2)
        item.setText(_translate("traffic_assignment", "Query name", None))
        item = self.select_link_list.horizontalHeaderItem(3)
        item.setText(_translate("traffic_assignment", "Del", None))
        self.do_select_link.setText(_translate("traffic_assignment", "Select link analysis", None))
        self.but_build_query.setText(_translate("traffic_assignment", "Build Query", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("traffic_assignment", "Critical analysis", None))
        self.list_link_extraction.setAccessibleName(_translate("traffic_assignment", "<html><head/><body><p>xcxc</p></body></html>", None))
        item = self.list_link_extraction.horizontalHeaderItem(0)
        item.setText(_translate("traffic_assignment", "Link ID", None))
        item = self.list_link_extraction.horizontalHeaderItem(1)
        item.setText(_translate("traffic_assignment", "Direction", None))
        self.do_extract_link_flows.setText(_translate("traffic_assignment", "Perform link flow extraction", None))
        self.but_build_query_extract.setText(_translate("traffic_assignment", "Build Query", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("traffic_assignment", "Link flow extraction", None))
        self.do_assignment.setText(_translate("traffic_assignment", "ASSIGN", None))
        self.cancel_all.setText(_translate("traffic_assignment", "CANCEL", None))
        self.lblnodematch_13.setText(_translate("traffic_assignment", "Algorithm", None))
        self.progress_label0.setText(_translate("traffic_assignment", "Status Message 0", None))
        self.do_path_file.setText(_translate("traffic_assignment", "Save complete path file", None))
        self.groupBox.setTitle(_translate("traffic_assignment", "Outputs", None))
        self.critical_matrix_path.setText(_translate("traffic_assignment", "...", None))
        self.lbl_output.setText(_translate("traffic_assignment", "Output", None))
        self.select_critical_analysis_output.setText(_translate("traffic_assignment", "Critical output", None))
        self.path_file_display.setText(_translate("traffic_assignment", "...", None))
        self.select_path_file_name.setText(_translate("traffic_assignment", "Select output file", None))
        self.select_result.setText(_translate("traffic_assignment", "Assignment results", None))
        self.do_group_outputs.setText(_translate("traffic_assignment", "Group outputs in a single database", None))
        self.critical_matrix_path_2.setText(_translate("traffic_assignment", "...", None))
        self.select_link_flow_extraction_output.setText(_translate("traffic_assignment", "Critical output", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("traffic_assignment", "Assignment", None))


