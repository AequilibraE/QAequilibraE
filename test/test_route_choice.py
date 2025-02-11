import pytest
from PyQt5.QtCore import Qt

from qaequilibrae.modules.paths_procedures.route_choice_dialog import RouteChoiceDialog


# TODO: test both algorithm selection
# @pytest.mark.parametrize("save_file", [True, False])
def test_create_choice_set(coquimbo_project, qtbot):
    dialog = RouteChoiceDialog(coquimbo_project)

    # Choice set generation
    dialog.max_routes.setText("5")

    # Route choice
    dialog.cob_net_field.setCurrentText("distance")
    dialog.ln_parameter.setText("0.00011")
    qtbot.mouseClick(dialog.but_add_to_cost, Qt.LeftButton)

    dialog.ln_psl.setText("1.1")

    # Graph configuration
    dialog.chb_check_centroids.setChecked(False)

    # path = qtbot.screenshot(dialog.tabWidget.widget(0))
    # print(path)

    dialog.node_from.setText("77011")
    dialog.node_to.setText("74089")
    dialog.ln_demand.setText("1.0")

    # path = qtbot.screenshot(dialog.tabWidget.widget(1))
    # print(path)

    qtbot.mouseClick(dialog.but_visualize, Qt.LeftButton)
    # dialog.execute_single()

    # print(dialog.__dict__)


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
