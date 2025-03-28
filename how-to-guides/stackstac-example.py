"""
## Load pystac items into an Xarray

In this code you will : 

- Scrape the STAC using pystac-client to get pystac-items
- Load the `pystac-item` into Xarray.DataArray using `stackstac`
- Stream the actual data in memory with dask workflow included in `stackstac`

!!! info
    This specific example uses the collections **hrdem-mosaic-1m**
    from CCMEO's datacube

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

# --8<-- [start:code]
import pystac_client
import stackstac

# Define a bounding box for an AOI in EPSG:4326
bbox=[-71.2155,45.4012,-71.1079, 45.5083]
bbox_crs = "EPSG:4326"

# Link to ccmeo datacube stac-api
stac_root = "https://datacube.services.geo.ca/stac/api"
catalog = pystac_client.Client.open(stac_root)

search = catalog.search(
	collections=['hrdem-mosaic-1m'], 
    bbox=bbox,) 

# Re-order the proj:transform
result_items = []
# Use the pagination to improve efficiency
# Iterate over returned page and update the transform for each items
for page in search.pages():
    for item in page:
        # reorder_transform() function is define above
        reordered_transform = reorder_transform(
                                item.properties["proj:transform"]
                                )
        item.properties["proj:transform"] = reordered_transform
        result_items.append(item)

# Importing unnecessary assets may cause memory and speed issues.
# To know the assets available in this collection :
print(result_items[0].assets.keys())
# >> dict_keys(['dsm', 'dtm', 'dsm-vrt', 'dtm-vrt', 'thumbnail', 
#               'hillshade-dsm', 'hillshade-dtm', 'extent',
#               'coverage',])

items_xarray = stackstac.stack(result_items, 
                          assets = ["dsm", "dtm"], 
                          bounds_latlon = bbox, 
                          chunksize = (1000, 1000),
                          epsg = 3979,
                          properties=False)

# At this point, the metadata and array shape are set, but the data itself isn't read.
# Running .compute() allows Dask to optimize the workflow, evaluating and executing it 
# in the most efficient way, optimizing resource usage.
# # --8<-- [end:code]

# --8<-- [start:example]
# Example : Get the mean surface height for the an AOI
# Perform the difference between dsm and dtm
items_xarray['surface_height'] = items_xarray[:, 0, :, :] - items_xarray[:, 1, :, :]
# To make sure you only get canopy height, use landcover to mask non-forested area
surface_height = items_xarray.surface_height.compute()
surface_height.mean()
# --8<-- [end:example]