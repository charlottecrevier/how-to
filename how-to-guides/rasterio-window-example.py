"""
## Read a subset of a distant COG

In this code you will : 

- Scrape the STAC using pystac-client to get link to a COG
- Read a subset of a distant COG based on an AOI

!!! info
    This specific example uses the collection mrdem-30 from CCMEO's datacube
"""
# --8<-- [start:code]
import pystac_client
import rasterio 
from rasterio.windows import from_bounds
from rasterio.warp import transform_geom
from shapely.geometry import box, shape


# Define a bounding box for an AOI (Ottawa) in EPSG:4326
bbox=[-75.8860,45.3157,-75.5261,45.5142]
bbox_crs = "EPSG:4326"

# Link to ccmeo datacube stac-api
stac_root = "https://datacube.services.geo.ca/stac/api"
catalog = pystac_client.Client.open(stac_root)

search = catalog.search(
	collections=['mrdem-30'], 
    bbox=bbox,
	) 

# Get the link to the data asset for mrdem-30 dtm
links = []
for page in search.pages():
	for item in page:
		links.append(item.assets['dtm'].href)

print(links)
# >> ['https://datacube-prod-data-public.s3.amazonaws.com/store/elevation/mrdem/mrdem-30/mrdem-30-dtm.tif']

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
# --8<-- [end:code]




