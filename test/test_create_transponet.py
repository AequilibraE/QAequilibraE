from os.path import join
from shutil import copytree
from uuid import uuid4

from aequilibrae import Project

from qgis.PyQt import QtWidgets
from qgis.core import QgsProject

from .utilities import load_test_layer
from qaequilibrae.modules.project_procedures.creates_transponet_dialog import CreatesTranspoNetDialog
from qaequilibrae.modules.project_procedures.creates_transponet_procedure import CreatesTranspoNetProcedure


def test_dialog(ae, tmp_path):
    path = join(tmp_path, uuid4().hex)
    copytree("test/data/NetworkPreparation", path)

    load_test_layer(path, "node")
    load_test_layer(path, "link")

    dialog = CreatesTranspoNetDialog(ae)
    dialog.project_destination.setText(path)

    links_columns = [
        "link_id",
        "a_node",
        "b_node",
        "direction",
        "distance",
        "modes",
        "link_type",
        "link_id",
        "a_node",
        "b_node",
        "direction",
        "distance",
        "modes",
        "link_type",
    ]
    nodes_columns = ["node_id", "is_centroid", "node_id", "is_centroid"]

    child = dialog.findChildren(QtWidgets.QComboBox)
    links_chd = []
    nodes_chd = []
    for chd in child:
        if chd.count() == 8:
            links_chd.append(chd)
        elif chd.count() == 4:
            nodes_chd.append(chd)

    for idx, chd in enumerate(links_chd):
        i = chd.findText(links_columns[idx])
        chd.setCurrentIndex(i)

    for idx, chd in enumerate(nodes_chd):
        i = chd.findText(nodes_columns[idx])
        chd.setCurrentIndex(i)

    dialog.create_net()

    QgsProject.instance().removeAllMapLayers()

    # Test assertions
    project = Project()
    project.open(dialog.worker_thread.proj_folder)

    project_links = project.network.links.data
    assert project_links.shape[0] == 4

    project_nodes = project.network.nodes.data
    assert project_nodes.shape[0] == 4
    assert project_nodes[project_nodes["is_centroid"] == 1].shape[0] == 2

    link_types = project.network.link_types
    assert "a" in link_types.all_types().keys()

    modes = project.network.modes
    for mode in ["a", "r", "x"]:
        assert mode in modes.all_modes().keys()


def test_procedure(ae, tmp_path):
    path = join(tmp_path, uuid4().hex)
    copytree("test/data/NetworkPreparation", path)

    load_test_layer(path, "node")
    load_test_layer(path, "link")

    nodes = QgsProject.instance().mapLayersByName("node")[0]
    links = QgsProject.instance().mapLayersByName("link")[0]

    links_fields = {
        "link_id": 7,
        "a_node": 0,
        "b_node": 1,
        "direction": 2,
        "distance": 3,
        "modes": 4,
        "link_type": 5,
        "name": -1,
        "cycleway": -1,
        "cycleway_right": -1,
        "cycleway_left": -1,
        "busway": -1,
        "busway_right": -1,
        "busway_left": -1,
        "lanes_ab": -1,
        "lanes_ba": -1,
        "capacity_ab": -1,
        "capacity_ba": -1,
        "speed_ab": -1,
        "speed_ba": -1,
    }
    nodes_fields = {"node_id": 0, "is_centroid": 1}

    proj_folder = join(path, "project")
    parent = CreatesTranspoNetDialog(ae)
    dialog = CreatesTranspoNetProcedure(parent, proj_folder, nodes, nodes_fields, links, links_fields)
    dialog.doWork()

    project = Project()
    project.open(proj_folder)

    project_links = project.network.links.data
    assert project_links.shape[0] == 4

    project_nodes = project.network.nodes.data
    assert project_nodes.shape[0] == 4
    assert project_nodes[project_nodes["is_centroid"] == 1].shape[0] == 2

    link_types = project.network.link_types
    assert "a" in link_types.all_types().keys()

    modes = project.network.modes
    for mode in ["a", "r", "x"]:
        assert mode in modes.all_modes().keys()
