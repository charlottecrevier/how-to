# --------------------------
# ▶ USING GDAL COMMAND-LINE
# --------------------------
f"gdalwarp -t_srs EPSG:3857 -co COMPRESS=DEFLATE -co TILED=YES D:\WORK\04_CloudOptimizedPratices\00_data\MB-MB_The_Pas_UTM_14_2023-1m-dtm.tif D:\WORK\04_CloudOptimizedPratices\00_data\MB-MB_The_Pas_UTM_14_2023-1m-dtm-reprojectedCL.tif"


# ----------------------------
# ▶ USING OSGEO'S GDAL MODULE
# ----------------------------
from pathlib import Path
from osgeo import gdal

# Define input and output file names
input_cog = Path(f"D:\\WORK\\04_CloudOptimizedPratices\\00_data\\MB-MB_The_Pas_UTM_14_2023-1m-dtm.tif")
output_cog = Path(f"D:\\WORK\\04_CloudOptimizedPratices\\00_data\\MB-MB_The_Pas_UTM_14_2023-1m-dtm_reprojected.tif")

# Open the source COG
src_ds = gdal.Open(input_cog)

# Set up the reprojection options
warp_options = gdal.WarpOptions(
    dstSRS="EPSG:3857",                                     # target CRS
    format="COG",                                           # output format (Cloud-Optimized GeoTIFF)
    creationOptions=["COMPRESS=DEFLATE", "TILES=YES"]       # COG settings
)

# Perform the reprojection
gdal.Warp(output_cog, src_ds, options=warp_options)

# Close datasets
src_ds = None
