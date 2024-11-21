from time import sleep

from .utilities import create_polygons_layer
from qaequilibrae.modules.project_procedures.adds_zones_dialog import AddZonesDialog


def test_add_zones(pt_project):
    _ = create_polygons_layer([97, 98, 99])

    dialog = AddZonesDialog(pt_project)
    dialog.chb_add_centroids.setChecked(True)

    dialog.changed_layer()
    dialog.run()

    sleep(2)

    assert len(pt_project.project.zoning.all_zones()) == 3
