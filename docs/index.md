# Cloud-Optimized Geospatial Data Access
!!! Note
    All the libraries and ressources presented are open-source and have there own licensing.
    Please refere to the specific libraries doucmentation for sharing mechanism.

Suggested and non-exhaustive best practices and tutorials using open-source libraries for Cloud Optimized data access
for Government of Canada data collections. 

!!! info "Link to CCMEO COG collections "
    STAC API : <https://datacube.services.geo.ca/stac/api/>  
    STAC API via STAC-Browser : <https://radiantearth.github.io/stac-browser/#/external/datacube.services.geo.ca/stac/api/?.language=en>

<!--- 
What should be on the main page : 
A single sentence that says what the product is, succinctly and memorably.
A paragraph of one to three short sentences, that describe what the product does.
A third paragraph of similar length, this time explaining what need the product meets.
Finally, a paragraph that describes whom the product is useful for.
-->
---

## In this site...
<div class="grid cards" markdown>
-   __How-to guides__

    ---

    **Code examples** covering key operations and common tasks
    
    :arrow_right: [how-to guides](pystac-client.md)

-   __Quick links__

    ---

    Useful references to **external resources**  


    :arrow_right: [Quick links](reference.md)
</div>
---

## Libraries
Non-exhaustive list of libraries used in the examples.

### To discover data

From [Radiant Earth] :  

- [pystac-client]

### To access data  

Third party libraries using STAC objects :

- [stackstac]
- [odc-stac]

Based on GDAL :

- [rasterio]
- [rioxarray]

## Report an Issue

If you encounter any issues, please create a new issue using our template.
</issues/new>  

[pystac-client]: https://pystac-client.readthedocs.io/en/stable/usage.html
[rasterio]: https://rasterio.readthedocs.io/en/latest/quickstart.html
[stackstac]: https://stackstac.readthedocs.io/en/latest/basic.html
[odc-stac]: https://odc-stac.readthedocs.io/en/latest/
[rioxarray]: https://corteva.github.io/rioxarray/stable/
[Radiant Earth]: https://github.com/radiantearth
*[COG]: Cloud Optimized GeoTIFF
*[CCMEO]: Canadian Center for Mapping and Earth Observation, Natural Resources Canada
*[STAC]: Spatio-Temporal Asset Catalog
