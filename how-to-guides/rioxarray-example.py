"""
## Stream data using rioxarray

In this code you will : 

- Use xarray to read header of distant COG
- Open the distant COG by chunks
- Read an area of interest into a Xarray in memory

!!! info
    This specific example uses the collection **hrdem-lidar** from CCMEO's datacube

!!! Warning 
    By default, the bbox used for clipping data inside rio.clip_bbox() needs to be in 
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

bands = []
for page in search.pages():
    for item in page:
        print(item)
        print(item.assets['dtm'].href)
        band = rioxarray.open_rasterio(
            item.assets['dtm'].href, 
            chunks=512,
            ).rio.clip_box(*bbox,crs=bbox_crs)
# --8<-- [end:code]



