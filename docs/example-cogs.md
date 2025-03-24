# Accessing COG's data
This section present examples on how to use python libraries to access and use COG's 
data from the CCMEO datacube collections. 

## Using rasterio

The following code examples uses the rasterio library. To install rasterio see [rasterio installation].
``` sh
--8<-- "how-to-guides/rasterio-requirements.txt:2"
```

For more details on the rasterio library, see the [rasterio quickstart] documentation.

!!! Note
    The following examples starts with a request to the CCMEO STAC API via the pystac-client library.  

    For more details on how to discover data through the STAC API, see the **[Interacting with CCMEO STAC API]** section

<!-- START: Read the header of a cog using rasterio -->
::: how-to-guides.rasterio-header-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC

``` py linenums="1" hl_lines="26-33"
--8<-- "how-to-guides/rasterio-header-example.py:code"
```
<!-- END: Read the header of a cog using rasterio -->

<!-- START: Read a subset of a cog using rasterio -->
::: how-to-guides.rasterio-window-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC

``` py linenums="1" hl_lines="27-35"
--8<-- "how-to-guides/rasterio-window-example.py:code"
```
<!-- END: Read a subset of a cog using rasterio -->

## Using rioxarray

Rioxarray is based on rasterio, and can be used to read data into xarray object. 
The following code example uses the rioxarray library. To install see [rioxarray installation].
``` sh
--8<-- "how-to-guides/rioxarray-requirements.txt"
```
For more details on the rasterio library, see the [rioxarray] documentation. 
::: how-to-guides.rioxarray-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC

``` py linenums="1"
--8<-- "how-to-guides/rioxarray-example.py:code"
```


[rasterio installation]: https://rasterio.readthedocs.io/en/stable/installation.html
[rasterio quickstart]: https://rasterio.readthedocs.io/en/latest/quickstart.html
[Interacting with CCMEO STAC API]: pystac-client.md
[rioxarray installation]: https://corteva.github.io/rioxarray/stable/installation.html
[rioxarray]: https://corteva.github.io/rioxarray/stable/index.html

*[COG]: Cloud Optimized GeoTIFF
*[STAC]: Spatio-Temporal Asset Catalog