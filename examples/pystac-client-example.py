# Code using pystac-client to search the ccmeo's datacube stac-api
import pystac_client

# Link to ccmeo datacube stac-api
stac_root = "https://datacube.services.geo.ca/stac/api"
# Initialiser le client STAC
catalog = pystac_client.Client.open(stac_root)

# Get the list of available collection id
for collection in catalog.get_collections():
    print(collection.id)

# Define search parameters
# Define a collection for filtering
# In this example, we use the mosaic collection of HRDEM tiles
collections = ['hrdem-mosaic-1m']
# We define a bounding box extent to filter the data
extent = [-79.28229773059192, 44.31501485755303, -79.1702187573089, 44.3929540402247]

# Others can be added, this example only filter on collection id
# TODO : add the link to what is available as filter
search = catalog.search(
	collections=collections, 
	bbox=extent) 

# Get the list of items for this collection
items = search.item_collection()	

# List all the link to the cogs for a specific asset
links=[]
for item in items:
	links.append(item.assets['dtm'].href)