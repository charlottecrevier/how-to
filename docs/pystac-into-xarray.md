# Load pystac-client items into Xarray
!!! info 
    To load a single COG (using the link to the s3 object) into an xarray, see [Access COG data using rioxarray]

[Xarray] is build on NumPy and Pandas, adding capabilities for labeled and multi-dimensional arrays (e.g., climate data, satellite images). It extends NumPy arrays by attaching metadata (coordinates, labels), making it easier to work with data dimensions like time, latitude, longitude, and other variables.

Xarray can use Dask arrays for lazy evaluation, enabling work with large datasets that don't fit in memory. Dask optimizes workflows by parallelizing tasks, reading data in chunks, and improving performance and memory efficiency.

Sources : [Xarray: Parallel Computing with Dask] 

!!! Warning
    GDAL's GetGeoTransform and rasterio use different formats for transform metadata. When using GDAL based method you need to re-order the transform. 
    See [Re-order the STAC proj:Transform] for more details.
    ``` py
    --8<-- "how-to-guides/odc-stac-example.py:transform"
    ```
     
    For more information, please see [STAC documentation on proj:transform]

# Using stackstac

This is a third party library based on Xarray, but not listed under the Xarray documentation. 

## Using odc-stac

This is a third party library based on Xarray, but not listed under the Xarray documentation. 

The following code examples uses the odc-stac library. To install odc-stac see [odc-stac installation].
``` sh
--8<-- "how-to-guides/odc-stac-requirements.txt"
```

<!-- START: Read with odc-stac -->
::: how-to-guides.odc-stac-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC

``` py linenums="1" 
--8<-- "how-to-guides/odc-stac-example.py:code"
```

<!-- Example of what can be done once the metadata was loader into an xarray :

``` py linenums="1" 
--8<-- "how-to-guides/odc-stac-example.py:example"
``` -->
<!-- END: Read with odc-stac -->


[Access COG data using rioxarray]: example-cogs.md/#using-rioxarray
[Xarray]: https://docs.xarray.dev/en/stable/
[Xarray: Parallel Computing with Dask]: https://docs.xarray.dev/en/stable/user-guide/dask.html
[STAC documentation on proj:transform]:  https://github.com/stac-extensions/projection?tab=readme-ov-file#projtransform
[Re-order the STAC proj:Transform]: reorder-transform-example.md
[odc-stac installation]: https://odc-stac.readthedocs.io/en/latest/intro.html#installation