# GeoNames-based-city-index

# Informations
You can download the Geonames datasets ([Cities1000.zip](http://download.geonames.org/export/dump/cities1000.zip) , [AlternativeNames](http://download.geonames.org/export/dump/alternateNames.zip) , [postcodes](http://download.geonames.org/export/zip/allCountries.zip)) on http://download.geonames.org/export/

Data is cleaned, modified, merged, prepared to be send trough different pipes. Luigi module is used to created these pipes and pandas is used to clean and modify the data.

At the output pipeline, the city objects are added to your Algoria Index. Each city object provides at least the following attributes:
⋅⋅* name
⋅⋅* country
⋅⋅* alternative names
⋅⋅* postcode(s)
⋅⋅* population
⋅⋅* lat/lng position

# Launch tests

```
python test.py
```

# Utilisation

Put the 3 files in /pipe_files/entrance_file/

```
python app.py main --applicationid "YOUR_APPLICATION_ID" --adminapikey "YOUR_ADMIN_API_KEY" --algoliaindex "YOUR_INDEX_NAME" --local-scheduler
```
