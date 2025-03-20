"""
####WORK IN PROGRESS#####
In this code you will : 
- Use xarray to read header of distant COG
- 
"""
####WORK IN PROGRESS#####
import numpy as np
import pystac_client
import rioxarray
import xarray as xr

# TODO : Define a bounding box at the edge of the 2 collections
bbox=[-75.8860,45.3157,-75.5261,45.5142] 
bbox_crs = "EPSG:4326"

# Link to ccmeo datacube stac-api
stac_root = "https://datacube.services.geo.ca/stac/api"
# Initialize the STAC client
catalog = pystac_client.Client.open(stac_root)

search = catalog.search(
	collections=['hrdem-mosaic-1m','mrdem-30'], 
    bbox=bbox,
	) 

# Load STAC items as Xarray
# This selects relevant assets from the STAC collection search results then convert them into a multi-dimensional arrays.
# The resulting dimensions are time, band, y and x. 
# No data is actually read a this stage apart from COG headers, as this is implemented as a lazy operation.
# dtm_links = []
bands = []
for page in search.pages():
    for item in page:
        print(item)
        print(item.assets['dtm'].href)
        # test = rasterio.open(item.assets['dtm'].href)
        band = rioxarray.open_rasterio(item.assets['dtm'].href, chunks=512)
        bands.append(band)




