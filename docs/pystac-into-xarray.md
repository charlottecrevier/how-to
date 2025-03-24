# Load pystac-client items into Xarray
!!! Warning
    GDAL's GetGeoTransform and rasterio use different formats for transform metadata. When using GDAL method you need to re-order the transform. 
    See [Re-order the STAC proj:Transform] for more details.
    ``` py
    --8<-- "how-to-guides/odc-stac-example.py:transform"
    ```
     
    For more information, please see [STAC documentation on proj:transform]



[STAC documentation on proj:transform]:  https://github.com/stac-extensions/projection?tab=readme-ov-file#projtransform
[Re-order the STAC proj:Transform]: reorder-transform-example.md