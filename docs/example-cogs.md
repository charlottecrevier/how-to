# Accessing COG Data
Examples on how to use python libraries to access and use COGs. Demonstrating one of the cloud
optimized advantages, being able to access a **[portion of the data]** without having to download the entire file.  

See <https://guide.cloudnativegeo.org/>

## Using [rasterio]

``` sh
--8<-- "how-to-guides/rasterio-requirements.txt:2"
```

The developers of the rasterio library provide additional examples of usage. 
For more details on the rasterio library, see the [rasterio] documentation.

!!! Note
    The following examples starts with a request to the CCMEO STAC API via the pystac-client library.  

    For more details on how to discover data through the STAC API, see the **[Interacting with CCMEO STAC API]** section

<!-- START: Read the header of a cog using rasterio -->
::: how-to-guides.rasterio-header-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC

``` py linenums="1" hl_lines="23-35"
--8<-- "how-to-guides/rasterio-header-example.py:code"
```
<!-- END: Read the header of a cog using rasterio -->

<!-- START: Read a portion of a cog using rasterio -->
::: how-to-guides.rasterio-window-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC

``` py linenums="1" hl_lines="27-37"
--8<-- "how-to-guides/rasterio-window-example.py:code"
```
<!-- END: Read a portion of a cog using rasterio -->

## Using [rioxarray]

Rioxarray is based on rasterio, and can be used to read data into xarray object. The developpers of the rioxarray library provide additional usage examples, like this [one](https://corteva.github.io/rioxarray/stable/examples/read-locks.html).

!!! info
    [Xarray] is build on NumPy and Pandas, adding capabilities for labeled and multi-dimensional arrays (e.g., climate data, satellite images). It extends NumPy arrays by attaching metadata (coordinates, labels), making it easier to work with data dimensions like time, latitude, longitude, and other variables.

    Xarray can use Dask arrays for lazy evaluation, enabling work with large datasets that don't fit in memory. Dask optimizes workflows by parallelizing tasks, reading data in chunks, and improving performance and memory efficiency.

    Source : [Xarray: Parallel Computing with Dask] 

``` sh
--8<-- "how-to-guides/rioxarray-requirements.txt"
```
Source :  [rioxarray installation]

::: how-to-guides.rioxarray-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC

!!! Note 
    When using `rioxarray.open_rasterio()` set `chunks` to enable lazy loading with Dask. This allows Dask to read data in smaller chunks, improving speed and memory usage through parallel computing. For example, a `chunk` size of 1000 for both x and y means Dask reads 100x100 boxes instead of the entire array, processing multiple chunks simultaneously.

``` py linenums="1" hl_lines="20-23"
--8<-- "how-to-guides/rioxarray-example.py:code"
```


[rasterio installation]: https://rasterio.readthedocs.io/en/stable/installation.html
[rasterio]: https://rasterio.readthedocs.io/en/latest/quickstart.html
[Interacting with CCMEO STAC API]: pystac-client.md
[rioxarray installation]: https://corteva.github.io/rioxarray/stable/installation.html
[rioxarray]: https://corteva.github.io/rioxarray/stable/index.html
[Xarray]: https://docs.xarray.dev/en/stable/
[Xarray: Parallel Computing with Dask]: https://docs.xarray.dev/en/stable/user-guide/dask.html
[portion of the data]: #how-to-guides.rasterio-window-example--read-a-portion-of-a-remote-cog

*[COG]: Cloud Optimized GeoTIFF
*[STAC]: Spatio-Temporal Asset Catalog
*[CCMEO]: Canada Center for Mapping and Earth Observation, Natural Resources Canada
