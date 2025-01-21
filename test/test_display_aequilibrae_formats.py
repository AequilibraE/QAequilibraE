import os
import numpy as np
import pytest
import sys

from qgis.core import QgsProject

from qaequilibrae.modules.matrix_procedures.display_aequilibrae_formats_dialog import DisplayAequilibraEFormatsDialog


pytestmark = pytest.mark.skipif(sys.platform.startswith("win"), reason="Running on Windows")


def test_display_data_no_path(ae, mocker):
    function = "qaequilibrae.modules.matrix_procedures.display_aequilibrae_formats_dialog.DisplayAequilibraEFormatsDialog.get_file_name"
    mocker.patch(function, return_value=(None, None))

    dialog = DisplayAequilibraEFormatsDialog(ae)
    dialog.close()

    messagebar = ae.iface.messageBar()
    error_message = "Error::Path provided is not a valid dataset"
    assert messagebar.messages[1][-1] == error_message, "Level 1 error message is missing"


@pytest.mark.parametrize(
    ("has_project", "path"),
    [
        (True, "matrices/demand.aem"),
        (False, "matrices/demand.aem"),
        (True, "matrices/SiouxFalls.omx"),
        (False, "matrices/SiouxFalls.omx"),
    ],
)
def test_display_data_with_path(tmpdir, ae_with_project, mocker, has_project, path):
    file_path = f"test/data/SiouxFalls_project/{path}"
    name, extension = path.split(".")
    file_func = "qaequilibrae.modules.matrix_procedures.display_aequilibrae_formats_dialog.DisplayAequilibraEFormatsDialog.get_file_name"
    mocker.patch(file_func, return_value=(file_path, extension.upper()))

    if "/" in name:
        _, name = name.split("/")
    out_func = "qaequilibrae.modules.matrix_procedures.display_aequilibrae_formats_dialog.DisplayAequilibraEFormatsDialog.csv_file_path"
    mocker.patch(out_func, return_value=f"{tmpdir}/{name}.csv")

    dialog = DisplayAequilibraEFormatsDialog(ae_with_project, file_path, has_project)
    dialog.export()
    dialog.exit_procedure()

    assert np.sum(dialog.data_to_show.matrix["matrix"]) == 360600
    assert "matrix" in dialog.list_cores
    assert "taz" in dialog.list_indices
    assert dialog.error is None
    assert dialog.data_type == extension.upper()
    assert os.path.isfile(f"{tmpdir}/{name}.csv")


# TODO: Ideally, we would test if the visualization is working
@pytest.mark.parametrize("element", ["row", "columns"])
def test_select_elements(ae_with_project, mocker, element):
    file_path = "test/data/SiouxFalls_project/matrices/sfalls_skims.omx"
    _, extension = file_path.split(".")
    file_func = "qaequilibrae.modules.matrix_procedures.display_aequilibrae_formats_dialog.DisplayAequilibraEFormatsDialog.get_file_name"
    mocker.patch(file_func, return_value=(file_path, extension.upper()))

    dialog = DisplayAequilibraEFormatsDialog(ae_with_project, "", True)
    dialog.no_mapping.setChecked(False)
    if element == "row":
        dialog.by_row.setChecked(True)
        dialog.table.selectRow(0)
    else:
        dialog.by_col.setChecked(True)
        dialog.table.selectColumn(0)

    dialog.exit_procedure()

    # For both columns and rows
    existing_layers = [vector.name() for vector in QgsProject.instance().mapLayers().values()]
    assert "matrix_row" in existing_layers

    layer = QgsProject.instance().mapLayersByName("zones")[0]
    field_names = [field.name() for field in layer.fields()]
    assert "metrics_data" in field_names

    metrics = [round(feat["metrics_data"], 0) for feat in layer.getFeatures()]
    assert metrics == [0.0, 6.0, 4.0]

    dialog.omx.close()
