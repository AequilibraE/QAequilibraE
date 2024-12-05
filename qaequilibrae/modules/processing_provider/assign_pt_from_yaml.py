import importlib.util as iutil
import sys
import textwrap

from datetime import datetime as dt

from qgis.core import QgsProcessingAlgorithm, QgsProcessingMultiStepFeedback, QgsProcessingParameterFile
from qgis.core import QgsProcessingParameterDefinition, QgsProcessingParameterBoolean

from qaequilibrae.i18n.translate import trlt


class ptAssignYAML(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterFile(
                "conf_file",
                self.tr("Configuration file (.yaml)"),
                behavior=QgsProcessingParameterFile.File,
                fileFilter="",
                defaultValue=None,
            )
        )

        advparameters = [
            QgsProcessingParameterBoolean(
                "datetime_to_resultname", self.tr("Include current datetime to result name"), defaultValue=True
            )
        ]

        for param in advparameters:
            param.setFlags(param.flags() | QgsProcessingParameterDefinition.FlagAdvanced)
            self.addParameter(param)

    def processAlgorithm(self, parameters, context, model_feedback):
        feedback = QgsProcessingMultiStepFeedback(5, model_feedback)

        # Checks if we have access to aequilibrae library
        if iutil.find_spec("aequilibrae") is None:
            sys.exit(self.tr("AequilibraE module not found"))

        from aequilibrae.paths import TransitAssignment, TransitClass
        from aequilibrae.project import Project
        from aequilibrae.matrix import AequilibraeMatrix
        from aequilibrae.project.database_connection import database_connection
        from aequilibrae.transit.transit_graph_builder import TransitGraphBuilder
        import yaml

        feedback.pushInfo(self.tr("Getting parameters from YAML"))

        pathfile = parameters["conf_file"]
        with open(pathfile, "r") as f:
            params = yaml.safe_load(f)

        feedback.pushInfo(" ")
        feedback.setCurrentStep(1)

        # Opening project
        feedback.pushInfo(self.tr("Opening project"))

        project = Project()
        project.open(params["project_path"])
        project.network.build_graphs()

        # Load PT Graph
        pt_con = database_connection("transit")
        params["graph"]["public_transport_conn"] = pt_con

        graph_db = TransitGraphBuilder.from_db(**params["graph"])
        graph_db.create_graph()
        graph_db.create_line_geometry(method="connector project match", graph="c")

        graph = graph_db.to_transit_graph()

        # Load AequilibraE Matrix
        mat = AequilibraeMatrix()
        mat.load(params["matrix_path"])
        mat.computational_view()

        feedback.pushInfo(" ")
        feedback.setCurrentStep(2)

        # Setting up assignment
        feedback.pushInfo(self.tr("Setting up assignment"))

        # Create the assignment class
        assigclass = TransitClass(name="pt", graph=graph, matrix=mat)
        assigclass.set_demand_matrix_core(params["matrix_core"])

        # Create PT Assignment object
        assig = TransitAssignment()
        assig.add_class(assigclass)
        assig.set_time_field(params["assignment"]["time_field"])
        assig.set_frequency_field(params["assignment"]["frequency"])
        assig.set_algorithm(params["assignment"]["algorithm"])

        feedback.pushInfo(" ")
        feedback.setCurrentStep(3)

        # Running assignment
        feedback.pushInfo(self.tr("Running assignment"))
        assig.execute()
        feedback.pushInfo(" ")
        feedback.setCurrentStep(4)

        # Saving outputs
        feedback.pushInfo(self.tr("Saving outputs"))
        if str(parameters["datetime_to_resultname"]) == "True":
            params["result_name"] = params["result_name"] + dt.now().strftime("_%Y-%m-%d_%Hh%M")
        assig.save_results(params["result_name"])

        feedback.pushInfo(" ")
        feedback.setCurrentStep(5)

        project.close()

        return {"Output": "PT assignment successfully completed"}

    def name(self):
        return "ptassignfromyaml"

    def displayName(self):
        return self.tr("PT assignment from file")

    def group(self):
        return self.tr("4. Public Transport")

    def groupId(self):
        return "publictransport"

    def shortHelpString(self):
        return textwrap.dedent("\n".join([self.string_order(1), self.string_order(2), self.string_order(3)]))

    def createInstance(self):
        return ptAssignYAML()

    def string_order(self, order):
        if order == 1:
            return self.tr("Run a pt assignment using a YAML configuration file.")
        elif order == 2:
            return self.tr("Example of valid configuration file:")
        elif order == 3:
            return textwrap.dedent(
                """\
                project: D:/AequilibraE/Project/
                
                result_name: sce_from_yaml
                
                transit_classes:
                    - student:
                        matrix_path: D:/AequilibraE/Project/matrices/demand.aem
                        matrix_core: student_pt
                        blocked_centroid_flows: True
                        skims: travel_time, distance
                    - worker:
                        matrix_path: D:/AequilibraE/Project/matrices/demand.aem
                        matrix_core: worker_pt
                        blocked_centroid_flows: True
                        
                assignment:
                    period_id: 1
                """
            )

    def tr(self, message):
        return trlt("ptAssignYAML", message)
