from os import listdir

import pytest
from PyQt5.QtCore import Qt
from qgis.core import QgsProject

from qaequilibrae.modules.matrix_procedures.results_lister import list_results
from qaequilibrae.modules.paths_procedures.route_choice_dialog import RouteChoiceDialog


@pytest.mark.skip("The addition of dlg2 is breaking the test")
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

    layers = list(QgsProject.instance().mapLayers().values())
    layers = [lyr.name() for lyr in layers]
    assert "route_set-77011-74089" in layers


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
