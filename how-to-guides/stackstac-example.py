"""
## Load pystac items into an Xarray

In this code you will : 

- Scrape the STAC using pystac-client to get pystac-items
- Load the pystac-items into Xarray using odc-stac
- Stream the actual data in memory with dask workflow included in odc-stac

!!! info
    This specific example uses the collection **hrdem-lidar** from CCMEO's datacube

"""
# --8<-- [start:transform]
def reorder_transform(gdal_transform):
    """
    Reorders the GDAL GeoTransform (6-element tuple) into the 9-element format
    that is compatible with proj:transform.
    """
    return [gdal_transform[1], gdal_transform[2], gdal_transform[0],
            gdal_transform[4], gdal_transform[5], gdal_transform[3],
            0, 0, 1]
# --8<-- [end:transform]

import pystac_client
import stackstac
