import importlib.util as iutil
import tempfile
import sys
from pathlib import Path
from os.path import join

from qgis.core import QgsProcessingAlgorithm, QgsProcessingParameterFile, QgsProcessingParameterEnum

from qaequilibrae.i18n.translate import trlt


class ExportMatrix(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterFile(
                "src",
                self.tr("Matrix"),
                behavior=QgsProcessingParameterFile.File,
                fileFilter="*.omx, *.aem",
                defaultValue=None,
            )
        )
        self.addParameter(
            QgsProcessingParameterFile(
                "dst",
                self.tr("Output folder"),
                behavior=QgsProcessingParameterFile.Folder,
                defaultValue=None,
            )
        )
        self.addParameter(
            QgsProcessingParameterEnum(
                "output_format",
                self.tr("File format"),
                options=[".csv", ".omx", ".aem"],
                defaultValue=".csv",
            )
        )

    def processAlgorithm(self, parameters, context, model_feedback):
        # Checks if we have access to aequilibrae library
        if iutil.find_spec("aequilibrae") is None:
            sys.exit(self.tr("AequilibraE module not found"))

        from aequilibrae.matrix import AequilibraeMatrix

        file_format = ["csv", "omx", "aem"]
        format = file_format[parameters["output_format"]]
        file_name, ext = parameters["src"].split("/")[-1].split(".")
        dst_path = join(parameters["dst"], f"{file_name}.{format}")

        kwargs = {"file_path": dst_path, "memory_only": False}
        mat = AequilibraeMatrix()

        if ext == "omx":
            if format == "omx":
                mat.create_from_omx(omx_path=parameters["src"], **kwargs)
            elif format in ["csv", "aem"]:
                mat.create_from_omx(parameters["src"])
                mat.export(dst_path)
        elif ext == "aem":
            mat.load(parameters["src"])
            mat.export(dst_path)

        mat.close()

        return {"Output": dst_path}

    def name(self):
        return self.tr("Export matrices")

    def displayName(self):
        return self.tr("Export matrices")

    def group(self):
        return self.tr("Data")

    def groupId(self):
        return self.tr("Data")

    def shortHelpString(self):
        return self.tr("Export an existing *.omx or *.aem matrix file into *.csv, *.aem or *.omx")

    def createInstance(self):
        return ExportMatrix()

    def tr(self, message):
        return trlt("ExportMatrix", message)
