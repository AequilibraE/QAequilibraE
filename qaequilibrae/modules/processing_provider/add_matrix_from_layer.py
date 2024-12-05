import importlib.util as iutil
import sys
import numpy as np
import pandas as pd
from scipy.sparse import coo_matrix

from qgis.core import QgsProcessingMultiStepFeedback, QgsProcessingParameterString
from qgis.core import QgsProcessingParameterField, QgsProcessingParameterMapLayer, QgsProcessingParameterFile
from qgis.core import QgsProcessingAlgorithm

from qaequilibrae.i18n.translate import trlt


class AddMatrixFromLayer(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterMapLayer("matrix_layer", self.tr("Matrix Layer")))
        self.addParameter(
            QgsProcessingParameterField(
                "origin",
                self.tr("Origin"),
                type=QgsProcessingParameterField.Numeric,
                parentLayerParameterName="matrix_layer",
                allowMultiple=False,
                defaultValue="origin",
            )
        )
        self.addParameter(
            QgsProcessingParameterField(
                "destination",
                self.tr("Destination"),
                type=QgsProcessingParameterField.Numeric,
                parentLayerParameterName="matrix_layer",
                allowMultiple=False,
                defaultValue="destination",
            )
        )
        self.addParameter(
            QgsProcessingParameterField(
                "value",
                self.tr("Value"),
                type=QgsProcessingParameterField.Numeric,
                parentLayerParameterName="matrix_layer",
                allowMultiple=False,
                defaultValue="value",
            )
        )
        self.addParameter(
            QgsProcessingParameterFile(
                "matrix_file",
                self.tr("Output name"),
                behavior=QgsProcessingParameterFile.File,
                fileFilter="",
                defaultValue=None,
            )
        )

        self.addParameter(
            QgsProcessingParameterString("matrix_core", self.tr("Matrix core"), multiLine=False, defaultValue="Value")
        )

    def processAlgorithm(self, parameters, context, model_feedback):
        # Checks if we have access to aequilibrae library
        if iutil.find_spec("aequilibrae") is None:
            sys.exit(self.tr("AequilibraE module not found"))

        from aequilibrae.matrix import AequilibraeMatrix

        feedback = QgsProcessingMultiStepFeedback(3, model_feedback)

        origin = parameters["origin"]
        destination = parameters["destination"]
        value = parameters["value"]
        list_cores = [parameters["matrix_core"]]
        path_to_file = parameters["matrix_file"]

        # Import layer as a pandas df
        feedback.pushInfo(self.tr("Importing layer"))
        layer = self.parameterAsVectorLayer(parameters, "matrix_layer", context)

        columns = [origin, destination, value]
        data = [feat.attributes() for feat in layer.getFeatures()]

        trip_df = pd.DataFrame(data=data, columns=columns)
        feedback.pushInfo("")
        feedback.setCurrentStep(1)

        # Borrowed from AequilibraE's "create_from_trip_list"
        zones_list = sorted(set(list(trip_df[origin].unique()) + list(trip_df[destination].unique())))
        zones_df = pd.DataFrame({"zone": zones_list, "idx": list(np.arange(len(zones_list)))})

        trip_df = trip_df.merge(
            zones_df.rename(columns={"zone": origin, "idx": origin + "_idx"}), on=origin, how="left"
        ).merge(zones_df.rename(columns={"zone": destination, "idx": destination + "_idx"}), on=destination, how="left")

        nb_of_zones = len(zones_list)
        feedback.pushInfo(self.tr("{}x{} matrix imported ").format(nb_of_zones, nb_of_zones))
        feedback.pushInfo(" ")
        feedback.setCurrentStep(2)

        mat = AequilibraeMatrix()
        mat.create_empty(
            file_name=path_to_file[:-4] + ".aem", zones=nb_of_zones, matrix_names=list_cores, memory_only=False
        )

        m = (
            coo_matrix(
                (trip_df[value], (trip_df[origin + "_idx"], trip_df[destination + "_idx"])),
                shape=(nb_of_zones, nb_of_zones),
            )
            .toarray()
            .astype(np.float64)
        )

        mat.matrix[mat.names[0]][:, :] = m[:, :]
        mat.save()

        feedback.pushInfo(" ")
        feedback.setCurrentStep(3)

        return {"Output": f"{mat.name}, {mat.description} ({path_to_file})"}

    def name(self):
        return "exportmatrixasaem"

    def displayName(self):
        return self.tr("Add matrix from layer to aem file")

    def group(self):
        return self.tr("2. Data")

    def groupId(self):
        return "data"

    def shortHelpString(self):
        return "\n".join(
            [
                self.string_order(1),
                self.string_order(2),
                self.string_order(3),
                self.string_order(4),
                self.string_order(5),
            ]
        )

    def createInstance(self):
        return AddMatrixFromLayer()

    def string_order(self, order):
        if order == 1:
            return self.tr("Save a layer to an existing *.aem file. Notice that:")
        elif order == 2:
            return self.tr("- the original matrix stored in the layer needs to be in list format")
        elif order == 3:
            return self.tr("- origin and destination fields need to be integers")
        elif order == 4:
            return self.tr("- value field can be either integer or real")
        elif order == 5:
            return self.tr("- if matrix_core already exists, it will be updated and previous data will be lost")

    def tr(self, message):
        return trlt("AddMatrixFromLayer", message)
