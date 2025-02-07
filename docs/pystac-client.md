* TODO Ajouter le lien vers le code sur github   

# Interacting with CCMEO STAC API
This section present example on how to use python libraries to discover the available
collection from the CCMEO datacube STAC API. 

::: how-to-guides.pystac-client-example
    options:
        show_source: false
        members: no

This code uses the pystac-client library.   
Here are the requirements : 
```
--8<-- "how-to-guides/pystac-client-requirements.txt"
```

Import pystac-client to begin.
```python
--8<-- "how-to-guides/pystac-client-example.py:12:12"
```

Connect to the CCMEO STAC API
```python
--8<-- "how-to-guides/pystac-client-example.py:14:17"
```

<!--- Ceci ne fonctionne pas comme voulu
Explore why
--8<-- "how-to-guides/pystac-client-example.py:19:19" -->
Get the list of available collection id
```python
--8<-- "how-to-guides/pystac-client-example.py:20:21"
```

Define search parameters
```python
--8<-- "how-to-guides/pystac-client-example.py:24:28"
```

Make your request with the item search 
```python
--8<-- "how-to-guides/pystac-client-example.py:30:34"
```
Access items from search and save links to distant DTM COG files into a list. Consider using the pagination to avoid timeout for collection with multiples items
```python
--8<-- "how-to-guides/pystac-client-example.py:39:44"
```

For certificate error while accessing the STAC API : <https://pystac-client.readthedocs.io/en/stable/usage.html#using-custom-certificates>





