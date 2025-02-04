"""
In this code you will : 
- Scrape the STAC using pystac-client to get link to a COG
- Read header metadata from a distant COG file
- Read a subset of a distant COG based on an AOI

Ressources : 
# https://rasterio.readthedocs.io/en/latest/quickstart.html
"""

import pystac_client
import rasterio 
from rasterio.windows import from_bounds
from rasterio.warp import transform_geom
from shapely.geometry import box, shape


# Define a bounding box for an AOI (Ottawa) in EPSG:4326
bbox=[-75.8860,45.3157,-75.5261,45.5142]
bbox_crs = "EPSG:4326"

# Get the link to the mrdem-30 dtm cog 
# Link to ccmeo datacube stac-api
stac_root = "https://datacube.services.geo.ca/stac/api"
# Initialiser le client STAC
catalog = pystac_client.Client.open(stac_root)

search = catalog.search(
	collections=['mrdem-30'], 
    bbox=bbox,
	) 

# Get the link to the data asset for mrdem-30 dtm
links = []
for item in search.items():
    links.append(item.get_assets(role='data')['dtm'].href)

print(links)
# >> ['https://datacube-prod-data-public.s3.amazonaws.com/store/elevation/mrdem/mrdem-30/mrdem-30-dtm.tif']

# REad the header of a distant COG 
with rasterio.open(links[0]) as src:
    # Read the header of a COG
    print(src.tags())
    # >> {'AREA_OR_POINT': 'Area', 'TIFFTAG_DATETIME': '2024:06:13 12:00:00'}
    print(src.profile)
    # >> {'driver': 'GTiff', 'dtype': 'float32', 'nodata': -32767.0, 'width': 183687, 'height': 159655, 'count': 1, 'crs': CRS.from_epsg(3979), 'transform': Affine(30.0, 0.0, -2454000.0,
    #    0.0, -30.0, 3887400.0), 'blockxsize': 512, 'blockysize': 512, 'tiled': True, 'compress': 'lzw', 'interleave': 'band'}

# Read the COG for AOI
with rasterio.open(links[0]) as src:
    # Transform bbox to src EPSG
    transformed_bbox = shape(transform_geom(src.crs, bbox_crs, box(*bbox))).bounds
    # Define the window to read the values
    window=from_bounds(transformed_bbox[0], transformed_bbox[1], 
                       transformed_bbox[2], transformed_bbox[3], src.transform)
    # Read value from file
    rst = src.read(1, window=window)

# Perfom analysis ...

# TODO : add the wrtting of the final array to a tiff file





