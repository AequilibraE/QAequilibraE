import importlib.util as iutil
import sys
from os.path import join
import pandas as pd

from qgis.core import QgsProcessingMultiStepFeedback, QgsProcessing, QgsProcessingAlgorithm
from qgis.core import QgsProcessingParameterFile, QgsProcessingParameterNumber, QgsProcessingParameterString
from qgis.core import QgsFeature, QgsVectorLayer, QgsDataSourceUri, QgsProcessingParameterBoolean

from qgis import processing

from qaequilibrae.i18n.translate import trlt
from qaequilibrae.modules.common_tools import standard_path, polygon_from_radius


class AddConnectors(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterNumber(
                "num_connectors",
                self.tr("Connectors per centroid"),
                type=QgsProcessingParameterNumber.Integer,
                minValue=1,
                defaultValue=1,
            )
        )
        self.addParameter(
            QgsProcessingParameterString(
                "mode", self.tr("Modes to connect (defaults to all)"), multiLine=False,
            )
        )
        self.addParameter(
            QgsProcessingParameterFile(
                "project_path",
                self.tr("Project path"),
                behavior=QgsProcessingParameterFile.Folder,
                defaultValue=standard_path(),
            )
        )
        self.addParameter(
            QgsProcessingParameterString(
                "link_type", self.tr("Link types to connect (defaults to all)"), multiLine=False,
            )
        )

    def processAlgorithm(self, parameters, context, model_feedback):
        # Checks if we have access to aequilibrae library
        if iutil.find_spec("aequilibrae") is None:
            sys.exit(self.tr("AequilibraE module not found"))

        from aequilibrae import Project

        feedback = QgsProcessingMultiStepFeedback(2, model_feedback)
        feedback.pushInfo(self.tr("Opening project"))

        project = Project()
        project.open(parameters["project_path"])

        nodes = project.network.nodes
        nodes.refresh()

        centroids = nodes.data[nodes.data["is_centroid"] == 1].node_id.tolist()

        feedback.pushInfo(" ")
        feedback.setCurrentStep(1)

        # Adding connectors
        num_connectors = parameters["num_connectors"]
        mode = parameters["mode"]
        feedback.pushInfo(self.tr('Adding {} connectors when none exists for mode "{}"').format(num_connectors, mode))

        for counter, zone_id in enumerate(centroids):
            node = nodes.get(zone_id)
            geo = polygon_from_radius(node.geometry)
            for mode_id in modes:
                node.connect_mode(area=geo, mode_id=mode_id, link_types=link_types, connectors=num_connectors)

        feedback.pushInfo(" ")
        feedback.setCurrentStep(2)

        project.network.nodes.refresh()
        project.network.links.refresh()
        project.close()

        return {"Output": parameters["project_path"]}

    def name(self):
        return "addcentroidconnector"

    def displayName(self):
        return self.tr("Add centroid connectors")

    def group(self):
        return self.tr("1. Model Building")

    def groupId(self):
        return "modelbuilding"

    def shortHelpString(self):
        return self.tr("Go through all the centroids and add connectors only if none exists for the chosen mode")

    def createInstance(self):
        return AddConnectors()

    def tr(self, message):
        return trlt("AddConnectors", message)
