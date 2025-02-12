import pytest
import numpy as np
from os import listdir
from PyQt5.QtCore import Qt
from qgis.core import QgsProject

from aequilibrae.matrix import AequilibraeMatrix

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

    counter = 0
    layers = list(QgsProject.instance().mapLayers().values())
    for layer in layers:
        if "route_set" in layer.name():
            counter += 1

    assert counter == 3


def create_matrix(index: np.ndarray, path: str):
    names_list = ["demand"]
    zones = index.shape[0]

    mat = AequilibraeMatrix()
    mat.create_empty(zones=zones, matrix_names=names_list, memory_only=False, file_name=path)
    mat.index = index[:]
    mat.matrices[:, :, 0] = np.random.randint(1, 11, size=(zones, zones))[:, :]
    mat.matrices.flush()


@pytest.mark.parametrize("save", [True, False])
def test_assign_and_save(ae_with_project, qtbot, save):
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

    dialog.chb_save_choice_set.setChecked(save)
    dialog.cob_matrices.setCurrentText("demand.aem")
    qtbot.mouseClick(dialog.but_perform_assig, Qt.LeftButton)

    counter = 0
    all_folders = listdir(dialog.project.project_base_path)
    for folder in all_folders:
        if "origin id=" in folder:
            counter += 1

    if save:
        assert counter == 24
    else:
        assert counter == 0


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
