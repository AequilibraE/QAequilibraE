import os

import numpy as np
import qgis
from aequilibrae.paths.route_choice import RouteChoice
from qgis.PyQt import uic
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QDialog
from qgis.core import QgsVectorLayer, QgsProject

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), "forms/ui_execute_single.ui"))


class VisualizeSingle(QDialog, FORM_CLASS):
    def __init__(self, iface, graph, algo, kwargs, demand):
        QDialog.__init__(self)
        self.iface = iface
        self.setupUi(self)

        self.graph = graph
        self._algo = algo
        self._kwargs = kwargs
        self.demand = demand

        self.error = None

    def execute_single(self):
        self.from_node = self.__validate_node_id(self.node_from.text())
        self.to_node = self.__validate_node_id(self.node_to.text())

        nodes_of_interest = np.array([self.from_node, self.to_node], dtype=np.int64)

        self.graph.prepare_graph(nodes_of_interest)
        self.graph.set_graph("utility")

        rc = RouteChoice(self.graph)
        rc.set_choice_set_generation(self._algo, **self._kwargs)
        results = rc.execute_single(self.from_node, self.to_node, self.demand)

        self._plot_results(results)

    def __validate_node_id(self, node_id: str):
        # Check if we have only numbers
        if not node_id.isdigit():
            self.error = self.tr("Wrong input value for node ID")

        # Check if node_id exists
        node_id = int(node_id)
        if node_id not in self.__project_nodes:
            self.error = self.tr("Node ID doesn't exist in project")

        return node_id

    def _plot_results(self, res):
        for idx, feat in enumerate(res):

            exp = '"link_id" IN {}'.format(feat)
            self.link_layer.selectByExpression(exp)

            selected_features = [f for f in self.link_layer.getSelectedFeatures()]

            temp_layer_name = f"route_set_{idx}-{self.from_node}-{self.to_node}"
            temp_layer = QgsVectorLayer(
                "LineString?crs={}".format(self.link_layer.crs().authid()), temp_layer_name, "memory"
            )
            temp_layer.dataProvider().addAttributes(self.link_layer.fields())
            temp_layer.updateFields()
            temp_layer.startEditing()
            for feature in selected_features:
                temp_layer.dataProvider().addFeature(feature)
            temp_layer.commitChanges()

            QgsProject.instance().addMapLayer(temp_layer)

        qgis.utils.iface.mapCanvas().refresh()
