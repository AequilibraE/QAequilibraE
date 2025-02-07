import pytest
from PyQt5.QtCore import Qt

from qaequilibrae.modules.paths_procedures.route_choice_dialog import RouteChoice


# TODO: test both algorithm selection
# @pytest.mark.parametrize("save_file", [True, False])
@pytest.mark.skip()
def test_create_choice_set(coquimbo_project, qtbot):
    dialog = RouteChoice(coquimbo_project)

    dialog.node_from.setText("71645")
    dialog.node_to.setText("79385")
    qtbot.mouseClick(dialog.but_add_node, Qt.LeftButton)
    dialog.node_from.setText("77011")
    dialog.node_to.setText("74089")
    qtbot.mouseClick(dialog.but_add_node, Qt.LeftButton)

    dialog.cob_graph_cost.setCurrentText("distance")
    dialog.chb_check_centroids.setChecked(False)
    qtbot.mouseClick(dialog.but_add_graph, Qt.LeftButton)
