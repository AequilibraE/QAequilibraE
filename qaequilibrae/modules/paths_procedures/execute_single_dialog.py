import os

import numpy as np
from aequilibrae.paths.route_choice import RouteChoice
from qgis.PyQt import uic
from qgis.PyQt.QtWidgets import QDialog

from qaequilibrae.modules.paths_procedures.route_choice_plot import plot_results

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), "forms/ui_execute_single.ui"))


class VisualizeSingle(QDialog, FORM_CLASS):
    def __init__(self, iface, graph, algo, kwargs, demand, link_layer):
        QDialog.__init__(self)
        self.iface = iface
        self.setupUi(self)

        self.graph = graph
        self._algo = algo
        self._kwargs = kwargs
        self.demand = demand
        self.link_layer = link_layer

        self.but_visualize.clicked.connect(self.execute_single)
        self.sld_max_routes.valueChanged.connect(self.set_max_routes)

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

    def set_max_routes(self):
        self._kwargs["max_routes"] = self.sld_max_routes.value()