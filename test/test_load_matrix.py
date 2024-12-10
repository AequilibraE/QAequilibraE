import numpy as np
import pandas as pd
from PyQt5.QtCore import QTimer

from qaequilibrae.modules.common_tools.data_layer_from_dataframe import layer_from_dataframe
from qaequilibrae.modules.matrix_procedures.load_matrix_dialog import LoadMatrixDialog


def test_matrix_menu(ae_with_project, qtbot, timeoutDetector):
    from qaequilibrae.modules.matrix_procedures.load_matrix_dialog import LoadMatrixDialog
    from test.test_qaequilibrae_menu_with_project import check_if_new_active_window_matches_class

    def handle_trigger():
        check_if_new_active_window_matches_class(qtbot, LoadMatrixDialog)

    action = ae_with_project.menuActions["Data"][1]
    assert action.text() == "Import matrices", "Wrong text content"
    QTimer.singleShot(10, handle_trigger)
    action.trigger()


# TODO: test removing the matrices
def test_save_matrix(ae_with_project, folder_path, timeoutDetector):
    file_name = f"{folder_path}/test_matrix.aem"

    df = pd.read_csv("test/data/SiouxFalls_project/SiouxFalls_od.csv")
    _ = layer_from_dataframe(df, "open_layer")

    dialog = LoadMatrixDialog(ae_with_project)
    dialog.sparse = True
    dialog.output_name = file_name
    dialog.field_from.setCurrentText("O")
    dialog.field_to.setCurrentText("D")
    dialog.field_cells.setCurrentText("Ton")
    dialog.has_errors()
    dialog.worker_thread.signal.connect(dialog.signal_handler)
    dialog.worker_thread.doWork()
    dialog.worker_thread.report = None
    dialog.build_worker_thread()
    dialog.worker_thread.doWork()

    from aequilibrae.matrix import AequilibraeMatrix

    mat = AequilibraeMatrix()
    mat.load(file_name)

    assert mat.matrix["ton"].shape == (24, 24)
    assert np.sum(np.nan_to_num(mat.matrix["ton"])[:, :]) == 360600
    assert (mat.index == np.arange(1, 25)).all()

    dialog.close()
