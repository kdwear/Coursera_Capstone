```python

```


```python
import numpy as np # library to handle data in a vectorized manner

import pandas as pd # library for data analsysis
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

import json # library to handle JSON files

#!conda install -c conda-forge geopy --yes # uncomment this line if you haven't completed the Foursquare API lab
from geopy.geocoders import Nominatim # convert an address into latitude and longitude values

import requests # library to handle requests
from pandas.io.json import json_normalize # tranform JSON file into a pandas dataframe

# Matplotlib and associated plotting modules
import matplotlib.cm as cm
import matplotlib.colors as colors

# import k-means from clustering stage
from sklearn.cluster import KMeans

#!conda install -c conda-forge folium=0.5.0 --yes # uncomment this line if you haven't completed the Foursquare API lab
import folium # map rendering library

print('Libraries imported.')
```

    Libraries imported.



```python
print ('Capstone project - The Battle of Neighborhoods')
print ()
print ()
print ('Introduction')
print ()
print ()
print ('This capstone project is the analysis around the opportunity to open a restaruant around the Bronx Zoo in New York.\n')
print ('Year 2020 has been very trying times for everyone in the Country as well an open the door for opportunity.')
print ('As non travel restrictions were put in place, people stayed closer to home, visiting attractions close to home.  People were laid off and needed to find other sources of income')
print ()
print ('The Bronx Zoo was the attraction identified for our analysis, as family friendly oriented')
print ('The Capstone Project will analyze the current restaurants close to the Bronz Zoo')
print ('The report will feature the detail of each specific type of restaurants as well the mapped locations of the restaurants based on the vicinity of the Bronx Zoo.')
print ()
print ('Problem')
print ()
print ('Due to lose of income, need to look at opportunity in supplementing inccome in opening restaurant in the Bronx Zoo area ')
print ()
print ('Data Section')
print ()
print () 
print ('Data link used was:newyork_data_json')
print ('Used New York Data to obtain Boroughs and Neighborhoods Details')
print ()
print ()
print ('Foursquare API Data')
print ()
print ()
print ('In order to gather data about different venues in different neighborhoods, including the Bronx, Foursquare locational informatino was used')
print ('Foursquare is a location data provider with information about venues within a specific area')
print ('Information can include venue name, address, postal code, category, longitude, latitude and distance')
print ('Foursquare information about the restaurant categories was used as the key analysis of our project')
print ()
print ('First step was to gather the neighborhood information of New York and break out the Boroughs and Neighborhoods')
print ('Once the neighborhoods were determined, and Bronx identified, a map of the Bronz was created')
print ('In reviewing the map of the Bronx, the Bronx Zoo is one of the main attrations of the area')
print ('By using the Foursquare API Data, we were able to determine the longitude and latitude of the Bronz Zoo')
print ('Using the search query within the Foursquare user agent, it allowed us to specifically key into the type of restaurants')
print ()
print ('The type of data that the Foursquare contained about the venue was:')
print ('     - Name')
print ('     - Categories')
print ('     - Address')
print ('     - Longitude and Latitude')
print ('     - Distance')
print ('     - Postal Code')
print ('     - City, State')
print ()
print (' This information allowed us to analyze the specific restaurant type of interest near the Bronx Zoo, which was used to finalize the type of restaurant to open')




       
```

    Capstone project - The Battle of Neighborhoods
    
    
    Introduction
    
    
    This capstone project is the analysis around the opportunity to open a restaruant around the Bronx Zoo in New York.
    
    Year 2020 has been very trying times for everyone in the Country as well an open the door for opportunity.
    As non travel restrictions were put in place, people stayed closer to home, visiting attractions close to home.  People were laid off and needed to find other sources of income
    
    The Bronx Zoo was the attraction identified for our analysis, as family friendly oriented
    The Capstone Project will analyze the current restaurants close to the Bronz Zoo
    The report will feature the detail of each specific type of restaurants as well the mapped locations of the restaurants based on the vicinity of the Bronx Zoo.
    
    Problem
    
    Due to lose of income, need to look at opportunity in supplementing inccome in opening restaurant in the Bronx Zoo area 
    
    Data Section
    
    
    Data link used was:newyork_data_json
    Used New York Data to obtain Boroughs and Neighborhoods Details
    
    
    Foursquare API Data
    
    
    In order to gather data about different venues in different neighborhoods, including the Bronx, Foursquare locational informatino was used
    Foursquare is a location data provider with information about venues within a specific area
    Information can include venue name, address, postal code, category, longitude, latitude and distance
    Foursquare information about the restaurant categories was used as the key analysis of our project
    
    First step was to gather the neighborhood information of New York and break out the Boroughs and Neighborhoods
    Once the neighborhoods were determined, and Bronx identified, a map of the Bronz was created
    In reviewing the map of the Bronx, the Bronx Zoo is one of the main attrations of the area
    By using the Foursquare API Data, we were able to determine the longitude and latitude of the Bronz Zoo
    Using the search query within the Foursquare user agent, it allowed us to specifically key into the type of restaurants
    
    The type of data that the Foursquare contained about the venue was:
         - Name
         - Categories
         - Address
         - Longitude and Latitude
         - Distance
         - Postal Code
         - City, State
    
     This information allowed us to analyze the specific restaurant type of interest near the Bronx Zoo, which was used to finalize the type of restaurant to open



```python

```
