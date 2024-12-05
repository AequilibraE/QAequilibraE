import pytest
import re
import pandas as pd
import numpy as np
import sqlite3
from os.path import isfile, join
from os import makedirs
from shapely.geometry import Point
from aequilibrae.matrix import AequilibraeMatrix
from aequilibrae.project import Project
from qgis.core import QgsApplication, QgsProcessingContext, QgsProcessingFeedback
from qgis.core import QgsProject, QgsField
from PyQt5.QtCore import QVariant

from qaequilibrae.modules.common_tools.data_layer_from_dataframe import layer_from_dataframe

from qaequilibrae.modules.processing_provider.provider import Provider

# from qaequilibrae.modules.processing_provider.Add_connectors import AddConnectors
from qaequilibrae.modules.processing_provider.add_links_from_layer import AddLinksFromLayer
from qaequilibrae.modules.processing_provider.add_matrix_from_layer import AddMatrixFromLayer
from qaequilibrae.modules.processing_provider.assign_pt_from_yaml import ptAssignYAML
from qaequilibrae.modules.processing_provider.assign_traffic_from_yaml import TrafficAssignYAML
from qaequilibrae.modules.processing_provider.create_matrix_from_layer import CreateMatrixFromLayer
from qaequilibrae.modules.processing_provider.create_pt_graph import CreatePTGraph
from qaequilibrae.modules.processing_provider.export_matrix import ExportMatrix
from qaequilibrae.modules.processing_provider.import_gtfs import ImportGTFS
from qaequilibrae.modules.processing_provider.matrix_calculator import MatrixCalculator
from qaequilibrae.modules.processing_provider.project_from_layer import ProjectFromLayer
from qaequilibrae.modules.processing_provider.renumber_nodes_from_layer import RenumberNodesFromLayer


def qgis_app():
    qgs = QgsApplication([], False)
    qgs.initQgis()
    yield qgs
    qgs.exitQgis()


def test_provider_exists(qgis_app):
    provider = Provider()
    QgsApplication.processingRegistry().addProvider(provider)

    registry = QgsApplication.processingRegistry()
    provider_names = [p.name().lower() for p in registry.providers()]
    assert "aequilibrae" in provider_names


@pytest.mark.parametrize("format", [0, 1, 2])
@pytest.mark.parametrize("source_file", ["sfalls_skims.omx", "demand.aem"])
def test_export_matrix(folder_path, source_file, format):
    makedirs(folder_path)
    action = ExportMatrix()

    parameters = {
        "src": f"test/data/SiouxFalls_project/matrices/{source_file}",
        "dst": folder_path,
        "output_format": format,
    }

    context = QgsProcessingContext()
    feedback = QgsProcessingFeedback()

    result = action.processAlgorithm(parameters, context, feedback)

    assert isfile(result["Output"])


def test_matrix_from_layer(folder_path):
    makedirs(folder_path)

    df = pd.read_csv("test/data/SiouxFalls_project/SiouxFalls_od.csv")
    layer = layer_from_dataframe(df, "SiouxFalls_od")

    action = AddMatrixFromLayer()

    parameters = {
        "matrix_layer": layer,
        "origin": "O",
        "destination": "D",
        "value": "Ton",
        "matrix_file": join(folder_path, "siouxfalls_od.aem"),
        "matrix_core": "MAT_CORE",
    }

    context = QgsProcessingContext()
    feedback = QgsProcessingFeedback()

    _ = action.run(parameters, context, feedback)

    assert isfile(parameters["matrix_file"])

    mat = AequilibraeMatrix()
    mat.load(parameters["matrix_file"])

    info = mat.__dict__
    assert info["names"] == [parameters["matrix_core"]]
    assert info["zones"] == 24
    assert np.sum(info["matrix"][parameters["matrix_core"]][:, :]) == 360600


# @pytest.mark.parametrize("load_sfalls_from_layer", ["tmp"], indirect=True)
# def test_project_from_layer(folder_path, load_sfalls_from_layer):

#     linkslayer = QgsProject.instance().mapLayersByName("Links layer")[0]

#     linkslayer.startEditing()
#     field = QgsField("ltype", QVariant.String)
#     linkslayer.addAttribute(field)
#     linkslayer.updateFields()

#     for feature in linkslayer.getFeatures():
#         feature["ltype"] = "road"
#         linkslayer.updateFeature(feature)

#     linkslayer.commitChanges()

#     action = ProjectFromLayer()

#     parameters = {
#         "links": linkslayer,
#         "link_id": "link_id",
#         "link_type": "ltype",
#         "direction": "direction",
#         "modes": "modes",
#         "folder": folder_path,
#         "project_name": "from_test",
#     }

#     context = QgsProcessingContext()
#     feedback = QgsProcessingFeedback()

#     result = action.run(parameters, context, feedback)

#     assert result[0]["Output"] == join(folder_path, parameters["project_name"])

#     QgsProject.instance().clear()

#     project = Project()
#     project.open(join(folder_path, parameters["project_name"]))

#     assert project.network.count_links() == 76
#     assert project.network.count_nodes() == 24


# def test_add_centroid_connector(pt_no_feed):
#     project = pt_no_feed.project
#     project_folder = project.project_base_path

#     nodes = project.network.nodes

#     cnt = nodes.new_centroid(100_000)
#     cnt.geometry = Point(-71.34, -29.95)
#     cnt.save()

#     action = AddConnectors()

#     parameters = {"num_connectors": 3, "mode": "c", "project_path": project_folder}

#     context = QgsProcessingContext()
#     feedback = QgsProcessingFeedback()

#     result = action.processAlgorithm(parameters, context, feedback)

#     assert result["Output"] == project_folder

#     node_qry = "select count(node_id) from nodes where is_centroid=1"
#     node_count = project.conn.execute(node_qry).fetchone()[0]
#     assert node_count == 1

#     link_qry = "select count(name) from links where name like 'centroid connector%'"
#     link_count = project.conn.execute(link_qry).fetchone()[0]
#     assert link_count == 3


@pytest.mark.parametrize("load_sfalls_from_layer", ["tmp"], indirect=True)
def test_renumber_from_centroids(ae_with_project, load_sfalls_from_layer):
    project = ae_with_project.project
    project_folder = project.project_base_path

    nodeslayer = QgsProject.instance().mapLayersByName("Nodes layer")[0]

    nodeslayer.startEditing()
    for feat in nodeslayer.getFeatures():
        value = feat["id"] + 1000
        nodeslayer.changeAttributeValue(feat.id(), nodeslayer.fields().indexFromName("id"), value)

    nodeslayer.commitChanges()

    action = RenumberNodesFromLayer()

    parameters = {"nodes": nodeslayer, "node_id": "id", "project_path": project_folder}

    context = QgsProcessingContext()
    feedback = QgsProcessingFeedback()

    result = action.run(parameters, context, feedback)

    assert result[0]["Output"] == project_folder

    node_qry = "select node_id from nodes;"
    node_count = project.conn.execute(node_qry).fetchall()
    node_count = [n[0] for n in node_count]
    assert node_count == list(range(1001, 1025))


def test_assign_from_yaml(ae_with_project):
    folder = ae_with_project.project.project_base_path
    file_path = join(folder, "config.yml")

    assert isfile(file_path)

    string_to_replace = "path_to_project"

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    updated_content = re.sub(re.escape(string_to_replace), folder, content)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(updated_content)

    action = TrafficAssignYAML()

    parameters = {"conf_file": file_path}

    context = QgsProcessingContext()
    feedback = QgsProcessingFeedback()

    result = action.processAlgorithm(parameters, context, feedback)

    assert result["Output"] == "Traffic assignment successfully completed"

    assert isfile(join(folder, "results_database.sqlite"))

    conn = sqlite3.connect(join(folder, "results_database.sqlite"))
    tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchone()[0]
    assert tables == "test_from_yaml"

    row = conn.execute("SELECT * FROM test_from_yaml;").fetchone()
    assert row


def test_create_pt_graph(coquimbo_project):

    project = coquimbo_project.project
    project_folder = project.project_base_path

    action = CreatePTGraph()

    parameters = {
        "project_path": project_folder,
        "access_mode": "c",
        "block_flows": False,
        "walking_edges": False,
        "outer_stops_transfers": False,
        "has_zones": False,
    }

    context = QgsProcessingContext()
    feedback = QgsProcessingFeedback()

    result = action.run(parameters, context, feedback)
    assert result[0]["Output"] == "PT graph successfully created"

    periods = project.network.periods
    assert periods.data.shape[0] == 1


@pytest.mark.parametrize("allow_map_match", [True, False])
def test_import_gtfs(pt_no_feed, allow_map_match):
    project = pt_no_feed.project
    project_folder = project.project_base_path

    action = ImportGTFS()

    parameters = {
        "project_path": project_folder,
        "gtfs_file": "test/data/coquimbo_project/gtfs_coquimbo.zip",
        "gtfs_agency": "Lisanco",
        "gtfs_date": "2016-04-16",
        "allow_map_match": allow_map_match,
    }

    context = QgsProcessingContext()
    feedback = QgsProcessingFeedback()

    result = action.run(parameters, context, feedback)
    assert result[0]["Output"] == "Traffic assignment successfully completed"
