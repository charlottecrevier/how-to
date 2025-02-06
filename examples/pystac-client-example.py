"""
# How to use pystac-client to get a list of tile(s) from the hrdem-mosaic-2m

In this example you will learn how to :   
 - Queries the ccmeo datacube STAC API with pystac-client to get the available collection;    
 - Queries the ccmeo datacube STAC API with pystac-client with a subset of filter;   
 - Access the data href for the specific filter.  
	# TODO : create a list of file returned

"""
# Import the library needed
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
collections = ['hrdem-mosaic-2m']
# We define a bounding box extent to filter the data
extent = [-79.28229773059192, 44.31501485755303, -79.1702187573089, 44.3929540402247]

# TODO : add the link to what is available as filter
search = catalog.search(
	collections=collections, 
	bbox=extent
	) 

## Basic example of accessing COG's link for the DTM ##
# https://pystac-client.readthedocs.io/en/stable/usage.html#itemsearch

# Get the list of items for this collection
items = search.item_collection()	

# List all the link to the cogs for a specific asset
links=[]
for item in items:
	links.append(item.assets['dtm'].href)

# Depending on your request, you might want to consider using the 
# pagination to avoid timeout. Replace line 27-33 with :
links=[]
for page in search.pages():
	for item in page:
		links.append(item.assets['dtm'].href)