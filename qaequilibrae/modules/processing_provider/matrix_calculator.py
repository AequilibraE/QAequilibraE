import importlib.util as iutil
import sys
import textwrap
import yaml

from qgis.core import QgsProcessingAlgorithm, QgsProcessingMultiStepFeedback, QgsProcessingParameterFile
from qgis.core import (
    QgsProcessingParameterDefinition,
    QgsProcessingParameterFileDestination,
    QgsProcessingParameterString,
)

from qaequilibrae.i18n.translate import trlt


class MatrixCalculator(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.operation_map = {
            "min(": "np.min(",
            "max(": "np.max(",
            "abs(": "np.absolute(",
            "ln(": "np.log(",
            "exp(": "np.exp(",
            "power(": "np.power(",
            "null_diag(": "np.null_diag(",
        }

        self.addParameter(
            QgsProcessingParameterFile(
                "conf_file",
                self.tr("Matrix configuration file (.yaml)"),
                behavior=QgsProcessingParameterFile.File,
                fileFilter="",
                defaultValue=None,
            )
        )
        self.addParameter(
            QgsProcessingParameterString("procedure", self.tr("Matrix core"), multiLine=True, defaultValue="")
        )
        self.addParameter(
            QgsProcessingParameterString("matrix_core", self.tr("Matrix core"), multiLine=False, defaultValue="matrix")
        )
        self.addParameter(
            QgsProcessingParameterFileDestination("file_name", self.tr("File name"), "AequilibraE Matrix (*.aem)")
        )

        advparams = [
            QgsProcessingParameterString(
                "filtering_matrix", self.tr("Filtering matrix"), multiLine=False, optional=True, defaultValue=None
            )
        ]

        for param in advparams:
            param.setFlags(param.flags() | QgsProcessingParameterDefinition.FlagAdvanced)
            self.addParameter(param)

    def processAlgorithm(self, parameters, context, model_feedback):
        # Checks if we have access to aequilibrae library
        if iutil.find_spec("aequilibrae") is None:
            sys.exit(self.tr("AequilibraE module not found"))

        from aequilibrae.matrix import AequilibraeMatrix

        feedback = QgsProcessingMultiStepFeedback(4, model_feedback)
        feedback.pushInfo(self.tr("Getting matrices from configuration file"))

        with open(parameters["conf_file"], "r") as f:
            params = yaml.safe_load(f)

        # Load matrices
        matrices = {}
        index = []
        for matrix in params:
            for name, values in matrix.items():
                mat = AequilibraeMatrix()
                mat.load(values["matrix_path"])
                matrices[name] = mat.get_matrix(values["matrix_core"])
                index[:] = mat.index[:]
                mat.close()

        expression = parameters["procedure"]

        # Replace the expression for matrices variables
        for key in matrices.keys():
            if key in expression:
                expression = expression.replace(key, f"matrices['{key}']")

        # Replace the expression for numpy operations
        for key in self.operation_map.keys():
            if key in expression:
                expression = expression.replace(key, self.operation_map[key])

        out = eval(expression)

        mat = AequilibraeMatrix()
        mat.create_empty(
            file_name=parameters["file_name"],
            zones=len(index),
            matrix_names=[parameters["matrix_core"]],
            memory_only=False,
        )
        mat.matrix[parameters["matrix_core"]][:, :] = out[:, :]
        mat.index[:] = index[:]
        mat.close()

        return {"Output": "Finished"}

    def name(self):
        return "matrixcalc"

    def displayName(self):
        return self.tr("Matrix calculator")

    def group(self):
        return self.tr("2. Data")

    def groupId(self):
        return "data"

    def shortHelpString(self):
        return textwrap.dedent(
            "\n".join(
                [
                    self.string_order(1),
                    self.string_order(2),
                    self.string_order(3),
                    self.string_order(4),
                    self.string_order(5),
                    self.string_order(6),
                    self.string_order(7),
                ]
            )
        )

    def createInstance(self):
        return MatrixCalculator()

    def string_order(self, order):
        if order == 1:
            return self.tr("Run a matrix calculation based on a request and a matrix config file (.yaml) :")
        elif order == 2:
            return self.tr("- Matrix configuration file (.yaml file)")
        elif order == 3:
            return (
                self.tr("- Request as a formula, example : ")
                + "null_diag( abs( max( t(matA)-(matB*3), zeros ) + power(matC,2) ) )"
            )
        elif order == 4:
            return self.tr("- .aem file and matrix core to store calculated matrix")
        elif order == 5:
            return self.tr(
                "- filtering matrix, a matrix of 0 and 1 defined in matrix config file that will be used to update only a part of the destination matrix "
            )
        elif order == 6:
            return self.tr("Example of valid matrix configuration file:")
        elif order == 7:
            return textwrap.dedent(
                """\
                Matrices:
                    - generation:
                        matrix_path: D:/AequilibraE/Project/matrices/socioeconomic_2024.aem
                        matrix_core: generation
                    - pop2024:
                        matrix_path: D:/AequilibraE/Project/matrices/socioeconomic_2024.aem
                        matrix_core: pop_dest
                    - emp2024:
                        matrix_path: D:/AequilibraE/Project/matrices/socioeconomic_2024.aem
                        matrix_core: emp_dest
                    - gen_time:
                        matrix_path: D:/AequilibraE/Project/matrices/aon_skims.aem
                        matrix_core: gen_time
               """
            )

    def tr(self, message):
        return trlt("MatrixCalculator", message)
