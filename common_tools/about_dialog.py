"""
 -----------------------------------------------------------------------------------------------------------
 Package:    AequilibraE

 Name:       About dialog
 Purpose:    Dialog for showing the About window

 Original Author:  Pedro Camargo (c@margo.co)
 Contributors:
 Last edited by: Pedro Camargo

 Website:    www.AequilibraE.com
 Repository:  https://github.com/AequilibraE/AequilibraE

 Created:    2018-06-29
 Updated:
 Copyright:   (c) AequilibraE authors
 Licence:     See LICENSE.TXT
 -----------------------------------------------------------------------------------------------------------
 """

from qgis.core import *
from qgis.PyQt import QtWidgets, uic
import qgis
from qgis.PyQt import QtGui
import webbrowser

import os
from os.path import dirname, abspath
from .auxiliary_functions import standard_path
from aequilibrae.paths import release_name, release_version

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__),  'forms/ui_about.ui'))

class AboutDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, iface):
        QtWidgets.QDialog.__init__(self)
        self.iface = iface
        self.setupUi(self)
        self.path = standard_path()

        self.but_mailing.clicked.connect(self.go_to_mailing_list)
        self.but_close.clicked.connect(self.exit_procedure)

        repository = 'https://github.com/AequilibraE/AequilibraE-GUI'
        self.wiki = "https://github.com/aequilibrae/aequilibrae/wiki"
        sponsors = ['IPEA (2015)']
        developers = ['Pedro Camargo','Yu-Chu Huang' ,'Jamie Cook (MacOS binaries)']

        d = dirname(dirname(abspath(__file__)))
        my_file = os.path.join(d, 'metadata.txt')
        b = '?'
        with open(my_file, 'r') as a:
            for line in a.readlines():
                if line[:7] == 'version':
                    b = line[8:]
                    break

        self.all_items = []
        self.all_items.append(['AequilibraE Version name', release_name])
        self.all_items.append(['AequilibraE Version number', release_version])
        self.all_items.append(['GUI version', b])
        self.all_items.append(['GUI Repository', repository])
        self.all_items.append(['Minimum QGIS', '3.0'])
        self.all_items.append(['Developers', developers])
        self.all_items.append(['Sponsors', sponsors])

        self.assemble()

    def assemble(self):
        titles = []
        row_count = 0

        for r, t in self.all_items:
            titles.append(r)
            self.about_table.insertRow(row_count)
            if isinstance(t, list):
                lv = QtWidgets.QListWidget()
                lv.addItems(t)
                self.about_table.setCellWidget(row_count, 0, lv)
                self.about_table.setRowHeight(row_count, len(t)*self.about_table.rowHeight(row_count))
            else:
                self.about_table.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(t)))

            row_count += 1
        self.about_table.setVerticalHeaderLabels(titles)

    def go_to_mailing_list(self):
        webbrowser.open(self.wiki, new=2)
        self.exit_procedure()

    def exit_procedure(self):
        self.close()
