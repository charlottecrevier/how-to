# Accessing COG's data
This section present examples on how to use python libraries to access and use COG's 
data from the CCMEO datacube collections. 

## Using rasterio

The following code examples uses the rasterio library. To install rasterio see [rasterio installation].
``` sh
--8<-- "how-to-guides/rasterio-requirements.txt:2"
```

For more details on the rasterio library, see the [rasterio quickstart] documentation.

<!-- START: Read the header of a cog using rasterio -->
::: how-to-guides.rasterio-header-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC

``` py linenums="1" hl_lines="26-33"
--8<-- "how-to-guides/rasterio-header-example.py:16"
```
<!-- END: Read the header of a cog using rasterio -->

<!-- START: Read a subset of a cog using rasterio -->
::: how-to-guides.rasterio-window-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC

``` py linenums="1" hl_lines="30-42"
--8<-- "how-to-guides/rasterio-window-example.py:13"
```

[rasterio installation]: https://rasterio.readthedocs.io/en/stable/installation.html
[rasterio quickstart]: https://rasterio.readthedocs.io/en/latest/quickstart.html