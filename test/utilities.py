# coding=utf-8
"""Common functionality used by regression tests."""

import logging
import os
import sys
from shutil import copyfile
from os.path import abspath, dirname, exists, join

from PyQt5.QtCore import QVariant
from qgis.core import (
    QgsCoordinateReferenceSystem,
    QgsFeature,
    QgsField,
    QgsGeometry,
    QgsPointXY,
    QgsProject,
    QgsVectorLayer,
)


LOGGER = logging.getLogger("QGIS")
QGIS_APP = None  # Static variable used to hold hand to running QGIS app
CANVAS = None
PARENT = None
IFACE = None


def get_qgis_app():
    """Start one QGIS application to test against.

    :returns: Handle to QGIS app, canvas, iface and parent. If there are any
        errors the tuple members will be returned as None.
    :rtype: (QgsApplication, CANVAS, IFACE, PARENT)

    If QGIS is already running the handle to that app will be returned.
    """
    os.environ["QT_QPA_PLATFORM"] = "offscreen"
    sys.path.insert(0, abspath(join(dirname(dirname(__file__)), "qaequilibrae")))
    try:
        from qgis.PyQt import QtGui, QtCore
        from qgis.core import QgsApplication
        from qgis.gui import QgsMapCanvas
        from .qgis_interface import QgisInterface
    except ImportError:
        return None, None, None, None

    global QGIS_APP  # pylint: disable=W0603

    if QGIS_APP is None:
        gui_flag = True  # All test will run qgis in gui mode
        # noinspection PyPep8Naming
        QGIS_APP = QgsApplication(sys.argv, gui_flag)
        # Make sure QGIS_PREFIX_PATH is set in your env if needed!
        QGIS_APP.initQgis()
        s = QGIS_APP.showSettings()
        LOGGER.debug(s)

    global PARENT  # pylint: disable=W0603
    if PARENT is None:
        # noinspection PyPep8Naming
        PARENT = QtGui.QWidget()

    global CANVAS  # pylint: disable=W0603
    if CANVAS is None:
        # noinspection PyPep8Naming
        CANVAS = QgsMapCanvas(PARENT)
        CANVAS.resize(QtCore.QSize(400, 400))

    global IFACE  # pylint: disable=W0603
    if IFACE is None:
        # QgisInterface is a stub implementation of the QGIS plugin interface
        # noinspection PyPep8Naming
        IFACE = QgisInterface(CANVAS)

    return QGIS_APP, CANVAS, IFACE, PARENT


def load_points_vector():
    """Creates a vector layer in memory named 'Centroids' to be used with Coquimbo data."""

    nodes_layer = QgsVectorLayer("Point?crs=epsg:4326", "Centroids", "memory")
    if not nodes_layer.isValid():
        print("Nodes layer failed to load!")
    else:
        field_id = QgsField("ID", QVariant.Int)
        nodes_layer.dataProvider().addAttributes([field_id])

        field_zone_id = QgsField("zone_id", QVariant.Int)
        nodes_layer.dataProvider().addAttributes([field_zone_id])

        nodes_layer.updateFields()
        points = [
            QgsPointXY(-71.3509, -29.9393),
            QgsPointXY(-71.3182, -29.9619),
            QgsPointXY(12.4606, 41.9093),
        ]

        zone_ids = [97, 98, 99]

        features = []
        for i, (point, zone_id) in enumerate(zip(points, zone_ids)):
            feature = QgsFeature()
            feature.setGeometry(QgsGeometry.fromPointXY(point))
            feature.setAttributes([i + 1, zone_id])
            features.append(feature)

        nodes_layer.dataProvider().addFeatures(features)

        QgsProject.instance().addMapLayer(nodes_layer)


def create_links_with_matrix():
    """Creates a vector layer in memory which consists in a square with coordinates
    ((0, 0), (0, 1), (1, 1), (1, 0)), and a line which corresponds to one of its
    diagonals ((0, 0), (1, 1)). The layer has four attributes: field ID (fid), matrix_ab,
    matrix_ba, and total. It is used to test GIS plots."""

    layer = QgsVectorLayer("Linestring?crs=epsg:4326", "lines", "memory")
    if not layer.isValid():
        print("lines layer failed to load!")
    else:
        field_id = QgsField("link_id", QVariant.Int)
        matrix_ab = QgsField("matrix_ab", QVariant.Int)
        matrix_ba = QgsField("matrix_ba", QVariant.Int)
        matrix_tot = QgsField("matrix_tot", QVariant.Int)

        layer.dataProvider().addAttributes([field_id, matrix_ab, matrix_ba, matrix_tot])
        layer.updateFields()

        lines = [
            [QgsPointXY(1, 0), QgsPointXY(1, 1)],
            [QgsPointXY(1, 0), QgsPointXY(0, 0)],
            [QgsPointXY(0, 0), QgsPointXY(0, 1)],
            [QgsPointXY(0, 1), QgsPointXY(1, 1)],
            [QgsPointXY(0, 0), QgsPointXY(1, 1)],
        ]

        attributes = ([1, 2, 3, 4, 5], [50, 42, 17, 32, 19], [50, 63, 18, 32, 11], [100, 105, 35, 64, 30])

        features = []
        for i, (line, fid, ab, ba, tot) in enumerate(zip(lines, *attributes)):
            feature = QgsFeature()
            feature.setGeometry(QgsGeometry.fromPolylineXY(line))
            feature.setAttributes([fid, ab, ba, tot])
            features.append(feature)

        layer.dataProvider().addFeatures(features)

        QgsProject.instance().addMapLayer(layer)


def create_polygons_layer(parameters):
    """Creates
    To be used with Coquimbo data."""
    layer = QgsVectorLayer("Polygon?crs=epsg:4326", "polygon", "memory")
    if not layer.isValid():
        print("Polygon layer failed to load!")
    else:
        field_id = QgsField("ID", QVariant.Int)
        field_zone_id = QgsField("zone_id", QVariant.Int)
        nickname = QgsField("name", QVariant.String)

        layer.dataProvider().addAttributes([field_id, field_zone_id, nickname])
        layer.updateFields()

        polys = [
            [
                QgsPointXY(-71.2487, -29.8936),
                QgsPointXY(-71.2487, -29.8895),
                QgsPointXY(-71.2441, -29.8895),
                QgsPointXY(-71.2441, -29.8936),
                QgsPointXY(-71.2487, -29.8936),
            ],
            [
                QgsPointXY(-71.2401, -29.8945),
                QgsPointXY(-71.2401, -29.8928),
                QgsPointXY(-71.2375, -29.8928),
                QgsPointXY(-71.2375, -29.8945),
                QgsPointXY(-71.2401, -29.8945),
            ],
            [
                QgsPointXY(-71.2329, -29.8800),
                QgsPointXY(-71.2329, -29.8758),
                QgsPointXY(-71.2280, -29.8758),
                QgsPointXY(-71.2280, -29.8800),
                QgsPointXY(-71.2329, -29.8800),
            ],
        ]

        attributes = (parameters, [None, None, None])

        features = []
        for i, (poly, zone_id, name) in enumerate(zip(polys, *attributes)):
            feature = QgsFeature()
            feature.setGeometry(QgsGeometry.fromPolygonXY([poly]))
            feature.setAttributes([i + 1, zone_id, name])
            features.append(feature)

        layer.dataProvider().addFeatures(features)

        QgsProject.instance().addMapLayer(layer)

        return layer


def load_sfalls_from_layer(path):
    """Creates Sioux Falls links and nodes layers"""

    fldr_pth = "test/data/SiouxFalls_project" if path == None else path

    if fldr_pth == path:
        if not exists(fldr_pth):
            os.makedirs(fldr_pth)
        copyfile("test/data/SiouxFalls_project/SiouxFalls.gpkg", f"{fldr_pth}/SiouxFalls.gpkg")

    path_to_gpkg = f"{fldr_pth}/SiouxFalls.gpkg"

    # append the layername part
    gpkg_links_layer = path_to_gpkg + "|layername=links"
    gpkg_nodes_layer = path_to_gpkg + "|layername=nodes"

    linkslayer = QgsVectorLayer(gpkg_links_layer, "Links layer", "ogr")
    nodeslayer = QgsVectorLayer(gpkg_nodes_layer, "Nodes layer", "ogr")

    if not linkslayer.isValid():
        print("Links layer failed to load!")
    else:
        QgsProject.instance().addMapLayer(linkslayer)

    if not nodeslayer.isValid():
        print("Nodes layer failed to load!")
    else:
        QgsProject.instance().addMapLayer(nodeslayer)
        var = QgsProject.instance().mapLayersByName("Nodes layer")
        if not var[0].crs().isValid():
            crs = QgsCoordinateReferenceSystem("EPSG:4326")
            var[0].setCrs(crs)


def run_assignment(aeq_from_qgis):
    """Runs traffic assignment with Sioux Falls data."""

    from aequilibrae.paths import TrafficAssignment, TrafficClass

    project = aeq_from_qgis.project
    project.network.build_graphs()

    graph = project.network.graphs["c"]
    graph.set_graph("free_flow_time")
    graph.set_skimming(["free_flow_time", "distance"])
    graph.set_blocked_centroid_flows(False)

    demand = project.matrices.get_matrix("demand.aem")
    demand.computational_view(["matrix"])

    assigclass = TrafficClass("car", graph, demand)

    assig = TrafficAssignment()

    assig.set_classes([assigclass])
    assig.set_vdf("BPR")
    assig.set_vdf_parameters({"alpha": "b", "beta": "power"})
    assig.set_capacity_field("capacity")
    assig.set_time_field("free_flow_time")
    assig.set_algorithm("bfw")
    assig.max_iter = 5
    assig.rgap_target = 0.01
    assig.execute()

    assig.save_results("assignment")
    assig.save_skims("assignment", which_ones="all", format="omx")

    return aeq_from_qgis


def load_test_layer(folder, file_name):
    """Loads generic links and nodes layers."""

    if not exists(folder):
        os.makedirs(folder)
    copyfile(f"test/data/NetworkPreparation/{file_name}.csv", f"{folder}/{file_name}.csv")

    csv_path = f"{folder}/{file_name}.csv"

    if file_name == "link":
        uri = "file://{}?delimiter=,&crs=epsg:4326&wktField={}".format(csv_path, "geometry")
    else:
        uri = "file://{}?delimiter=,&crs=epsg:4326&xField={}&yField={}".format(csv_path, "x", "y")

    layer = QgsVectorLayer(uri, file_name, "delimitedtext")

    if not layer.isValid():
        print("Layer failed to load!")
    else:
        QgsProject.instance().addMapLayer(layer)
