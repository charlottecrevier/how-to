# How to use pystac-client to get a list of tile(s) from the hrdem-mosaic-1m
[Code example](pystac-client-example.py) that:
 - Queries the ccmeo datacube STAC API with pystac-client to get the available collection;
 - Queries the ccmeo datacube STAC API with pystac-client with a subset of filter;
 - Access the data href for the specific filter.
 #TODO : create a list of file returned

# How to use rasterio to read the header and  a subset of a remote COG 
[Code example](rasterio-example.py) that :
- Replicate the steps above to access the data href for a specific item/collection; 
- Read the header of a distant COG;
- Read a subset of a distant cog based on an area of interest;
- TODO : Save the subset into as a tif file

# How to use rioxarray to read a subset of a remote COG
# How to use stackstac to read a subset of a remote COG into a xarray.DataArray

# Suggested references for pystac-client
- On the pystac-client documentation website https://pystac-client.readthedocs.io/en/stable/
    - https://pystac-client.readthedocs.io/en/stable/usage.html#itemsearch
    - https://pystac-client.readthedocs.io/en/stable/api.html#item-search
    - https://pystac-client.readthedocs.io/en/stable/tutorials.html#item-search-with-intersects
- On the pystac-client github repo https://github.com/stac-utils/pystac-client/tree/main/docs/tutorials
- To install the pystac-client https://github.com/stac-utils/pystac-client

# Suggested reference for STAC 
- On the stac website : https://stacspec.org/en/tutorials/

# Suggested references for COG in python 
- https://guide.cloudnativegeo.org/
- COG specification: https://www.cogeo.org/
- https://stackstac.readthedocs.io/en/latest/
- On the rasterio documentation website 
    - https://rasterio.readthedocs.io/en/stable/quickstart.html 
    - https://rasterio.readthedocs.io/en/stable/topics/reading.html

