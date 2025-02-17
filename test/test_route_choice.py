import sqlite3
from os import listdir
from os.path import join
from pathlib import Path

import numpy as np
import pytest
from aequilibrae.matrix.aequilibrae_matrix import AequilibraeMatrix
from PyQt5.QtCore import Qt
from qgis.core import QgsProject

from qaequilibrae.modules.matrix_procedures.results_lister import list_results
from qaequilibrae.modules.paths_procedures.route_choice_dialog import RouteChoiceDialog


def test_execute_single(coquimbo_project, qtbot):
    dialog = RouteChoiceDialog(coquimbo_project)

    # Choice set generation
    dialog.max_routes.setText("3")

    # Route choice
    dialog.cob_net_field.setCurrentText("distance")
    dialog.ln_parameter.setText("0.00011")
    qtbot.mouseClick(dialog.but_add_to_cost, Qt.LeftButton)

    dialog.ln_psl.setText("1.1")

    # Graph configuration
    dialog.chb_check_centroids.setChecked(False)

    # Workflow
    dialog.node_from.setText("77011")
    dialog.node_to.setText("74089")
    dialog.ln_demand.setText("1.0")

    qtbot.mouseClick(dialog.but_visualize, Qt.LeftButton)

    dialog.dlg2.exit_procedure()

    layers = list(QgsProject.instance().mapLayers().values())
    layers = [lyr.name() for lyr in layers]
    assert "route_set-77011-74089" in layers


@pytest.mark.parametrize("save", [True, False])
def test_assign_and_save(ae_with_project, qtbot, save):
    dialog = RouteChoiceDialog(ae_with_project)

    # Choice set generation
    dialog.max_routes.setText("3")

    # Route choice
    dialog.cob_net_field.setCurrentText("distance")
    dialog.ln_parameter.setText("0.01")
    qtbot.mouseClick(dialog.but_add_to_cost, Qt.LeftButton)

    dialog.ln_psl.setText("1.1")

    # Graph configuration
    dialog.chb_check_centroids.setChecked(False)

    dialog.chb_save_choice_set.setChecked(save)
    dialog.cob_matrices.setCurrentText("demand.aem")
    qtbot.mouseClick(dialog.but_perform_assig, Qt.LeftButton)

    all_folders = listdir(dialog.project.project_base_path)
    if save:
        assert "results_database.sqlite" in all_folders

        res = list_results(ae_with_project.project.project_base_path)
        assert "route_choice_uncompressed" in res["table_name"].tolist()
    else:
        assert "results_database.sqlite" not in all_folders


def test_build_and_save(ae_with_project, qtbot):
    dialog = RouteChoiceDialog(ae_with_project)

    dialog.matrices.reload()
    dialog.list_matrices()

    # Choice set generation
    dialog.max_routes.setText("3")

    # Route choice
    dialog.cob_net_field.setCurrentText("distance")
    dialog.ln_parameter.setText("0.01")
    qtbot.mouseClick(dialog.but_add_to_cost, Qt.LeftButton)

    dialog.ln_psl.setText("1.1")

    # Graph configuration
    dialog.chb_check_centroids.setChecked(False)

    dialog.cob_matrices.setCurrentText("demand.aem")
    qtbot.mouseClick(dialog.but_build_and_save, Qt.LeftButton)

    counter = 0
    all_folders = listdir(dialog.project.project_base_path)
    for folder in all_folders:
        if "origin id=" in folder:
            counter += 1

    assert counter == 24


def create_matrix(index: np.ndarray, path: str):
    names_list = ["demand"]
    zones = index.shape[0]

    mat = AequilibraeMatrix()
    mat.create_empty(zones=zones, matrix_names=names_list, memory_only=False, file_name=path)
    mat.index[:] = index[:]

    for name in names_list:
        mat.matrix[name][:, :] = np.full((zones, zones), 10.0)[:, :]

    mat.matrices.flush()


@pytest.mark.skip("Not working")
def test_sub_area_analysis(coquimbo_project, qtbot):
    pth = join(coquimbo_project.project.project_base_path, "matrices/demand.aem")
    create_matrix(np.arange(1, 134), pth)

    matrices = coquimbo_project.project.matrices
    matrices.update_database()
    matrices.reload()

    dialog = RouteChoiceDialog(coquimbo_project)

    # Select zones
    dialog.qgis_project.load_layer_by_name("zones")
    exp = '"zone_id" IN (29, 30, 31, 32, 33, 34, 37, 38, 39, 40, 49, 50, 51, 52, 57, 58, 59, 60)'
    dialog.zones_layer.selectByExpression(exp)

    dialog.matrices.reload()
    dialog.list_matrices()

    # Choice set generation
    dialog.max_routes.setText("5")
    dialog.cob_algo.setCurrentText("BFSLE")
    dialog.penalty.setText("1.02")

    # Route choice
    dialog.cob_net_field.setCurrentText("distance")
    dialog.ln_parameter.setText("0.011")
    qtbot.mouseClick(dialog.but_add_to_cost, Qt.LeftButton)

    dialog.ln_psl.setText("1.1")

    # Graph configuration
    dialog.chb_check_centroids.setChecked(False)

    # Set sub-area analysis
    dialog.chb_set_sub_area.setChecked(True)
    dialog.rdo_selected_zones.setChecked(True)

    # Execute workflow
    dialog.chb_save_choice_set.setChecked(True)
    dialog.cob_matrices.setCurrentText("b''")
    qtbot.mouseClick(dialog.but_perform_assig, Qt.LeftButton)


def test_select_link_analysis(coquimbo_project, qtbot):
    pth = join(coquimbo_project.project.project_base_path, "matrices/demand.aem")
    create_matrix(np.arange(1, 134), pth)

    matrices = coquimbo_project.project.matrices
    matrices.update_database()
    matrices.reload()

    dialog = RouteChoiceDialog(coquimbo_project)

    dialog.matrices.reload()
    dialog.list_matrices()

    # Choice set generation
    dialog.max_routes.setText("5")
    dialog.cob_algo.setCurrentText("BFSLE")
    dialog.penalty.setText("1.00")

    # Route choice
    dialog.cob_net_field.setCurrentText("distance")
    dialog.ln_parameter.setText("0.011")
    qtbot.mouseClick(dialog.but_add_to_cost, Qt.LeftButton)

    dialog.ln_psl.setText("1.1")

    # Graph configuration
    dialog.chb_check_centroids.setChecked(False)

    # Set select link analysis
    dialog.chb_set_select_link.setChecked(True)
    dialog.ln_qry_name.setText("sl1")
    dialog.ln_link_id.setText("7369")
    dialog.cob_direction.setCurrentText("AB")
    qtbot.mouseClick(dialog.but_add_qry, Qt.LeftButton)
    dialog.ln_link_id.setText("20983")
    dialog.cob_direction.setCurrentText("AB")
    qtbot.mouseClick(dialog.but_add_qry, Qt.LeftButton)
    qtbot.mouseClick(dialog.but_save_qry, Qt.LeftButton)
    dialog.ln_qry_name.setText("sl2")
    dialog.ln_link_id.setText("7369")
    dialog.cob_direction.setCurrentText("AB")
    qtbot.mouseClick(dialog.but_add_qry, Qt.LeftButton)
    qtbot.mouseClick(dialog.but_save_qry, Qt.LeftButton)
    dialog.ln_mat_name.setText("select_link_analysis")

    # Execute workflow
    dialog.chb_save_choice_set.setChecked(True)
    dialog.cob_matrices.setCurrentText("b''")
    qtbot.mouseClick(dialog.but_perform_assig, Qt.LeftButton)

    matrices = listdir(dialog.project.matrices.fldr)
    assert "select_link_analysis.omx" in matrices

    pth = Path(dialog.project.project_base_path)
    conn = sqlite3.connect(pth / "results_database.sqlite")
    results = [x[0] for x in conn.execute("SELECT name FROM sqlite_master WHERE type ='table'").fetchall()]
    assert "select_link_analysis_uncompressed" in results


# dialog.ln_parameter.setText("0,15")
# qtbot.mouseClick(dialog.but_add_to_cost, Qt.LeftButton)
# messagebar = dialog.iface.messageBar()
# assert messagebar.messages[1][-1] == 'Input error:Wrong value in parameter.'

# dialog.ln_parameter.setText("abc")
# qtbot.mouseClick(dialog.but_add_to_cost, Qt.LeftButton)
# messagebar = dialog.iface.messageBar()
# assert messagebar.messages[1][-1] == 'Input error:Wrong value in parameter.'

# dialog.ln_parameter.setText("")
# qtbot.mouseClick(dialog.but_add_to_cost, Qt.LeftButton)
# messagebar = dialog.iface.messageBar()
# assert messagebar.messages[1][-1] == 'Input error:Check parameter value.'
