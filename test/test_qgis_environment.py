from qgis.core import QgsProviderRegistry

from .utilities import get_qgis_app


def test_qgis_environment():
    """QGIS environment has the expected providers"""

    _ = get_qgis_app()

    prov_reg = QgsProviderRegistry.instance()

    assert len(prov_reg.providerList()) > 20, "Missing too many providers"
    assert "spatialite" in prov_reg.providerList()
