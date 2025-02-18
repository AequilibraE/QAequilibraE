import os

import numpy as np
from aequilibrae.paths.route_choice import RouteChoice
from qgis.PyQt import uic
from qgis.PyQt.QtCore import pyqtSlot
from qgis.PyQt.QtWidgets import QDialog

from qaequilibrae.modules.common_tools.debouncer import Debouncer
from qaequilibrae.modules.paths_procedures.plot_route_choice import plot_results

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), "forms/ui_execute_single.ui"))


class VisualizeSingle(QDialog, FORM_CLASS):
    def __init__(self, iface, graph, algorithm, kwargs, demand, link_layer):
        QDialog.__init__(self)
        self.iface = iface
        self.setupUi(self)

        self.graph = graph
        self._algo = algorithm
        self._kwargs = kwargs
        self.demand = demand
        self.link_layer = link_layer

        self.debouncer = Debouncer(delay_ms=4_000, callback=self.on_input_changed)

        self.node_from.textChanged.connect(self._on_node_from_changed)
        self.node_to.textChanged.connect(self._on_node_to_changed)
        self.sld_max_routes.valueChanged.connect(self._on_slider_changed)

    def execute_single(self):
        self.from_node = int(self.node_from.text())
        self.to_node = int(self.node_to.text())

        nodes_of_interest = np.array([self.from_node, self.to_node], dtype=np.int64)

        self.graph.prepare_graph(nodes_of_interest)
        self.graph.set_graph("utility")

        rc = RouteChoice(self.graph)
        rc.set_choice_set_generation(self._algo, **self._kwargs)
        _ = rc.execute_single(self.from_node, self.to_node, self.demand)

        plot_results(rc.get_results().to_pandas(), self.from_node, self.to_node, self.link_layer)

    def exit_procedure(self):
        self.close()

    @pyqtSlot(str)
    def _on_node_from_changed(self, text):
        self.debouncer(("node_from", text))

    @pyqtSlot(str)
    def _on_node_to_changed(self, text):
        self.debouncer(("node_to", text))

    @pyqtSlot(int)
    def _on_slider_changed(self, value):
        self.debouncer(("sld_max_routes", value))

    def on_input_changed(self, source_and_value):
        source, value = source_and_value
        if source == "sld_max_routes":
            self._kwargs["max_routes"] = value

        self.execute_single()
