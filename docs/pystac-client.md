# Interacting with CCMEO STAC API
This section present example on how to use python libraries to discover the available
collection from the CCMEO datacube STAC API. 

The following code examples uses the pystac-client library. To install pystac client see [pystac-client]
``` sh
--8<-- "how-to-guides/pystac-client-requirements.txt:3:3"
```

For more details on search paramters available with pystac-client, see documentation 
https://pystac-client.readthedocs.io/en/stable/usage.html#itemsearch

::: how-to-guides.pystac-client-items-example
    options:
        show_source: false
        members: no
        show_root_toc_entry: false # To remove the name of the file in the TOC

Import pystac-client to begin.
``` py
--8<-- "how-to-guides/pystac-client-items-example.py:12:12"
```

Connect to the CCMEO STAC API
``` py
--8<-- "how-to-guides/pystac-client-items-example.py:14:17"
```

<!--- Ceci ne fonctionne pas comme voulu
Explore why
--8<-- "how-to-guides/pystac-client-example.py:19:19" -->
Get the list of available collection id
``` py
--8<-- "how-to-guides/pystac-client-items-example.py:20:21"
```

Define search parameters
``` py
--8<-- "how-to-guides/pystac-client-items-example.py:24:28"
```

Make your request with the item search 
``` py
--8<-- "how-to-guides/pystac-client-items-example.py:30:34"
```
Access items from search and save links to distant DTM COG files into a list. Consider using the pagination to avoid timeout for collection with multiples items
``` py
--8<-- "how-to-guides/pystac-client-items-example.py:39:44"
```

For certificate error while accessing the STAC API : <https://pystac-client.readthedocs.io/en/stable/usage.html#using-custom-certificates>

[pystac-client]: https://github.com/stac-utils/pystac-client



