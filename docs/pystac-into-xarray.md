# Third Party Libraries

!!! Warning
    The following libraries are not part of the [STAC utils] ecosystem. 
    
Examples of loading [pystac-client] items object into Xarray object. To load a single COG (using the link to the s3 object) into an xarray, see [Access COG data using rioxarray]

!!! Warning
    GDAL's GetGeoTransform and rasterio use different formats for transform metadata. When using GDAL based method you need to re-order the transform. 
    See [Re-order the STAC proj:Transform] for more details.
    ``` py
    --8<-- "how-to-guides/odc-stac-example.py:transform"
    ```
        
    For more information, please see [STAC documentation on proj:transform]

## Using [stackstac]

This is a third party library based on Xarray, but not listed under the Xarray documentation. 

``` sh
--8<-- "how-to-guides/stackstac-requirements.txt"
```
For more details see [stackstac installation].

<!-- START: Read with stackstac-stac -->
::: how-to-guides.stackstac-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC

``` py linenums="1" hl_lines="36-41"
--8<-- "how-to-guides/stackstac-example.py:code"
```

See `Xarray.DataArray` for details on methods : <https://docs.xarray.dev/en/stable/generated/xarray.DataArray.html>

``` py linenums="1" 
--8<-- "how-to-guides/stackstac-example.py:example"
```

## Using [odc-stac]

This is a third party library based on Xarray, but not listed under the Xarray documentation. 

``` sh
--8<-- "how-to-guides/odc-stac-requirements.txt"
```
For more details see [odc-stac installation].

<!-- START: Read with odc-stac -->
::: how-to-guides.odc-stac-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC

``` py linenums="1" hl_lines="38-41"
--8<-- "how-to-guides/odc-stac-example.py:code"
```

<!-- Example of what can be done once the metadata was loader into an xarray :

``` py linenums="1" 
--8<-- "how-to-guides/odc-stac-example.py:example"
``` -->
<!-- END: Read with odc-stac -->

## Community Notebook complete examples

- [Loading multi-collections in a Xarray.Dataset]
- [Calculating the flow direction using open source library pyflwdir and Xarray.DataArray]

[Access COG data using rioxarray]: example-cogs.md/#using-rioxarray
[Xarray]: https://docs.xarray.dev/en/stable/
[Xarray: Parallel Computing with Dask]: https://docs.xarray.dev/en/stable/user-guide/dask.html
[STAC documentation on proj:transform]:  https://github.com/stac-extensions/projection?tab=readme-ov-file#projtransform
[Re-order the STAC proj:Transform]: reorder-transform-example.md
[odc-stac installation]: https://odc-stac.readthedocs.io/en/latest/intro.html#installation
[stackstac installation]: https://stackstac.readthedocs.io/en/latest/#installation
[STAC utils]: https://github.com/stac-utils
[pystac-client]: https://pystac-client.readthedocs.io/en/stable/
[stackstac]: https://stackstac.readthedocs.io/en/latest/

<!-- TODO : Find a better way to link those jupyternotebooks... -->
[Loading multi-collections in a Xarray.Dataset]: https://github.com/charlottecrevier/how-to/blob/cebcb055e8e57b768df20577ca5ea7f34c367c0c/how-to-guides/notebook/multi-collection-example.ipynb
[Calculating the flow direction using open source library pyflwdir and Xarray.DataArray]: https://github.com/charlottecrevier/how-to/blob/cebcb055e8e57b768df20577ca5ea7f34c367c0c/how-to-guides/notebook/pyflwdir-example.ipynb