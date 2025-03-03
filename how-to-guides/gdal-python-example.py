"""
In this example, you will learn to:
- Query the CCMEO datacube STAC API with pystac-client with a subset of filter;
- Save locally the streamed COG;
- Reproject the locally saved COG.

!!! info
	This specific example uses the collection hrdem-mosaic-2m from CCMEO's datacube
"""
#🔶🔶🔶 ⬇⬇⬇ Remove the following
import os
os.environ["REQUESTS_CA_BUNDLE"] = f"D:\\ELEVATION\\99_Certificates\\NRCAN-RootCA.pem"
#🔶🔶🔶 ⬆⬆⬆ Remove the following

# --8<-- [start:code]
import pystac_client
from osgeo import gdal
from pathlib import Path

# Define your local paths to save temporary and reprojected COGs
your_work_dir = Path("C:/")

# === STEP 1: Define area of interest & Access the STAC API ===
# Define the dataset collection and the bounding box area of interest in EPSG:4326
collections = ['hrdem-mosaic-2m']
bbox = [-79.28, 44.32, -79.27, 44.33]

# Connect to the CCMEO Datacube STAC API
stac_root = "https://datacube.services.geo.ca/stac/api"
catalog = pystac_client.Client.open(stac_root)

# Search for available datasets within the defined area of interest
search = catalog.search(collections=collections, bbox=bbox)

# Retrieve the first available DTM asset link
links = [item.assets['dtm'].href for page in search.pages() for item in page]

# Validate that at least one asset was found
if not links:
    raise Exception("No asset found for the specified area of interest.")

# Define the input COG URL for GDAL streaming
input_cog = f"/vsicurl_streaming/{links[0].replace('https://', 'http://')}"


# === STEP 2: Save the COG locally before reprojection ===
# Define local file path for saving the streamed COG
temporary_cog = Path(your_work_dir / "hrdem_saved.tif")

# Open the remote COG using GDAL
src_ds = gdal.Open(input_cog)

# Save the streamed COG locally to avoid repeated downloads
gdal.Translate(
    temporary_cog, src_ds, format="COG",
    xRes=30, yRes=30,										# Downsample resolution to speed up processing
    creationOptions=["COMPRESS=DEFLATE", "TILED=YES"])

# Close the dataset to free memory
src_ds = None


# === STEP 3: Reproject the saved COG ===
# Define local file path for reprojecting the COG
output_cog = Path(your_work_dir / "hrdem_reprojected.tif")

# Open the locally saved COG for reprojection
tmp_ds = gdal.Open(temporary_cog)

# Set up the reprojection options
warp_options = gdal.WarpOptions(
    dstSRS="EPSG:3857",                                     # target CRS
    format="COG",                                           # output format (Cloud-Optimized GeoTIFF)
	resampleAlg=gdal.GRA_Bilinear,
    creationOptions=["COMPRESS=DEFLATE", "TILES=YES"]       # COG settings
)

# Close the dataset to free memory
tmp_ds = None

# Perform the reprojection and save the result
gdal.Warp(output_cog, tmp_ds, options=warp_options)


# === STEP 4: Verify the output ===
# Open local temporary and reproejct COG to compare projections
temporary_ds = gdal.Open(temporary_cog)
reprojected_ds = gdal.Open(output_cog)

# Read projection metadata
print("Temporary COG Projection:", temporary_ds.GetProjection())
print("Reprojected COG Projection:", reprojected_ds.GetProjection())
# --8<-- [end:code]
