<!-- ---
subtitle: Non-exhaustive gathering of relevant resources.
--- -->

# Quick Links 
Non-exhaustive gathering of relevant resources.
## Cloud-Optimized solution 
[Cloud-Optimized Geospatial Formats Guide] from Cloud Native Geospatial
### Suggested references for STAC 
- [STAC specification]
- [STAC tutorial]
### Suggested references for COG's
- [COG specification] from cogeo
- COG format [intro] and [advanced] from Cloud Native Geospatial

---
## Using python 
### Suggested references for STAC API discovery
- pystac-client  

    - [Install pystac-client]
    - pystac-client [GitHub repository]
    - Some useful links from the [pystac-client] documentation website : 
        - [Item search usage example]
        - [Item search tutorial with intersects]
        - [Item search API reference]

### Suggested references for COG access
- [rasterio]

    - [Quickstart] 
    - [Reading dataset]

- GDAL

    - [GDAL COG Options]
    - [GDAL CLI modules]

- [rioxarray]

    - [Getting started]
    - [Examples]

### Additional python library of interest 
- [stackstac]

    - [Basic Example]
    
- [xarray]
- [dask]

---
## Using QGIS 
### Resources for the stac browser plugin in QGIS
- [STAC API Browser Plugin]
- QGIS [CHANGELOG] with new STAC functionality

### Resources for data streaming from QGIS
- [Tutorial] loading a COG to QGIS


[pystac-client]: https://pystac-client.readthedocs.io/en/stable/
[Item search usage example]: https://pystac-client.readthedocs.io/en/stable/usage.html#itemsearch
[Item search API reference]: <https://pystac-client.readthedocs.io/en/stable/api.html#item-search>
[Item search tutorial with intersects]: https://pystac-client.readthedocs.io/en/stable/tutorials/item-search-intersects.html
[GitHub repository]: https://github.com/stac-utils/pystac-client/tree/main/docs/tutorials
[Install pystac-client]: https://github.com/stac-utils/pystac-client
[STAC specification]: https://stacspec.org/en/
[STAC tutorial]: https://stacspec.org/en/tutorials/
[Cloud-Optimized Geospatial Formats Guide]: https://guide.cloudnativegeo.org/
[COG specification]: https://www.cogeo.org/
[intro]: https://guide.cloudnativegeo.org/cloud-optimized-geotiffs/intro.html
[advanced]: https://guide.cloudnativegeo.org/cloud-optimized-geotiffs/cogs-details.html
[rasterio]: https://github.com/rasterio/rasterio
[Reading dataset]: https://rasterio.readthedocs.io/en/stable/topics/reading.html
[Quickstart]: https://rasterio.readthedocs.io/en/stable/quickstart.html
[stackstac]: https://stackstac.readthedocs.io/en/latest/
[Basic example]: https://stackstac.readthedocs.io/en/latest/basic.html
[GDAL COG Options]: https://gdal.org/en/stable/drivers/raster/cog.html#raster-cog
[GDAL CLI modules]: https://gdal.org/en/stable/programs/index.html#raster-programs
[rioxarray]: https://corteva.github.io/rioxarray/stable/
[Getting started]: https://corteva.github.io/rioxarray/stable/getting_started/getting_started.html
[Examples]: <https://corteva.github.io/rioxarray/stable/examples/examples.html
[xarray]: https://xarray.dev/
[dask]: https://docs.dask.org/en/stable/
[STAC API Browser Plugin]: https://stacspec.org/en/tutorials/2-intro-to-stac-api-browser-qgis-plugin/
[CHANGELOG]: https://qgis.org/project/visual-changelogs/visualchangelog340/#feature-stac-integration
[Tutorial]: https://cogeo.org/qgis-tutorial.html

*[COG]: Cloud Optimized GeoTIFF
*[STAC]: Spatio-Temporal Asset Catalog