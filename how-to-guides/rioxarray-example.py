"""
## Read a portion of a remote COG into an xarray

In this code you will : 

- Query a STAC API with pystac-client to get link to a COG;  
- Use rioxarray to read header of remote COG;
- Open the remote COG by chunks;
- Read an area of interest into an in memory Xarray object

!!! info
    This specific example uses the collection **hrdem-lidar** from CCMEO's datacube

!!! Warning 
    By default, the bbox used for clipping data inside `rio.clip_bbox()` needs to be in 
    the projected coordinate system.  
    See <https://corteva.github.io/rioxarray/stable/examples/clip_box.html#Clip-using-a-bounding-box>
"""
# --8<-- [start:code]
import pystac_client
import rioxarray

bbox=[-75.8860,45.3157,-75.5261,45.5142] 
bbox_crs = "EPSG:4326"

# Link to ccmeo datacube stac-api
stac_root = "https://datacube.services.geo.ca/stac/api"
# Initialize the STAC client
catalog = pystac_client.Client.open(stac_root)

search = catalog.search(
	collections=['mrdem-30'], 
    bbox=bbox,
	) 

# Use the rioxarray.open_rasterio() and clip it to the bbox
for page in search.pages():
    for item in page:
        band = rioxarray.open_rasterio(
            item.assets['dtm'].href, 
            chunks=512,
            ).rio.clip_box(*bbox,crs=bbox_crs)

# At this point the data is not read in the Xarray object
# See the Xarray object details
print(band)

# Now, all xarray.DataArray methods are available
print(type(band))
# >> <class 'xarray.core.dataarray.DataArray'>

# Perform analysis...

# To read the data
band.compute()
# --8<-- [end:code]



