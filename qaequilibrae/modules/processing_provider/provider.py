__author__ = "Arthur Evrard"

from os.path import join
import sys
from pathlib import Path

from qgis.core import QgsProcessingProvider
from qgis.PyQt.QtGui import QIcon

provider_path = Path(__file__).parent.parent.parent
if str(provider_path) not in sys.path:
    sys.path.append(str(provider_path))


class Provider(QgsProcessingProvider):

    def loadAlgorithms(self):
        from .project_from_layer import ProjectFromLayer
        from .project_from_osm import ProjectFromOSM

        # from .Add_connectors import AddConnectors
        from .assign_traffic_from_yaml import TrafficAssignYAML
        from .export_matrix import ExportMatrix
        from .create_matrix_from_layer import CreateMatrixFromLayer
        from .add_matrix_from_layer import AddMatrixFromLayer
        from .add_links_from_layer import AddLinksFromLayer
        from .renumber_nodes_from_layer import RenumberNodesFromLayer
        from .matrix_calculator import MatrixCalculator
        from .import_gtfs import ImportGTFS
        from .create_pt_graph import CreatePTGraph
        from .assign_pt_from_yaml import ptAssignYAML

        self.addAlgorithm(ProjectFromOSM())
        self.addAlgorithm(ProjectFromLayer())
        self.addAlgorithm(CreateMatrixFromLayer())
        self.addAlgorithm(AddMatrixFromLayer())
        self.addAlgorithm(MatrixCalculator())
        self.addAlgorithm(ExportMatrix())
        self.addAlgorithm(AddLinksFromLayer())
        self.addAlgorithm(RenumberNodesFromLayer())
        # self.addAlgorithm(AddConnectors())
        self.addAlgorithm(TrafficAssignYAML())
        self.addAlgorithm(ImportGTFS())
        self.addAlgorithm(CreatePTGraph())
        self.addAlgorithm(ptAssignYAML())

    def id(self):
        """The ID used for identifying the provider.
        This string should be a unique, short, character only string,
        eg "qgis" or "gdal". This string should not be localised.
        """
        return "aequilibrae"

    def name(self):
        """The human friendly name of the plugin in Processing.
        This string should be as short as possible (e.g. "Lastools", not
        "Lastools version 1.0.1 64-bit") and localised.
        """
        return "AequilibraE"

    def icon(self):
        """Should return a QIcon which is used for your provider inside
        the Processing toolbox.
        """
        return QIcon(join(provider_path, "icon.png"))
