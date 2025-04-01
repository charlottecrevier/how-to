# --------------------------
# ▶ USING GDAL COMMAND-LINE
# --------------------------
f"gdalwarp -t_srs EPSG:3857 -co COMPRESS=DEFLATE -co TILED=YES D:\WORK\04_CloudOptimizedPratices\00_data\MB-MB_The_Pas_UTM_14_2023-1m-dtm.tif D:\WORK\04_CloudOptimizedPratices\00_data\MB-MB_The_Pas_UTM_14_2023-1m-dtm-reprojectedCL.tif"
