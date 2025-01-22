from qgis.utils import iface

from qaequilibrae.qaequilibrae import AequilibraEMenu
from .utilities import get_qgis_app


def test_if_dialog_opens():
    """Test we can click OK."""

    _ = get_qgis_app()

    dialog = AequilibraEMenu(iface)

    assert dialog is not None
