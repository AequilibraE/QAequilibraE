import pandas as pd
import geopandas as gpd

from qgis.core import QgsVectorLayer


def geodataframe_from_layer(layer: QgsVectorLayer) -> gpd.GeoDataFrame:
    """Creates a gpd.GeoDataFrame from a data layer."""

    data = []
    geoms = []

    for feat in layer.getFeatures():
        data.append(feat.attributes())
        geoms.append(feat.geometry().asWkt())

    columns = [field.name() for field in layer.fields()]

    df = pd.DataFrame(data, columns=columns)

    df = gpd.GeoDataFrame(df, geometry=gpd.GeoSeries.from_wkt(geoms), crs=layer.crs().authid())
    df["geoms"] = df["geometry"].to_wkb()

    return df
