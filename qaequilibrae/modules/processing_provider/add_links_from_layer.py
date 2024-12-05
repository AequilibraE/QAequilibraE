import importlib.util as iutil
import sys
from string import ascii_letters

from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessing, QgsProcessingMultiStepFeedback, QgsProcessingParameterVectorLayer
from qgis.core import QgsProcessingParameterField, QgsProcessingParameterFile

from qaequilibrae.i18n.translate import trlt
from qaequilibrae.modules.common_tools import geodataframe_from_layer, standard_path


class AddLinksFromLayer(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                "links", self.tr("Links"), types=[QgsProcessing.TypeVectorLine], defaultValue=None
            )
        )
        self.addParameter(
            QgsProcessingParameterField(
                "link_type",
                self.tr("Link type"),
                type=QgsProcessingParameterField.String,
                parentLayerParameterName="links",
                allowMultiple=False,
                defaultValue="link_type",
            )
        )
        self.addParameter(
            QgsProcessingParameterField(
                "direction",
                self.tr("Direction"),
                type=QgsProcessingParameterField.Numeric,
                parentLayerParameterName="links",
                allowMultiple=False,
                defaultValue="direction",
            )
        )
        self.addParameter(
            QgsProcessingParameterField(
                "modes",
                self.tr("Modes"),
                type=QgsProcessingParameterField.String,
                parentLayerParameterName="links",
                allowMultiple=False,
                defaultValue="modes",
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

    def processAlgorithm(self, parameters, context, model_feedback):
        # Checks if we have access to aequilibrae library
        if iutil.find_spec("aequilibrae") is None:
            sys.exit(self.tr("AequilibraE module not found"))

        from aequilibrae import Project

        feedback = QgsProcessingMultiStepFeedback(5, model_feedback)
        feedback.pushInfo(self.tr("Opening project"))

        project_path = parameters["project_path"]
        project = Project()
        project.open(project_path)

        feedback.pushInfo(self.tr("Importing links layer"))

        # Load layer as GeoDataFrame
        layer = self.parameterAsVectorLayer(parameters, "links", context)
        gdf = geodataframe_from_layer(layer).infer_objects()

        columns = [parameters["link_type"], parameters["direction"], parameters["modes"], "geometry"]

        gdf = gdf[columns]
        gdf.columns = ["link_type", "direction", "modes", "geometry"]

        # We check if all modes exist in the project
        all_modes = set("".join(gdf["modes"].unique()))
        modes = project.network.modes
        current_modes = list(modes.all_modes().keys())
        all_modes = [x for x in all_modes if x not in current_modes]
        for md in all_modes:
            new_mode = modes.new(md)
            new_mode.mode_name = md
            new_mode.description = "Mode automatically added during project creation from layers"
            modes.add(new_mode)
            new_mode.save()

        # We check if all link types exist in the project
        all_link_types = gdf["link_type"].unique()
        link_types = project.network.link_types
        current_lt = [lt.link_type for lt in link_types.all_types().values()]
        letters = [x for x in list(ascii_letters) if x not in link_types.all_types().keys()]
        all_link_types = [lt for lt in all_link_types if lt not in current_lt]
        for lt in all_link_types:
            new_link_type = link_types.new(letters[0])
            letters = letters[1:]
            new_link_type.link_type = lt
            new_link_type.description = "Link type automatically added during project creation from layers"
            new_link_type.save()

        feedback.pushInfo(" ")
        feedback.setCurrentStep(2)

        links = project.network.links

        # Now let's add all the fields we had
        for _, record in gdf.iterrows():
            new_link = links.new()

            new_link.direction = record.direction
            new_link.modes = record.modes
            new_link.link_type = record.link_type
            new_link.geometry = record.geometry
            new_link.save()

        feedback.pushInfo(" ")
        feedback.setCurrentStep(2)

        feedback.pushInfo(self.tr("Adding links"))

        feedback.pushInfo(" ")
        feedback.setCurrentStep(3)
        project.close()
        feedback.pushInfo(self.tr("Closing project"))

        return {"Output": project_path}

    def name(self):
        return "addlinksfromlayer"

    def displayName(self):
        return self.tr("Add links from layer to project")

    def group(self):
        return self.tr("1. Model Building")

    def groupId(self):
        return "modelbuilding"

    def shortHelpString(self):
        return self.tr("Take links from a layer and add them to an existing AequilibraE project")

    def createInstance(self):
        return AddLinksFromLayer()

    def tr(self, message):
        return trlt("AddLinksFromLayer", message)
