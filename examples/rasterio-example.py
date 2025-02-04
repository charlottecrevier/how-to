import pystac_client
import rasterio 
from rasterio.windows import from_bounds
# Simple read ideas :
# 1. Read the header of the mrdem-30m cog file
# 2. Read the values for a AOI
# 3. Read pixel value of different places in hrdem-mosaic-1m (transect) and 
# make a graph to show elevation

# Read the header of a distant COG
# We will be using the tile we got 


# Define a bounding box for an AOI (Ottawa)
bbox=[-75.8860,45.3157,-75.5261,45.5142]

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
# ['https://datacube-prod-data-public.s3.amazonaws.com/store/elevation/mrdem/mrdem-30/mrdem-30-dtm.tif']

with rasterio.open(links[0]) as src:
    print(src.meta)
    rst = src.read(1, window=from_bounds(bbox[0], bbox[1], bbox[2], bbox[3], src.transform))



