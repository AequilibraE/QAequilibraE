import importlib.util as iutil
import sys

from qgis.core import QgsProcessingAlgorithm, QgsProcessingParameterFile
from qgis.core import QgsProcessingParameterBoolean, QgsProcessingParameterString, QgsProcessingParameterNumber
from qgis.core import QgsProcessingParameterDefinition

from qaequilibrae.modules.common_tools import standard_path
from qaequilibrae.i18n.translate import trlt


class CreatePTGraph(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterFile(
                "project_path",
                self.tr("Project path"),
                behavior=QgsProcessingParameterFile.Folder,
                defaultValue=standard_path(),
            )
        )
        self.addParameter(
            QgsProcessingParameterString("access_mode", self.tr("Mode"), multiLine=False, defaultValue="w")
        )
        self.addParameter(
            QgsProcessingParameterBoolean("block_flows", self.tr("Block flows through centroids"), defaultValue=True)
        )
        self.addParameter(
            QgsProcessingParameterBoolean("walking_edges", self.tr("Project with walking edges"), defaultValue=False)
        )
        self.addParameter(
            QgsProcessingParameterBoolean(
                "outer_stops_transfers", self.tr("Project with outer stops transfers"), defaultValue=False
            )
        )

        advparams = [
            QgsProcessingParameterBoolean("has_zones", self.tr("Project has zoning information"), defaultValue=True),
            QgsProcessingParameterNumber(
                "period_id", self.tr("Period ID"), type=QgsProcessingParameterNumber.Integer, minValue=1, defaultValue=1
            ),
        ]

        for param in advparams:
            param.setFlags(param.flags() | QgsProcessingParameterDefinition.FlagAdvanced)
            self.addParameter(param)

    def processAlgorithm(self, parameters, context, feedback):
        # Checks if we have access to aequilibrae library
        if iutil.find_spec("aequilibrae") is None:
            sys.exit(self.tr("AequilibraE module not found"))

        from aequilibrae.transit import Transit
        from aequilibrae.project import Project

        feedback.pushInfo(self.tr("Opening project"))
        # Opening project
        project = Project()
        project.open(parameters["project_path"])
        data = Transit(project)

        feedback.pushInfo(" ")
        feedback.pushInfo(self.tr("Creating graph"))
        # Creating graph
        if "has_zones" in parameters and parameters["has_zones"] == True:
            graph.add_zones(project.zoning)

        graph = data.create_graph(
            with_outer_stop_transfers=parameters["outer_stops_transfers"],
            with_walking_edges=parameters["walking_edges"],
            blocking_centroid_flows=parameters["block_flows"],
            connector_method="overlapping_regions",
        )
        feedback.pushInfo(" ")

        # Connector matching
        project.network.build_graphs()
        graph.create_line_geometry(method="connector project match", graph=parameters["access_mode"])

        feedback.pushInfo(self.tr("Saving graph"))
        # Saving graph
        data.save_graphs()

        feedback.pushInfo(" ")

        project.close()

        return {"Output": "PT graph successfully created"}

    def name(self):
        return "createptgraph"

    def displayName(self):
        return self.tr("Create PT graph")

    def group(self):
        return self.tr("4. Public Transport")

    def groupId(self):
        return "publictransport"

    def shortHelpString(self):
        return "Creates a graph to be used with PT Assignment"

    def createInstance(self):
        return CreatePTGraph()

    def tr(self, message):
        return trlt("CreatePTGraph", message)
