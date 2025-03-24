# Load pystac-client items into Xarray
!!! Warning
    GDAL's GetGeoTransform and rasterio use different formats for transform metadata. The order expected in the STAC proj:transform is the same as reported by rasterio. When using GDAL method you need to re-order the transform. 

    ``` py
    --8<-- "how-to-guides/odc-stac-example.py:transform"
    ```
     
    For more information, please see [STAC documentation on proj:transform]



[STAC documentation on proj:transform]:  https://github.com/stac-extensions/projection?tab=readme-ov-file#projtransform