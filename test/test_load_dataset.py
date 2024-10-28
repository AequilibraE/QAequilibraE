import pytest

from qgis.core import QgsProject
from qaequilibrae.modules.matrix_procedures.load_dataset_dialog import LoadDatasetDialog


@pytest.mark.parametrize("method", ["csv", "parquet", "open layer"])
def test_load_dialog(ae_with_project, method, folder_path, load_synthetic_future_vector, timeoutDetector):
    dialog = LoadDatasetDialog(ae_with_project)
    dialog.path = folder_path

    if method in ["csv", "parquet"]:
        dialog.load_fields_to_combo_boxes()
        dialog.cob_data_layer.setCurrentText("synthetic_future_vector")

        out_name = f"{folder_path}/synthetic_future_vector.{method}"
        dialog.load_with_file_name(out_name)

        assert dialog.worker_thread is None

    elif method == "open layer":
        layer = QgsProject.instance().mapLayersByName("synthetic_future_vector")[0]
        
        dialog.layer = layer
        dialog.radio_layer_matrix.setChecked(True)

        dialog.size_it_accordingly(True)
        dialog.cob_index_field.setCurrentText("index")
        dialog.output_name = f"{folder_path}/synthetic_future_vector.csv"
        dialog.cob_data_layer.setCurrentText("synthetic_future_vector")

        dialog.single_use = True
        dialog.load_the_vector()

    assert dialog.selected_fields == ["index", "origins", "destinations"]
    assert dialog.dataset.shape[0] == 24
    assert (dialog.dataset.sum(axis=0)["origins"] == dialog.dataset.sum(axis=0)["destinations"]) > 0
