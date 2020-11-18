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
import requests # library to handle requests
import pandas as pd # library for data analsysis
import numpy as np # library to handle data in a vectorized manner
import random # library for random number generation


!pip install geopy
from geopy.geocoders import Nominatim # module to convert an address into latitude and longitude values

# libraries for displaying images
from IPython.display import Image 
from IPython.core.display import HTML 
    
# tranforming json file into a pandas dataframe library
from pandas.io.json import json_normalize


! pip install folium==0.5.0
import folium # plotting library

print('Folium installed')
print('Libraries imported.')
```

    Collecting geopy
    [?25l  Downloading https://files.pythonhosted.org/packages/07/e1/9c72de674d5c2b8fcb0738a5ceeb5424941fefa080bfe4e240d0bacb5a38/geopy-2.0.0-py3-none-any.whl (111kB)
    [K     |████████████████████████████████| 112kB 10.0MB/s eta 0:00:01
    [?25hCollecting geographiclib<2,>=1.49 (from geopy)
      Downloading https://files.pythonhosted.org/packages/8b/62/26ec95a98ba64299163199e95ad1b0e34ad3f4e176e221c40245f211e425/geographiclib-1.50-py3-none-any.whl
    Installing collected packages: geographiclib, geopy
    Successfully installed geographiclib-1.50 geopy-2.0.0
    Requirement already satisfied: folium==0.5.0 in /home/jupyterlab/conda/envs/python/lib/python3.6/site-packages (0.5.0)
    Requirement already satisfied: branca in /home/jupyterlab/conda/envs/python/lib/python3.6/site-packages (from folium==0.5.0) (0.4.1)
    Requirement already satisfied: jinja2 in /home/jupyterlab/conda/envs/python/lib/python3.6/site-packages (from folium==0.5.0) (2.11.2)
    Requirement already satisfied: requests in /home/jupyterlab/conda/envs/python/lib/python3.6/site-packages (from folium==0.5.0) (2.24.0)
    Requirement already satisfied: six in /home/jupyterlab/conda/envs/python/lib/python3.6/site-packages (from folium==0.5.0) (1.15.0)
    Requirement already satisfied: MarkupSafe>=0.23 in /home/jupyterlab/conda/envs/python/lib/python3.6/site-packages (from jinja2->folium==0.5.0) (1.1.1)
    Requirement already satisfied: idna<3,>=2.5 in /home/jupyterlab/conda/envs/python/lib/python3.6/site-packages (from requests->folium==0.5.0) (2.10)
    Requirement already satisfied: certifi>=2017.4.17 in /home/jupyterlab/conda/envs/python/lib/python3.6/site-packages (from requests->folium==0.5.0) (2020.6.20)
    Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /home/jupyterlab/conda/envs/python/lib/python3.6/site-packages (from requests->folium==0.5.0) (1.25.11)
    Requirement already satisfied: chardet<4,>=3.0.2 in /home/jupyterlab/conda/envs/python/lib/python3.6/site-packages (from requests->folium==0.5.0) (3.0.4)
    Folium installed
    Libraries imported.



```python
CLIENT_ID = 'XOMNN5V4YTDAU4HRS1NHJQMW5IYKWCWXXGCE2ZNPW4NKNU3O' # your Foursquare ID
CLIENT_SECRET = 'VMCFJQKYJT3TFKSLNMJNXNEC3EDSSLWGHUR5B3QUCODZ1K1L' # your Foursquare Secret
VERSION = '20180604'
LIMIT = 30
print('Your credentails:')
print('CLIENT_ID: ' + CLIENT_ID)
print('CLIENT_SECRET:' + CLIENT_SECRET)
```

    Your credentails:
    CLIENT_ID: XOMNN5V4YTDAU4HRS1NHJQMW5IYKWCWXXGCE2ZNPW4NKNU3O
    CLIENT_SECRET:VMCFJQKYJT3TFKSLNMJNXNEC3EDSSLWGHUR5B3QUCODZ1K1L



```python

```


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
!wget -q -O 'newyork_data.json' https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/labs/newyork_data.json
print('Data downloaded!')
```

    Data downloaded!



```python
print ('Methodology Section')
print ()
print ('To determine the neighborhoods in the New York area, first gathered the Boroughs and Neighborhoods in New York')
print ()
```


```python
with open('newyork_data.json') as json_data:
    newyork_data = json.load(json_data)
```


```python
newyork_data
```




    {'type': 'FeatureCollection',
     'totalFeatures': 306,
     'features': [{'type': 'Feature',
       'id': 'nyu_2451_34572.1',
       'geometry': {'type': 'Point',
        'coordinates': [-73.84720052054902, 40.89470517661]},
       'geometry_name': 'geom',
       'properties': {'name': 'Wakefield',
        'stacked': 1,
        'annoline1': 'Wakefield',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.84720052054902,
         40.89470517661,
         -73.84720052054902,
         40.89470517661]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.2',
       'geometry': {'type': 'Point',
        'coordinates': [-73.82993910812398, 40.87429419303012]},
       'geometry_name': 'geom',
       'properties': {'name': 'Co-op City',
        'stacked': 2,
        'annoline1': 'Co-op',
        'annoline2': 'City',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.82993910812398,
         40.87429419303012,
         -73.82993910812398,
         40.87429419303012]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.3',
       'geometry': {'type': 'Point',
        'coordinates': [-73.82780644716412, 40.887555677350775]},
       'geometry_name': 'geom',
       'properties': {'name': 'Eastchester',
        'stacked': 1,
        'annoline1': 'Eastchester',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.82780644716412,
         40.887555677350775,
         -73.82780644716412,
         40.887555677350775]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.4',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90564259591682, 40.89543742690383]},
       'geometry_name': 'geom',
       'properties': {'name': 'Fieldston',
        'stacked': 1,
        'annoline1': 'Fieldston',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.90564259591682,
         40.89543742690383,
         -73.90564259591682,
         40.89543742690383]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.5',
       'geometry': {'type': 'Point',
        'coordinates': [-73.9125854610857, 40.890834493891305]},
       'geometry_name': 'geom',
       'properties': {'name': 'Riverdale',
        'stacked': 1,
        'annoline1': 'Riverdale',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.9125854610857,
         40.890834493891305,
         -73.9125854610857,
         40.890834493891305]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.6',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90281798724604, 40.88168737120521]},
       'geometry_name': 'geom',
       'properties': {'name': 'Kingsbridge',
        'stacked': 1,
        'annoline1': 'Kingsbridge',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.90281798724604,
         40.88168737120521,
         -73.90281798724604,
         40.88168737120521]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.7',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91065965862981, 40.87655077879964]},
       'geometry_name': 'geom',
       'properties': {'name': 'Marble Hill',
        'stacked': 2,
        'annoline1': 'Marble',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.91065965862981,
         40.87655077879964,
         -73.91065965862981,
         40.87655077879964]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.8',
       'geometry': {'type': 'Point',
        'coordinates': [-73.86731496814176, 40.89827261213805]},
       'geometry_name': 'geom',
       'properties': {'name': 'Woodlawn',
        'stacked': 1,
        'annoline1': 'Woodlawn',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.86731496814176,
         40.89827261213805,
         -73.86731496814176,
         40.89827261213805]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.9',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8793907395681, 40.87722415599446]},
       'geometry_name': 'geom',
       'properties': {'name': 'Norwood',
        'stacked': 1,
        'annoline1': 'Norwood',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.8793907395681,
         40.87722415599446,
         -73.8793907395681,
         40.87722415599446]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.10',
       'geometry': {'type': 'Point',
        'coordinates': [-73.85744642974207, 40.88103887819211]},
       'geometry_name': 'geom',
       'properties': {'name': 'Williamsbridge',
        'stacked': 1,
        'annoline1': 'Williamsbridge',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.85744642974207,
         40.88103887819211,
         -73.85744642974207,
         40.88103887819211]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.11',
       'geometry': {'type': 'Point',
        'coordinates': [-73.83579759808117, 40.866858107252696]},
       'geometry_name': 'geom',
       'properties': {'name': 'Baychester',
        'stacked': 1,
        'annoline1': 'Baychester',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.83579759808117,
         40.866858107252696,
         -73.83579759808117,
         40.866858107252696]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.12',
       'geometry': {'type': 'Point',
        'coordinates': [-73.85475564017999, 40.85741349808865]},
       'geometry_name': 'geom',
       'properties': {'name': 'Pelham Parkway',
        'stacked': 1,
        'annoline1': 'Pelham Parkway',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.85475564017999,
         40.85741349808865,
         -73.85475564017999,
         40.85741349808865]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.13',
       'geometry': {'type': 'Point',
        'coordinates': [-73.78648845267413, 40.84724670491813]},
       'geometry_name': 'geom',
       'properties': {'name': 'City Island',
        'stacked': 2,
        'annoline1': 'City',
        'annoline2': 'Island',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.78648845267413,
         40.84724670491813,
         -73.78648845267413,
         40.84724670491813]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.14',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8855121841913, 40.870185164975325]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bedford Park',
        'stacked': 2,
        'annoline1': 'Bedford',
        'annoline2': 'Park',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.8855121841913,
         40.870185164975325,
         -73.8855121841913,
         40.870185164975325]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.15',
       'geometry': {'type': 'Point',
        'coordinates': [-73.9104159619131, 40.85572707719664]},
       'geometry_name': 'geom',
       'properties': {'name': 'University Heights',
        'stacked': 2,
        'annoline1': 'University',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.9104159619131,
         40.85572707719664,
         -73.9104159619131,
         40.85572707719664]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.16',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91967159119565, 40.84789792606271]},
       'geometry_name': 'geom',
       'properties': {'name': 'Morris Heights',
        'stacked': 2,
        'annoline1': 'Morris',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.91967159119565,
         40.84789792606271,
         -73.91967159119565,
         40.84789792606271]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.17',
       'geometry': {'type': 'Point',
        'coordinates': [-73.89642655981623, 40.86099679638654]},
       'geometry_name': 'geom',
       'properties': {'name': 'Fordham',
        'stacked': 1,
        'annoline1': 'Fordham',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.89642655981623,
         40.86099679638654,
         -73.89642655981623,
         40.86099679638654]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.18',
       'geometry': {'type': 'Point',
        'coordinates': [-73.88735617532338, 40.84269615786053]},
       'geometry_name': 'geom',
       'properties': {'name': 'East Tremont',
        'stacked': 2,
        'annoline1': 'East',
        'annoline2': 'Tremont',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.88735617532338,
         40.84269615786053,
         -73.88735617532338,
         40.84269615786053]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.19',
       'geometry': {'type': 'Point',
        'coordinates': [-73.87774474910545, 40.83947505672653]},
       'geometry_name': 'geom',
       'properties': {'name': 'West Farms',
        'stacked': 2,
        'annoline1': 'West',
        'annoline2': 'Farms',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.87774474910545,
         40.83947505672653,
         -73.87774474910545,
         40.83947505672653]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.20',
       'geometry': {'type': 'Point',
        'coordinates': [-73.9261020935813, 40.836623010706056]},
       'geometry_name': 'geom',
       'properties': {'name': 'High  Bridge',
        'stacked': 1,
        'annoline1': 'Highbridge',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.9261020935813,
         40.836623010706056,
         -73.9261020935813,
         40.836623010706056]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.21',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90942160757436, 40.819754370594936]},
       'geometry_name': 'geom',
       'properties': {'name': 'Melrose',
        'stacked': 1,
        'annoline1': 'Melrose',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.90942160757436,
         40.819754370594936,
         -73.90942160757436,
         40.819754370594936]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.22',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91609987487575, 40.80623874935177]},
       'geometry_name': 'geom',
       'properties': {'name': 'Mott Haven',
        'stacked': 1,
        'annoline1': 'Mott Haven',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.91609987487575,
         40.80623874935177,
         -73.91609987487575,
         40.80623874935177]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.23',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91322139386135, 40.801663627756206]},
       'geometry_name': 'geom',
       'properties': {'name': 'Port Morris',
        'stacked': 2,
        'annoline1': 'Port',
        'annoline2': 'Morris',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.91322139386135,
         40.801663627756206,
         -73.91322139386135,
         40.801663627756206]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.24',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8957882009446, 40.81509904545822]},
       'geometry_name': 'geom',
       'properties': {'name': 'Longwood',
        'stacked': 1,
        'annoline1': 'Longwood',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.8957882009446,
         40.81509904545822,
         -73.8957882009446,
         40.81509904545822]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.25',
       'geometry': {'type': 'Point',
        'coordinates': [-73.88331505955291, 40.80972987938709]},
       'geometry_name': 'geom',
       'properties': {'name': 'Hunts Point',
        'stacked': 2,
        'annoline1': 'Hunts',
        'annoline2': 'Point',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.88331505955291,
         40.80972987938709,
         -73.88331505955291,
         40.80972987938709]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.26',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90150648943059, 40.82359198585534]},
       'geometry_name': 'geom',
       'properties': {'name': 'Morrisania',
        'stacked': 1,
        'annoline1': 'Morrisania',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.90150648943059,
         40.82359198585534,
         -73.90150648943059,
         40.82359198585534]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.27',
       'geometry': {'type': 'Point',
        'coordinates': [-73.86574609554924, 40.821012197914015]},
       'geometry_name': 'geom',
       'properties': {'name': 'Soundview',
        'stacked': 1,
        'annoline1': 'Soundview',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.86574609554924,
         40.821012197914015,
         -73.86574609554924,
         40.821012197914015]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.28',
       'geometry': {'type': 'Point',
        'coordinates': [-73.85414416189266, 40.80655112003589]},
       'geometry_name': 'geom',
       'properties': {'name': 'Clason Point',
        'stacked': 2,
        'annoline1': 'Clason',
        'annoline2': 'Point',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.85414416189266,
         40.80655112003589,
         -73.85414416189266,
         40.80655112003589]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.29',
       'geometry': {'type': 'Point',
        'coordinates': [-73.81635002158441, 40.81510925804005]},
       'geometry_name': 'geom',
       'properties': {'name': 'Throgs Neck',
        'stacked': 1,
        'annoline1': 'Throgs Neck',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.81635002158441,
         40.81510925804005,
         -73.81635002158441,
         40.81510925804005]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.30',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8240992675385, 40.844245936947374]},
       'geometry_name': 'geom',
       'properties': {'name': 'Country Club',
        'stacked': 2,
        'annoline1': 'Country',
        'annoline2': 'Club',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.8240992675385,
         40.844245936947374,
         -73.8240992675385,
         40.844245936947374]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.31',
       'geometry': {'type': 'Point',
        'coordinates': [-73.85600310535783, 40.837937822267286]},
       'geometry_name': 'geom',
       'properties': {'name': 'Parkchester',
        'stacked': 1,
        'annoline1': 'Parkchester',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.85600310535783,
         40.837937822267286,
         -73.85600310535783,
         40.837937822267286]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.32',
       'geometry': {'type': 'Point',
        'coordinates': [-73.84219407604444, 40.8406194964327]},
       'geometry_name': 'geom',
       'properties': {'name': 'Westchester Square',
        'stacked': 2,
        'annoline1': 'Westchester',
        'annoline2': 'Square',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.84219407604444,
         40.8406194964327,
         -73.84219407604444,
         40.8406194964327]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.33',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8662991807561, 40.84360847124718]},
       'geometry_name': 'geom',
       'properties': {'name': 'Van Nest',
        'stacked': 2,
        'annoline1': 'Van',
        'annoline2': 'Nest',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.8662991807561,
         40.84360847124718,
         -73.8662991807561,
         40.84360847124718]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.34',
       'geometry': {'type': 'Point',
        'coordinates': [-73.85040178030421, 40.847549063536334]},
       'geometry_name': 'geom',
       'properties': {'name': 'Morris Park',
        'stacked': 1,
        'annoline1': 'Morris Park',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.85040178030421,
         40.847549063536334,
         -73.85040178030421,
         40.847549063536334]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.35',
       'geometry': {'type': 'Point',
        'coordinates': [-73.88845196134804, 40.85727710073895]},
       'geometry_name': 'geom',
       'properties': {'name': 'Belmont',
        'stacked': 1,
        'annoline1': 'Belmont',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.88845196134804,
         40.85727710073895,
         -73.88845196134804,
         40.85727710073895]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.36',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91719048210393, 40.88139497727086]},
       'geometry_name': 'geom',
       'properties': {'name': 'Spuyten Duyvil',
        'stacked': 2,
        'annoline1': 'Spuyten',
        'annoline2': 'Duyvil',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.91719048210393,
         40.88139497727086,
         -73.91719048210393,
         40.88139497727086]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.37',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90453054908927, 40.90854282950666]},
       'geometry_name': 'geom',
       'properties': {'name': 'North Riverdale',
        'stacked': 2,
        'annoline1': 'North',
        'annoline2': 'Riverdale',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.90453054908927,
         40.90854282950666,
         -73.90453054908927,
         40.90854282950666]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.38',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8320737824047, 40.85064140940335]},
       'geometry_name': 'geom',
       'properties': {'name': 'Pelham Bay',
        'stacked': 2,
        'annoline1': 'Pelham',
        'annoline2': 'Bay',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.8320737824047,
         40.85064140940335,
         -73.8320737824047,
         40.85064140940335]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.39',
       'geometry': {'type': 'Point',
        'coordinates': [-73.82620275994073, 40.82657951686922]},
       'geometry_name': 'geom',
       'properties': {'name': 'Schuylerville',
        'stacked': 1,
        'annoline1': 'Schuylerville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.82620275994073,
         40.82657951686922,
         -73.82620275994073,
         40.82657951686922]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.40',
       'geometry': {'type': 'Point',
        'coordinates': [-73.81388514428619, 40.821986118163494]},
       'geometry_name': 'geom',
       'properties': {'name': 'Edgewater Park',
        'stacked': 2,
        'annoline1': 'Edgewater',
        'annoline2': 'Park',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.81388514428619,
         40.821986118163494,
         -73.81388514428619,
         40.821986118163494]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.41',
       'geometry': {'type': 'Point',
        'coordinates': [-73.84802729582735, 40.819014376988314]},
       'geometry_name': 'geom',
       'properties': {'name': 'Castle Hill',
        'stacked': 2,
        'annoline1': 'Castle',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.84802729582735,
         40.819014376988314,
         -73.84802729582735,
         40.819014376988314]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.42',
       'geometry': {'type': 'Point',
        'coordinates': [-73.86332361652777, 40.87137078192371]},
       'geometry_name': 'geom',
       'properties': {'name': 'Olinville',
        'stacked': 1,
        'annoline1': 'Olinville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.86332361652777,
         40.87137078192371,
         -73.86332361652777,
         40.87137078192371]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.43',
       'geometry': {'type': 'Point',
        'coordinates': [-73.84161194831223, 40.86296562477998]},
       'geometry_name': 'geom',
       'properties': {'name': 'Pelham Gardens',
        'stacked': 2,
        'annoline1': 'Pelham',
        'annoline2': 'Gardens',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.84161194831223,
         40.86296562477998,
         -73.84161194831223,
         40.86296562477998]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.44',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91558941773444, 40.83428380733851]},
       'geometry_name': 'geom',
       'properties': {'name': 'Concourse',
        'stacked': 1,
        'annoline1': 'Concourse',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.91558941773444,
         40.83428380733851,
         -73.91558941773444,
         40.83428380733851]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.45',
       'geometry': {'type': 'Point',
        'coordinates': [-73.85053524451935, 40.82977429787161]},
       'geometry_name': 'geom',
       'properties': {'name': 'Unionport',
        'stacked': 1,
        'annoline1': 'Unionport',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.85053524451935,
         40.82977429787161,
         -73.85053524451935,
         40.82977429787161]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.46',
       'geometry': {'type': 'Point',
        'coordinates': [-73.84808271877168, 40.88456130303732]},
       'geometry_name': 'geom',
       'properties': {'name': 'Edenwald',
        'stacked': 1,
        'annoline1': 'Edenwald',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.84808271877168,
         40.88456130303732,
         -73.84808271877168,
         40.88456130303732]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.47',
       'geometry': {'type': 'Point',
        'coordinates': [-74.03062069353813, 40.625801065010656]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bay Ridge',
        'stacked': 1,
        'annoline1': 'Bay Ridge',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-74.03062069353813,
         40.625801065010656,
         -74.03062069353813,
         40.625801065010656]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.48',
       'geometry': {'type': 'Point',
        'coordinates': [-73.99517998380729, 40.61100890202044]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bensonhurst',
        'stacked': 1,
        'annoline1': 'Bensonhurst',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.99517998380729,
         40.61100890202044,
         -73.99517998380729,
         40.61100890202044]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.49',
       'geometry': {'type': 'Point',
        'coordinates': [-74.01031618527784, 40.64510294925429]},
       'geometry_name': 'geom',
       'properties': {'name': 'Sunset Park',
        'stacked': 2,
        'annoline1': 'Sunset',
        'annoline2': 'Park',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-74.01031618527784,
         40.64510294925429,
         -74.01031618527784,
         40.64510294925429]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.50',
       'geometry': {'type': 'Point',
        'coordinates': [-73.95424093127393, 40.7302009848647]},
       'geometry_name': 'geom',
       'properties': {'name': 'Greenpoint',
        'stacked': 1,
        'annoline1': 'Greenpoint',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.95424093127393,
         40.7302009848647,
         -73.95424093127393,
         40.7302009848647]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.51',
       'geometry': {'type': 'Point',
        'coordinates': [-73.97347087708445, 40.59526001306593]},
       'geometry_name': 'geom',
       'properties': {'name': 'Gravesend',
        'stacked': 1,
        'annoline1': 'Gravesend',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.97347087708445,
         40.59526001306593,
         -73.97347087708445,
         40.59526001306593]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.52',
       'geometry': {'type': 'Point',
        'coordinates': [-73.96509448785336, 40.57682506566604]},
       'geometry_name': 'geom',
       'properties': {'name': 'Brighton Beach',
        'stacked': 2,
        'annoline1': 'Brighton',
        'annoline2': 'Beach',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.96509448785336,
         40.57682506566604,
         -73.96509448785336,
         40.57682506566604]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.53',
       'geometry': {'type': 'Point',
        'coordinates': [-73.94318640482979, 40.58689012678384]},
       'geometry_name': 'geom',
       'properties': {'name': 'Sheepshead Bay',
        'stacked': 2,
        'annoline1': 'Sheepshead',
        'annoline2': 'Bay',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.94318640482979,
         40.58689012678384,
         -73.94318640482979,
         40.58689012678384]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.54',
       'geometry': {'type': 'Point',
        'coordinates': [-73.95743840559939, 40.61443251335098]},
       'geometry_name': 'geom',
       'properties': {'name': 'Manhattan Terrace',
        'stacked': 2,
        'annoline1': 'Manhattan',
        'annoline2': 'Terrace',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.95743840559939,
         40.61443251335098,
         -73.95743840559939,
         40.61443251335098]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.55',
       'geometry': {'type': 'Point',
        'coordinates': [-73.95840106533903, 40.63632589026677]},
       'geometry_name': 'geom',
       'properties': {'name': 'Flatbush',
        'stacked': 1,
        'annoline1': 'Flatbush',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.95840106533903,
         40.63632589026677,
         -73.95840106533903,
         40.63632589026677]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.56',
       'geometry': {'type': 'Point',
        'coordinates': [-73.94329119073582, 40.67082917695294]},
       'geometry_name': 'geom',
       'properties': {'name': 'Crown Heights',
        'stacked': 2,
        'annoline1': 'Crown',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.94329119073582,
         40.67082917695294,
         -73.94329119073582,
         40.67082917695294]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.57',
       'geometry': {'type': 'Point',
        'coordinates': [-73.93610256185836, 40.64171776668961]},
       'geometry_name': 'geom',
       'properties': {'name': 'East Flatbush',
        'stacked': 1,
        'annoline1': 'East Flatbush',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.93610256185836,
         40.64171776668961,
         -73.93610256185836,
         40.64171776668961]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.58',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98042110559474, 40.642381958003526]},
       'geometry_name': 'geom',
       'properties': {'name': 'Kensington',
        'stacked': 1,
        'annoline1': 'Kensington',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.98042110559474,
         40.642381958003526,
         -73.98042110559474,
         40.642381958003526]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.59',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98007340430172, 40.65694583575104]},
       'geometry_name': 'geom',
       'properties': {'name': 'Windsor Terrace',
        'stacked': 2,
        'annoline1': 'Windsor',
        'annoline2': 'Terrace',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.98007340430172,
         40.65694583575104,
         -73.98007340430172,
         40.65694583575104]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.60',
       'geometry': {'type': 'Point',
        'coordinates': [-73.9648592426269, 40.676822262254724]},
       'geometry_name': 'geom',
       'properties': {'name': 'Prospect Heights',
        'stacked': 2,
        'annoline1': 'Prospect',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.9648592426269,
         40.676822262254724,
         -73.9648592426269,
         40.676822262254724]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.61',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91023536176607, 40.66394994339755]},
       'geometry_name': 'geom',
       'properties': {'name': 'Brownsville',
        'stacked': 1,
        'annoline1': 'Brownsville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.91023536176607,
         40.66394994339755,
         -73.91023536176607,
         40.66394994339755]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.62',
       'geometry': {'type': 'Point',
        'coordinates': [-73.95811529220927, 40.70714439344251]},
       'geometry_name': 'geom',
       'properties': {'name': 'Williamsburg',
        'stacked': 1,
        'annoline1': 'Williamsburg',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.95811529220927,
         40.70714439344251,
         -73.95811529220927,
         40.70714439344251]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.63',
       'geometry': {'type': 'Point',
        'coordinates': [-73.92525797487045, 40.69811611017901]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bushwick',
        'stacked': 1,
        'annoline1': 'Bushwick',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.92525797487045,
         40.69811611017901,
         -73.92525797487045,
         40.69811611017901]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.64',
       'geometry': {'type': 'Point',
        'coordinates': [-73.94178488690297, 40.687231607720456]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bedford Stuyvesant',
        'stacked': 1,
        'annoline1': 'Bedford Stuyvesant',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.94178488690297,
         40.687231607720456,
         -73.94178488690297,
         40.687231607720456]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.65',
       'geometry': {'type': 'Point',
        'coordinates': [-73.99378225496424, 40.695863722724084]},
       'geometry_name': 'geom',
       'properties': {'name': 'Brooklyn Heights',
        'stacked': 2,
        'annoline1': 'Brooklyn',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.99378225496424,
         40.695863722724084,
         -73.99378225496424,
         40.695863722724084]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.66',
       'geometry': {'type': 'Point',
        'coordinates': [-73.99856139218463, 40.687919722485574]},
       'geometry_name': 'geom',
       'properties': {'name': 'Cobble Hill',
        'stacked': 2,
        'annoline1': 'Cobble',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.99856139218463,
         40.687919722485574,
         -73.99856139218463,
         40.687919722485574]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.67',
       'geometry': {'type': 'Point',
        'coordinates': [-73.99465372828006, 40.680540231076485]},
       'geometry_name': 'geom',
       'properties': {'name': 'Carroll Gardens',
        'stacked': 2,
        'annoline1': 'Carroll',
        'annoline2': 'Gardens',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.99465372828006,
         40.680540231076485,
         -73.99465372828006,
         40.680540231076485]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.68',
       'geometry': {'type': 'Point',
        'coordinates': [-74.0127589747356, 40.676253230250886]},
       'geometry_name': 'geom',
       'properties': {'name': 'Red Hook',
        'stacked': 2,
        'annoline1': 'Red',
        'annoline2': 'Hook',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-74.0127589747356,
         40.676253230250886,
         -74.0127589747356,
         40.676253230250886]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.69',
       'geometry': {'type': 'Point',
        'coordinates': [-73.99444087145339, 40.673931143187154]},
       'geometry_name': 'geom',
       'properties': {'name': 'Gowanus',
        'stacked': 1,
        'annoline1': 'Gowanus',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.99444087145339,
         40.673931143187154,
         -73.99444087145339,
         40.673931143187154]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.70',
       'geometry': {'type': 'Point',
        'coordinates': [-73.97290574369092, 40.68852726018977]},
       'geometry_name': 'geom',
       'properties': {'name': 'Fort Greene',
        'stacked': 2,
        'annoline1': 'Fort',
        'annoline2': 'Greene',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.97290574369092,
         40.68852726018977,
         -73.97290574369092,
         40.68852726018977]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.71',
       'geometry': {'type': 'Point',
        'coordinates': [-73.97705030183924, 40.67232052268197]},
       'geometry_name': 'geom',
       'properties': {'name': 'Park Slope',
        'stacked': 2,
        'annoline1': 'Park',
        'annoline2': 'Slope',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.97705030183924,
         40.67232052268197,
         -73.97705030183924,
         40.67232052268197]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.72',
       'geometry': {'type': 'Point',
        'coordinates': [-73.87661596457296, 40.68239101144211]},
       'geometry_name': 'geom',
       'properties': {'name': 'Cypress Hills',
        'stacked': 2,
        'annoline1': 'Cypress',
        'annoline2': 'Hills',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.87661596457296,
         40.68239101144211,
         -73.87661596457296,
         40.68239101144211]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.73',
       'geometry': {'type': 'Point',
        'coordinates': [-73.88069863917366, 40.669925700847045]},
       'geometry_name': 'geom',
       'properties': {'name': 'East New York',
        'stacked': 1,
        'annoline1': 'East New York',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.88069863917366,
         40.669925700847045,
         -73.88069863917366,
         40.669925700847045]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.74',
       'geometry': {'type': 'Point',
        'coordinates': [-73.87936970045875, 40.64758905230874]},
       'geometry_name': 'geom',
       'properties': {'name': 'Starrett City',
        'stacked': 2,
        'annoline1': 'Starrett',
        'annoline2': 'City',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.87936970045875,
         40.64758905230874,
         -73.87936970045875,
         40.64758905230874]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.75',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90209269778966, 40.63556432797428]},
       'geometry_name': 'geom',
       'properties': {'name': 'Canarsie',
        'stacked': 1,
        'annoline1': 'Canarsie',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.90209269778966,
         40.63556432797428,
         -73.90209269778966,
         40.63556432797428]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.76',
       'geometry': {'type': 'Point',
        'coordinates': [-73.92911302644674, 40.630446043757466]},
       'geometry_name': 'geom',
       'properties': {'name': 'Flatlands',
        'stacked': 1,
        'annoline1': 'Flatlands',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.92911302644674,
         40.630446043757466,
         -73.92911302644674,
         40.630446043757466]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.77',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90818571777423, 40.606336421685626]},
       'geometry_name': 'geom',
       'properties': {'name': 'Mill Island',
        'stacked': 2,
        'annoline1': 'Mill',
        'annoline2': 'Island',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.90818571777423,
         40.606336421685626,
         -73.90818571777423,
         40.606336421685626]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.78',
       'geometry': {'type': 'Point',
        'coordinates': [-73.94353722891886, 40.57791350308657]},
       'geometry_name': 'geom',
       'properties': {'name': 'Manhattan Beach',
        'stacked': 2,
        'annoline1': 'Manhattan',
        'annoline2': 'Beach',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.94353722891886,
         40.57791350308657,
         -73.94353722891886,
         40.57791350308657]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.79',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98868295821637, 40.57429256471601]},
       'geometry_name': 'geom',
       'properties': {'name': 'Coney Island',
        'stacked': 1,
        'annoline1': 'Coney Island',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.98868295821637,
         40.57429256471601,
         -73.98868295821637,
         40.57429256471601]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.80',
       'geometry': {'type': 'Point',
        'coordinates': [-73.99875221443519, 40.59951870282238]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bath Beach',
        'stacked': 2,
        'annoline1': 'Bath',
        'annoline2': 'Beach',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.99875221443519,
         40.59951870282238,
         -73.99875221443519,
         40.59951870282238]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.81',
       'geometry': {'type': 'Point',
        'coordinates': [-73.99049823044811, 40.633130512758015]},
       'geometry_name': 'geom',
       'properties': {'name': 'Borough Park',
        'stacked': 2,
        'annoline1': 'Borough',
        'annoline2': 'Park',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.99049823044811,
         40.633130512758015,
         -73.99049823044811,
         40.633130512758015]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.82',
       'geometry': {'type': 'Point',
        'coordinates': [-74.01931375636022, 40.619219457722636]},
       'geometry_name': 'geom',
       'properties': {'name': 'Dyker Heights',
        'stacked': 2,
        'annoline1': 'Dyker',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-74.01931375636022,
         40.619219457722636,
         -74.01931375636022,
         40.619219457722636]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.83',
       'geometry': {'type': 'Point',
        'coordinates': [-73.93010170691196, 40.590848433902046]},
       'geometry_name': 'geom',
       'properties': {'name': 'Gerritsen Beach',
        'stacked': 2,
        'annoline1': 'Gerritsen',
        'annoline2': 'Beach',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.93010170691196,
         40.590848433902046,
         -73.93010170691196,
         40.590848433902046]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.84',
       'geometry': {'type': 'Point',
        'coordinates': [-73.93134404108497, 40.609747779894604]},
       'geometry_name': 'geom',
       'properties': {'name': 'Marine Park',
        'stacked': 1,
        'annoline1': 'Marine Park',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.93134404108497,
         40.609747779894604,
         -73.93134404108497,
         40.609747779894604]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.85',
       'geometry': {'type': 'Point',
        'coordinates': [-73.96784306216367, 40.693229421881504]},
       'geometry_name': 'geom',
       'properties': {'name': 'Clinton Hill',
        'stacked': 2,
        'annoline1': 'Clinton',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.96784306216367,
         40.693229421881504,
         -73.96784306216367,
         40.693229421881504]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.86',
       'geometry': {'type': 'Point',
        'coordinates': [-74.0078731120024, 40.57637537890224]},
       'geometry_name': 'geom',
       'properties': {'name': 'Sea Gate',
        'stacked': 2,
        'annoline1': 'Sea',
        'annoline2': 'Gate',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-74.0078731120024,
         40.57637537890224,
         -74.0078731120024,
         40.57637537890224]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.87',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98346337431099, 40.69084402109802]},
       'geometry_name': 'geom',
       'properties': {'name': 'Downtown',
        'stacked': 1,
        'annoline1': 'Downtown',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.98346337431099,
         40.69084402109802,
         -73.98346337431099,
         40.69084402109802]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.88',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98374824115798, 40.685682912091444]},
       'geometry_name': 'geom',
       'properties': {'name': 'Boerum Hill',
        'stacked': 2,
        'annoline1': 'Boerum',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.98374824115798,
         40.685682912091444,
         -73.98374824115798,
         40.685682912091444]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.89',
       'geometry': {'type': 'Point',
        'coordinates': [-73.95489867077713, 40.658420017469815]},
       'geometry_name': 'geom',
       'properties': {'name': 'Prospect Lefferts Gardens',
        'stacked': 3,
        'annoline1': 'Prospect',
        'annoline2': 'Lefferts',
        'annoline3': 'Gardens',
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.95489867077713,
         40.658420017469815,
         -73.95489867077713,
         40.658420017469815]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.90',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91306831787395, 40.678402554795355]},
       'geometry_name': 'geom',
       'properties': {'name': 'Ocean Hill',
        'stacked': 2,
        'annoline1': 'Ocean',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.91306831787395,
         40.678402554795355,
         -73.91306831787395,
         40.678402554795355]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.91',
       'geometry': {'type': 'Point',
        'coordinates': [-73.86797598081334, 40.67856995727479]},
       'geometry_name': 'geom',
       'properties': {'name': 'City Line',
        'stacked': 2,
        'annoline1': 'City',
        'annoline2': 'Line',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.86797598081334,
         40.67856995727479,
         -73.86797598081334,
         40.67856995727479]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.92',
       'geometry': {'type': 'Point',
        'coordinates': [-73.89855633630317, 40.61514955045308]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bergen Beach',
        'stacked': 2,
        'annoline1': 'Bergen',
        'annoline2': 'Beach',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.89855633630317,
         40.61514955045308,
         -73.89855633630317,
         40.61514955045308]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.93',
       'geometry': {'type': 'Point',
        'coordinates': [-73.95759523489838, 40.62559589869843]},
       'geometry_name': 'geom',
       'properties': {'name': 'Midwood',
        'stacked': 1,
        'annoline1': 'Midwood',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.95759523489838,
         40.62559589869843,
         -73.95759523489838,
         40.62559589869843]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.94',
       'geometry': {'type': 'Point',
        'coordinates': [-73.96261316716048, 40.647008603185185]},
       'geometry_name': 'geom',
       'properties': {'name': 'Prospect Park South',
        'stacked': 2,
        'annoline1': 'Prospect',
        'annoline2': 'Park South',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.96261316716048,
         40.647008603185185,
         -73.96261316716048,
         40.647008603185185]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.95',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91607483951324, 40.62384524478419]},
       'geometry_name': 'geom',
       'properties': {'name': 'Georgetown',
        'stacked': 1,
        'annoline1': 'Georgetown',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.91607483951324,
         40.62384524478419,
         -73.91607483951324,
         40.62384524478419]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.96',
       'geometry': {'type': 'Point',
        'coordinates': [-73.93885815269195, 40.70849241041548]},
       'geometry_name': 'geom',
       'properties': {'name': 'East Williamsburg',
        'stacked': 2,
        'annoline1': 'East',
        'annoline2': 'Williamsburg',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.93885815269195,
         40.70849241041548,
         -73.93885815269195,
         40.70849241041548]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.97',
       'geometry': {'type': 'Point',
        'coordinates': [-73.95880857587582, 40.714822906532014]},
       'geometry_name': 'geom',
       'properties': {'name': 'North Side',
        'stacked': 1,
        'annoline1': 'North Side',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.95880857587582,
         40.714822906532014,
         -73.95880857587582,
         40.714822906532014]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.98',
       'geometry': {'type': 'Point',
        'coordinates': [-73.95800095153331, 40.71086147265064]},
       'geometry_name': 'geom',
       'properties': {'name': 'South Side',
        'stacked': 1,
        'annoline1': 'South Side',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.95800095153331,
         40.71086147265064,
         -73.95800095153331,
         40.71086147265064]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.99',
       'geometry': {'type': 'Point',
        'coordinates': [-73.96836678035541, 40.61305976667942]},
       'geometry_name': 'geom',
       'properties': {'name': 'Ocean Parkway',
        'stacked': 2,
        'annoline1': 'Ocean',
        'annoline2': 'Parkway',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.96836678035541,
         40.61305976667942,
         -73.96836678035541,
         40.61305976667942]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.100',
       'geometry': {'type': 'Point',
        'coordinates': [-74.03197914537984, 40.61476812694226]},
       'geometry_name': 'geom',
       'properties': {'name': 'Fort Hamilton',
        'stacked': 2,
        'annoline1': 'Fort',
        'annoline2': 'Hamilton',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-74.03197914537984,
         40.61476812694226,
         -74.03197914537984,
         40.61476812694226]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.101',
       'geometry': {'type': 'Point',
        'coordinates': [-73.99427936255978, 40.71561842231432]},
       'geometry_name': 'geom',
       'properties': {'name': 'Chinatown',
        'stacked': 1,
        'annoline1': 'Chinatown',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.99427936255978,
         40.71561842231432,
         -73.99427936255978,
         40.71561842231432]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.102',
       'geometry': {'type': 'Point',
        'coordinates': [-73.93690027985234, 40.85190252555305]},
       'geometry_name': 'geom',
       'properties': {'name': 'Washington Heights',
        'stacked': 2,
        'annoline1': 'Washington',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.93690027985234,
         40.85190252555305,
         -73.93690027985234,
         40.85190252555305]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.103',
       'geometry': {'type': 'Point',
        'coordinates': [-73.92121042203897, 40.86768396449915]},
       'geometry_name': 'geom',
       'properties': {'name': 'Inwood',
        'stacked': 1,
        'annoline1': 'Inwood',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.92121042203897,
         40.86768396449915,
         -73.92121042203897,
         40.86768396449915]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.104',
       'geometry': {'type': 'Point',
        'coordinates': [-73.94968791883366, 40.823604284811935]},
       'geometry_name': 'geom',
       'properties': {'name': 'Hamilton Heights',
        'stacked': 2,
        'annoline1': 'Hamilton',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.94968791883366,
         40.823604284811935,
         -73.94968791883366,
         40.823604284811935]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.105',
       'geometry': {'type': 'Point',
        'coordinates': [-73.9573853935188, 40.8169344294978]},
       'geometry_name': 'geom',
       'properties': {'name': 'Manhattanville',
        'stacked': 2,
        'annoline1': 'Manhattanville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.9573853935188,
         40.8169344294978,
         -73.9573853935188,
         40.8169344294978]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.106',
       'geometry': {'type': 'Point',
        'coordinates': [-73.94321112603905, 40.81597606742414]},
       'geometry_name': 'geom',
       'properties': {'name': 'Central Harlem',
        'stacked': 2,
        'annoline1': 'Central',
        'annoline2': 'Harlem',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.94321112603905,
         40.81597606742414,
         -73.94321112603905,
         40.81597606742414]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.107',
       'geometry': {'type': 'Point',
        'coordinates': [-73.94418223148524, 40.79224946663033]},
       'geometry_name': 'geom',
       'properties': {'name': 'East Harlem',
        'stacked': 2,
        'annoline1': 'East',
        'annoline2': 'Harlem',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.94418223148524,
         40.79224946663033,
         -73.94418223148524,
         40.79224946663033]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.108',
       'geometry': {'type': 'Point',
        'coordinates': [-73.96050763135, 40.775638573301805]},
       'geometry_name': 'geom',
       'properties': {'name': 'Upper East Side',
        'stacked': 3,
        'annoline1': 'Upper',
        'annoline2': 'East',
        'annoline3': 'Side',
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.96050763135,
         40.775638573301805,
         -73.96050763135,
         40.775638573301805]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.109',
       'geometry': {'type': 'Point',
        'coordinates': [-73.94711784471826, 40.775929849884875]},
       'geometry_name': 'geom',
       'properties': {'name': 'Yorkville',
        'stacked': 1,
        'annoline1': 'Yorkville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.94711784471826,
         40.775929849884875,
         -73.94711784471826,
         40.775929849884875]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.110',
       'geometry': {'type': 'Point',
        'coordinates': [-73.9588596881376, 40.76811265828733]},
       'geometry_name': 'geom',
       'properties': {'name': 'Lenox Hill',
        'stacked': 2,
        'annoline1': 'Lenox',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.9588596881376,
         40.76811265828733,
         -73.9588596881376,
         40.76811265828733]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.111',
       'geometry': {'type': 'Point',
        'coordinates': [-73.94916769227953, 40.76215960576283]},
       'geometry_name': 'geom',
       'properties': {'name': 'Roosevelt Island',
        'stacked': 1,
        'annoline1': 'Roosevelt Island',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 56,
        'borough': 'Manhattan',
        'bbox': [-73.94916769227953,
         40.76215960576283,
         -73.94916769227953,
         40.76215960576283]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.112',
       'geometry': {'type': 'Point',
        'coordinates': [-73.97705923630603, 40.787657998534854]},
       'geometry_name': 'geom',
       'properties': {'name': 'Upper West Side',
        'stacked': 3,
        'annoline1': 'Upper',
        'annoline2': 'West',
        'annoline3': 'Side',
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.97705923630603,
         40.787657998534854,
         -73.97705923630603,
         40.787657998534854]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.113',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98533777001262, 40.77352888942166]},
       'geometry_name': 'geom',
       'properties': {'name': 'Lincoln Square',
        'stacked': 2,
        'annoline1': 'Lincoln',
        'annoline2': 'Square',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.98533777001262,
         40.77352888942166,
         -73.98533777001262,
         40.77352888942166]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.114',
       'geometry': {'type': 'Point',
        'coordinates': [-73.99611936309479, 40.75910089146212]},
       'geometry_name': 'geom',
       'properties': {'name': 'Clinton',
        'stacked': 1,
        'annoline1': 'Clinton',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.99611936309479,
         40.75910089146212,
         -73.99611936309479,
         40.75910089146212]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.115',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98166882730304, 40.75469110270623]},
       'geometry_name': 'geom',
       'properties': {'name': 'Midtown',
        'stacked': 1,
        'annoline1': 'Midtown',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.98166882730304,
         40.75469110270623,
         -73.98166882730304,
         40.75469110270623]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.116',
       'geometry': {'type': 'Point',
        'coordinates': [-73.97833207924127, 40.748303077252174]},
       'geometry_name': 'geom',
       'properties': {'name': 'Murray Hill',
        'stacked': 2,
        'annoline1': 'Murray',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.97833207924127,
         40.748303077252174,
         -73.97833207924127,
         40.748303077252174]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.117',
       'geometry': {'type': 'Point',
        'coordinates': [-74.00311633472813, 40.744034706747975]},
       'geometry_name': 'geom',
       'properties': {'name': 'Chelsea',
        'stacked': 1,
        'annoline1': 'Chelsea',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-74.00311633472813,
         40.744034706747975,
         -74.00311633472813,
         40.744034706747975]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.118',
       'geometry': {'type': 'Point',
        'coordinates': [-73.99991402945902, 40.72693288536128]},
       'geometry_name': 'geom',
       'properties': {'name': 'Greenwich Village',
        'stacked': 2,
        'annoline1': 'Greenwich',
        'annoline2': 'Village',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.99991402945902,
         40.72693288536128,
         -73.99991402945902,
         40.72693288536128]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.119',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98222616506416, 40.727846777270244]},
       'geometry_name': 'geom',
       'properties': {'name': 'East Village',
        'stacked': 2,
        'annoline1': 'East',
        'annoline2': 'Village',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.98222616506416,
         40.727846777270244,
         -73.98222616506416,
         40.727846777270244]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.120',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98089031999291, 40.71780674892765]},
       'geometry_name': 'geom',
       'properties': {'name': 'Lower East Side',
        'stacked': 3,
        'annoline1': 'Lower',
        'annoline2': 'East',
        'annoline3': 'Side',
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.98089031999291,
         40.71780674892765,
         -73.98089031999291,
         40.71780674892765]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.121',
       'geometry': {'type': 'Point',
        'coordinates': [-74.01068328559087, 40.721521967443216]},
       'geometry_name': 'geom',
       'properties': {'name': 'Tribeca',
        'stacked': 1,
        'annoline1': 'Tribeca',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-74.01068328559087,
         40.721521967443216,
         -74.01068328559087,
         40.721521967443216]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.122',
       'geometry': {'type': 'Point',
        'coordinates': [-73.99730467208073, 40.71932379395907]},
       'geometry_name': 'geom',
       'properties': {'name': 'Little Italy',
        'stacked': 2,
        'annoline1': 'Little',
        'annoline2': 'Italy',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.99730467208073,
         40.71932379395907,
         -73.99730467208073,
         40.71932379395907]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.123',
       'geometry': {'type': 'Point',
        'coordinates': [-74.00065666959759, 40.72218384131794]},
       'geometry_name': 'geom',
       'properties': {'name': 'Soho',
        'stacked': 1,
        'annoline1': 'Soho',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-74.00065666959759,
         40.72218384131794,
         -74.00065666959759,
         40.72218384131794]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.124',
       'geometry': {'type': 'Point',
        'coordinates': [-74.00617998126812, 40.73443393572434]},
       'geometry_name': 'geom',
       'properties': {'name': 'West Village',
        'stacked': 2,
        'annoline1': 'West',
        'annoline2': 'Village',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-74.00617998126812,
         40.73443393572434,
         -74.00617998126812,
         40.73443393572434]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.125',
       'geometry': {'type': 'Point',
        'coordinates': [-73.96428617740655, 40.797307041702865]},
       'geometry_name': 'geom',
       'properties': {'name': 'Manhattan Valley',
        'stacked': 2,
        'annoline1': 'Manhattan',
        'annoline2': 'Valley',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.96428617740655,
         40.797307041702865,
         -73.96428617740655,
         40.797307041702865]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.126',
       'geometry': {'type': 'Point',
        'coordinates': [-73.96389627905332, 40.807999738165826]},
       'geometry_name': 'geom',
       'properties': {'name': 'Morningside Heights',
        'stacked': 2,
        'annoline1': 'Morningside',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.96389627905332,
         40.807999738165826,
         -73.96389627905332,
         40.807999738165826]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.127',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98137594833541, 40.737209832715]},
       'geometry_name': 'geom',
       'properties': {'name': 'Gramercy',
        'stacked': 1,
        'annoline1': 'Gramercy',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.98137594833541,
         40.737209832715,
         -73.98137594833541,
         40.737209832715]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.128',
       'geometry': {'type': 'Point',
        'coordinates': [-74.01686930508617, 40.71193198394565]},
       'geometry_name': 'geom',
       'properties': {'name': 'Battery Park City',
        'stacked': 3,
        'annoline1': 'Battery',
        'annoline2': 'Park',
        'annoline3': 'City',
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-74.01686930508617,
         40.71193198394565,
         -74.01686930508617,
         40.71193198394565]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.129',
       'geometry': {'type': 'Point',
        'coordinates': [-74.0106654452127, 40.70710710727048]},
       'geometry_name': 'geom',
       'properties': {'name': 'Financial District',
        'stacked': 2,
        'annoline1': 'Financial',
        'annoline2': 'District',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-74.0106654452127,
         40.70710710727048,
         -74.0106654452127,
         40.70710710727048]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.130',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91565374304234, 40.76850859335492]},
       'geometry_name': 'geom',
       'properties': {'name': 'Astoria',
        'stacked': 1,
        'annoline1': 'Astoria',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.91565374304234,
         40.76850859335492,
         -73.91565374304234,
         40.76850859335492]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.131',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90184166838284, 40.74634908860222]},
       'geometry_name': 'geom',
       'properties': {'name': 'Woodside',
        'stacked': 1,
        'annoline1': 'Woodside',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.90184166838284,
         40.74634908860222,
         -73.90184166838284,
         40.74634908860222]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.132',
       'geometry': {'type': 'Point',
        'coordinates': [-73.88282109164365, 40.75198138007367]},
       'geometry_name': 'geom',
       'properties': {'name': 'Jackson Heights',
        'stacked': 2,
        'annoline1': 'Jackson',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.88282109164365,
         40.75198138007367,
         -73.88282109164365,
         40.75198138007367]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.133',
       'geometry': {'type': 'Point',
        'coordinates': [-73.88165622288388, 40.744048505122024]},
       'geometry_name': 'geom',
       'properties': {'name': 'Elmhurst',
        'stacked': 1,
        'annoline1': 'Elmhurst',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.88165622288388,
         40.744048505122024,
         -73.88165622288388,
         40.744048505122024]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.134',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8381376460028, 40.65422527738487]},
       'geometry_name': 'geom',
       'properties': {'name': 'Howard Beach',
        'stacked': 2,
        'annoline1': 'Howard',
        'annoline2': 'Beach',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.8381376460028,
         40.65422527738487,
         -73.8381376460028,
         40.65422527738487]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.135',
       'geometry': {'type': 'Point',
        'coordinates': [-73.85682497345258, 40.74238175015667]},
       'geometry_name': 'geom',
       'properties': {'name': 'Corona',
        'stacked': 1,
        'annoline1': 'Corona',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.85682497345258,
         40.74238175015667,
         -73.85682497345258,
         40.74238175015667]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.136',
       'geometry': {'type': 'Point',
        'coordinates': [-73.84447500788983, 40.72526378216503]},
       'geometry_name': 'geom',
       'properties': {'name': 'Forest Hills',
        'stacked': 2,
        'annoline1': 'Forest',
        'annoline2': 'Hills',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.84447500788983,
         40.72526378216503,
         -73.84447500788983,
         40.72526378216503]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.137',
       'geometry': {'type': 'Point',
        'coordinates': [-73.82981905825703, 40.7051790354148]},
       'geometry_name': 'geom',
       'properties': {'name': 'Kew Gardens',
        'stacked': 2,
        'annoline1': 'Kew',
        'annoline2': 'Gardens',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.82981905825703,
         40.7051790354148,
         -73.82981905825703,
         40.7051790354148]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.138',
       'geometry': {'type': 'Point',
        'coordinates': [-73.83183321446887, 40.69794731471763]},
       'geometry_name': 'geom',
       'properties': {'name': 'Richmond Hill',
        'stacked': 2,
        'annoline1': 'Richmond',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.83183321446887,
         40.69794731471763,
         -73.83183321446887,
         40.69794731471763]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.139',
       'geometry': {'type': 'Point',
        'coordinates': [-73.83177300329582, 40.76445419697846]},
       'geometry_name': 'geom',
       'properties': {'name': 'Flushing',
        'stacked': 1,
        'annoline1': 'Flushing',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.83177300329582,
         40.76445419697846,
         -73.83177300329582,
         40.76445419697846]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.140',
       'geometry': {'type': 'Point',
        'coordinates': [-73.93920223915505, 40.75021734610528]},
       'geometry_name': 'geom',
       'properties': {'name': 'Long Island City',
        'stacked': 3,
        'annoline1': 'Long',
        'annoline2': 'Island',
        'annoline3': 'City',
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.93920223915505,
         40.75021734610528,
         -73.93920223915505,
         40.75021734610528]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.141',
       'geometry': {'type': 'Point',
        'coordinates': [-73.92691617561577, 40.74017628351924]},
       'geometry_name': 'geom',
       'properties': {'name': 'Sunnyside',
        'stacked': 1,
        'annoline1': 'Sunnyside',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.92691617561577,
         40.74017628351924,
         -73.92691617561577,
         40.74017628351924]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.142',
       'geometry': {'type': 'Point',
        'coordinates': [-73.86704147658772, 40.76407323883091]},
       'geometry_name': 'geom',
       'properties': {'name': 'East Elmhurst',
        'stacked': 2,
        'annoline1': 'East',
        'annoline2': 'Elmhurst',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.86704147658772,
         40.76407323883091,
         -73.86704147658772,
         40.76407323883091]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.143',
       'geometry': {'type': 'Point',
        'coordinates': [-73.89621713626859, 40.725427374093606]},
       'geometry_name': 'geom',
       'properties': {'name': 'Maspeth',
        'stacked': 1,
        'annoline1': 'Maspeth',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.89621713626859,
         40.725427374093606,
         -73.89621713626859,
         40.725427374093606]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.144',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90143517559589, 40.70832315613858]},
       'geometry_name': 'geom',
       'properties': {'name': 'Ridgewood',
        'stacked': 1,
        'annoline1': 'Ridgewood',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.90143517559589,
         40.70832315613858,
         -73.90143517559589,
         40.70832315613858]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.145',
       'geometry': {'type': 'Point',
        'coordinates': [-73.87074167435605, 40.70276242967838]},
       'geometry_name': 'geom',
       'properties': {'name': 'Glendale',
        'stacked': 1,
        'annoline1': 'Glendale',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.87074167435605,
         40.70276242967838,
         -73.87074167435605,
         40.70276242967838]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.146',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8578268690537, 40.72897409480735]},
       'geometry_name': 'geom',
       'properties': {'name': 'Rego Park',
        'stacked': 1,
        'annoline1': 'Rego Park',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.8578268690537,
         40.72897409480735,
         -73.8578268690537,
         40.72897409480735]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.147',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8581104655432, 40.68988687915789]},
       'geometry_name': 'geom',
       'properties': {'name': 'Woodhaven',
        'stacked': 1,
        'annoline1': 'Woodhaven',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.8581104655432,
         40.68988687915789,
         -73.8581104655432,
         40.68988687915789]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.148',
       'geometry': {'type': 'Point',
        'coordinates': [-73.84320266173447, 40.680708468265415]},
       'geometry_name': 'geom',
       'properties': {'name': 'Ozone Park',
        'stacked': 1,
        'annoline1': 'Ozone Park',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.84320266173447,
         40.680708468265415,
         -73.84320266173447,
         40.680708468265415]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.149',
       'geometry': {'type': 'Point',
        'coordinates': [-73.80986478649041, 40.66854957767195]},
       'geometry_name': 'geom',
       'properties': {'name': 'South Ozone Park',
        'stacked': 2,
        'annoline1': 'South',
        'annoline2': 'Ozone Park',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.80986478649041,
         40.66854957767195,
         -73.80986478649041,
         40.66854957767195]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.150',
       'geometry': {'type': 'Point',
        'coordinates': [-73.84304528896125, 40.784902749260205]},
       'geometry_name': 'geom',
       'properties': {'name': 'College Point',
        'stacked': 2,
        'annoline1': 'College',
        'annoline2': 'Point',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.84304528896125,
         40.784902749260205,
         -73.84304528896125,
         40.784902749260205]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.151',
       'geometry': {'type': 'Point',
        'coordinates': [-73.81420216610863, 40.78129076602694]},
       'geometry_name': 'geom',
       'properties': {'name': 'Whitestone',
        'stacked': 1,
        'annoline1': 'Whitestone',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.81420216610863,
         40.78129076602694,
         -73.81420216610863,
         40.78129076602694]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.152',
       'geometry': {'type': 'Point',
        'coordinates': [-73.7742736306867, 40.76604063281064]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bayside',
        'stacked': 1,
        'annoline1': 'Bayside',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.7742736306867,
         40.76604063281064,
         -73.7742736306867,
         40.76604063281064]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.153',
       'geometry': {'type': 'Point',
        'coordinates': [-73.79176243728061, 40.76172954903262]},
       'geometry_name': 'geom',
       'properties': {'name': 'Auburndale',
        'stacked': 1,
        'annoline1': 'Auburndale',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.79176243728061,
         40.76172954903262,
         -73.79176243728061,
         40.76172954903262]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.154',
       'geometry': {'type': 'Point',
        'coordinates': [-73.7388977558074, 40.7708261928267]},
       'geometry_name': 'geom',
       'properties': {'name': 'Little Neck',
        'stacked': 2,
        'annoline1': 'Little',
        'annoline2': 'Neck',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.7388977558074,
         40.7708261928267,
         -73.7388977558074,
         40.7708261928267]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.155',
       'geometry': {'type': 'Point',
        'coordinates': [-73.7424982072733, 40.76684609790763]},
       'geometry_name': 'geom',
       'properties': {'name': 'Douglaston',
        'stacked': 1,
        'annoline1': 'Douglaston',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.7424982072733,
         40.76684609790763,
         -73.7424982072733,
         40.76684609790763]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.156',
       'geometry': {'type': 'Point',
        'coordinates': [-73.71548118999145, 40.74944079974332]},
       'geometry_name': 'geom',
       'properties': {'name': 'Glen Oaks',
        'stacked': 2,
        'annoline1': 'Glen',
        'annoline2': 'Oaks',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.71548118999145,
         40.74944079974332,
         -73.71548118999145,
         40.74944079974332]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.157',
       'geometry': {'type': 'Point',
        'coordinates': [-73.72012814826903, 40.72857318176675]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bellerose',
        'stacked': 1,
        'annoline1': 'Bellerose',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.72012814826903,
         40.72857318176675,
         -73.72012814826903,
         40.72857318176675]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.158',
       'geometry': {'type': 'Point',
        'coordinates': [-73.82087764933566, 40.722578244228046]},
       'geometry_name': 'geom',
       'properties': {'name': 'Kew Gardens Hills',
        'stacked': 3,
        'annoline1': 'Kew',
        'annoline2': 'Gardens',
        'annoline3': 'Hills',
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.82087764933566,
         40.722578244228046,
         -73.82087764933566,
         40.722578244228046]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.159',
       'geometry': {'type': 'Point',
        'coordinates': [-73.78271337003264, 40.7343944653313]},
       'geometry_name': 'geom',
       'properties': {'name': 'Fresh Meadows',
        'stacked': 2,
        'annoline1': 'Fresh',
        'annoline2': 'Meadows',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.78271337003264,
         40.7343944653313,
         -73.78271337003264,
         40.7343944653313]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.160',
       'geometry': {'type': 'Point',
        'coordinates': [-73.81174822458634, 40.71093547252271]},
       'geometry_name': 'geom',
       'properties': {'name': 'Briarwood',
        'stacked': 1,
        'annoline1': 'Briarwood',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.81174822458634,
         40.71093547252271,
         -73.81174822458634,
         40.71093547252271]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.161',
       'geometry': {'type': 'Point',
        'coordinates': [-73.79690165888289, 40.70465736068717]},
       'geometry_name': 'geom',
       'properties': {'name': 'Jamaica Center',
        'stacked': 2,
        'annoline1': 'Jamaica',
        'annoline2': 'Center',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.79690165888289,
         40.70465736068717,
         -73.79690165888289,
         40.70465736068717]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.162',
       'geometry': {'type': 'Point',
        'coordinates': [-73.75494976234332, 40.74561857141855]},
       'geometry_name': 'geom',
       'properties': {'name': 'Oakland Gardens',
        'stacked': 2,
        'annoline1': 'Oakland',
        'annoline2': 'Gardens',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.75494976234332,
         40.74561857141855,
         -73.75494976234332,
         40.74561857141855]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.163',
       'geometry': {'type': 'Point',
        'coordinates': [-73.73871484578424, 40.718893092167356]},
       'geometry_name': 'geom',
       'properties': {'name': 'Queens Village',
        'stacked': 2,
        'annoline1': 'Queens',
        'annoline2': 'Village',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.73871484578424,
         40.718893092167356,
         -73.73871484578424,
         40.718893092167356]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.164',
       'geometry': {'type': 'Point',
        'coordinates': [-73.75925009335594, 40.71124344191904]},
       'geometry_name': 'geom',
       'properties': {'name': 'Hollis',
        'stacked': 1,
        'annoline1': 'Hollis',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.75925009335594,
         40.71124344191904,
         -73.75925009335594,
         40.71124344191904]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.165',
       'geometry': {'type': 'Point',
        'coordinates': [-73.7904261313554, 40.696911253789885]},
       'geometry_name': 'geom',
       'properties': {'name': 'South Jamaica',
        'stacked': 1,
        'annoline1': 'South Jamaica',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.7904261313554,
         40.696911253789885,
         -73.7904261313554,
         40.696911253789885]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.166',
       'geometry': {'type': 'Point',
        'coordinates': [-73.75867603727717, 40.69444538522359]},
       'geometry_name': 'geom',
       'properties': {'name': 'St. Albans',
        'stacked': 1,
        'annoline1': 'St. Albans',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.75867603727717,
         40.69444538522359,
         -73.75867603727717,
         40.69444538522359]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.167',
       'geometry': {'type': 'Point',
        'coordinates': [-73.77258787620906, 40.67521139591733]},
       'geometry_name': 'geom',
       'properties': {'name': 'Rochdale',
        'stacked': 1,
        'annoline1': 'Rochdale',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.77258787620906,
         40.67521139591733,
         -73.77258787620906,
         40.67521139591733]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.168',
       'geometry': {'type': 'Point',
        'coordinates': [-73.76042092682287, 40.666230490368584]},
       'geometry_name': 'geom',
       'properties': {'name': 'Springfield Gardens',
        'stacked': 2,
        'annoline1': 'Springfield',
        'annoline2': 'Gardens',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.76042092682287,
         40.666230490368584,
         -73.76042092682287,
         40.666230490368584]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.169',
       'geometry': {'type': 'Point',
        'coordinates': [-73.73526873708026, 40.692774639160845]},
       'geometry_name': 'geom',
       'properties': {'name': 'Cambria Heights',
        'stacked': 2,
        'annoline1': 'Cambria',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.73526873708026,
         40.692774639160845,
         -73.73526873708026,
         40.692774639160845]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.170',
       'geometry': {'type': 'Point',
        'coordinates': [-73.73526079428278, 40.659816433428084]},
       'geometry_name': 'geom',
       'properties': {'name': 'Rosedale',
        'stacked': 1,
        'annoline1': 'Rosedale',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.73526079428278,
         40.659816433428084,
         -73.73526079428278,
         40.659816433428084]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.171',
       'geometry': {'type': 'Point',
        'coordinates': [-73.75497968043872, 40.603134432500894]},
       'geometry_name': 'geom',
       'properties': {'name': 'Far Rockaway',
        'stacked': 2,
        'annoline1': 'Far Rockaway',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.75497968043872,
         40.603134432500894,
         -73.75497968043872,
         40.603134432500894]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.172',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8200548911032, 40.60302658351238]},
       'geometry_name': 'geom',
       'properties': {'name': 'Broad Channel',
        'stacked': 2,
        'annoline1': 'Broad',
        'annoline2': 'Channel',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.8200548911032,
         40.60302658351238,
         -73.8200548911032,
         40.60302658351238]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.173',
       'geometry': {'type': 'Point',
        'coordinates': [-73.92551196994168, 40.55740128845452]},
       'geometry_name': 'geom',
       'properties': {'name': 'Breezy Point',
        'stacked': 2,
        'annoline1': 'Breezy',
        'annoline2': 'Point',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.92551196994168,
         40.55740128845452,
         -73.92551196994168,
         40.55740128845452]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.174',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90228960391673, 40.775923015642896]},
       'geometry_name': 'geom',
       'properties': {'name': 'Steinway',
        'stacked': 1,
        'annoline1': 'Steinway',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.90228960391673,
         40.775923015642896,
         -73.90228960391673,
         40.775923015642896]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.175',
       'geometry': {'type': 'Point',
        'coordinates': [-73.80436451720988, 40.79278140360048]},
       'geometry_name': 'geom',
       'properties': {'name': 'Beechhurst',
        'stacked': 1,
        'annoline1': 'Beechhurst',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.80436451720988,
         40.79278140360048,
         -73.80436451720988,
         40.79278140360048]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.176',
       'geometry': {'type': 'Point',
        'coordinates': [-73.7768022262158, 40.782842806245554]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bay Terrace',
        'stacked': 2,
        'annoline1': 'Bay',
        'annoline2': 'Terrace',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.7768022262158,
         40.782842806245554,
         -73.7768022262158,
         40.782842806245554]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.177',
       'geometry': {'type': 'Point',
        'coordinates': [-73.77613282391705, 40.595641807368494]},
       'geometry_name': 'geom',
       'properties': {'name': 'Edgemere',
        'stacked': 1,
        'annoline1': 'Edgemere',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.77613282391705,
         40.595641807368494,
         -73.77613282391705,
         40.595641807368494]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.178',
       'geometry': {'type': 'Point',
        'coordinates': [-73.79199233136943, 40.58914394372971]},
       'geometry_name': 'geom',
       'properties': {'name': 'Arverne',
        'stacked': 1,
        'annoline1': 'Arverne',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.79199233136943,
         40.58914394372971,
         -73.79199233136943,
         40.58914394372971]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.179',
       'geometry': {'type': 'Point',
        'coordinates': [-73.82236121088751, 40.582801696845586]},
       'geometry_name': 'geom',
       'properties': {'name': 'Rockaway Beach',
        'stacked': 2,
        'annoline1': 'Rockaway',
        'annoline2': 'Beach',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.82236121088751,
         40.582801696845586,
         -73.82236121088751,
         40.582801696845586]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.180',
       'geometry': {'type': 'Point',
        'coordinates': [-73.85754672410827, 40.572036730217015]},
       'geometry_name': 'geom',
       'properties': {'name': 'Neponsit',
        'stacked': 1,
        'annoline1': 'Neponsit',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.85754672410827,
         40.572036730217015,
         -73.85754672410827,
         40.572036730217015]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.181',
       'geometry': {'type': 'Point',
        'coordinates': [-73.81276269135866, 40.764126122614066]},
       'geometry_name': 'geom',
       'properties': {'name': 'Murray Hill',
        'stacked': 2,
        'annoline1': 'Murray',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.81276269135866,
         40.764126122614066,
         -73.81276269135866,
         40.764126122614066]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.182',
       'geometry': {'type': 'Point',
        'coordinates': [-73.70884705889246, 40.741378421945434]},
       'geometry_name': 'geom',
       'properties': {'name': 'Floral Park',
        'stacked': 1,
        'annoline1': 'Floral Park',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.70884705889246,
         40.741378421945434,
         -73.70884705889246,
         40.741378421945434]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.183',
       'geometry': {'type': 'Point',
        'coordinates': [-73.76714166714729, 40.7209572076444]},
       'geometry_name': 'geom',
       'properties': {'name': 'Holliswood',
        'stacked': 1,
        'annoline1': 'Holliswood',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.76714166714729,
         40.7209572076444,
         -73.76714166714729,
         40.7209572076444]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.184',
       'geometry': {'type': 'Point',
        'coordinates': [-73.7872269693666, 40.71680483014613]},
       'geometry_name': 'geom',
       'properties': {'name': 'Jamaica Estates',
        'stacked': 2,
        'annoline1': 'Jamaica',
        'annoline2': 'Estates',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.7872269693666,
         40.71680483014613,
         -73.7872269693666,
         40.71680483014613]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.185',
       'geometry': {'type': 'Point',
        'coordinates': [-73.82580915110559, 40.7445723092867]},
       'geometry_name': 'geom',
       'properties': {'name': 'Queensboro Hill',
        'stacked': 2,
        'annoline1': 'Queensboro',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.82580915110559,
         40.7445723092867,
         -73.82580915110559,
         40.7445723092867]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.186',
       'geometry': {'type': 'Point',
        'coordinates': [-73.79760300912672, 40.723824901829204]},
       'geometry_name': 'geom',
       'properties': {'name': 'Hillcrest',
        'stacked': 1,
        'annoline1': 'Hillcrest',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.79760300912672,
         40.723824901829204,
         -73.79760300912672,
         40.723824901829204]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.187',
       'geometry': {'type': 'Point',
        'coordinates': [-73.93157506072878, 40.761704526054146]},
       'geometry_name': 'geom',
       'properties': {'name': 'Ravenswood',
        'stacked': 1,
        'annoline1': 'Ravenswood',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.93157506072878,
         40.761704526054146,
         -73.93157506072878,
         40.761704526054146]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.188',
       'geometry': {'type': 'Point',
        'coordinates': [-73.84963782402441, 40.66391841925139]},
       'geometry_name': 'geom',
       'properties': {'name': 'Lindenwood',
        'stacked': 1,
        'annoline1': 'Lindenwood',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.84963782402441,
         40.66391841925139,
         -73.84963782402441,
         40.66391841925139]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.189',
       'geometry': {'type': 'Point',
        'coordinates': [-73.74025607989822, 40.66788389660247]},
       'geometry_name': 'geom',
       'properties': {'name': 'Laurelton',
        'stacked': 1,
        'annoline1': 'Laurelton',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.74025607989822,
         40.66788389660247,
         -73.74025607989822,
         40.66788389660247]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.190',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8625247141374, 40.736074570830795]},
       'geometry_name': 'geom',
       'properties': {'name': 'Lefrak City',
        'stacked': 2,
        'annoline1': 'Lefrak',
        'annoline2': 'City',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.8625247141374,
         40.736074570830795,
         -73.8625247141374,
         40.736074570830795]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.191',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8540175039252, 40.57615556543109]},
       'geometry_name': 'geom',
       'properties': {'name': 'Belle Harbor',
        'stacked': 1,
        'annoline1': 'Belle Harbor',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.8540175039252,
         40.57615556543109,
         -73.8540175039252,
         40.57615556543109]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.192',
       'geometry': {'type': 'Point',
        'coordinates': [-73.84153370226186, 40.58034295646131]},
       'geometry_name': 'geom',
       'properties': {'name': 'Rockaway Park',
        'stacked': 1,
        'annoline1': 'Rockaway Park',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.84153370226186,
         40.58034295646131,
         -73.84153370226186,
         40.58034295646131]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.193',
       'geometry': {'type': 'Point',
        'coordinates': [-73.79664750844047, 40.59771061565768]},
       'geometry_name': 'geom',
       'properties': {'name': 'Somerville',
        'stacked': 1,
        'annoline1': 'Somerville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.79664750844047,
         40.59771061565768,
         -73.79664750844047,
         40.59771061565768]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.194',
       'geometry': {'type': 'Point',
        'coordinates': [-73.75175310731153, 40.66000322733613]},
       'geometry_name': 'geom',
       'properties': {'name': 'Brookville',
        'stacked': 1,
        'annoline1': 'Brookville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.75175310731153,
         40.66000322733613,
         -73.75175310731153,
         40.66000322733613]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.195',
       'geometry': {'type': 'Point',
        'coordinates': [-73.73889198912481, 40.73301404027834]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bellaire',
        'stacked': 1,
        'annoline1': 'Bellaire',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.73889198912481,
         40.73301404027834,
         -73.73889198912481,
         40.73301404027834]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.196',
       'geometry': {'type': 'Point',
        'coordinates': [-73.85751790676447, 40.7540709990489]},
       'geometry_name': 'geom',
       'properties': {'name': 'North Corona',
        'stacked': 2,
        'annoline1': 'North',
        'annoline2': 'Corona',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.85751790676447,
         40.7540709990489,
         -73.85751790676447,
         40.7540709990489]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.197',
       'geometry': {'type': 'Point',
        'coordinates': [-73.8410221123401, 40.7146110815117]},
       'geometry_name': 'geom',
       'properties': {'name': 'Forest Hills Gardens',
        'stacked': 3,
        'annoline1': 'Forest',
        'annoline2': 'Hills',
        'annoline3': 'Gardens',
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.8410221123401,
         40.7146110815117,
         -73.8410221123401,
         40.7146110815117]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.198',
       'geometry': {'type': 'Point',
        'coordinates': [-74.07935312512797, 40.6449815710044]},
       'geometry_name': 'geom',
       'properties': {'name': 'St. George',
        'stacked': 2,
        'annoline1': 'St.',
        'annoline2': 'George',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.07935312512797,
         40.6449815710044,
         -74.07935312512797,
         40.6449815710044]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.199',
       'geometry': {'type': 'Point',
        'coordinates': [-74.08701650516625, 40.64061455913511]},
       'geometry_name': 'geom',
       'properties': {'name': 'New Brighton',
        'stacked': 2,
        'annoline1': 'New',
        'annoline2': 'Brighton',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.08701650516625,
         40.64061455913511,
         -74.08701650516625,
         40.64061455913511]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.200',
       'geometry': {'type': 'Point',
        'coordinates': [-74.07790192660066, 40.62692762538176]},
       'geometry_name': 'geom',
       'properties': {'name': 'Stapleton',
        'stacked': 1,
        'annoline1': 'Stapleton',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.07790192660066,
         40.62692762538176,
         -74.07790192660066,
         40.62692762538176]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.201',
       'geometry': {'type': 'Point',
        'coordinates': [-74.06980526716141, 40.61530494652761]},
       'geometry_name': 'geom',
       'properties': {'name': 'Rosebank',
        'stacked': 1,
        'annoline1': 'Rosebank',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.06980526716141,
         40.61530494652761,
         -74.06980526716141,
         40.61530494652761]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.202',
       'geometry': {'type': 'Point',
        'coordinates': [-74.1071817826561, 40.63187892654607]},
       'geometry_name': 'geom',
       'properties': {'name': 'West Brighton',
        'stacked': 2,
        'annoline1': 'West',
        'annoline2': 'Brighton',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.1071817826561,
         40.63187892654607,
         -74.1071817826561,
         40.63187892654607]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.203',
       'geometry': {'type': 'Point',
        'coordinates': [-74.08724819983729, 40.624184791313006]},
       'geometry_name': 'geom',
       'properties': {'name': 'Grymes Hill',
        'stacked': 2,
        'annoline1': 'Grymes',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.08724819983729,
         40.624184791313006,
         -74.08724819983729,
         40.624184791313006]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.204',
       'geometry': {'type': 'Point',
        'coordinates': [-74.1113288180088, 40.59706851814673]},
       'geometry_name': 'geom',
       'properties': {'name': 'Todt Hill',
        'stacked': 2,
        'annoline1': 'Todt',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.1113288180088,
         40.59706851814673,
         -74.1113288180088,
         40.59706851814673]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.205',
       'geometry': {'type': 'Point',
        'coordinates': [-74.0795529253982, 40.58024741350956]},
       'geometry_name': 'geom',
       'properties': {'name': 'South Beach',
        'stacked': 2,
        'annoline1': 'South',
        'annoline2': 'Beach',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.0795529253982,
         40.58024741350956,
         -74.0795529253982,
         40.58024741350956]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.206',
       'geometry': {'type': 'Point',
        'coordinates': [-74.12943426797008, 40.63366930554365]},
       'geometry_name': 'geom',
       'properties': {'name': 'Port Richmond',
        'stacked': 2,
        'annoline1': 'Port',
        'annoline2': 'Richmond',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.12943426797008,
         40.63366930554365,
         -74.12943426797008,
         40.63366930554365]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.207',
       'geometry': {'type': 'Point',
        'coordinates': [-74.15008537046981, 40.632546390481124]},
       'geometry_name': 'geom',
       'properties': {'name': "Mariner's Harbor",
        'stacked': 2,
        'annoline1': "Mariner's",
        'annoline2': 'Harbor',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.15008537046981,
         40.632546390481124,
         -74.15008537046981,
         40.632546390481124]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.208',
       'geometry': {'type': 'Point',
        'coordinates': [-74.17464532993542, 40.63968297845542]},
       'geometry_name': 'geom',
       'properties': {'name': 'Port Ivory',
        'stacked': 2,
        'annoline1': 'Port',
        'annoline2': 'Ivory',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.17464532993542,
         40.63968297845542,
         -74.17464532993542,
         40.63968297845542]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.209',
       'geometry': {'type': 'Point',
        'coordinates': [-74.11918058534842, 40.61333593766742]},
       'geometry_name': 'geom',
       'properties': {'name': 'Castleton Corners',
        'stacked': 2,
        'annoline1': 'Castleton',
        'annoline2': 'Corners',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.11918058534842,
         40.61333593766742,
         -74.11918058534842,
         40.61333593766742]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.210',
       'geometry': {'type': 'Point',
        'coordinates': [-74.16496031329827, 40.594252379161695]},
       'geometry_name': 'geom',
       'properties': {'name': 'New Springville',
        'stacked': 2,
        'annoline1': 'New',
        'annoline2': 'Springville',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.16496031329827,
         40.594252379161695,
         -74.16496031329827,
         40.594252379161695]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.211',
       'geometry': {'type': 'Point',
        'coordinates': [-74.19073717538116, 40.58631375103281]},
       'geometry_name': 'geom',
       'properties': {'name': 'Travis',
        'stacked': 1,
        'annoline1': 'Travis',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.19073717538116,
         40.58631375103281,
         -74.19073717538116,
         40.58631375103281]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.212',
       'geometry': {'type': 'Point',
        'coordinates': [-74.1164794360638, 40.57257231820632]},
       'geometry_name': 'geom',
       'properties': {'name': 'New Dorp',
        'stacked': 2,
        'annoline1': 'New',
        'annoline2': 'Dorp',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.1164794360638,
         40.57257231820632,
         -74.1164794360638,
         40.57257231820632]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.213',
       'geometry': {'type': 'Point',
        'coordinates': [-74.12156593771896, 40.5584622432888]},
       'geometry_name': 'geom',
       'properties': {'name': 'Oakwood',
        'stacked': 1,
        'annoline1': 'Oakwood',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.12156593771896,
         40.5584622432888,
         -74.12156593771896,
         40.5584622432888]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.214',
       'geometry': {'type': 'Point',
        'coordinates': [-74.14932381490992, 40.549480228713605]},
       'geometry_name': 'geom',
       'properties': {'name': 'Great Kills',
        'stacked': 2,
        'annoline1': 'Great',
        'annoline2': 'Kills',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.14932381490992,
         40.549480228713605,
         -74.14932381490992,
         40.549480228713605]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.215',
       'geometry': {'type': 'Point',
        'coordinates': [-74.1643308041936, 40.542230747450745]},
       'geometry_name': 'geom',
       'properties': {'name': 'Eltingville',
        'stacked': 1,
        'annoline1': 'Eltingville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.1643308041936,
         40.542230747450745,
         -74.1643308041936,
         40.542230747450745]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.216',
       'geometry': {'type': 'Point',
        'coordinates': [-74.17854866165878, 40.53811417474507]},
       'geometry_name': 'geom',
       'properties': {'name': 'Annadale',
        'stacked': 1,
        'annoline1': 'Annadale',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.17854866165878,
         40.53811417474507,
         -74.17854866165878,
         40.53811417474507]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.217',
       'geometry': {'type': 'Point',
        'coordinates': [-74.20524582480326, 40.541967622888755]},
       'geometry_name': 'geom',
       'properties': {'name': 'Woodrow',
        'stacked': 1,
        'annoline1': 'Woodrow',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.20524582480326,
         40.541967622888755,
         -74.20524582480326,
         40.541967622888755]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.218',
       'geometry': {'type': 'Point',
        'coordinates': [-74.24656934235283, 40.50533376115642]},
       'geometry_name': 'geom',
       'properties': {'name': 'Tottenville',
        'stacked': 1,
        'annoline1': 'Tottenville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.24656934235283,
         40.50533376115642,
         -74.24656934235283,
         40.50533376115642]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.219',
       'geometry': {'type': 'Point',
        'coordinates': [-74.08055351790115, 40.637316067110326]},
       'geometry_name': 'geom',
       'properties': {'name': 'Tompkinsville',
        'stacked': 1,
        'annoline1': 'Tompkinsville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.08055351790115,
         40.637316067110326,
         -74.08055351790115,
         40.637316067110326]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.220',
       'geometry': {'type': 'Point',
        'coordinates': [-74.09629029235458, 40.61919310792676]},
       'geometry_name': 'geom',
       'properties': {'name': 'Silver Lake',
        'stacked': 2,
        'annoline1': 'Silver',
        'annoline2': 'Lake',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.09629029235458,
         40.61919310792676,
         -74.09629029235458,
         40.61919310792676]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.221',
       'geometry': {'type': 'Point',
        'coordinates': [-74.0971255217853, 40.61276015756489]},
       'geometry_name': 'geom',
       'properties': {'name': 'Sunnyside',
        'stacked': 1,
        'annoline1': 'Sunnyside',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.0971255217853,
         40.61276015756489,
         -74.0971255217853,
         40.61276015756489]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.222',
       'geometry': {'type': 'Point',
        'coordinates': [-73.96101312466779, 40.643675183340974]},
       'geometry_name': 'geom',
       'properties': {'name': 'Ditmas Park',
        'stacked': 2,
        'annoline1': 'Ditmas',
        'annoline2': 'Park',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.96101312466779,
         40.643675183340974,
         -73.96101312466779,
         40.643675183340974]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.223',
       'geometry': {'type': 'Point',
        'coordinates': [-73.93718680559314, 40.66094656188111]},
       'geometry_name': 'geom',
       'properties': {'name': 'Wingate',
        'stacked': 1,
        'annoline1': 'Wingate',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.93718680559314,
         40.66094656188111,
         -73.93718680559314,
         40.66094656188111]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.224',
       'geometry': {'type': 'Point',
        'coordinates': [-73.92688212616955, 40.655572313280764]},
       'geometry_name': 'geom',
       'properties': {'name': 'Rugby',
        'stacked': 1,
        'annoline1': 'Rugby',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.92688212616955,
         40.655572313280764,
         -73.92688212616955,
         40.655572313280764]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.225',
       'geometry': {'type': 'Point',
        'coordinates': [-74.08015734936296, 40.60919044434558]},
       'geometry_name': 'geom',
       'properties': {'name': 'Park Hill',
        'stacked': 2,
        'annoline1': 'Park',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.08015734936296,
         40.60919044434558,
         -74.08015734936296,
         40.60919044434558]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.226',
       'geometry': {'type': 'Point',
        'coordinates': [-74.13304143951704, 40.62109047275409]},
       'geometry_name': 'geom',
       'properties': {'name': 'Westerleigh',
        'stacked': 1,
        'annoline1': 'Westerleigh',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.13304143951704,
         40.62109047275409,
         -74.13304143951704,
         40.62109047275409]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.227',
       'geometry': {'type': 'Point',
        'coordinates': [-74.15315246387762, 40.620171512231884]},
       'geometry_name': 'geom',
       'properties': {'name': 'Graniteville',
        'stacked': 1,
        'annoline1': 'Graniteville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.15315246387762,
         40.620171512231884,
         -74.15315246387762,
         40.620171512231884]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.228',
       'geometry': {'type': 'Point',
        'coordinates': [-74.16510420241124, 40.63532509911492]},
       'geometry_name': 'geom',
       'properties': {'name': 'Arlington',
        'stacked': 1,
        'annoline1': 'Arlington',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.16510420241124,
         40.63532509911492,
         -74.16510420241124,
         40.63532509911492]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.229',
       'geometry': {'type': 'Point',
        'coordinates': [-74.06712363225574, 40.596312571276734]},
       'geometry_name': 'geom',
       'properties': {'name': 'Arrochar',
        'stacked': 1,
        'annoline1': 'Arrochar',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.06712363225574,
         40.596312571276734,
         -74.06712363225574,
         40.596312571276734]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.230',
       'geometry': {'type': 'Point',
        'coordinates': [-74.0766743627905, 40.59826835959991]},
       'geometry_name': 'geom',
       'properties': {'name': 'Grasmere',
        'stacked': 1,
        'annoline1': 'Grasmere',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.0766743627905,
         40.59826835959991,
         -74.0766743627905,
         40.59826835959991]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.231',
       'geometry': {'type': 'Point',
        'coordinates': [-74.08751118005578, 40.59632891379513]},
       'geometry_name': 'geom',
       'properties': {'name': 'Old Town',
        'stacked': 2,
        'annoline1': 'Old',
        'annoline2': 'Town',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.08751118005578,
         40.59632891379513,
         -74.08751118005578,
         40.59632891379513]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.232',
       'geometry': {'type': 'Point',
        'coordinates': [-74.09639905312521, 40.588672948199275]},
       'geometry_name': 'geom',
       'properties': {'name': 'Dongan Hills',
        'stacked': 2,
        'annoline1': 'Dongan',
        'annoline2': 'Hills',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.09639905312521,
         40.588672948199275,
         -74.09639905312521,
         40.588672948199275]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.233',
       'geometry': {'type': 'Point',
        'coordinates': [-74.09348266303591, 40.57352690574283]},
       'geometry_name': 'geom',
       'properties': {'name': 'Midland Beach',
        'stacked': 2,
        'annoline1': 'Midland',
        'annoline2': 'Beach',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.09348266303591,
         40.57352690574283,
         -74.09348266303591,
         40.57352690574283]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.234',
       'geometry': {'type': 'Point',
        'coordinates': [-74.10585598545434, 40.57621558711788]},
       'geometry_name': 'geom',
       'properties': {'name': 'Grant City',
        'stacked': 2,
        'annoline1': 'Grant',
        'annoline2': 'City',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.10585598545434,
         40.57621558711788,
         -74.10585598545434,
         40.57621558711788]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.235',
       'geometry': {'type': 'Point',
        'coordinates': [-74.10432707469124, 40.56425549307335]},
       'geometry_name': 'geom',
       'properties': {'name': 'New Dorp Beach',
        'stacked': 3,
        'annoline1': 'New',
        'annoline2': 'Dorp',
        'annoline3': 'Beach',
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.10432707469124,
         40.56425549307335,
         -74.10432707469124,
         40.56425549307335]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.236',
       'geometry': {'type': 'Point',
        'coordinates': [-74.13916622175768, 40.55398800858462]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bay Terrace',
        'stacked': 2,
        'annoline1': 'Bay',
        'annoline2': 'Terrace',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.13916622175768,
         40.55398800858462,
         -74.13916622175768,
         40.55398800858462]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.237',
       'geometry': {'type': 'Point',
        'coordinates': [-74.19174105747814, 40.531911920489605]},
       'geometry_name': 'geom',
       'properties': {'name': 'Huguenot',
        'stacked': 1,
        'annoline1': 'Huguenot',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.19174105747814,
         40.531911920489605,
         -74.19174105747814,
         40.531911920489605]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.238',
       'geometry': {'type': 'Point',
        'coordinates': [-74.21983106616777, 40.524699376118136]},
       'geometry_name': 'geom',
       'properties': {'name': 'Pleasant Plains',
        'stacked': 2,
        'annoline1': 'Pleasant',
        'annoline2': 'Plains',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.21983106616777,
         40.524699376118136,
         -74.21983106616777,
         40.524699376118136]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.239',
       'geometry': {'type': 'Point',
        'coordinates': [-74.22950350260027, 40.50608165346305]},
       'geometry_name': 'geom',
       'properties': {'name': 'Butler Manor',
        'stacked': 2,
        'annoline1': 'Butler',
        'annoline2': 'Manor',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.22950350260027,
         40.50608165346305,
         -74.22950350260027,
         40.50608165346305]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.240',
       'geometry': {'type': 'Point',
        'coordinates': [-74.23215775896526, 40.53053148283314]},
       'geometry_name': 'geom',
       'properties': {'name': 'Charleston',
        'stacked': 1,
        'annoline1': 'Charleston',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.23215775896526,
         40.53053148283314,
         -74.23215775896526,
         40.53053148283314]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.241',
       'geometry': {'type': 'Point',
        'coordinates': [-74.21572851113952, 40.54940400650072]},
       'geometry_name': 'geom',
       'properties': {'name': 'Rossville',
        'stacked': 1,
        'annoline1': 'Rossville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.21572851113952,
         40.54940400650072,
         -74.21572851113952,
         40.54940400650072]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.242',
       'geometry': {'type': 'Point',
        'coordinates': [-74.18588674583893, 40.54928582278321]},
       'geometry_name': 'geom',
       'properties': {'name': 'Arden Heights',
        'stacked': 2,
        'annoline1': 'Arden',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.18588674583893,
         40.54928582278321,
         -74.18588674583893,
         40.54928582278321]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.243',
       'geometry': {'type': 'Point',
        'coordinates': [-74.17079414786092, 40.555295236173194]},
       'geometry_name': 'geom',
       'properties': {'name': 'Greenridge',
        'stacked': 1,
        'annoline1': 'Greenridge',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.17079414786092,
         40.555295236173194,
         -74.17079414786092,
         40.555295236173194]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.244',
       'geometry': {'type': 'Point',
        'coordinates': [-74.15902208156601, 40.58913894875281]},
       'geometry_name': 'geom',
       'properties': {'name': 'Heartland Village',
        'stacked': 2,
        'annoline1': 'Heartland',
        'annoline2': 'Village',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.15902208156601,
         40.58913894875281,
         -74.15902208156601,
         40.58913894875281]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.245',
       'geometry': {'type': 'Point',
        'coordinates': [-74.1895604551969, 40.59472602746295]},
       'geometry_name': 'geom',
       'properties': {'name': 'Chelsea',
        'stacked': 1,
        'annoline1': 'Chelsea',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.1895604551969,
         40.59472602746295,
         -74.1895604551969,
         40.59472602746295]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.246',
       'geometry': {'type': 'Point',
        'coordinates': [-74.18725638381567, 40.60577868452358]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bloomfield',
        'stacked': 1,
        'annoline1': 'Bloomfield',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.18725638381567,
         40.60577868452358,
         -74.18725638381567,
         40.60577868452358]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.247',
       'geometry': {'type': 'Point',
        'coordinates': [-74.15940948657122, 40.6095918004203]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bulls Head',
        'stacked': 2,
        'annoline1': 'Bulls',
        'annoline2': 'Head',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.15940948657122,
         40.6095918004203,
         -74.15940948657122,
         40.6095918004203]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.248',
       'geometry': {'type': 'Point',
        'coordinates': [-73.95325646837112, 40.7826825671257]},
       'geometry_name': 'geom',
       'properties': {'name': 'Carnegie Hill',
        'stacked': 2,
        'annoline1': 'Carnegie',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.95325646837112,
         40.7826825671257,
         -73.95325646837112,
         40.7826825671257]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.249',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98843368023597, 40.72325901885768]},
       'geometry_name': 'geom',
       'properties': {'name': 'Noho',
        'stacked': 1,
        'annoline1': 'Noho',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.98843368023597,
         40.72325901885768,
         -73.98843368023597,
         40.72325901885768]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.250',
       'geometry': {'type': 'Point',
        'coordinates': [-74.00541529873355, 40.71522892046282]},
       'geometry_name': 'geom',
       'properties': {'name': 'Civic Center',
        'stacked': 2,
        'annoline1': 'Civic',
        'annoline2': 'Center',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-74.00541529873355,
         40.71522892046282,
         -74.00541529873355,
         40.71522892046282]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.251',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98871313285247, 40.7485096643122]},
       'geometry_name': 'geom',
       'properties': {'name': 'Midtown South',
        'stacked': 2,
        'annoline1': 'Midtown',
        'annoline2': 'South',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.98871313285247,
         40.7485096643122,
         -73.98871313285247,
         40.7485096643122]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.252',
       'geometry': {'type': 'Point',
        'coordinates': [-74.1340572986257, 40.56960594275505]},
       'geometry_name': 'geom',
       'properties': {'name': 'Richmond Town',
        'stacked': 2,
        'annoline1': 'Richmond',
        'annoline2': 'Town',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.1340572986257,
         40.56960594275505,
         -74.1340572986257,
         40.56960594275505]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.253',
       'geometry': {'type': 'Point',
        'coordinates': [-74.06667766061771, 40.60971934079284]},
       'geometry_name': 'geom',
       'properties': {'name': 'Shore Acres',
        'stacked': 2,
        'annoline1': 'Shore',
        'annoline2': 'Acres',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.06667766061771,
         40.60971934079284,
         -74.06667766061771,
         40.60971934079284]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.254',
       'geometry': {'type': 'Point',
        'coordinates': [-74.072642445484, 40.61917845202843]},
       'geometry_name': 'geom',
       'properties': {'name': 'Clifton',
        'stacked': 1,
        'annoline1': 'Clifton',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.072642445484,
         40.61917845202843,
         -74.072642445484,
         40.61917845202843]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.255',
       'geometry': {'type': 'Point',
        'coordinates': [-74.08402364740358, 40.6044731896879]},
       'geometry_name': 'geom',
       'properties': {'name': 'Concord',
        'stacked': 1,
        'annoline1': 'Concord',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.08402364740358,
         40.6044731896879,
         -74.08402364740358,
         40.6044731896879]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.256',
       'geometry': {'type': 'Point',
        'coordinates': [-74.09776206972522, 40.606794394801]},
       'geometry_name': 'geom',
       'properties': {'name': 'Emerson Hill',
        'stacked': 2,
        'annoline1': 'Emerson',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.09776206972522,
         40.606794394801,
         -74.09776206972522,
         40.606794394801]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.257',
       'geometry': {'type': 'Point',
        'coordinates': [-74.09805062373887, 40.63563000681151]},
       'geometry_name': 'geom',
       'properties': {'name': 'Randall Manor',
        'stacked': 2,
        'annoline1': 'Randall',
        'annoline2': 'Manor',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.09805062373887,
         40.63563000681151,
         -74.09805062373887,
         40.63563000681151]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.258',
       'geometry': {'type': 'Point',
        'coordinates': [-74.18622331749823, 40.63843283794795]},
       'geometry_name': 'geom',
       'properties': {'name': 'Howland Hook',
        'stacked': 2,
        'annoline1': 'Howland',
        'annoline2': 'Hook',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.18622331749823,
         40.63843283794795,
         -74.18622331749823,
         40.63843283794795]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.259',
       'geometry': {'type': 'Point',
        'coordinates': [-74.1418167896889, 40.630146741193826]},
       'geometry_name': 'geom',
       'properties': {'name': 'Elm Park',
        'stacked': 2,
        'annoline1': 'Elm',
        'annoline2': 'Park',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.1418167896889,
         40.630146741193826,
         -74.1418167896889,
         40.630146741193826]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.260',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91665331978048, 40.652117451793494]},
       'geometry_name': 'geom',
       'properties': {'name': 'Remsen Village',
        'stacked': 2,
        'annoline1': 'Remsen',
        'annoline2': 'Village',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.91665331978048,
         40.652117451793494,
         -73.91665331978048,
         40.652117451793494]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.261',
       'geometry': {'type': 'Point',
        'coordinates': [-73.88511776379292, 40.6627442796966]},
       'geometry_name': 'geom',
       'properties': {'name': 'New Lots',
        'stacked': 2,
        'annoline1': 'New',
        'annoline2': 'Lots',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.88511776379292,
         40.6627442796966,
         -73.88511776379292,
         40.6627442796966]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.262',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90233474295836, 40.63131755039667]},
       'geometry_name': 'geom',
       'properties': {'name': 'Paerdegat Basin',
        'stacked': 2,
        'annoline1': 'Paerdegat',
        'annoline2': 'Basin',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.90233474295836,
         40.63131755039667,
         -73.90233474295836,
         40.63131755039667]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.263',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91515391550404, 40.61597423962336]},
       'geometry_name': 'geom',
       'properties': {'name': 'Mill Basin',
        'stacked': 2,
        'annoline1': 'Mill',
        'annoline2': 'Basin',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.91515391550404,
         40.61597423962336,
         -73.91515391550404,
         40.61597423962336]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.264',
       'geometry': {'type': 'Point',
        'coordinates': [-73.79646462081593, 40.71145964370482]},
       'geometry_name': 'geom',
       'properties': {'name': 'Jamaica Hills',
        'stacked': 2,
        'annoline1': 'Jamaica',
        'annoline2': 'Hills',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.79646462081593,
         40.71145964370482,
         -73.79646462081593,
         40.71145964370482]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.265',
       'geometry': {'type': 'Point',
        'coordinates': [-73.79671678028349, 40.73350025429757]},
       'geometry_name': 'geom',
       'properties': {'name': 'Utopia',
        'stacked': 1,
        'annoline1': 'Utopia',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.79671678028349,
         40.73350025429757,
         -73.79671678028349,
         40.73350025429757]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.266',
       'geometry': {'type': 'Point',
        'coordinates': [-73.80486120040537, 40.73493618075478]},
       'geometry_name': 'geom',
       'properties': {'name': 'Pomonok',
        'stacked': 1,
        'annoline1': 'Pomonok',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.80486120040537,
         40.73493618075478,
         -73.80486120040537,
         40.73493618075478]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.267',
       'geometry': {'type': 'Point',
        'coordinates': [-73.89467996270574, 40.7703173929982]},
       'geometry_name': 'geom',
       'properties': {'name': 'Astoria Heights',
        'stacked': 2,
        'annoline1': 'Astoria',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.89467996270574,
         40.7703173929982,
         -73.89467996270574,
         40.7703173929982]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.268',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90119903387667, 40.83142834161548]},
       'geometry_name': 'geom',
       'properties': {'name': 'Claremont Village',
        'stacked': 2,
        'annoline1': 'Claremont',
        'annoline2': 'Village',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.90119903387667,
         40.83142834161548,
         -73.90119903387667,
         40.83142834161548]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.269',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91584652759009, 40.824780490842905]},
       'geometry_name': 'geom',
       'properties': {'name': 'Concourse Village',
        'stacked': 2,
        'annoline1': 'Concourse',
        'annoline2': 'Village',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.91584652759009,
         40.824780490842905,
         -73.91584652759009,
         40.824780490842905]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.270',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91655551964419, 40.84382617671654]},
       'geometry_name': 'geom',
       'properties': {'name': 'Mount Eden',
        'stacked': 2,
        'annoline1': 'Mount',
        'annoline2': 'Eden',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.91655551964419,
         40.84382617671654,
         -73.91655551964419,
         40.84382617671654]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.271',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90829930881988, 40.84884160724665]},
       'geometry_name': 'geom',
       'properties': {'name': 'Mount Hope',
        'stacked': 2,
        'annoline1': 'Mount',
        'annoline2': 'Hope',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.90829930881988,
         40.84884160724665,
         -73.90829930881988,
         40.84884160724665]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.272',
       'geometry': {'type': 'Point',
        'coordinates': [-73.96355614094303, 40.76028033131374]},
       'geometry_name': 'geom',
       'properties': {'name': 'Sutton Place',
        'stacked': 2,
        'annoline1': 'Sutton',
        'annoline2': 'Place',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.96355614094303,
         40.76028033131374,
         -73.96355614094303,
         40.76028033131374]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.273',
       'geometry': {'type': 'Point',
        'coordinates': [-73.95386782130745, 40.743414090073536]},
       'geometry_name': 'geom',
       'properties': {'name': 'Hunters Point',
        'stacked': 2,
        'annoline1': 'Hunters',
        'annoline2': 'Point',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.95386782130745,
         40.743414090073536,
         -73.95386782130745,
         40.743414090073536]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.274',
       'geometry': {'type': 'Point',
        'coordinates': [-73.96770824581834, 40.75204236950722]},
       'geometry_name': 'geom',
       'properties': {'name': 'Turtle Bay',
        'stacked': 2,
        'annoline1': 'Turtle',
        'annoline2': 'Bay',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.96770824581834,
         40.75204236950722,
         -73.96770824581834,
         40.75204236950722]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.275',
       'geometry': {'type': 'Point',
        'coordinates': [-73.97121928722265, 40.746917410740195]},
       'geometry_name': 'geom',
       'properties': {'name': 'Tudor City',
        'stacked': 2,
        'annoline1': 'Tudor',
        'annoline2': 'City',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.97121928722265,
         40.746917410740195,
         -73.97121928722265,
         40.746917410740195]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.276',
       'geometry': {'type': 'Point',
        'coordinates': [-73.97405170469203, 40.73099955477061]},
       'geometry_name': 'geom',
       'properties': {'name': 'Stuyvesant Town',
        'stacked': 2,
        'annoline1': 'Stuyvesant',
        'annoline2': 'Town',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.97405170469203,
         40.73099955477061,
         -73.97405170469203,
         40.73099955477061]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.277',
       'geometry': {'type': 'Point',
        'coordinates': [-73.9909471052826, 40.739673047638426]},
       'geometry_name': 'geom',
       'properties': {'name': 'Flatiron',
        'stacked': 1,
        'annoline1': 'Flatiron',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-73.9909471052826,
         40.739673047638426,
         -73.9909471052826,
         40.739673047638426]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.278',
       'geometry': {'type': 'Point',
        'coordinates': [-73.91819286431682, 40.74565180608076]},
       'geometry_name': 'geom',
       'properties': {'name': 'Sunnyside Gardens',
        'stacked': 2,
        'annoline1': 'Sunnyside',
        'annoline2': 'Gardens',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.91819286431682,
         40.74565180608076,
         -73.91819286431682,
         40.74565180608076]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.279',
       'geometry': {'type': 'Point',
        'coordinates': [-73.93244235260178, 40.73725071694497]},
       'geometry_name': 'geom',
       'properties': {'name': 'Blissville',
        'stacked': 1,
        'annoline1': 'Blissville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.93244235260178,
         40.73725071694497,
         -73.93244235260178,
         40.73725071694497]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.280',
       'geometry': {'type': 'Point',
        'coordinates': [-73.99550751888415, 40.70328109093014]},
       'geometry_name': 'geom',
       'properties': {'name': 'Fulton Ferry',
        'stacked': 2,
        'annoline1': 'Fulton',
        'annoline2': 'Ferry',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.99550751888415,
         40.70328109093014,
         -73.99550751888415,
         40.70328109093014]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.281',
       'geometry': {'type': 'Point',
        'coordinates': [-73.98111603592393, 40.70332149882874]},
       'geometry_name': 'geom',
       'properties': {'name': 'Vinegar Hill',
        'stacked': 2,
        'annoline1': 'Vinegar',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.98111603592393,
         40.70332149882874,
         -73.98111603592393,
         40.70332149882874]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.282',
       'geometry': {'type': 'Point',
        'coordinates': [-73.93053108817338, 40.67503986503237]},
       'geometry_name': 'geom',
       'properties': {'name': 'Weeksville',
        'stacked': 1,
        'annoline1': 'Weeksville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.93053108817338,
         40.67503986503237,
         -73.93053108817338,
         40.67503986503237]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.283',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90331684852599, 40.67786104769531]},
       'geometry_name': 'geom',
       'properties': {'name': 'Broadway Junction',
        'stacked': 2,
        'annoline1': 'Broadway',
        'annoline2': 'Junction',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.90331684852599,
         40.67786104769531,
         -73.90331684852599,
         40.67786104769531]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.284',
       'geometry': {'type': 'Point',
        'coordinates': [-73.9887528074504, 40.70317632822692]},
       'geometry_name': 'geom',
       'properties': {'name': 'Dumbo',
        'stacked': 1,
        'annoline1': 'Dumbo',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.9887528074504,
         40.70317632822692,
         -73.9887528074504,
         40.70317632822692]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.285',
       'geometry': {'type': 'Point',
        'coordinates': [-74.12059399718001, 40.60180957631444]},
       'geometry_name': 'geom',
       'properties': {'name': 'Manor Heights',
        'stacked': 2,
        'annoline1': 'Manor',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.12059399718001,
         40.60180957631444,
         -74.12059399718001,
         40.60180957631444]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.286',
       'geometry': {'type': 'Point',
        'coordinates': [-74.13208447484298, 40.60370692627371]},
       'geometry_name': 'geom',
       'properties': {'name': 'Willowbrook',
        'stacked': 1,
        'annoline1': 'Willowbrook',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.13208447484298,
         40.60370692627371,
         -74.13208447484298,
         40.60370692627371]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.287',
       'geometry': {'type': 'Point',
        'coordinates': [-74.21776636068567, 40.541139922091766]},
       'geometry_name': 'geom',
       'properties': {'name': 'Sandy Ground',
        'stacked': 2,
        'annoline1': 'Sandy',
        'annoline2': 'Ground',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.21776636068567,
         40.541139922091766,
         -74.21776636068567,
         40.541139922091766]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.288',
       'geometry': {'type': 'Point',
        'coordinates': [-74.12727240604946, 40.579118742961214]},
       'geometry_name': 'geom',
       'properties': {'name': 'Egbertville',
        'stacked': 1,
        'annoline1': 'Egbertville',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.12727240604946,
         40.579118742961214,
         -74.12727240604946,
         40.579118742961214]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.289',
       'geometry': {'type': 'Point',
        'coordinates': [-73.89213760232822, 40.56737588957032]},
       'geometry_name': 'geom',
       'properties': {'name': 'Roxbury',
        'stacked': 1,
        'annoline1': 'Roxbury',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.89213760232822,
         40.56737588957032,
         -73.89213760232822,
         40.56737588957032]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.290',
       'geometry': {'type': 'Point',
        'coordinates': [-73.95918459428702, 40.598525095137255]},
       'geometry_name': 'geom',
       'properties': {'name': 'Homecrest',
        'stacked': 1,
        'annoline1': 'Homecrest',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.95918459428702,
         40.598525095137255,
         -73.95918459428702,
         40.598525095137255]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.291',
       'geometry': {'type': 'Point',
        'coordinates': [-73.88114319200604, 40.716414511158185]},
       'geometry_name': 'geom',
       'properties': {'name': 'Middle Village',
        'stacked': 2,
        'annoline1': 'Middle',
        'annoline2': 'Village',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.88114319200604,
         40.716414511158185,
         -73.88114319200604,
         40.716414511158185]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.292',
       'geometry': {'type': 'Point',
        'coordinates': [-74.20152556457658, 40.52626406734812]},
       'geometry_name': 'geom',
       'properties': {'name': "Prince's Bay",
        'stacked': 2,
        'annoline1': "Prince's",
        'annoline2': 'Bay',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.20152556457658,
         40.52626406734812,
         -74.20152556457658,
         40.52626406734812]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.293',
       'geometry': {'type': 'Point',
        'coordinates': [-74.13792663771568, 40.57650629379489]},
       'geometry_name': 'geom',
       'properties': {'name': 'Lighthouse Hill',
        'stacked': 2,
        'annoline1': 'Lighthouse',
        'annoline2': 'Hill',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.13792663771568,
         40.57650629379489,
         -74.13792663771568,
         40.57650629379489]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.294',
       'geometry': {'type': 'Point',
        'coordinates': [-74.22957080626941, 40.51954145748909]},
       'geometry_name': 'geom',
       'properties': {'name': 'Richmond Valley',
        'stacked': 2,
        'annoline1': 'Richmond',
        'annoline2': 'Valley',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.22957080626941,
         40.51954145748909,
         -74.22957080626941,
         40.51954145748909]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.295',
       'geometry': {'type': 'Point',
        'coordinates': [-73.82667757138641, 40.79060155670148]},
       'geometry_name': 'geom',
       'properties': {'name': 'Malba',
        'stacked': 1,
        'annoline1': 'Malba',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.82667757138641,
         40.79060155670148,
         -73.82667757138641,
         40.79060155670148]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.296',
       'geometry': {'type': 'Point',
        'coordinates': [-73.890345709872, 40.6819989345173]},
       'geometry_name': 'geom',
       'properties': {'name': 'Highland Park',
        'stacked': 2,
        'annoline1': 'Highland',
        'annoline2': 'Park',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.890345709872,
         40.6819989345173,
         -73.890345709872,
         40.6819989345173]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.297',
       'geometry': {'type': 'Point',
        'coordinates': [-73.94841515328893, 40.60937770113766]},
       'geometry_name': 'geom',
       'properties': {'name': 'Madison',
        'stacked': 1,
        'annoline1': 'Madison',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.94841515328893,
         40.60937770113766,
         -73.94841515328893,
         40.60937770113766]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.298',
       'geometry': {'type': 'Point',
        'coordinates': [-73.86172577555115, 40.85272297633017]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bronxdale',
        'stacked': 1,
        'annoline1': 'Bronxdale',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.86172577555115,
         40.85272297633017,
         -73.86172577555115,
         40.85272297633017]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.299',
       'geometry': {'type': 'Point',
        'coordinates': [-73.85931863221647, 40.86578787802982]},
       'geometry_name': 'geom',
       'properties': {'name': 'Allerton',
        'stacked': 1,
        'annoline1': 'Allerton',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.85931863221647,
         40.86578787802982,
         -73.85931863221647,
         40.86578787802982]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.300',
       'geometry': {'type': 'Point',
        'coordinates': [-73.90152264513144, 40.8703923914147]},
       'geometry_name': 'geom',
       'properties': {'name': 'Kingsbridge Heights',
        'stacked': 2,
        'annoline1': 'Kingsbridge',
        'annoline2': 'Heights',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Bronx',
        'bbox': [-73.90152264513144,
         40.8703923914147,
         -73.90152264513144,
         40.8703923914147]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.301',
       'geometry': {'type': 'Point',
        'coordinates': [-73.94817709920184, 40.64692606658579]},
       'geometry_name': 'geom',
       'properties': {'name': 'Erasmus',
        'stacked': 1,
        'annoline1': 'Erasmus',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Brooklyn',
        'bbox': [-73.94817709920184,
         40.64692606658579,
         -73.94817709920184,
         40.64692606658579]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.302',
       'geometry': {'type': 'Point',
        'coordinates': [-74.00011136202637, 40.75665808227519]},
       'geometry_name': 'geom',
       'properties': {'name': 'Hudson Yards',
        'stacked': 2,
        'annoline1': 'Hudson',
        'annoline2': 'Yards',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Manhattan',
        'bbox': [-74.00011136202637,
         40.75665808227519,
         -74.00011136202637,
         40.75665808227519]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.303',
       'geometry': {'type': 'Point',
        'coordinates': [-73.80553002968718, 40.58733774018741]},
       'geometry_name': 'geom',
       'properties': {'name': 'Hammels',
        'stacked': 1,
        'annoline1': 'Hammels',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.80553002968718,
         40.58733774018741,
         -73.80553002968718,
         40.58733774018741]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.304',
       'geometry': {'type': 'Point',
        'coordinates': [-73.76596781445627, 40.611321691283834]},
       'geometry_name': 'geom',
       'properties': {'name': 'Bayswater',
        'stacked': 1,
        'annoline1': 'Bayswater',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.76596781445627,
         40.611321691283834,
         -73.76596781445627,
         40.611321691283834]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.305',
       'geometry': {'type': 'Point',
        'coordinates': [-73.94563070334091, 40.756091297094706]},
       'geometry_name': 'geom',
       'properties': {'name': 'Queensbridge',
        'stacked': 1,
        'annoline1': 'Queensbridge',
        'annoline2': None,
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Queens',
        'bbox': [-73.94563070334091,
         40.756091297094706,
         -73.94563070334091,
         40.756091297094706]}},
      {'type': 'Feature',
       'id': 'nyu_2451_34572.306',
       'geometry': {'type': 'Point',
        'coordinates': [-74.08173992211962, 40.61731079252983]},
       'geometry_name': 'geom',
       'properties': {'name': 'Fox Hills',
        'stacked': 2,
        'annoline1': 'Fox',
        'annoline2': 'Hills',
        'annoline3': None,
        'annoangle': 0.0,
        'borough': 'Staten Island',
        'bbox': [-74.08173992211962,
         40.61731079252983,
         -74.08173992211962,
         40.61731079252983]}}],
     'crs': {'type': 'name', 'properties': {'name': 'urn:ogc:def:crs:EPSG::4326'}},
     'bbox': [-74.2492599487305,
      40.5033187866211,
      -73.7061614990234,
      40.9105606079102]}




```python
neighborhoods_data = newyork_data['features']
```


```python
neighborhoods_data[0]
```




    {'type': 'Feature',
     'id': 'nyu_2451_34572.1',
     'geometry': {'type': 'Point',
      'coordinates': [-73.84720052054902, 40.89470517661]},
     'geometry_name': 'geom',
     'properties': {'name': 'Wakefield',
      'stacked': 1,
      'annoline1': 'Wakefield',
      'annoline2': None,
      'annoline3': None,
      'annoangle': 0.0,
      'borough': 'Bronx',
      'bbox': [-73.84720052054902,
       40.89470517661,
       -73.84720052054902,
       40.89470517661]}}




```python
print ('Next Determine columns to pick up from Data set')
```

    Next Determine columns to pick up from Data set



```python
# define the dataframe columns
column_names = ['Borough', 'Neighborhood', 'Latitude', 'Longitude'] 

# instantiate the dataframe
neighborhoods = pd.DataFrame(columns=column_names)
```


```python
neighborhoods
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Borough</th>
      <th>Neighborhood</th>
      <th>Latitude</th>
      <th>Longitude</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
for data in neighborhoods_data:
    borough = neighborhood_name = data['properties']['borough'] 
    neighborhood_name = data['properties']['name']
        
    neighborhood_latlon = data['geometry']['coordinates']
    neighborhood_lat = neighborhood_latlon[1]
    neighborhood_lon = neighborhood_latlon[0]
    
    neighborhoods = neighborhoods.append({'Borough': borough,
                                          'Neighborhood': neighborhood_name,
                                          'Latitude': neighborhood_lat,
                                          'Longitude': neighborhood_lon}, ignore_index=True)
```


```python
neighborhoods.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Borough</th>
      <th>Neighborhood</th>
      <th>Latitude</th>
      <th>Longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bronx</td>
      <td>Wakefield</td>
      <td>40.894705</td>
      <td>-73.847201</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bronx</td>
      <td>Co-op City</td>
      <td>40.874294</td>
      <td>-73.829939</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bronx</td>
      <td>Eastchester</td>
      <td>40.887556</td>
      <td>-73.827806</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bronx</td>
      <td>Fieldston</td>
      <td>40.895437</td>
      <td>-73.905643</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bronx</td>
      <td>Riverdale</td>
      <td>40.890834</td>
      <td>-73.912585</td>
    </tr>
  </tbody>
</table>
</div>




```python
print('The dataframe has {} boroughs and {} neighborhoods.'.format(
        len(neighborhoods['Borough'].unique()),
        neighborhoods.shape[0]
    )
)
```

    The dataframe has 5 boroughs and 306 neighborhoods.



```python
print ('Determined Borough 0 - Bronz had 5 boroughs and 306 neighbourhoods')
```

    Determined Borough 0 - Bronz had 5 boroughs and 306 neighbourhoods



```python
address = 'New York City, NY'

geolocator = Nominatim(user_agent="ny_explorer")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of New York City are {}, {}.'.format(latitude, longitude))
```

    The geograpical coordinate of New York City are 40.7127281, -74.0060152.



```python
print ('New York Lat and Longitude is 40.71 and -74.00')
```

    New York Lat and Longitude is 40.71 and -74.00



```python
# create map of New York using latitude and longitude values
map_newyork = folium.Map(location=[latitude, longitude], zoom_start=10)

# add markers to map
for lat, lng, borough, neighborhood in zip(neighborhoods['Latitude'], neighborhoods['Longitude'], neighborhoods['Borough'], neighborhoods['Neighborhood']):
    label = '{}, {}'.format(neighborhood, borough)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='blue',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7,
        parse_html=False).add_to(map_newyork)  
    
map_newyork
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe src="about:blank" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" data-html=PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwLjAlOwogICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAo8L2hlYWQ+Cjxib2R5PiAgICAKICAgIAogICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb2xpdW0tbWFwIiBpZD0ibWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5IiA+PC9kaXY+CiAgICAgICAgCjwvYm9keT4KPHNjcmlwdD4gICAgCiAgICAKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSA9IEwubWFwKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ21hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OScsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7Y2VudGVyOiBbNDAuODQ5MzA0NDUsLTczLjg3NzEzNzkxODM1MjA2XSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHpvb206IDEwLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbWF4Qm91bmRzOiBib3VuZHMsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBsYXllcnM6IFtdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgd29ybGRDb3B5SnVtcDogZmFsc2UsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjcnM6IEwuQ1JTLkVQU0czODU3CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0pOwogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgdGlsZV9sYXllcl9iYzQ1MmZmOTA5OWY0MDQ4OGVjNDY5YTQzMWMyYTVmMyA9IEwudGlsZUxheWVyKAogICAgICAgICAgICAgICAgJ2h0dHBzOi8ve3N9LnRpbGUub3BlbnN0cmVldG1hcC5vcmcve3p9L3t4fS97eX0ucG5nJywKICAgICAgICAgICAgICAgIHsKICAiYXR0cmlidXRpb24iOiBudWxsLAogICJkZXRlY3RSZXRpbmEiOiBmYWxzZSwKICAibWF4Wm9vbSI6IDE4LAogICJtaW5ab29tIjogMSwKICAibm9XcmFwIjogZmFsc2UsCiAgInN1YmRvbWFpbnMiOiAiYWJjIgp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDg4ZWM0NTVmNDJmNDg1NGI0NDVhYjY5ZWJiYjgxN2YgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44OTQ3MDUxNzY2MSwtNzMuODQ3MjAwNTIwNTQ5MDJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMTRhYjRjN2Q4MDYzNDZmOWE4NjBmNjkzODk4Y2VkZDEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDhiYzQ4MDExNzFkNDI1Mzg4OWUwNzE5N2FlZTI1ZjAgPSAkKCc8ZGl2IGlkPSJodG1sX2Q4YmM0ODAxMTcxZDQyNTM4ODllMDcxOTdhZWUyNWYwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5XYWtlZmllbGQsIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xNGFiNGM3ZDgwNjM0NmY5YTg2MGY2OTM4OThjZWRkMS5zZXRDb250ZW50KGh0bWxfZDhiYzQ4MDExNzFkNDI1Mzg4OWUwNzE5N2FlZTI1ZjApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDg4ZWM0NTVmNDJmNDg1NGI0NDVhYjY5ZWJiYjgxN2YuYmluZFBvcHVwKHBvcHVwXzE0YWI0YzdkODA2MzQ2ZjlhODYwZjY5Mzg5OGNlZGQxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzMxOGYxZGQzYzY2MzRiMWQ4ZDFkMzA0YjczNGUzMzNkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODc0Mjk0MTkzMDMwMTIsLTczLjgyOTkzOTEwODEyMzk4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzRkOGNhZjA0YTRmZTRiZjg4MWUxNTEwZjAxZTA4ZmI2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2E0NjIwNTBlYTAzMzQ3ODU4NTA5ZDZlNjM2MTgyNGNkID0gJCgnPGRpdiBpZD0iaHRtbF9hNDYyMDUwZWEwMzM0Nzg1ODUwOWQ2ZTYzNjE4MjRjZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q28tb3AgQ2l0eSwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzRkOGNhZjA0YTRmZTRiZjg4MWUxNTEwZjAxZTA4ZmI2LnNldENvbnRlbnQoaHRtbF9hNDYyMDUwZWEwMzM0Nzg1ODUwOWQ2ZTYzNjE4MjRjZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zMThmMWRkM2M2NjM0YjFkOGQxZDMwNGI3MzRlMzMzZC5iaW5kUG9wdXAocG9wdXBfNGQ4Y2FmMDRhNGZlNGJmODgxZTE1MTBmMDFlMDhmYjYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYThjNzlmYTM1NWFiNDMyMmFkNDUyNDNmODExZjJlYzQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44ODc1NTU2NzczNTA3NzUsLTczLjgyNzgwNjQ0NzE2NDEyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2Q3YmMxZTgwNzI2YjRmNTBhNmJkOWU0MWM1NjEyMWYyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzNkZDFiMGVjMGRhNjQ1MjU4NjZjMWQzZDYxOGMzZDZiID0gJCgnPGRpdiBpZD0iaHRtbF8zZGQxYjBlYzBkYTY0NTI1ODY2YzFkM2Q2MThjM2Q2YiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RWFzdGNoZXN0ZXIsIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kN2JjMWU4MDcyNmI0ZjUwYTZiZDllNDFjNTYxMjFmMi5zZXRDb250ZW50KGh0bWxfM2RkMWIwZWMwZGE2NDUyNTg2NmMxZDNkNjE4YzNkNmIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYThjNzlmYTM1NWFiNDMyMmFkNDUyNDNmODExZjJlYzQuYmluZFBvcHVwKHBvcHVwX2Q3YmMxZTgwNzI2YjRmNTBhNmJkOWU0MWM1NjEyMWYyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Q4YmQ0NWQzYTgyMjRlOTRiMWUwOWMwYmFmOWJhNmNkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODk1NDM3NDI2OTAzODMsLTczLjkwNTY0MjU5NTkxNjgyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2YyMWMyNmNhN2UzNzRmZDNhNWIwY2Y0MmMyNTE5N2Q2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzBjMGQzOGM4N2E5ZTRkYTFiMDY3NzQxNjhkYjlhZWQzID0gJCgnPGRpdiBpZD0iaHRtbF8wYzBkMzhjODdhOWU0ZGExYjA2Nzc0MTY4ZGI5YWVkMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RmllbGRzdG9uLCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZjIxYzI2Y2E3ZTM3NGZkM2E1YjBjZjQyYzI1MTk3ZDYuc2V0Q29udGVudChodG1sXzBjMGQzOGM4N2E5ZTRkYTFiMDY3NzQxNjhkYjlhZWQzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Q4YmQ0NWQzYTgyMjRlOTRiMWUwOWMwYmFmOWJhNmNkLmJpbmRQb3B1cChwb3B1cF9mMjFjMjZjYTdlMzc0ZmQzYTViMGNmNDJjMjUxOTdkNik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80Y2U1ZDkxZWM4YzQ0OWQyODFjZWQ3NmE5ZDJiZWEyYSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg5MDgzNDQ5Mzg5MTMwNSwtNzMuOTEyNTg1NDYxMDg1N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zMzk4ZjI1NTliY2Q0OGQyYmYwMzYzNzQ5OTkxMmI0NiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kOGFjOWU5MTA3MmI0YTU2ODZmNjY4NDVkNmIwZGNiNyA9ICQoJzxkaXYgaWQ9Imh0bWxfZDhhYzllOTEwNzJiNGE1Njg2ZjY2ODQ1ZDZiMGRjYjciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJpdmVyZGFsZSwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzMzOThmMjU1OWJjZDQ4ZDJiZjAzNjM3NDk5OTEyYjQ2LnNldENvbnRlbnQoaHRtbF9kOGFjOWU5MTA3MmI0YTU2ODZmNjY4NDVkNmIwZGNiNyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80Y2U1ZDkxZWM4YzQ0OWQyODFjZWQ3NmE5ZDJiZWEyYS5iaW5kUG9wdXAocG9wdXBfMzM5OGYyNTU5YmNkNDhkMmJmMDM2Mzc0OTk5MTJiNDYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYjUwOWU3NTg2M2FjNDdhNmFjMTZlMjU4MWM3YTU2NzggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44ODE2ODczNzEyMDUyMSwtNzMuOTAyODE3OTg3MjQ2MDRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfN2Y1ZjRhZDBhYTBiNDIzMGI3ODVmNWRmYzY1NDgwZTIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZThlOTQwMGFjYWM0NDY5ZThlZWNjNmFmYTU4YjlhMGYgPSAkKCc8ZGl2IGlkPSJodG1sX2U4ZTk0MDBhY2FjNDQ2OWU4ZWVjYzZhZmE1OGI5YTBmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5LaW5nc2JyaWRnZSwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzdmNWY0YWQwYWEwYjQyMzBiNzg1ZjVkZmM2NTQ4MGUyLnNldENvbnRlbnQoaHRtbF9lOGU5NDAwYWNhYzQ0NjllOGVlY2M2YWZhNThiOWEwZik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iNTA5ZTc1ODYzYWM0N2E2YWMxNmUyNTgxYzdhNTY3OC5iaW5kUG9wdXAocG9wdXBfN2Y1ZjRhZDBhYTBiNDIzMGI3ODVmNWRmYzY1NDgwZTIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfODU4YTNiZjYzNDMzNDQxYmJiYWZmMWViYmNjYmYwYjggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NzY1NTA3Nzg3OTk2NCwtNzMuOTEwNjU5NjU4NjI5ODFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNWFjYTY5Mjg2NDYwNDIxOGJlNjZmYTNlZTQ3MzcwY2QgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYmMxMTFmNjU5NWU1NGQ3OWJjNWQ4NjM3OWEzYjVlM2EgPSAkKCc8ZGl2IGlkPSJodG1sX2JjMTExZjY1OTVlNTRkNzliYzVkODYzNzlhM2I1ZTNhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NYXJibGUgSGlsbCwgTWFuaGF0dGFuPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81YWNhNjkyODY0NjA0MjE4YmU2NmZhM2VlNDczNzBjZC5zZXRDb250ZW50KGh0bWxfYmMxMTFmNjU5NWU1NGQ3OWJjNWQ4NjM3OWEzYjVlM2EpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfODU4YTNiZjYzNDMzNDQxYmJiYWZmMWViYmNjYmYwYjguYmluZFBvcHVwKHBvcHVwXzVhY2E2OTI4NjQ2MDQyMThiZTY2ZmEzZWU0NzM3MGNkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzNlMmJmYjdmODExOTQzNzc4NTViMzMzZDVkYzcwOTZjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODk4MjcyNjEyMTM4MDUsLTczLjg2NzMxNDk2ODE0MTc2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2M0MDJkYTgxZTJmYTQ0NTFiMmQ0YWQ2YTc5MWE1ZjEzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2IyZTg5MDJkNjBhMTRiZDU4ZjQ1MjU5YjMwYzY1YjJlID0gJCgnPGRpdiBpZD0iaHRtbF9iMmU4OTAyZDYwYTE0YmQ1OGY0NTI1OWIzMGM2NWIyZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V29vZGxhd24sIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jNDAyZGE4MWUyZmE0NDUxYjJkNGFkNmE3OTFhNWYxMy5zZXRDb250ZW50KGh0bWxfYjJlODkwMmQ2MGExNGJkNThmNDUyNTliMzBjNjViMmUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfM2UyYmZiN2Y4MTE5NDM3Nzg1NWIzMzNkNWRjNzA5NmMuYmluZFBvcHVwKHBvcHVwX2M0MDJkYTgxZTJmYTQ0NTFiMmQ0YWQ2YTc5MWE1ZjEzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzcwMjllY2E2ZTUxMDQ3N2I5ODY3NGRkNDIyZTIzZGZlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODc3MjI0MTU1OTk0NDYsLTczLjg3OTM5MDczOTU2ODFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfN2QxY2UwODkxOTliNDdiMWE0MTRmYjA0MzhiYmI2YjcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYWRkMDI0NWFhZTdkNDVlODhhYjQ1OGIwY2IyMThiZTcgPSAkKCc8ZGl2IGlkPSJodG1sX2FkZDAyNDVhYWU3ZDQ1ZTg4YWI0NThiMGNiMjE4YmU3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ob3J3b29kLCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfN2QxY2UwODkxOTliNDdiMWE0MTRmYjA0MzhiYmI2Yjcuc2V0Q29udGVudChodG1sX2FkZDAyNDVhYWU3ZDQ1ZTg4YWI0NThiMGNiMjE4YmU3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzcwMjllY2E2ZTUxMDQ3N2I5ODY3NGRkNDIyZTIzZGZlLmJpbmRQb3B1cChwb3B1cF83ZDFjZTA4OTE5OWI0N2IxYTQxNGZiMDQzOGJiYjZiNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80YmMzOWIwNzViZjE0MGMzYTIxZDQ3YWFjNzQzN2Y1ZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg4MTAzODg3ODE5MjExLC03My44NTc0NDY0Mjk3NDIwN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mMjhiYWZhNGFkODg0NTdhOTYyYTA2Y2Q0YjEwNDAzNiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yNDEyMjYwZGQ0ODg0MGRmOGQ0NTdiZDkyODdiZDZkNyA9ICQoJzxkaXYgaWQ9Imh0bWxfMjQxMjI2MGRkNDg4NDBkZjhkNDU3YmQ5Mjg3YmQ2ZDciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldpbGxpYW1zYnJpZGdlLCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZjI4YmFmYTRhZDg4NDU3YTk2MmEwNmNkNGIxMDQwMzYuc2V0Q29udGVudChodG1sXzI0MTIyNjBkZDQ4ODQwZGY4ZDQ1N2JkOTI4N2JkNmQ3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzRiYzM5YjA3NWJmMTQwYzNhMjFkNDdhYWM3NDM3ZjVlLmJpbmRQb3B1cChwb3B1cF9mMjhiYWZhNGFkODg0NTdhOTYyYTA2Y2Q0YjEwNDAzNik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lMGVhZTFjNzg0ZDg0OTYxYTcwN2EyOWM3ODVhY2UzMiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg2Njg1ODEwNzI1MjY5NiwtNzMuODM1Nzk3NTk4MDgxMTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNzIxZWQ0OWI0MjYyNDFjZjlkZmRmYmJiZTQ2M2E4ZGMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTlhOTczMmYyMmQzNDI4Nzk3NWFhZTcxNGRhM2JmMmMgPSAkKCc8ZGl2IGlkPSJodG1sXzU5YTk3MzJmMjJkMzQyODc5NzVhYWU3MTRkYTNiZjJjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CYXljaGVzdGVyLCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNzIxZWQ0OWI0MjYyNDFjZjlkZmRmYmJiZTQ2M2E4ZGMuc2V0Q29udGVudChodG1sXzU5YTk3MzJmMjJkMzQyODc5NzVhYWU3MTRkYTNiZjJjKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2UwZWFlMWM3ODRkODQ5NjFhNzA3YTI5Yzc4NWFjZTMyLmJpbmRQb3B1cChwb3B1cF83MjFlZDQ5YjQyNjI0MWNmOWRmZGZiYmJlNDYzYThkYyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jZjUzNGQwMjhjZmM0OGY4YTNiOTU2ZGRhYzkzMGJkOSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg1NzQxMzQ5ODA4ODY1LC03My44NTQ3NTU2NDAxNzk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lYmJlNjc5NTQ4MDE0MWZhYjk1MDI4Y2YxNWQ4NzQ4ZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83ZDVhMjAxNDU3ZmQ0MDJkODgwMDEzN2ZhNzFmYzA1MyA9ICQoJzxkaXYgaWQ9Imh0bWxfN2Q1YTIwMTQ1N2ZkNDAyZDg4MDAxMzdmYTcxZmMwNTMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlBlbGhhbSBQYXJrd2F5LCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZWJiZTY3OTU0ODAxNDFmYWI5NTAyOGNmMTVkODc0OGQuc2V0Q29udGVudChodG1sXzdkNWEyMDE0NTdmZDQwMmQ4ODAwMTM3ZmE3MWZjMDUzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2NmNTM0ZDAyOGNmYzQ4ZjhhM2I5NTZkZGFjOTMwYmQ5LmJpbmRQb3B1cChwb3B1cF9lYmJlNjc5NTQ4MDE0MWZhYjk1MDI4Y2YxNWQ4NzQ4ZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82YzY4OGI3YTM0Yjk0NTk5YWZkYWU4Zjc3NDk5MDYyOSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg0NzI0NjcwNDkxODEzLC03My43ODY0ODg0NTI2NzQxM10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zM2E1NTZjMzk4OTI0NmQ5YTA5NzdkM2Y1Y2Q4ZjAzYyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85ZThmYTBkNzYzYzA0NDliODcyNjgyYTY2OGMxNjY5MSA9ICQoJzxkaXYgaWQ9Imh0bWxfOWU4ZmEwZDc2M2MwNDQ5Yjg3MjY4MmE2NjhjMTY2OTEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNpdHkgSXNsYW5kLCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzNhNTU2YzM5ODkyNDZkOWEwOTc3ZDNmNWNkOGYwM2Muc2V0Q29udGVudChodG1sXzllOGZhMGQ3NjNjMDQ0OWI4NzI2ODJhNjY4YzE2NjkxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzZjNjg4YjdhMzRiOTQ1OTlhZmRhZThmNzc0OTkwNjI5LmJpbmRQb3B1cChwb3B1cF8zM2E1NTZjMzk4OTI0NmQ5YTA5NzdkM2Y1Y2Q4ZjAzYyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xNTFmYTZkYThmYzM0MTVkYTE2M2RiZTcyNTJmNDQ2ZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg3MDE4NTE2NDk3NTMyNSwtNzMuODg1NTEyMTg0MTkxM10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9kNjM4YzNmNGQwMjM0ZWE4ODc3OWVjZjYzOWExZTI0MiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81MTljNjkxZjUzMjM0Y2RlOWIxZjZiMTEzZWM4M2Y4YSA9ICQoJzxkaXYgaWQ9Imh0bWxfNTE5YzY5MWY1MzIzNGNkZTliMWY2YjExM2VjODNmOGEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJlZGZvcmQgUGFyaywgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Q2MzhjM2Y0ZDAyMzRlYTg4Nzc5ZWNmNjM5YTFlMjQyLnNldENvbnRlbnQoaHRtbF81MTljNjkxZjUzMjM0Y2RlOWIxZjZiMTEzZWM4M2Y4YSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xNTFmYTZkYThmYzM0MTVkYTE2M2RiZTcyNTJmNDQ2ZS5iaW5kUG9wdXAocG9wdXBfZDYzOGMzZjRkMDIzNGVhODg3NzllY2Y2MzlhMWUyNDIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZWY0OWJmMDRlZmFhNGM0OThlOTk5YzIwOTE5ZDQ2NGIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NTU3MjcwNzcxOTY2NCwtNzMuOTEwNDE1OTYxOTEzMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xNTkyNTM4NWMyOTY0YjQzYmUzNDRhNDc1YzYyN2ZlMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iYmYwYzdhZjVhNGQ0NWM5YjYzOTZiZTM0ZTliMTIzNSA9ICQoJzxkaXYgaWQ9Imh0bWxfYmJmMGM3YWY1YTRkNDVjOWI2Mzk2YmUzNGU5YjEyMzUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlVuaXZlcnNpdHkgSGVpZ2h0cywgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzE1OTI1Mzg1YzI5NjRiNDNiZTM0NGE0NzVjNjI3ZmUxLnNldENvbnRlbnQoaHRtbF9iYmYwYzdhZjVhNGQ0NWM5YjYzOTZiZTM0ZTliMTIzNSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lZjQ5YmYwNGVmYWE0YzQ5OGU5OTljMjA5MTlkNDY0Yi5iaW5kUG9wdXAocG9wdXBfMTU5MjUzODVjMjk2NGI0M2JlMzQ0YTQ3NWM2MjdmZTEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNjNkNzRmYjgzZmM2NDA4M2JlZmNlNTk0ZDVlNDdjZTMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NDc4OTc5MjYwNjI3MSwtNzMuOTE5NjcxNTkxMTk1NjVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjAzN2JhMjAxZTY5NGRhNmI5MWZkZDRhYzc2NGRmZmEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNjVmNDZmZTU0NmY4NDY5Njk4YjZmZjg2NWFiNTE4OGIgPSAkKCc8ZGl2IGlkPSJodG1sXzY1ZjQ2ZmU1NDZmODQ2OTY5OGI2ZmY4NjVhYjUxODhiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Nb3JyaXMgSGVpZ2h0cywgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2YwMzdiYTIwMWU2OTRkYTZiOTFmZGQ0YWM3NjRkZmZhLnNldENvbnRlbnQoaHRtbF82NWY0NmZlNTQ2Zjg0Njk2OThiNmZmODY1YWI1MTg4Yik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82M2Q3NGZiODNmYzY0MDgzYmVmY2U1OTRkNWU0N2NlMy5iaW5kUG9wdXAocG9wdXBfZjAzN2JhMjAxZTY5NGRhNmI5MWZkZDRhYzc2NGRmZmEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZmE3Mjc4ZmFkM2JhNGZlMjhmZGM3OGNiNzk1ZTNjNTIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NjA5OTY3OTYzODY1NCwtNzMuODk2NDI2NTU5ODE2MjNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMjM3MWQyNTUzMGYwNGU2NThmZjEyNTAyZjI3NGNlODEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTI0ZWFkMzdkM2ExNDQzNzg3NWQ3NDhkODNkYjRkZTQgPSAkKCc8ZGl2IGlkPSJodG1sX2UyNGVhZDM3ZDNhMTQ0Mzc4NzVkNzQ4ZDgzZGI0ZGU0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Gb3JkaGFtLCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMjM3MWQyNTUzMGYwNGU2NThmZjEyNTAyZjI3NGNlODEuc2V0Q29udGVudChodG1sX2UyNGVhZDM3ZDNhMTQ0Mzc4NzVkNzQ4ZDgzZGI0ZGU0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ZhNzI3OGZhZDNiYTRmZTI4ZmRjNzhjYjc5NWUzYzUyLmJpbmRQb3B1cChwb3B1cF8yMzcxZDI1NTMwZjA0ZTY1OGZmMTI1MDJmMjc0Y2U4MSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iYzg2YmU5NWE0ZGQ0MTYxOTI3MzhlZWY3YjdlZGVhOSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg0MjY5NjE1Nzg2MDUzLC03My44ODczNTYxNzUzMjMzOF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85YjUzM2Y3ZDU2MDM0MzM0YTY5MWQ0YzVhYjNkOWE3OCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wZWYwZTIzNTQ2M2Y0MTY3ODgwNjZiMmYzNTY0OWYzNSA9ICQoJzxkaXYgaWQ9Imh0bWxfMGVmMGUyMzU0NjNmNDE2Nzg4MDY2YjJmMzU2NDlmMzUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVhc3QgVHJlbW9udCwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzliNTMzZjdkNTYwMzQzMzRhNjkxZDRjNWFiM2Q5YTc4LnNldENvbnRlbnQoaHRtbF8wZWYwZTIzNTQ2M2Y0MTY3ODgwNjZiMmYzNTY0OWYzNSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iYzg2YmU5NWE0ZGQ0MTYxOTI3MzhlZWY3YjdlZGVhOS5iaW5kUG9wdXAocG9wdXBfOWI1MzNmN2Q1NjAzNDMzNGE2OTFkNGM1YWIzZDlhNzgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNGI3YTBhYjBhYmJhNDNkOWIxZmQ2YTFmMDRhZjBhNTAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44Mzk0NzUwNTY3MjY1MywtNzMuODc3NzQ0NzQ5MTA1NDVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODA4YjgwNDRlOGZkNDY1N2EwYTEwZjk5MzExMmYwOTQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMTBiM2M3ZDMwZjQxNGY3Mjg4ODc5MDUzYjkwZjQxZWQgPSAkKCc8ZGl2IGlkPSJodG1sXzEwYjNjN2QzMGY0MTRmNzI4ODg3OTA1M2I5MGY0MWVkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5XZXN0IEZhcm1zLCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfODA4YjgwNDRlOGZkNDY1N2EwYTEwZjk5MzExMmYwOTQuc2V0Q29udGVudChodG1sXzEwYjNjN2QzMGY0MTRmNzI4ODg3OTA1M2I5MGY0MWVkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzRiN2EwYWIwYWJiYTQzZDliMWZkNmExZjA0YWYwYTUwLmJpbmRQb3B1cChwb3B1cF84MDhiODA0NGU4ZmQ0NjU3YTBhMTBmOTkzMTEyZjA5NCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81MDY1ODNkNTcxNmQ0ODQ0YTVjZDQ0ODI3NzRkOWVmYiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjgzNjYyMzAxMDcwNjA1NiwtNzMuOTI2MTAyMDkzNTgxM10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84MWU5ZjRkMzEyNGI0YWQ0ODIwYTYwZDE5NjdmMDg2MCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jYjMwYTA3YmJlYzI0Y2U3OWM0OTdiZTI3YmYxZmJkMCA9ICQoJzxkaXYgaWQ9Imh0bWxfY2IzMGEwN2JiZWMyNGNlNzljNDk3YmUyN2JmMWZiZDAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkhpZ2ggIEJyaWRnZSwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzgxZTlmNGQzMTI0YjRhZDQ4MjBhNjBkMTk2N2YwODYwLnNldENvbnRlbnQoaHRtbF9jYjMwYTA3YmJlYzI0Y2U3OWM0OTdiZTI3YmYxZmJkMCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81MDY1ODNkNTcxNmQ0ODQ0YTVjZDQ0ODI3NzRkOWVmYi5iaW5kUG9wdXAocG9wdXBfODFlOWY0ZDMxMjRiNGFkNDgyMGE2MGQxOTY3ZjA4NjApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNGIzNzdjODJiZmY1NDA1NGEwZmFhZWJjNGI0ZWY1ZTAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44MTk3NTQzNzA1OTQ5MzYsLTczLjkwOTQyMTYwNzU3NDM2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzMxNzRiNTM2NThjZTRkMDZhOTMxZTlkZWM3MTM4YjI1ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2YxOTFhM2M0OGM4YTQ1ZGJiMDE0NDJiYjIwYjZlZGU2ID0gJCgnPGRpdiBpZD0iaHRtbF9mMTkxYTNjNDhjOGE0NWRiYjAxNDQyYmIyMGI2ZWRlNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TWVscm9zZSwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzMxNzRiNTM2NThjZTRkMDZhOTMxZTlkZWM3MTM4YjI1LnNldENvbnRlbnQoaHRtbF9mMTkxYTNjNDhjOGE0NWRiYjAxNDQyYmIyMGI2ZWRlNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80YjM3N2M4MmJmZjU0MDU0YTBmYWFlYmM0YjRlZjVlMC5iaW5kUG9wdXAocG9wdXBfMzE3NGI1MzY1OGNlNGQwNmE5MzFlOWRlYzcxMzhiMjUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfN2MyMDM2Njg0NmQ1NDNiNWJmMTI5ZDY3YTE5MWY2ODYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44MDYyMzg3NDkzNTE3NywtNzMuOTE2MDk5ODc0ODc1NzVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNTRhZTJhODJlNWI3NDI4ZWIyYjZkZjI1ZWJiYzFmYTkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMTdhMWY4YWY3NmMwNDJmNzlkNjRlYWE5MjRjOWNkYjUgPSAkKCc8ZGl2IGlkPSJodG1sXzE3YTFmOGFmNzZjMDQyZjc5ZDY0ZWFhOTI0YzljZGI1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Nb3R0IEhhdmVuLCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNTRhZTJhODJlNWI3NDI4ZWIyYjZkZjI1ZWJiYzFmYTkuc2V0Q29udGVudChodG1sXzE3YTFmOGFmNzZjMDQyZjc5ZDY0ZWFhOTI0YzljZGI1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzdjMjAzNjY4NDZkNTQzYjViZjEyOWQ2N2ExOTFmNjg2LmJpbmRQb3B1cChwb3B1cF81NGFlMmE4MmU1Yjc0MjhlYjJiNmRmMjVlYmJjMWZhOSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zNzY5MTg1NjVkMGU0OGRlYmQ0MWRiOTZlMjE3YTMyZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjgwMTY2MzYyNzc1NjIwNiwtNzMuOTEzMjIxMzkzODYxMzVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzA1ZTk4NzNhNzI5NDBlNGEyMjNjNTllM2NiZDVmZDkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTQxYjU3NjVkMDg2NGM1MTlmOTc1YWQ1NjdmMzEzMWEgPSAkKCc8ZGl2IGlkPSJodG1sXzU0MWI1NzY1ZDA4NjRjNTE5Zjk3NWFkNTY3ZjMxMzFhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Qb3J0IE1vcnJpcywgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzMwNWU5ODczYTcyOTQwZTRhMjIzYzU5ZTNjYmQ1ZmQ5LnNldENvbnRlbnQoaHRtbF81NDFiNTc2NWQwODY0YzUxOWY5NzVhZDU2N2YzMTMxYSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zNzY5MTg1NjVkMGU0OGRlYmQ0MWRiOTZlMjE3YTMyZC5iaW5kUG9wdXAocG9wdXBfMzA1ZTk4NzNhNzI5NDBlNGEyMjNjNTllM2NiZDVmZDkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfY2Q5ZTQzMzk3OTQwNGQxZTg4Y2I1YWM3YWQ4ZGJkNjAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44MTUwOTkwNDU0NTgyMiwtNzMuODk1Nzg4MjAwOTQ0Nl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80MTNjYmVhZjhmYjg0NjQ3OWY0MjU3ODJmY2JmMWRmNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zNDU4MDU2NGYzZGQ0NTAzYTcyYTRlYzJjYjBlN2I3NCA9ICQoJzxkaXYgaWQ9Imh0bWxfMzQ1ODA1NjRmM2RkNDUwM2E3MmE0ZWMyY2IwZTdiNzQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxvbmd3b29kLCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNDEzY2JlYWY4ZmI4NDY0NzlmNDI1NzgyZmNiZjFkZjcuc2V0Q29udGVudChodG1sXzM0NTgwNTY0ZjNkZDQ1MDNhNzJhNGVjMmNiMGU3Yjc0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2NkOWU0MzM5Nzk0MDRkMWU4OGNiNWFjN2FkOGRiZDYwLmJpbmRQb3B1cChwb3B1cF80MTNjYmVhZjhmYjg0NjQ3OWY0MjU3ODJmY2JmMWRmNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zYTUwODNlNmQwYzE0YzU2ODgyYjU2NmJjNmZhYjBiOSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjgwOTcyOTg3OTM4NzA5LC03My44ODMzMTUwNTk1NTI5MV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8wYmI1NDM2OTUxZGY0M2ExOWI3ZDQ4NjRiYjAyOWE0MCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80ZmRiYTMwM2U3N2I0MzM0OGE1ZTJhNmZkMjMxNzU3NiA9ICQoJzxkaXYgaWQ9Imh0bWxfNGZkYmEzMDNlNzdiNDMzNDhhNWUyYTZmZDIzMTc1NzYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkh1bnRzIFBvaW50LCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMGJiNTQzNjk1MWRmNDNhMTliN2Q0ODY0YmIwMjlhNDAuc2V0Q29udGVudChodG1sXzRmZGJhMzAzZTc3YjQzMzQ4YTVlMmE2ZmQyMzE3NTc2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzNhNTA4M2U2ZDBjMTRjNTY4ODJiNTY2YmM2ZmFiMGI5LmJpbmRQb3B1cChwb3B1cF8wYmI1NDM2OTUxZGY0M2ExOWI3ZDQ4NjRiYjAyOWE0MCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xZTY4MTVkNzNlMmU0YTNkOWQ4ODFmNmY2ZjE2MjZlMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjgyMzU5MTk4NTg1NTM0LC03My45MDE1MDY0ODk0MzA1OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80ZDdkNzY2OTk2MDA0YmZlYjYzYjVhYjYxMmUxNTVlNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yYmY3NWNlNGMxZmE0MzkzOTRiODkyNTQ3MmM0ZWI5NCA9ICQoJzxkaXYgaWQ9Imh0bWxfMmJmNzVjZTRjMWZhNDM5Mzk0Yjg5MjU0NzJjNGViOTQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk1vcnJpc2FuaWEsIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80ZDdkNzY2OTk2MDA0YmZlYjYzYjVhYjYxMmUxNTVlNC5zZXRDb250ZW50KGh0bWxfMmJmNzVjZTRjMWZhNDM5Mzk0Yjg5MjU0NzJjNGViOTQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMWU2ODE1ZDczZTJlNGEzZDlkODgxZjZmNmYxNjI2ZTEuYmluZFBvcHVwKHBvcHVwXzRkN2Q3NjY5OTYwMDRiZmViNjNiNWFiNjEyZTE1NWU0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzEzNmM0M2E0NWM2NDRhNTZhMWU3N2YxODkzNDYxMjE0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODIxMDEyMTk3OTE0MDE1LC03My44NjU3NDYwOTU1NDkyNF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yMzBiYjM1NDg3YTI0MTIwOGQwMmQ1NjBmNGEzMTJkYyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83Yjg1ZmVlZGIwZmI0MDZhODY5ODZlY2QzZTYzNjM2YiA9ICQoJzxkaXYgaWQ9Imh0bWxfN2I4NWZlZWRiMGZiNDA2YTg2OTg2ZWNkM2U2MzYzNmIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlNvdW5kdmlldywgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzIzMGJiMzU0ODdhMjQxMjA4ZDAyZDU2MGY0YTMxMmRjLnNldENvbnRlbnQoaHRtbF83Yjg1ZmVlZGIwZmI0MDZhODY5ODZlY2QzZTYzNjM2Yik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xMzZjNDNhNDVjNjQ0YTU2YTFlNzdmMTg5MzQ2MTIxNC5iaW5kUG9wdXAocG9wdXBfMjMwYmIzNTQ4N2EyNDEyMDhkMDJkNTYwZjRhMzEyZGMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTA2ODllYjgxMGRiNGZjZmFkOGQ5M2NlNzY0MWJhNTIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44MDY1NTExMjAwMzU4OSwtNzMuODU0MTQ0MTYxODkyNjZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzA4OWY3ZGRhYzI4NGU4OTkzZmNhZTZhNTU0MGNlZGQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzg5Y2I3ZDYxMzFjNDFkNmEyNzRlMjBhNjRjNzIwMDggPSAkKCc8ZGl2IGlkPSJodG1sXzc4OWNiN2Q2MTMxYzQxZDZhMjc0ZTIwYTY0YzcyMDA4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DbGFzb24gUG9pbnQsIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zMDg5ZjdkZGFjMjg0ZTg5OTNmY2FlNmE1NTQwY2VkZC5zZXRDb250ZW50KGh0bWxfNzg5Y2I3ZDYxMzFjNDFkNmEyNzRlMjBhNjRjNzIwMDgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYTA2ODllYjgxMGRiNGZjZmFkOGQ5M2NlNzY0MWJhNTIuYmluZFBvcHVwKHBvcHVwXzMwODlmN2RkYWMyODRlODk5M2ZjYWU2YTU1NDBjZWRkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2MwNTRmNmEyMGI0ZjRkZjA4YmE4N2JhZThiNTU4YjgwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODE1MTA5MjU4MDQwMDUsLTczLjgxNjM1MDAyMTU4NDQxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzI4YzgyODkxYjM2OTQ4OWFhM2E2ZWM0MjMxYzc0OWNkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2VmNjZhMjUyMjk4MDQxNjdiZTU5Nzg3M2Q2MDhhMGJhID0gJCgnPGRpdiBpZD0iaHRtbF9lZjY2YTI1MjI5ODA0MTY3YmU1OTc4NzNkNjA4YTBiYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGhyb2dzIE5lY2ssIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yOGM4Mjg5MWIzNjk0ODlhYTNhNmVjNDIzMWM3NDljZC5zZXRDb250ZW50KGh0bWxfZWY2NmEyNTIyOTgwNDE2N2JlNTk3ODczZDYwOGEwYmEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzA1NGY2YTIwYjRmNGRmMDhiYTg3YmFlOGI1NThiODAuYmluZFBvcHVwKHBvcHVwXzI4YzgyODkxYjM2OTQ4OWFhM2E2ZWM0MjMxYzc0OWNkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzVlMzkwYTRhZmRjMTRmZjViZDI4MzQ4MzVjMmRkMjQ2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODQ0MjQ1OTM2OTQ3Mzc0LC03My44MjQwOTkyNjc1Mzg1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzJhZTc3ZTk2MGJjZTRhODY4ODZmZmQwY2QwODFlMGVlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzgzMjBmOWExMjA2YjQ4YmViZDc5YzJlMzFiMjE0YjIyID0gJCgnPGRpdiBpZD0iaHRtbF84MzIwZjlhMTIwNmI0OGJlYmQ3OWMyZTMxYjIxNGIyMiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q291bnRyeSBDbHViLCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMmFlNzdlOTYwYmNlNGE4Njg4NmZmZDBjZDA4MWUwZWUuc2V0Q29udGVudChodG1sXzgzMjBmOWExMjA2YjQ4YmViZDc5YzJlMzFiMjE0YjIyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzVlMzkwYTRhZmRjMTRmZjViZDI4MzQ4MzVjMmRkMjQ2LmJpbmRQb3B1cChwb3B1cF8yYWU3N2U5NjBiY2U0YTg2ODg2ZmZkMGNkMDgxZTBlZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kYjdjNjVlZjI0NzQ0OTM3ODE0ZTkxNzE3OTY4MjA5NCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjgzNzkzNzgyMjI2NzI4NiwtNzMuODU2MDAzMTA1MzU3ODNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYjM3NzQxMTlhNDA3NDVhZjgxNTZiNjM0NzE1YWEwMjggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOGM2ZDljZWY0YWRiNDk3N2I0ZTY1MDkyZTczNGQwODkgPSAkKCc8ZGl2IGlkPSJodG1sXzhjNmQ5Y2VmNGFkYjQ5NzdiNGU2NTA5MmU3MzRkMDg5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5QYXJrY2hlc3RlciwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2IzNzc0MTE5YTQwNzQ1YWY4MTU2YjYzNDcxNWFhMDI4LnNldENvbnRlbnQoaHRtbF84YzZkOWNlZjRhZGI0OTc3YjRlNjUwOTJlNzM0ZDA4OSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kYjdjNjVlZjI0NzQ0OTM3ODE0ZTkxNzE3OTY4MjA5NC5iaW5kUG9wdXAocG9wdXBfYjM3NzQxMTlhNDA3NDVhZjgxNTZiNjM0NzE1YWEwMjgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNDdlN2ZmYzNkNjQ5NGI2OTg5NGQ4ZjU2OGY3ZjU2ZTkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NDA2MTk0OTY0MzI3LC03My44NDIxOTQwNzYwNDQ0NF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hNmJkMWNhNWU5Y2U0YTE5YjQ0MTM4YzMxNTg4NTExZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lYWYwYzJmYjJiZTI0ZWRhYmZjOWE2MWU3NjVlYjE3MSA9ICQoJzxkaXYgaWQ9Imh0bWxfZWFmMGMyZmIyYmUyNGVkYWJmYzlhNjFlNzY1ZWIxNzEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldlc3RjaGVzdGVyIFNxdWFyZSwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2E2YmQxY2E1ZTljZTRhMTliNDQxMzhjMzE1ODg1MTFkLnNldENvbnRlbnQoaHRtbF9lYWYwYzJmYjJiZTI0ZWRhYmZjOWE2MWU3NjVlYjE3MSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80N2U3ZmZjM2Q2NDk0YjY5ODk0ZDhmNTY4ZjdmNTZlOS5iaW5kUG9wdXAocG9wdXBfYTZiZDFjYTVlOWNlNGExOWI0NDEzOGMzMTU4ODUxMWQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDIyNDQ3ZGQ5MWUzNGMyMzk3NjFjOGJmMDg1MTM1ODggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NDM2MDg0NzEyNDcxOCwtNzMuODY2Mjk5MTgwNzU2MV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9iMTQyODlkNjNjNjk0YjgwYjI5YTVmNGU5YWJmNWJlNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jNjc1ZDczZGQ2MjM0YWE4YWFmZmI3OThkYjFmYTlkMiA9ICQoJzxkaXYgaWQ9Imh0bWxfYzY3NWQ3M2RkNjIzNGFhOGFhZmZiNzk4ZGIxZmE5ZDIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlZhbiBOZXN0LCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjE0Mjg5ZDYzYzY5NGI4MGIyOWE1ZjRlOWFiZjViZTcuc2V0Q29udGVudChodG1sX2M2NzVkNzNkZDYyMzRhYThhYWZmYjc5OGRiMWZhOWQyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2QyMjQ0N2RkOTFlMzRjMjM5NzYxYzhiZjA4NTEzNTg4LmJpbmRQb3B1cChwb3B1cF9iMTQyODlkNjNjNjk0YjgwYjI5YTVmNGU5YWJmNWJlNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81ZDAwYzI2MTNjZjk0MjI3OTc1ZDFjNWExYjljYzgxMCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg0NzU0OTA2MzUzNjMzNCwtNzMuODUwNDAxNzgwMzA0MjFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNWNkM2U2OTgwMzYwNGI0M2FkY2U1Nzc3YmM4ZWQ1NTMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfN2VmZWI5MWNhYTYwNDA1MjhhZmJlYjRjOTg0YjE2ZGQgPSAkKCc8ZGl2IGlkPSJodG1sXzdlZmViOTFjYWE2MDQwNTI4YWZiZWI0Yzk4NGIxNmRkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Nb3JyaXMgUGFyaywgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzVjZDNlNjk4MDM2MDRiNDNhZGNlNTc3N2JjOGVkNTUzLnNldENvbnRlbnQoaHRtbF83ZWZlYjkxY2FhNjA0MDUyOGFmYmViNGM5ODRiMTZkZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81ZDAwYzI2MTNjZjk0MjI3OTc1ZDFjNWExYjljYzgxMC5iaW5kUG9wdXAocG9wdXBfNWNkM2U2OTgwMzYwNGI0M2FkY2U1Nzc3YmM4ZWQ1NTMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfN2ZmOTZhZmM2OWY3NGIwYTgzODQ1MjQ0OWViYjk2NmYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NTcyNzcxMDA3Mzg5NSwtNzMuODg4NDUxOTYxMzQ4MDRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzcwNjQ4ZjZiZmZmNDVlNWJjYWQ1NTY3MzgwZDVmNWMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNjM5ODM0MDU3Zjc5NDIwNTljNDRkNTMzMzMxZDQ2NmYgPSAkKCc8ZGl2IGlkPSJodG1sXzYzOTgzNDA1N2Y3OTQyMDU5YzQ0ZDUzMzMzMWQ0NjZmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CZWxtb250LCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzcwNjQ4ZjZiZmZmNDVlNWJjYWQ1NTY3MzgwZDVmNWMuc2V0Q29udGVudChodG1sXzYzOTgzNDA1N2Y3OTQyMDU5YzQ0ZDUzMzMzMWQ0NjZmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzdmZjk2YWZjNjlmNzRiMGE4Mzg0NTI0NDllYmI5NjZmLmJpbmRQb3B1cChwb3B1cF8zNzA2NDhmNmJmZmY0NWU1YmNhZDU1NjczODBkNWY1Yyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lNDk3NTQyN2RlNWY0MjA3YmFjOGI0ZjRlMDIwNGYwNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg4MTM5NDk3NzI3MDg2LC03My45MTcxOTA0ODIxMDM5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85Yzk1MWQ2MzI0MmY0YWY4OThmNTY5NjZhZmZiZGQ4NiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zNzQ1OWNiM2NmMjE0MzhiOGVkOWY3MDExNWEwYjg0MiA9ICQoJzxkaXYgaWQ9Imh0bWxfMzc0NTljYjNjZjIxNDM4YjhlZDlmNzAxMTVhMGI4NDIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlNwdXl0ZW4gRHV5dmlsLCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOWM5NTFkNjMyNDJmNGFmODk4ZjU2OTY2YWZmYmRkODYuc2V0Q29udGVudChodG1sXzM3NDU5Y2IzY2YyMTQzOGI4ZWQ5ZjcwMTE1YTBiODQyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2U0OTc1NDI3ZGU1ZjQyMDdiYWM4YjRmNGUwMjA0ZjA0LmJpbmRQb3B1cChwb3B1cF85Yzk1MWQ2MzI0MmY0YWY4OThmNTY5NjZhZmZiZGQ4Nik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lZWNhNmQ2NTBhOGE0N2RiOWRmOGVjZTQxY2RjMzI0OSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjkwODU0MjgyOTUwNjY2LC03My45MDQ1MzA1NDkwODkyN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84ZDQ0NzA3ZTAyMDM0N2RlOTg4NGQ3YjhiYjY1ZDVjZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wNTBhY2MxN2Q4MGU0MGVjYTM5MzJjZjNiNDQ5MzI3MiA9ICQoJzxkaXYgaWQ9Imh0bWxfMDUwYWNjMTdkODBlNDBlY2EzOTMyY2YzYjQ0OTMyNzIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5vcnRoIFJpdmVyZGFsZSwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzhkNDQ3MDdlMDIwMzQ3ZGU5ODg0ZDdiOGJiNjVkNWNkLnNldENvbnRlbnQoaHRtbF8wNTBhY2MxN2Q4MGU0MGVjYTM5MzJjZjNiNDQ5MzI3Mik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lZWNhNmQ2NTBhOGE0N2RiOWRmOGVjZTQxY2RjMzI0OS5iaW5kUG9wdXAocG9wdXBfOGQ0NDcwN2UwMjAzNDdkZTk4ODRkN2I4YmI2NWQ1Y2QpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYWU3NWNlNjY4MTI5NDhjNzhhMzQ5NDNlZWM4NmI3NTEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NTA2NDE0MDk0MDMzNSwtNzMuODMyMDczNzgyNDA0N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hZDE1ZWUzNDc4ODg0YWZjOWRhN2RkY2RkMWNmYmNmMCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xZWI1ZWQ5YmU5MGU0NDY4OWE3ODMzODMzYjhlYzIxOCA9ICQoJzxkaXYgaWQ9Imh0bWxfMWViNWVkOWJlOTBlNDQ2ODlhNzgzMzgzM2I4ZWMyMTgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlBlbGhhbSBCYXksIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hZDE1ZWUzNDc4ODg0YWZjOWRhN2RkY2RkMWNmYmNmMC5zZXRDb250ZW50KGh0bWxfMWViNWVkOWJlOTBlNDQ2ODlhNzgzMzgzM2I4ZWMyMTgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYWU3NWNlNjY4MTI5NDhjNzhhMzQ5NDNlZWM4NmI3NTEuYmluZFBvcHVwKHBvcHVwX2FkMTVlZTM0Nzg4ODRhZmM5ZGE3ZGRjZGQxY2ZiY2YwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzVlNmViZDBkYzBhYTQ4ZjhiNGFmMjg1MjU4MmFiYjkzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODI2NTc5NTE2ODY5MjIsLTczLjgyNjIwMjc1OTk0MDczXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2FjYjBjOGExMTRiYjQ0N2ViNGQzZDBlYzllZGFhZWU1ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzI2NjVlYTg2ZmE2OTQ5YWNhOTYyOGU5NzRiYjc3YWJmID0gJCgnPGRpdiBpZD0iaHRtbF8yNjY1ZWE4NmZhNjk0OWFjYTk2MjhlOTc0YmI3N2FiZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U2NodXlsZXJ2aWxsZSwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2FjYjBjOGExMTRiYjQ0N2ViNGQzZDBlYzllZGFhZWU1LnNldENvbnRlbnQoaHRtbF8yNjY1ZWE4NmZhNjk0OWFjYTk2MjhlOTc0YmI3N2FiZik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81ZTZlYmQwZGMwYWE0OGY4YjRhZjI4NTI1ODJhYmI5My5iaW5kUG9wdXAocG9wdXBfYWNiMGM4YTExNGJiNDQ3ZWI0ZDNkMGVjOWVkYWFlZTUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNWNkMTc0NTYyZWU4NGM1ZGIxZDdjYmExYTQxNWI0YzYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44MjE5ODYxMTgxNjM0OTQsLTczLjgxMzg4NTE0NDI4NjE5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzlmNmYzMDFhZDcyODQyMDhiNTljN2RiMjM0Yjc4MzMyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzU2NTkzZDRlOWYwMjQwMWJiYzI1ZDVkNjAxMDdhMmYwID0gJCgnPGRpdiBpZD0iaHRtbF81NjU5M2Q0ZTlmMDI0MDFiYmMyNWQ1ZDYwMTA3YTJmMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RWRnZXdhdGVyIFBhcmssIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85ZjZmMzAxYWQ3Mjg0MjA4YjU5YzdkYjIzNGI3ODMzMi5zZXRDb250ZW50KGh0bWxfNTY1OTNkNGU5ZjAyNDAxYmJjMjVkNWQ2MDEwN2EyZjApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNWNkMTc0NTYyZWU4NGM1ZGIxZDdjYmExYTQxNWI0YzYuYmluZFBvcHVwKHBvcHVwXzlmNmYzMDFhZDcyODQyMDhiNTljN2RiMjM0Yjc4MzMyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2NmZjI3ZTZkOGJmOTRhYjU4NzllMjUxZGFjN2QxZDhhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODE5MDE0Mzc2OTg4MzE0LC03My44NDgwMjcyOTU4MjczNV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8wYWQwMmUyODBjN2M0NTk1YTRlMjRlMGIzNjJkZTE3NSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83ZDg0ZjgyZmQ2ODU0N2Y1ODc3MzJjNmRjMDAwNGYwMCA9ICQoJzxkaXYgaWQ9Imh0bWxfN2Q4NGY4MmZkNjg1NDdmNTg3NzMyYzZkYzAwMDRmMDAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNhc3RsZSBIaWxsLCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMGFkMDJlMjgwYzdjNDU5NWE0ZTI0ZTBiMzYyZGUxNzUuc2V0Q29udGVudChodG1sXzdkODRmODJmZDY4NTQ3ZjU4NzczMmM2ZGMwMDA0ZjAwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2NmZjI3ZTZkOGJmOTRhYjU4NzllMjUxZGFjN2QxZDhhLmJpbmRQb3B1cChwb3B1cF8wYWQwMmUyODBjN2M0NTk1YTRlMjRlMGIzNjJkZTE3NSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85NDE2OTc1OTNiZWU0ZmZkYmEyODkzYjAxNWRjODk2ZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg3MTM3MDc4MTkyMzcxLC03My44NjMzMjM2MTY1Mjc3N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mNmRhNTFhOThjYWY0ODEyOTI4MzI5NmVlOTBlMjJiYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wYzA0YzdkNTAxZTc0OGVhYWIzZGNhMzRjZDZiYmM0YiA9ICQoJzxkaXYgaWQ9Imh0bWxfMGMwNGM3ZDUwMWU3NDhlYWFiM2RjYTM0Y2Q2YmJjNGIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk9saW52aWxsZSwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Y2ZGE1MWE5OGNhZjQ4MTI5MjgzMjk2ZWU5MGUyMmJhLnNldENvbnRlbnQoaHRtbF8wYzA0YzdkNTAxZTc0OGVhYWIzZGNhMzRjZDZiYmM0Yik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85NDE2OTc1OTNiZWU0ZmZkYmEyODkzYjAxNWRjODk2Zi5iaW5kUG9wdXAocG9wdXBfZjZkYTUxYTk4Y2FmNDgxMjkyODMyOTZlZTkwZTIyYmEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzQwZTI4OWZjNThjNDc4NTlhYTYwNjA4YzY5Zjc3OGMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NjI5NjU2MjQ3Nzk5OCwtNzMuODQxNjExOTQ4MzEyMjNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODY0YmM5Y2JkODM4NGJjZDk5ZjU4MDA3ZWUyNTczMzkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzIxYzQ1OTNkNmU0NDFjMmIyZmE2MGI4NGFiZmYwODEgPSAkKCc8ZGl2IGlkPSJodG1sXzcyMWM0NTkzZDZlNDQxYzJiMmZhNjBiODRhYmZmMDgxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5QZWxoYW0gR2FyZGVucywgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzg2NGJjOWNiZDgzODRiY2Q5OWY1ODAwN2VlMjU3MzM5LnNldENvbnRlbnQoaHRtbF83MjFjNDU5M2Q2ZTQ0MWMyYjJmYTYwYjg0YWJmZjA4MSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jNDBlMjg5ZmM1OGM0Nzg1OWFhNjA2MDhjNjlmNzc4Yy5iaW5kUG9wdXAocG9wdXBfODY0YmM5Y2JkODM4NGJjZDk5ZjU4MDA3ZWUyNTczMzkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZWZiODNkMDBkMmViNGY1MWEyMTQ2ODNiMDdmYTkzNzIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44MzQyODM4MDczMzg1MSwtNzMuOTE1NTg5NDE3NzM0NDRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDQ5ZDRmYWFkZTlmNGNmNWIyYjhjMDYyNmMyNDUyMjUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNGQ0NmJlNjExZTMzNGRlMGE4MWMwNWQ2MjI0MGJmOWIgPSAkKCc8ZGl2IGlkPSJodG1sXzRkNDZiZTYxMWUzMzRkZTBhODFjMDVkNjIyNDBiZjliIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Db25jb3Vyc2UsIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kNDlkNGZhYWRlOWY0Y2Y1YjJiOGMwNjI2YzI0NTIyNS5zZXRDb250ZW50KGh0bWxfNGQ0NmJlNjExZTMzNGRlMGE4MWMwNWQ2MjI0MGJmOWIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZWZiODNkMDBkMmViNGY1MWEyMTQ2ODNiMDdmYTkzNzIuYmluZFBvcHVwKHBvcHVwX2Q0OWQ0ZmFhZGU5ZjRjZjViMmI4YzA2MjZjMjQ1MjI1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzQ5MDhhNzcyNGE0YzQ5MjliOWFiZDRiZGIzZDg0MmE2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODI5Nzc0Mjk3ODcxNjEsLTczLjg1MDUzNTI0NDUxOTM1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzIyNjM0NjA2ZDkwMTRmZTI5M2IxN2Q4NGU4Y2U4YTU0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2FjNjc0NGM1NDI4YjQxZGNhNGZmYzdmZTE4YzMzMWY5ID0gJCgnPGRpdiBpZD0iaHRtbF9hYzY3NDRjNTQyOGI0MWRjYTRmZmM3ZmUxOGMzMzFmOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VW5pb25wb3J0LCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMjI2MzQ2MDZkOTAxNGZlMjkzYjE3ZDg0ZThjZThhNTQuc2V0Q29udGVudChodG1sX2FjNjc0NGM1NDI4YjQxZGNhNGZmYzdmZTE4YzMzMWY5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzQ5MDhhNzcyNGE0YzQ5MjliOWFiZDRiZGIzZDg0MmE2LmJpbmRQb3B1cChwb3B1cF8yMjYzNDYwNmQ5MDE0ZmUyOTNiMTdkODRlOGNlOGE1NCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lMzJlZDVmYWNiOWE0M2Y0Yjc1MjkxNTg2ZDA2MjliMCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg4NDU2MTMwMzAzNzMyLC03My44NDgwODI3MTg3NzE2OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mZmU3OWJhMjk3Mjk0OGUyOTU5ZjYwMDk0MjVjYTA3MSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wZWIxMmNlOWMwYjY0NzE5YTFhMjU1ODY2YTJkNjlkYiA9ICQoJzxkaXYgaWQ9Imh0bWxfMGViMTJjZTljMGI2NDcxOWExYTI1NTg2NmEyZDY5ZGIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVkZW53YWxkLCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZmZlNzliYTI5NzI5NDhlMjk1OWY2MDA5NDI1Y2EwNzEuc2V0Q29udGVudChodG1sXzBlYjEyY2U5YzBiNjQ3MTlhMWEyNTU4NjZhMmQ2OWRiKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2UzMmVkNWZhY2I5YTQzZjRiNzUyOTE1ODZkMDYyOWIwLmJpbmRQb3B1cChwb3B1cF9mZmU3OWJhMjk3Mjk0OGUyOTU5ZjYwMDk0MjVjYTA3MSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lZDg2MDAyNWY5NWE0OTZlODFmZDUzMTAzMDQxM2QwMyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYyNTgwMTA2NTAxMDY1NiwtNzQuMDMwNjIwNjkzNTM4MTNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZGRhNzY2ZGMwNTUzNGFjZjg2NDYxNTRjM2E1YTJiMTcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMjkzZWI5NjllOTkyNDQxMzk4ZTlkMzQyOWE4M2MxODEgPSAkKCc8ZGl2IGlkPSJodG1sXzI5M2ViOTY5ZTk5MjQ0MTM5OGU5ZDM0MjlhODNjMTgxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CYXkgUmlkZ2UsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kZGE3NjZkYzA1NTM0YWNmODY0NjE1NGMzYTVhMmIxNy5zZXRDb250ZW50KGh0bWxfMjkzZWI5NjllOTkyNDQxMzk4ZTlkMzQyOWE4M2MxODEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZWQ4NjAwMjVmOTVhNDk2ZTgxZmQ1MzEwMzA0MTNkMDMuYmluZFBvcHVwKHBvcHVwX2RkYTc2NmRjMDU1MzRhY2Y4NjQ2MTU0YzNhNWEyYjE3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzc4ZmZiNTBiNjhlODQ1ZTFhMmVmM2I5NWNmMzc3MjMxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjExMDA4OTAyMDIwNDQsLTczLjk5NTE3OTk4MzgwNzI5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzg2MDNjZWQ3YzM5MTRlZjA5OTQ2YzUzNDc5ZjgyMjEyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzRhOTZhOThkZjc1MzRlNzBhZjAxNmNjNWVjZWY0MWZmID0gJCgnPGRpdiBpZD0iaHRtbF80YTk2YTk4ZGY3NTM0ZTcwYWYwMTZjYzVlY2VmNDFmZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmVuc29uaHVyc3QsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84NjAzY2VkN2MzOTE0ZWYwOTk0NmM1MzQ3OWY4MjIxMi5zZXRDb250ZW50KGh0bWxfNGE5NmE5OGRmNzUzNGU3MGFmMDE2Y2M1ZWNlZjQxZmYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNzhmZmI1MGI2OGU4NDVlMWEyZWYzYjk1Y2YzNzcyMzEuYmluZFBvcHVwKHBvcHVwXzg2MDNjZWQ3YzM5MTRlZjA5OTQ2YzUzNDc5ZjgyMjEyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzM5NjYxMDIwNjg0MTQwOTViYTZlOWYzYmZiZTBhYWVlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjQ1MTAyOTQ5MjU0MjksLTc0LjAxMDMxNjE4NTI3Nzg0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2JlZTIyNmQxYTE2YzRmOWFhZjE5MGQwMDZlMTk0YjA4ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2RlMjQ4YjlhMDdlYjQzMmU5MmRiYjFmOGJlODdmMjVhID0gJCgnPGRpdiBpZD0iaHRtbF9kZTI0OGI5YTA3ZWI0MzJlOTJkYmIxZjhiZTg3ZjI1YSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U3Vuc2V0IFBhcmssIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iZWUyMjZkMWExNmM0ZjlhYWYxOTBkMDA2ZTE5NGIwOC5zZXRDb250ZW50KGh0bWxfZGUyNDhiOWEwN2ViNDMyZTkyZGJiMWY4YmU4N2YyNWEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMzk2NjEwMjA2ODQxNDA5NWJhNmU5ZjNiZmJlMGFhZWUuYmluZFBvcHVwKHBvcHVwX2JlZTIyNmQxYTE2YzRmOWFhZjE5MGQwMDZlMTk0YjA4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzk1ZDkxNWEyOWIzODQyMzNiMzI2ZTk3ZWNmZmQ2MjhkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzMwMjAwOTg0ODY0NywtNzMuOTU0MjQwOTMxMjczOTNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOWVkODMxN2I5NGQ5NDdlNmFjYWUzNzFjNmNiMTA0ZWEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYjU0OGI5YjZkMjJmNDE5NmEzMTBiYzRjYjg1NDIyOGEgPSAkKCc8ZGl2IGlkPSJodG1sX2I1NDhiOWI2ZDIyZjQxOTZhMzEwYmM0Y2I4NTQyMjhhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5HcmVlbnBvaW50LCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOWVkODMxN2I5NGQ5NDdlNmFjYWUzNzFjNmNiMTA0ZWEuc2V0Q29udGVudChodG1sX2I1NDhiOWI2ZDIyZjQxOTZhMzEwYmM0Y2I4NTQyMjhhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzk1ZDkxNWEyOWIzODQyMzNiMzI2ZTk3ZWNmZmQ2MjhkLmJpbmRQb3B1cChwb3B1cF85ZWQ4MzE3Yjk0ZDk0N2U2YWNhZTM3MWM2Y2IxMDRlYSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80MjAwZDhkNzMwMWU0YzkxYmRiYjI3OThiYzc4MjQ0OSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU5NTI2MDAxMzA2NTkzLC03My45NzM0NzA4NzcwODQ0NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80NzFjYjBhNmZiMDY0OGU0ODQ4ZmRhNTAzNDhhMjM0MCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84YmNiZWE1NTUzM2Q0YmM0ODI0ZWU3MTNmODYxNTc5NiA9ICQoJzxkaXYgaWQ9Imh0bWxfOGJjYmVhNTU1MzNkNGJjNDgyNGVlNzEzZjg2MTU3OTYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkdyYXZlc2VuZCwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzQ3MWNiMGE2ZmIwNjQ4ZTQ4NDhmZGE1MDM0OGEyMzQwLnNldENvbnRlbnQoaHRtbF84YmNiZWE1NTUzM2Q0YmM0ODI0ZWU3MTNmODYxNTc5Nik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80MjAwZDhkNzMwMWU0YzkxYmRiYjI3OThiYzc4MjQ0OS5iaW5kUG9wdXAocG9wdXBfNDcxY2IwYTZmYjA2NDhlNDg0OGZkYTUwMzQ4YTIzNDApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZmYwYmFjYzk2NDM5NGVlNGFlNDY0NmMwOTk1ODlkZDMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NzY4MjUwNjU2NjYwNCwtNzMuOTY1MDk0NDg3ODUzMzZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNzEyMjZlYTU5YWM0NDYzMWFkYzBhZWVhMTZlYzBjZDkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzM5Nzk5Y2I2MzNmNDdmNWE5NzE2ZmM0YmJmOWVmYmYgPSAkKCc8ZGl2IGlkPSJodG1sXzczOTc5OWNiNjMzZjQ3ZjVhOTcxNmZjNGJiZjllZmJmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CcmlnaHRvbiBCZWFjaCwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzcxMjI2ZWE1OWFjNDQ2MzFhZGMwYWVlYTE2ZWMwY2Q5LnNldENvbnRlbnQoaHRtbF83Mzk3OTljYjYzM2Y0N2Y1YTk3MTZmYzRiYmY5ZWZiZik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mZjBiYWNjOTY0Mzk0ZWU0YWU0NjQ2YzA5OTU4OWRkMy5iaW5kUG9wdXAocG9wdXBfNzEyMjZlYTU5YWM0NDYzMWFkYzBhZWVhMTZlYzBjZDkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNzgyMzI3YWQ2MjhmNGU4NGI4NmRhYmZiYzljODljOTYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41ODY4OTAxMjY3ODM4NCwtNzMuOTQzMTg2NDA0ODI5NzldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMGEwMDY2MDUyNmQyNDM0ZGJhZjljMjQwNmY3ZWRlZDYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNWE3M2Q1NWZlYjYyNDYyNjg4N2U0YTVlN2Q2YTY0YTIgPSAkKCc8ZGl2IGlkPSJodG1sXzVhNzNkNTVmZWI2MjQ2MjY4ODdlNGE1ZTdkNmE2NGEyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TaGVlcHNoZWFkIEJheSwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzBhMDA2NjA1MjZkMjQzNGRiYWY5YzI0MDZmN2VkZWQ2LnNldENvbnRlbnQoaHRtbF81YTczZDU1ZmViNjI0NjI2ODg3ZTRhNWU3ZDZhNjRhMik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83ODIzMjdhZDYyOGY0ZTg0Yjg2ZGFiZmJjOWM4OWM5Ni5iaW5kUG9wdXAocG9wdXBfMGEwMDY2MDUyNmQyNDM0ZGJhZjljMjQwNmY3ZWRlZDYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZWJjYTU3ZTFkYmMwNDcyODhkYTgwY2U4NGY5NTIxOTIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MTQ0MzI1MTMzNTA5OCwtNzMuOTU3NDM4NDA1NTk5MzldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfN2VkNWFiYmRiMjE4NDczOGFhMjk2ZWM0NDU2ZWE4MzcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOGE1OGMxZGNmZTk4NDIzYThhNWZhZTJhNzg0YTJmYjcgPSAkKCc8ZGl2IGlkPSJodG1sXzhhNThjMWRjZmU5ODQyM2E4YTVmYWUyYTc4NGEyZmI3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NYW5oYXR0YW4gVGVycmFjZSwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzdlZDVhYmJkYjIxODQ3MzhhYTI5NmVjNDQ1NmVhODM3LnNldENvbnRlbnQoaHRtbF84YTU4YzFkY2ZlOTg0MjNhOGE1ZmFlMmE3ODRhMmZiNyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lYmNhNTdlMWRiYzA0NzI4OGRhODBjZTg0Zjk1MjE5Mi5iaW5kUG9wdXAocG9wdXBfN2VkNWFiYmRiMjE4NDczOGFhMjk2ZWM0NDU2ZWE4MzcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzk4ODhhNTNhNTJlNGMzOGIyOWI4YzEzNGVhZTkyNDkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MzYzMjU4OTAyNjY3NywtNzMuOTU4NDAxMDY1MzM5MDNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMWRmNGZlMDUzYjc1NDg0ODgzY2EwNzRhN2MyMTQ2MmQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNGI5MGM5MTJhZTUzNDk5ZGJiZDUzOTRiNjAxYzA3NTAgPSAkKCc8ZGl2IGlkPSJodG1sXzRiOTBjOTEyYWU1MzQ5OWRiYmQ1Mzk0YjYwMWMwNzUwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5GbGF0YnVzaCwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzFkZjRmZTA1M2I3NTQ4NDg4M2NhMDc0YTdjMjE0NjJkLnNldENvbnRlbnQoaHRtbF80YjkwYzkxMmFlNTM0OTlkYmJkNTM5NGI2MDFjMDc1MCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jOTg4OGE1M2E1MmU0YzM4YjI5YjhjMTM0ZWFlOTI0OS5iaW5kUG9wdXAocG9wdXBfMWRmNGZlMDUzYjc1NDg0ODgzY2EwNzRhN2MyMTQ2MmQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNjY3ZGQwYThkNjcxNDllZWE4ODhmOTg0ODU0ZWQ5ZmEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42NzA4MjkxNzY5NTI5NCwtNzMuOTQzMjkxMTkwNzM1ODJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYjg4YTlkMmZjZGY0NGM1Yzk1MmIxOTY5ZTNlMjJmMmUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMTk2OTRhNDNmNTlkNGNkN2E1ZWYxNTg3NzRhNzk1MmUgPSAkKCc8ZGl2IGlkPSJodG1sXzE5Njk0YTQzZjU5ZDRjZDdhNWVmMTU4Nzc0YTc5NTJlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Dcm93biBIZWlnaHRzLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjg4YTlkMmZjZGY0NGM1Yzk1MmIxOTY5ZTNlMjJmMmUuc2V0Q29udGVudChodG1sXzE5Njk0YTQzZjU5ZDRjZDdhNWVmMTU4Nzc0YTc5NTJlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzY2N2RkMGE4ZDY3MTQ5ZWVhODg4Zjk4NDg1NGVkOWZhLmJpbmRQb3B1cChwb3B1cF9iODhhOWQyZmNkZjQ0YzVjOTUyYjE5NjllM2UyMmYyZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wM2YxZmJlNjYzMjI0YTI0OGJlMTkwNWI5MjNmZDcyOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY0MTcxNzc2NjY4OTYxLC03My45MzYxMDI1NjE4NTgzNl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yODAzZGJiNjgyOTU0NTA5YjU0ZjkxNDAyZTU1M2Q1YyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82OGY2MjIyYmYxNzM0M2VjYjExOGE0MDVmMTFmYjYxZCA9ICQoJzxkaXYgaWQ9Imh0bWxfNjhmNjIyMmJmMTczNDNlY2IxMThhNDA1ZjExZmI2MWQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVhc3QgRmxhdGJ1c2gsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yODAzZGJiNjgyOTU0NTA5YjU0ZjkxNDAyZTU1M2Q1Yy5zZXRDb250ZW50KGh0bWxfNjhmNjIyMmJmMTczNDNlY2IxMThhNDA1ZjExZmI2MWQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMDNmMWZiZTY2MzIyNGEyNDhiZTE5MDViOTIzZmQ3MjguYmluZFBvcHVwKHBvcHVwXzI4MDNkYmI2ODI5NTQ1MDliNTRmOTE0MDJlNTUzZDVjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2FjNDQ1MGFjZmJjMjRmNDBhYTM1ZDRhM2U5YWIzNTgzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjQyMzgxOTU4MDAzNTI2LC03My45ODA0MjExMDU1OTQ3NF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zZmYyMmFiMTUwN2I0OTYxYjhmYzM5YTJlZTAyMjcyYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80NjcxYjU4YjJkNGE0YmQ5YjhhNmQ0MWU5YTBhZTQyMSA9ICQoJzxkaXYgaWQ9Imh0bWxfNDY3MWI1OGIyZDRhNGJkOWI4YTZkNDFlOWEwYWU0MjEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPktlbnNpbmd0b24sIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zZmYyMmFiMTUwN2I0OTYxYjhmYzM5YTJlZTAyMjcyYS5zZXRDb250ZW50KGh0bWxfNDY3MWI1OGIyZDRhNGJkOWI4YTZkNDFlOWEwYWU0MjEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYWM0NDUwYWNmYmMyNGY0MGFhMzVkNGEzZTlhYjM1ODMuYmluZFBvcHVwKHBvcHVwXzNmZjIyYWIxNTA3YjQ5NjFiOGZjMzlhMmVlMDIyNzJhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzk4MWJiNDQ0MTM3NjRiZGFhYTU0MjQwZTI2Nzk0YTFkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjU2OTQ1ODM1NzUxMDQsLTczLjk4MDA3MzQwNDMwMTcyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzIxMTdkNmQ4YTY4YjQ3ZDRhZjJmMmQ1NWVkNDBmN2QyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzI5YmM4MjhmNTFjZjQ0ODViOGIxNGZlYTEzOTAwN2VjID0gJCgnPGRpdiBpZD0iaHRtbF8yOWJjODI4ZjUxY2Y0NDg1YjhiMTRmZWExMzkwMDdlYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V2luZHNvciBUZXJyYWNlLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMjExN2Q2ZDhhNjhiNDdkNGFmMmYyZDU1ZWQ0MGY3ZDIuc2V0Q29udGVudChodG1sXzI5YmM4MjhmNTFjZjQ0ODViOGIxNGZlYTEzOTAwN2VjKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzk4MWJiNDQ0MTM3NjRiZGFhYTU0MjQwZTI2Nzk0YTFkLmJpbmRQb3B1cChwb3B1cF8yMTE3ZDZkOGE2OGI0N2Q0YWYyZjJkNTVlZDQwZjdkMik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80ZjA3Mzk4NThkZTQ0M2VhODgxZTg5YjBmYWQ2YjcwOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY3NjgyMjI2MjI1NDcyNCwtNzMuOTY0ODU5MjQyNjI2OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yODIwZGQ0Y2RiYzE0ZGFkYjRmYjIwNjY5ODE3MDI2ZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81NDVjN2Q5NTQxMWM0YjU0OWI5MmJjMjMwMDkzNmE2ZSA9ICQoJzxkaXYgaWQ9Imh0bWxfNTQ1YzdkOTU0MTFjNGI1NDliOTJiYzIzMDA5MzZhNmUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlByb3NwZWN0IEhlaWdodHMsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yODIwZGQ0Y2RiYzE0ZGFkYjRmYjIwNjY5ODE3MDI2ZC5zZXRDb250ZW50KGh0bWxfNTQ1YzdkOTU0MTFjNGI1NDliOTJiYzIzMDA5MzZhNmUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNGYwNzM5ODU4ZGU0NDNlYTg4MWU4OWIwZmFkNmI3MDguYmluZFBvcHVwKHBvcHVwXzI4MjBkZDRjZGJjMTRkYWRiNGZiMjA2Njk4MTcwMjZkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzdhMmVhOWM3YWQ4ZTQxNmViZDdkYTkyY2IyZTRhZDkwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjYzOTQ5OTQzMzk3NTUsLTczLjkxMDIzNTM2MTc2NjA3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzY4MjI1MDNjNzYyNjQzMDM4ZjRiMWNjNjljYzc4NTg3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzU3ZTUzYjFlOWRiNzRkYzc5ZjJkYzcyZWJjNWI0ZTMwID0gJCgnPGRpdiBpZD0iaHRtbF81N2U1M2IxZTlkYjc0ZGM3OWYyZGM3MmViYzViNGUzMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QnJvd25zdmlsbGUsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82ODIyNTAzYzc2MjY0MzAzOGY0YjFjYzY5Y2M3ODU4Ny5zZXRDb250ZW50KGh0bWxfNTdlNTNiMWU5ZGI3NGRjNzlmMmRjNzJlYmM1YjRlMzApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfN2EyZWE5YzdhZDhlNDE2ZWJkN2RhOTJjYjJlNGFkOTAuYmluZFBvcHVwKHBvcHVwXzY4MjI1MDNjNzYyNjQzMDM4ZjRiMWNjNjljYzc4NTg3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzhiMmQ5MmY1NDk4ZDRmYjJiMzhkNmI0YzFjOGFmZjFmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzA3MTQ0MzkzNDQyNTEsLTczLjk1ODExNTI5MjIwOTI3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2E1YTRiZjU1NTYzNDRhYzE5NTg3ZDRhNWNmNzIwMTliID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2NkMTFjNWM0MzJhNzQ4NDFiMjgzMjE1MjAzMzM5YTM2ID0gJCgnPGRpdiBpZD0iaHRtbF9jZDExYzVjNDMyYTc0ODQxYjI4MzIxNTIwMzMzOWEzNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V2lsbGlhbXNidXJnLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTVhNGJmNTU1NjM0NGFjMTk1ODdkNGE1Y2Y3MjAxOWIuc2V0Q29udGVudChodG1sX2NkMTFjNWM0MzJhNzQ4NDFiMjgzMjE1MjAzMzM5YTM2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzhiMmQ5MmY1NDk4ZDRmYjJiMzhkNmI0YzFjOGFmZjFmLmJpbmRQb3B1cChwb3B1cF9hNWE0YmY1NTU2MzQ0YWMxOTU4N2Q0YTVjZjcyMDE5Yik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83NzIxMjE2Y2QyZTA0M2Q1YmUxOTU4MzA1YWE2ODdjMyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY5ODExNjExMDE3OTAxLC03My45MjUyNTc5NzQ4NzA0NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hNGJjZGM4YzRiYzA0Y2RiYWY4MmEwZDdjMTUwYjM4ZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83NmRiNDgzOWEyNDk0NzVmYmIzMmJhMTNmOTNhYzA1MiA9ICQoJzxkaXYgaWQ9Imh0bWxfNzZkYjQ4MzlhMjQ5NDc1ZmJiMzJiYTEzZjkzYWMwNTIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJ1c2h3aWNrLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTRiY2RjOGM0YmMwNGNkYmFmODJhMGQ3YzE1MGIzOGYuc2V0Q29udGVudChodG1sXzc2ZGI0ODM5YTI0OTQ3NWZiYjMyYmExM2Y5M2FjMDUyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzc3MjEyMTZjZDJlMDQzZDViZTE5NTgzMDVhYTY4N2MzLmJpbmRQb3B1cChwb3B1cF9hNGJjZGM4YzRiYzA0Y2RiYWY4MmEwZDdjMTUwYjM4Zik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82ZTBjMDFjNGQyNWQ0Y2IyYTQ5NjJiNzEwZmQwOTk5MSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY4NzIzMTYwNzcyMDQ1NiwtNzMuOTQxNzg0ODg2OTAyOTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWMwYTZlYjg2YjJmNDRiYzkyMzI4MWI5Y2FjYzMzYjAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMWU1MmFkMWU5YzM1NGRiZWI5YTU4OWJmMGM1MTc4M2YgPSAkKCc8ZGl2IGlkPSJodG1sXzFlNTJhZDFlOWMzNTRkYmViOWE1ODliZjBjNTE3ODNmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CZWRmb3JkIFN0dXl2ZXNhbnQsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hYzBhNmViODZiMmY0NGJjOTIzMjgxYjljYWNjMzNiMC5zZXRDb250ZW50KGh0bWxfMWU1MmFkMWU5YzM1NGRiZWI5YTU4OWJmMGM1MTc4M2YpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNmUwYzAxYzRkMjVkNGNiMmE0OTYyYjcxMGZkMDk5OTEuYmluZFBvcHVwKHBvcHVwX2FjMGE2ZWI4NmIyZjQ0YmM5MjMyODFiOWNhY2MzM2IwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzgzNjM4YzI1MzZjMzQ2OTJiY2QyNGU4ZTIzYzE4NWU4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjk1ODYzNzIyNzI0MDg0LC03My45OTM3ODIyNTQ5NjQyNF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85MzQ1NDMyNzNjZTk0MTRhYTU5YjFkMWYzYWFkZGRlMiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lYmY1NTIzYWM5OGE0NjkzOGYyMTNmMjI1YzgxYWYwNiA9ICQoJzxkaXYgaWQ9Imh0bWxfZWJmNTUyM2FjOThhNDY5MzhmMjEzZjIyNWM4MWFmMDYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJyb29rbHluIEhlaWdodHMsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85MzQ1NDMyNzNjZTk0MTRhYTU5YjFkMWYzYWFkZGRlMi5zZXRDb250ZW50KGh0bWxfZWJmNTUyM2FjOThhNDY5MzhmMjEzZjIyNWM4MWFmMDYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfODM2MzhjMjUzNmMzNDY5MmJjZDI0ZThlMjNjMTg1ZTguYmluZFBvcHVwKHBvcHVwXzkzNDU0MzI3M2NlOTQxNGFhNTliMWQxZjNhYWRkZGUyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzViMjljNDU3YzBlYTRiNTBiNDA5ZTczNDQ3ZDQ2ZDQwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjg3OTE5NzIyNDg1NTc0LC03My45OTg1NjEzOTIxODQ2M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85OWQxMDQ1MTE0NmY0NzViYjc5ZjRhYjUzZWU1NWJmZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84MmI1NWI3NThhNzM0ZjdmYmU5ZGRkYzVkZDBlYjY3NyA9ICQoJzxkaXYgaWQ9Imh0bWxfODJiNTViNzU4YTczNGY3ZmJlOWRkZGM1ZGQwZWI2NzciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNvYmJsZSBIaWxsLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOTlkMTA0NTExNDZmNDc1YmI3OWY0YWI1M2VlNTViZmYuc2V0Q29udGVudChodG1sXzgyYjU1Yjc1OGE3MzRmN2ZiZTlkZGRjNWRkMGViNjc3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzViMjljNDU3YzBlYTRiNTBiNDA5ZTczNDQ3ZDQ2ZDQwLmJpbmRQb3B1cChwb3B1cF85OWQxMDQ1MTE0NmY0NzViYjc5ZjRhYjUzZWU1NWJmZik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84ZjdhMmU5NDVmZTc0ZDIyOTE5NWEyNzE5NjE4MGZjZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY4MDU0MDIzMTA3NjQ4NSwtNzMuOTk0NjUzNzI4MjgwMDZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjU0ODE1YTFkYTRhNDA1NzlmNjE4YmIwYTliYWU0ODUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMTU4YTZhNGFmY2UyNGU0ZWJmNmZkMWE0ZGY5YTNjMzUgPSAkKCc8ZGl2IGlkPSJodG1sXzE1OGE2YTRhZmNlMjRlNGViZjZmZDFhNGRmOWEzYzM1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DYXJyb2xsIEdhcmRlbnMsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mNTQ4MTVhMWRhNGE0MDU3OWY2MThiYjBhOWJhZTQ4NS5zZXRDb250ZW50KGh0bWxfMTU4YTZhNGFmY2UyNGU0ZWJmNmZkMWE0ZGY5YTNjMzUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOGY3YTJlOTQ1ZmU3NGQyMjkxOTVhMjcxOTYxODBmY2UuYmluZFBvcHVwKHBvcHVwX2Y1NDgxNWExZGE0YTQwNTc5ZjYxOGJiMGE5YmFlNDg1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2UzNGQ4NjEwMDNmMzRjZmI5MDIyNTIzYjZhMGFlNzliID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjc2MjUzMjMwMjUwODg2LC03NC4wMTI3NTg5NzQ3MzU2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzIxNmU1YzFjNTAxNjQzMzM5MWU4MTQwNWRhMzg1MzMxID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzc0YjI2YjJiYWU3ZjQ3MjU5Yjk0Y2VhYmY1NGMzMzA1ID0gJCgnPGRpdiBpZD0iaHRtbF83NGIyNmIyYmFlN2Y0NzI1OWI5NGNlYWJmNTRjMzMwNSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UmVkIEhvb2ssIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yMTZlNWMxYzUwMTY0MzMzOTFlODE0MDVkYTM4NTMzMS5zZXRDb250ZW50KGh0bWxfNzRiMjZiMmJhZTdmNDcyNTliOTRjZWFiZjU0YzMzMDUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZTM0ZDg2MTAwM2YzNGNmYjkwMjI1MjNiNmEwYWU3OWIuYmluZFBvcHVwKHBvcHVwXzIxNmU1YzFjNTAxNjQzMzM5MWU4MTQwNWRhMzg1MzMxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzc4ZGZlMmFmYTQ4OTRhMzg4OTFiMzJjNTYxNjZmNWFkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjczOTMxMTQzMTg3MTU0LC03My45OTQ0NDA4NzE0NTMzOV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yN2UzMDMyMTY5ZWU0Y2E2YWY3N2U0NWUwODYxMWI2YiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mOGE0MDlmNGQ1MDg0YmZiOTM1NzZkMmViYzQzZmY2ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfZjhhNDA5ZjRkNTA4NGJmYjkzNTc2ZDJlYmM0M2ZmNmYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkdvd2FudXMsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yN2UzMDMyMTY5ZWU0Y2E2YWY3N2U0NWUwODYxMWI2Yi5zZXRDb250ZW50KGh0bWxfZjhhNDA5ZjRkNTA4NGJmYjkzNTc2ZDJlYmM0M2ZmNmYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNzhkZmUyYWZhNDg5NGEzODg5MWIzMmM1NjE2NmY1YWQuYmluZFBvcHVwKHBvcHVwXzI3ZTMwMzIxNjllZTRjYTZhZjc3ZTQ1ZTA4NjExYjZiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzgyYTFhYTk4YTg0YzRkNGJhYzM0ZTM3Mzk5MTU2MDMzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjg4NTI3MjYwMTg5NzcsLTczLjk3MjkwNTc0MzY5MDkyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2ZkN2UwZTM3OWFkNzQxODFiY2VjMjliZTk1MjYwMzRlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzM2NTg1M2VhZTJjNDQ4OTk5NmE2YjQwNjdlYjA4Zjk3ID0gJCgnPGRpdiBpZD0iaHRtbF8zNjU4NTNlYWUyYzQ0ODk5OTZhNmI0MDY3ZWIwOGY5NyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Rm9ydCBHcmVlbmUsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mZDdlMGUzNzlhZDc0MTgxYmNlYzI5YmU5NTI2MDM0ZS5zZXRDb250ZW50KGh0bWxfMzY1ODUzZWFlMmM0NDg5OTk2YTZiNDA2N2ViMDhmOTcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfODJhMWFhOThhODRjNGQ0YmFjMzRlMzczOTkxNTYwMzMuYmluZFBvcHVwKHBvcHVwX2ZkN2UwZTM3OWFkNzQxODFiY2VjMjliZTk1MjYwMzRlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzFjZWE2NmY3OGNhMjQ2YzY4NzE3MjQyMDlhMGVlN2VjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjcyMzIwNTIyNjgxOTcsLTczLjk3NzA1MDMwMTgzOTI0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2U3NjU0OTNjMjUyYzQyMzZiZjdiNmI1OGU3OWZiZTMwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzAwMmUxODhmOTEyMDRiMGU4ZDNlNzE5ZjU0NjYzM2UzID0gJCgnPGRpdiBpZD0iaHRtbF8wMDJlMTg4ZjkxMjA0YjBlOGQzZTcxOWY1NDY2MzNlMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UGFyayBTbG9wZSwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2U3NjU0OTNjMjUyYzQyMzZiZjdiNmI1OGU3OWZiZTMwLnNldENvbnRlbnQoaHRtbF8wMDJlMTg4ZjkxMjA0YjBlOGQzZTcxOWY1NDY2MzNlMyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xY2VhNjZmNzhjYTI0NmM2ODcxNzI0MjA5YTBlZTdlYy5iaW5kUG9wdXAocG9wdXBfZTc2NTQ5M2MyNTJjNDIzNmJmN2I2YjU4ZTc5ZmJlMzApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNzNkN2E0MTY5ZWIwNGE5M2I3NjNhMGRhNjE0YmM2YTEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42ODIzOTEwMTE0NDIxMSwtNzMuODc2NjE1OTY0NTcyOTZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNDFiMGY0Nzk2NDg5NDQ0MWE3OTU0NDM2YjViY2I4MDMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMTI2NjhhZjgyMDczNDQ0Y2FiZTU3Nzk0ZDE2OTQ4NDIgPSAkKCc8ZGl2IGlkPSJodG1sXzEyNjY4YWY4MjA3MzQ0NGNhYmU1Nzc5NGQxNjk0ODQyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DeXByZXNzIEhpbGxzLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNDFiMGY0Nzk2NDg5NDQ0MWE3OTU0NDM2YjViY2I4MDMuc2V0Q29udGVudChodG1sXzEyNjY4YWY4MjA3MzQ0NGNhYmU1Nzc5NGQxNjk0ODQyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzczZDdhNDE2OWViMDRhOTNiNzYzYTBkYTYxNGJjNmExLmJpbmRQb3B1cChwb3B1cF80MWIwZjQ3OTY0ODk0NDQxYTc5NTQ0MzZiNWJjYjgwMyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82NzhkNGNhMDZhZmY0M2U5YmE5OTA3MWJiYjMzMWJmYSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY2OTkyNTcwMDg0NzA0NSwtNzMuODgwNjk4NjM5MTczNjZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZGQ2NzIzODhiMTM0NDk2MGFlYWJkNTIzNjRkZjgyMDcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYjExMDI5NDQ3NmM4NGY3NmJmNjZhMjlmNDQ5ZTFlNjggPSAkKCc8ZGl2IGlkPSJodG1sX2IxMTAyOTQ0NzZjODRmNzZiZjY2YTI5ZjQ0OWUxZTY4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5FYXN0IE5ldyBZb3JrLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZGQ2NzIzODhiMTM0NDk2MGFlYWJkNTIzNjRkZjgyMDcuc2V0Q29udGVudChodG1sX2IxMTAyOTQ0NzZjODRmNzZiZjY2YTI5ZjQ0OWUxZTY4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzY3OGQ0Y2EwNmFmZjQzZTliYTk5MDcxYmJiMzMxYmZhLmJpbmRQb3B1cChwb3B1cF9kZDY3MjM4OGIxMzQ0OTYwYWVhYmQ1MjM2NGRmODIwNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zMzllOWNiMTI2NmU0MzRmYjA4ZDdmN2RmNWNhYWJkZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY0NzU4OTA1MjMwODc0LC03My44NzkzNjk3MDA0NTg3NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82NTVkM2I4MTBjODE0NGVkODBmMjU3YTAzZjA3MmZiMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85NWU3ZDA1ZmEzMmU0MTYxYTgzNjJlYjNiYzNmYTY5ZSA9ICQoJzxkaXYgaWQ9Imh0bWxfOTVlN2QwNWZhMzJlNDE2MWE4MzYyZWIzYmMzZmE2OWUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlN0YXJyZXR0IENpdHksIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82NTVkM2I4MTBjODE0NGVkODBmMjU3YTAzZjA3MmZiMS5zZXRDb250ZW50KGh0bWxfOTVlN2QwNWZhMzJlNDE2MWE4MzYyZWIzYmMzZmE2OWUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMzM5ZTljYjEyNjZlNDM0ZmIwOGQ3ZjdkZjVjYWFiZGQuYmluZFBvcHVwKHBvcHVwXzY1NWQzYjgxMGM4MTQ0ZWQ4MGYyNTdhMDNmMDcyZmIxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2RjMmE2MTM5YjU2NTQ0YjU4OTBiZjIyMWNlNzg3NGMzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjM1NTY0MzI3OTc0MjgsLTczLjkwMjA5MjY5Nzc4OTY2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2MxMDBjNmE4MWE2NjQ4ZTliYjAwYmRiN2RhYzU4Y2UxID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzUwYjBjYTU4YmQ2MDQ0MjA5MjY3YTdiZTA2ZGI1YzE2ID0gJCgnPGRpdiBpZD0iaHRtbF81MGIwY2E1OGJkNjA0NDIwOTI2N2E3YmUwNmRiNWMxNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2FuYXJzaWUsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jMTAwYzZhODFhNjY0OGU5YmIwMGJkYjdkYWM1OGNlMS5zZXRDb250ZW50KGh0bWxfNTBiMGNhNThiZDYwNDQyMDkyNjdhN2JlMDZkYjVjMTYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZGMyYTYxMzliNTY1NDRiNTg5MGJmMjIxY2U3ODc0YzMuYmluZFBvcHVwKHBvcHVwX2MxMDBjNmE4MWE2NjQ4ZTliYjAwYmRiN2RhYzU4Y2UxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzgyZjU5MzQ1Y2QwMTQ3ZDBhZjMyNzhmMjBkMGVkNzcyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjMwNDQ2MDQzNzU3NDY2LC03My45MjkxMTMwMjY0NDY3NF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84ZGFkMjgyNzllODA0ZjAzYTJmMWVlYmExMDJjNjNkNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kNDQxOGE0ZjJkM2Y0MWYxOTczNjg2ZjM2YWFlZjE0NyA9ICQoJzxkaXYgaWQ9Imh0bWxfZDQ0MThhNGYyZDNmNDFmMTk3MzY4NmYzNmFhZWYxNDciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZsYXRsYW5kcywgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzhkYWQyODI3OWU4MDRmMDNhMmYxZWViYTEwMmM2M2Q3LnNldENvbnRlbnQoaHRtbF9kNDQxOGE0ZjJkM2Y0MWYxOTczNjg2ZjM2YWFlZjE0Nyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84MmY1OTM0NWNkMDE0N2QwYWYzMjc4ZjIwZDBlZDc3Mi5iaW5kUG9wdXAocG9wdXBfOGRhZDI4Mjc5ZTgwNGYwM2EyZjFlZWJhMTAyYzYzZDcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNjc2M2FjOWIxZjdhNDQyMTk4MmUwZTQ0N2E5M2NlNmMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MDYzMzY0MjE2ODU2MjYsLTczLjkwODE4NTcxNzc3NDIzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzMyOTBmY2M4YTVhMTQ4NDI5OGFjYjg2NDRlNDNlYTFlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzU1YTNiNzZmMTY1YzRiYWM4MzZhNTJkMDJmNWUzN2MxID0gJCgnPGRpdiBpZD0iaHRtbF81NWEzYjc2ZjE2NWM0YmFjODM2YTUyZDAyZjVlMzdjMSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TWlsbCBJc2xhbmQsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zMjkwZmNjOGE1YTE0ODQyOThhY2I4NjQ0ZTQzZWExZS5zZXRDb250ZW50KGh0bWxfNTVhM2I3NmYxNjVjNGJhYzgzNmE1MmQwMmY1ZTM3YzEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNjc2M2FjOWIxZjdhNDQyMTk4MmUwZTQ0N2E5M2NlNmMuYmluZFBvcHVwKHBvcHVwXzMyOTBmY2M4YTVhMTQ4NDI5OGFjYjg2NDRlNDNlYTFlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2IxNGRmZDljNjU5YzRiM2I5ZTM3NzI3ZjEwNWNmNDcyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTc3OTEzNTAzMDg2NTcsLTczLjk0MzUzNzIyODkxODg2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzc3YzI5YmNlYWYxNzQ0ZDA5MjAyMDNiYzlmNTk1ZWViID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzNkZjA2MjUyYTRmNTQyMjA5YWMyYWE3M2E5YjkzNjM0ID0gJCgnPGRpdiBpZD0iaHRtbF8zZGYwNjI1MmE0ZjU0MjIwOWFjMmFhNzNhOWI5MzYzNCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TWFuaGF0dGFuIEJlYWNoLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNzdjMjliY2VhZjE3NDRkMDkyMDIwM2JjOWY1OTVlZWIuc2V0Q29udGVudChodG1sXzNkZjA2MjUyYTRmNTQyMjA5YWMyYWE3M2E5YjkzNjM0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2IxNGRmZDljNjU5YzRiM2I5ZTM3NzI3ZjEwNWNmNDcyLmJpbmRQb3B1cChwb3B1cF83N2MyOWJjZWFmMTc0NGQwOTIwMjAzYmM5ZjU5NWVlYik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80NDIyZjA0NmJkZjA0Y2M1YTBlODMwYzg5YmIwMTkzZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU3NDI5MjU2NDcxNjAxLC03My45ODg2ODI5NTgyMTYzN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85NGFkZDZjZjBhZTA0Y2E3YjUzMjA0MmE2MjkxMmZjMiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84YTgxZGYzZWY4YzA0ZGMyYmE3NmMxMjZlZjY3NGJmMCA9ICQoJzxkaXYgaWQ9Imh0bWxfOGE4MWRmM2VmOGMwNGRjMmJhNzZjMTI2ZWY2NzRiZjAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNvbmV5IElzbGFuZCwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzk0YWRkNmNmMGFlMDRjYTdiNTMyMDQyYTYyOTEyZmMyLnNldENvbnRlbnQoaHRtbF84YTgxZGYzZWY4YzA0ZGMyYmE3NmMxMjZlZjY3NGJmMCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80NDIyZjA0NmJkZjA0Y2M1YTBlODMwYzg5YmIwMTkzZS5iaW5kUG9wdXAocG9wdXBfOTRhZGQ2Y2YwYWUwNGNhN2I1MzIwNDJhNjI5MTJmYzIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMTRiMDZmMjE0NzZmNDUxNThlZDg1OGY5ZmE4NmYxNzIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41OTk1MTg3MDI4MjIzOCwtNzMuOTk4NzUyMjE0NDM1MTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNmFjMDE0NjdhMmVmNDM5ZTg2MWQyYWQ3ZDRiMjE2YWUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMTA1Y2EyYmVhNGJhNDBlMzg4MDlhMzI0ODBlNzU5NTkgPSAkKCc8ZGl2IGlkPSJodG1sXzEwNWNhMmJlYTRiYTQwZTM4ODA5YTMyNDgwZTc1OTU5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CYXRoIEJlYWNoLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNmFjMDE0NjdhMmVmNDM5ZTg2MWQyYWQ3ZDRiMjE2YWUuc2V0Q29udGVudChodG1sXzEwNWNhMmJlYTRiYTQwZTM4ODA5YTMyNDgwZTc1OTU5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzE0YjA2ZjIxNDc2ZjQ1MTU4ZWQ4NThmOWZhODZmMTcyLmJpbmRQb3B1cChwb3B1cF82YWMwMTQ2N2EyZWY0MzllODYxZDJhZDdkNGIyMTZhZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83MGJjNDMwZjY0YjI0M2Q5YTM2OGM2MzlkNTE1MTZjZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYzMzEzMDUxMjc1ODAxNSwtNzMuOTkwNDk4MjMwNDQ4MTFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODIxYjcwMGMwYjVhNGQwMTg0Njg0MjVmYWVjYzc4MWEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMGZhYTgwZGZkMmY4NGEzYjg2MmZlZjgxNWQxY2RkOTYgPSAkKCc8ZGl2IGlkPSJodG1sXzBmYWE4MGRmZDJmODRhM2I4NjJmZWY4MTVkMWNkZDk2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Cb3JvdWdoIFBhcmssIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84MjFiNzAwYzBiNWE0ZDAxODQ2ODQyNWZhZWNjNzgxYS5zZXRDb250ZW50KGh0bWxfMGZhYTgwZGZkMmY4NGEzYjg2MmZlZjgxNWQxY2RkOTYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNzBiYzQzMGY2NGIyNDNkOWEzNjhjNjM5ZDUxNTE2Y2QuYmluZFBvcHVwKHBvcHVwXzgyMWI3MDBjMGI1YTRkMDE4NDY4NDI1ZmFlY2M3ODFhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2E0Yzk5Zjc5MzQwNTRiZjBhODE5OWUwYWNlMjA2YTE2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjE5MjE5NDU3NzIyNjM2LC03NC4wMTkzMTM3NTYzNjAyMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zMjA1NDJhOWY5MjE0MTg0YTU0YWJiNWNiMjMzNjgyZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81ZDA2OTEyZDkzNjk0NGQxYjA5OWUxYjI0NWZmMzVjMSA9ICQoJzxkaXYgaWQ9Imh0bWxfNWQwNjkxMmQ5MzY5NDRkMWIwOTllMWIyNDVmZjM1YzEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkR5a2VyIEhlaWdodHMsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zMjA1NDJhOWY5MjE0MTg0YTU0YWJiNWNiMjMzNjgyZS5zZXRDb250ZW50KGh0bWxfNWQwNjkxMmQ5MzY5NDRkMWIwOTllMWIyNDVmZjM1YzEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYTRjOTlmNzkzNDA1NGJmMGE4MTk5ZTBhY2UyMDZhMTYuYmluZFBvcHVwKHBvcHVwXzMyMDU0MmE5ZjkyMTQxODRhNTRhYmI1Y2IyMzM2ODJlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzViM2RjOTIxMmEyNzQ4ZTA5NGY1ZGQyNTJhZWUzNDkwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTkwODQ4NDMzOTAyMDQ2LC03My45MzAxMDE3MDY5MTE5Nl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85YzBmYWI0OWQyNzQ0NTRlOGFmZTg4NjIyNWIwZDJjMiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mNDZjMzZjYmU5YmE0YjViOTQxNmY1ZjA4NzFjOTQ1MCA9ICQoJzxkaXYgaWQ9Imh0bWxfZjQ2YzM2Y2JlOWJhNGI1Yjk0MTZmNWYwODcxYzk0NTAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkdlcnJpdHNlbiBCZWFjaCwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzljMGZhYjQ5ZDI3NDQ1NGU4YWZlODg2MjI1YjBkMmMyLnNldENvbnRlbnQoaHRtbF9mNDZjMzZjYmU5YmE0YjViOTQxNmY1ZjA4NzFjOTQ1MCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81YjNkYzkyMTJhMjc0OGUwOTRmNWRkMjUyYWVlMzQ5MC5iaW5kUG9wdXAocG9wdXBfOWMwZmFiNDlkMjc0NDU0ZThhZmU4ODYyMjViMGQyYzIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDJjNWRhNmNiM2JkNDI3NGE4NmZkY2I4OTVmZTYwZTcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MDk3NDc3Nzk4OTQ2MDQsLTczLjkzMTM0NDA0MTA4NDk3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzQxN2E1MTk3OWVkZTQ1MmI4ZGUzMmIxZjk5OTIxMWI3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2QyODJiMDE2MTU2YzRiZmU4ZmUxZDcxZDYyNDdmYjg1ID0gJCgnPGRpdiBpZD0iaHRtbF9kMjgyYjAxNjE1NmM0YmZlOGZlMWQ3MWQ2MjQ3ZmI4NSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TWFyaW5lIFBhcmssIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80MTdhNTE5NzllZGU0NTJiOGRlMzJiMWY5OTkyMTFiNy5zZXRDb250ZW50KGh0bWxfZDI4MmIwMTYxNTZjNGJmZThmZTFkNzFkNjI0N2ZiODUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDJjNWRhNmNiM2JkNDI3NGE4NmZkY2I4OTVmZTYwZTcuYmluZFBvcHVwKHBvcHVwXzQxN2E1MTk3OWVkZTQ1MmI4ZGUzMmIxZjk5OTIxMWI3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzQzNGViNzg2ZmM5MjRhYzRiYmYwOWM3ZThlZTZmOTFjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjkzMjI5NDIxODgxNTA0LC03My45Njc4NDMwNjIxNjM2N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xYThkMmViYzFiMjQ0YWVhYjM5YjI4NzlmZmJkNmM2MiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84NzBjZDIzYzJjYjE0YzZkYjJmZjk0MWFlMTA4MWM5ZSA9ICQoJzxkaXYgaWQ9Imh0bWxfODcwY2QyM2MyY2IxNGM2ZGIyZmY5NDFhZTEwODFjOWUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNsaW50b24gSGlsbCwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzFhOGQyZWJjMWIyNDRhZWFiMzliMjg3OWZmYmQ2YzYyLnNldENvbnRlbnQoaHRtbF84NzBjZDIzYzJjYjE0YzZkYjJmZjk0MWFlMTA4MWM5ZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80MzRlYjc4NmZjOTI0YWM0YmJmMDljN2U4ZWU2ZjkxYy5iaW5kUG9wdXAocG9wdXBfMWE4ZDJlYmMxYjI0NGFlYWIzOWIyODc5ZmZiZDZjNjIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZWYzNDY1MDkzYmIyNDJiMjg1ZjViZTBjYjUyYjE1MTkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NzYzNzUzNzg5MDIyNCwtNzQuMDA3ODczMTEyMDAyNF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82MjY2OWE4NjQ3NzU0YWFmYmEyNGY5Zjc3MDI0NzVmOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jMTExMzNjZDgwYTA0MGE1OThhYjU1YzM0MzdjZjJkOSA9ICQoJzxkaXYgaWQ9Imh0bWxfYzExMTMzY2Q4MGEwNDBhNTk4YWI1NWMzNDM3Y2YyZDkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlNlYSBHYXRlLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNjI2NjlhODY0Nzc1NGFhZmJhMjRmOWY3NzAyNDc1Zjguc2V0Q29udGVudChodG1sX2MxMTEzM2NkODBhMDQwYTU5OGFiNTVjMzQzN2NmMmQ5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2VmMzQ2NTA5M2JiMjQyYjI4NWY1YmUwY2I1MmIxNTE5LmJpbmRQb3B1cChwb3B1cF82MjY2OWE4NjQ3NzU0YWFmYmEyNGY5Zjc3MDI0NzVmOCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xYjdlZTc2MTc4NzE0NTVmOGMxZDIzZGFkMTUzZDgwZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY5MDg0NDAyMTA5ODAyLC03My45ODM0NjMzNzQzMTA5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yYTFmNGE4NGEwOWQ0NWZkYTFkMjJlZGMwZWU0NGIyMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85NDA4YmFiNTRjYzc0ZTRlYmQ5OGY3NmQ5ZTRlNTY2NyA9ICQoJzxkaXYgaWQ9Imh0bWxfOTQwOGJhYjU0Y2M3NGU0ZWJkOThmNzZkOWU0ZTU2NjciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRvd250b3duLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMmExZjRhODRhMDlkNDVmZGExZDIyZWRjMGVlNDRiMjEuc2V0Q29udGVudChodG1sXzk0MDhiYWI1NGNjNzRlNGViZDk4Zjc2ZDllNGU1NjY3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzFiN2VlNzYxNzg3MTQ1NWY4YzFkMjNkYWQxNTNkODBmLmJpbmRQb3B1cChwb3B1cF8yYTFmNGE4NGEwOWQ0NWZkYTFkMjJlZGMwZWU0NGIyMSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85MzhjNDc4ZWNjZTk0MmQzYWY4YzJmYjBiODQ1ZTljNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY4NTY4MjkxMjA5MTQ0NCwtNzMuOTgzNzQ4MjQxMTU3OThdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMWExMGI1NmFlZGZkNDg1MjgwMzI2MjIzYTBiODBiMmIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYzU0NmJiOWFjMTAxNDE3ZDgwZTc4ODBiNTVhYTM3YjUgPSAkKCc8ZGl2IGlkPSJodG1sX2M1NDZiYjlhYzEwMTQxN2Q4MGU3ODgwYjU1YWEzN2I1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Cb2VydW0gSGlsbCwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzFhMTBiNTZhZWRmZDQ4NTI4MDMyNjIyM2EwYjgwYjJiLnNldENvbnRlbnQoaHRtbF9jNTQ2YmI5YWMxMDE0MTdkODBlNzg4MGI1NWFhMzdiNSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85MzhjNDc4ZWNjZTk0MmQzYWY4YzJmYjBiODQ1ZTljNC5iaW5kUG9wdXAocG9wdXBfMWExMGI1NmFlZGZkNDg1MjgwMzI2MjIzYTBiODBiMmIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYWY4ZDhmY2JmOWY2NDFlZDhjNWUxMDUyMTBjOTYyZjUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42NTg0MjAwMTc0Njk4MTUsLTczLjk1NDg5ODY3MDc3NzEzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzY1ZTU5ZDQzODhiZDRlMjBhMTcxY2U1NDIwODc5ZDE3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2YzNDA0YjNkMjIwNjQwMmQ4MmFjZjBlOTI4YzJhNTZmID0gJCgnPGRpdiBpZD0iaHRtbF9mMzQwNGIzZDIyMDY0MDJkODJhY2YwZTkyOGMyYTU2ZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UHJvc3BlY3QgTGVmZmVydHMgR2FyZGVucywgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzY1ZTU5ZDQzODhiZDRlMjBhMTcxY2U1NDIwODc5ZDE3LnNldENvbnRlbnQoaHRtbF9mMzQwNGIzZDIyMDY0MDJkODJhY2YwZTkyOGMyYTU2Zik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hZjhkOGZjYmY5ZjY0MWVkOGM1ZTEwNTIxMGM5NjJmNS5iaW5kUG9wdXAocG9wdXBfNjVlNTlkNDM4OGJkNGUyMGExNzFjZTU0MjA4NzlkMTcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNGUzYWU5ZThiMDk2NDQ3MWJlZmEyZDBiMTQ1ODlmMjUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42Nzg0MDI1NTQ3OTUzNTUsLTczLjkxMzA2ODMxNzg3Mzk1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzdlZWYyNWY3ZmU3OTRhODliZGIyMjY0MTI5MDVhZGU4ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzdmMzJjM2RlNzAxNzQ3NDk4ZjFkNTdmOTJjNzRmYzEzID0gJCgnPGRpdiBpZD0iaHRtbF83ZjMyYzNkZTcwMTc0NzQ5OGYxZDU3ZjkyYzc0ZmMxMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+T2NlYW4gSGlsbCwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzdlZWYyNWY3ZmU3OTRhODliZGIyMjY0MTI5MDVhZGU4LnNldENvbnRlbnQoaHRtbF83ZjMyYzNkZTcwMTc0NzQ5OGYxZDU3ZjkyYzc0ZmMxMyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80ZTNhZTllOGIwOTY0NDcxYmVmYTJkMGIxNDU4OWYyNS5iaW5kUG9wdXAocG9wdXBfN2VlZjI1ZjdmZTc5NGE4OWJkYjIyNjQxMjkwNWFkZTgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMTRkNmMxZGMwOWM4NDA4OTg1NGU5ZWMwMTAyMjcxMWYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42Nzg1Njk5NTcyNzQ3OSwtNzMuODY3OTc1OTgwODEzMzRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZWU0MTBjMTY2MTA4NDAxZjlmMGIwOWNiYWRiNDk1YjEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZWQ2MmZiMjE3ZDVlNDg2YjhiNDdlZDE0MzA4NDEzMDEgPSAkKCc8ZGl2IGlkPSJodG1sX2VkNjJmYjIxN2Q1ZTQ4NmI4YjQ3ZWQxNDMwODQxMzAxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DaXR5IExpbmUsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lZTQxMGMxNjYxMDg0MDFmOWYwYjA5Y2JhZGI0OTViMS5zZXRDb250ZW50KGh0bWxfZWQ2MmZiMjE3ZDVlNDg2YjhiNDdlZDE0MzA4NDEzMDEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMTRkNmMxZGMwOWM4NDA4OTg1NGU5ZWMwMTAyMjcxMWYuYmluZFBvcHVwKHBvcHVwX2VlNDEwYzE2NjEwODQwMWY5ZjBiMDljYmFkYjQ5NWIxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2UzMmVmNmMxNDNmNzQ3ZWM5MDM4NmJjNTNhMjA0NmNjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjE1MTQ5NTUwNDUzMDgsLTczLjg5ODU1NjMzNjMwMzE3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzA5ZGQyNDNiNjhlYjQwYjg5OTRmZDY5NGExZTIwMmIxID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2VlOTI2ZGQxNzRmZTQzMDg5NmM3Y2I5MTU3NjZlZjNlID0gJCgnPGRpdiBpZD0iaHRtbF9lZTkyNmRkMTc0ZmU0MzA4OTZjN2NiOTE1NzY2ZWYzZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmVyZ2VuIEJlYWNoLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMDlkZDI0M2I2OGViNDBiODk5NGZkNjk0YTFlMjAyYjEuc2V0Q29udGVudChodG1sX2VlOTI2ZGQxNzRmZTQzMDg5NmM3Y2I5MTU3NjZlZjNlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2UzMmVmNmMxNDNmNzQ3ZWM5MDM4NmJjNTNhMjA0NmNjLmJpbmRQb3B1cChwb3B1cF8wOWRkMjQzYjY4ZWI0MGI4OTk0ZmQ2OTRhMWUyMDJiMSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iYjM4ODJlNjQ5Y2M0ZjM0YTg2YmI4ZjBiNDIwNmU3ZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYyNTU5NTg5ODY5ODQzLC03My45NTc1OTUyMzQ4OTgzOF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84MjEzZDQ5MjE3NGU0NWI2OGYyNGZiYThjMDNkM2NmZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lNTBiZDNiMmI5Y2U0NjE4YWJkZTFmYjMyMDBiNmVkMCA9ICQoJzxkaXYgaWQ9Imh0bWxfZTUwYmQzYjJiOWNlNDYxOGFiZGUxZmIzMjAwYjZlZDAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk1pZHdvb2QsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84MjEzZDQ5MjE3NGU0NWI2OGYyNGZiYThjMDNkM2NmZS5zZXRDb250ZW50KGh0bWxfZTUwYmQzYjJiOWNlNDYxOGFiZGUxZmIzMjAwYjZlZDApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYmIzODgyZTY0OWNjNGYzNGE4NmJiOGYwYjQyMDZlN2YuYmluZFBvcHVwKHBvcHVwXzgyMTNkNDkyMTc0ZTQ1YjY4ZjI0ZmJhOGMwM2QzY2ZlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzc2OTI0ODc0YTc0YzRmZmY5OTc2NTFiNzUwNzQzYmRmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjQ3MDA4NjAzMTg1MTg1LC03My45NjI2MTMxNjcxNjA0OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yOWI3ZDBmMzQ3OWE0MmI3OWVhZTU4MDIzMGNkNTRhNiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xNDA4ZDkzZmY3YTY0NDQzYTg0Y2M2NThlNjExMzIyYSA9ICQoJzxkaXYgaWQ9Imh0bWxfMTQwOGQ5M2ZmN2E2NDQ0M2E4NGNjNjU4ZTYxMTMyMmEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlByb3NwZWN0IFBhcmsgU291dGgsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yOWI3ZDBmMzQ3OWE0MmI3OWVhZTU4MDIzMGNkNTRhNi5zZXRDb250ZW50KGh0bWxfMTQwOGQ5M2ZmN2E2NDQ0M2E4NGNjNjU4ZTYxMTMyMmEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNzY5MjQ4NzRhNzRjNGZmZjk5NzY1MWI3NTA3NDNiZGYuYmluZFBvcHVwKHBvcHVwXzI5YjdkMGYzNDc5YTQyYjc5ZWFlNTgwMjMwY2Q1NGE2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzMzNjE3ZDU0ODRmYzQzOWZiMzNiYjJiMGY4MTNjNTg2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjIzODQ1MjQ0Nzg0MTksLTczLjkxNjA3NDgzOTUxMzI0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2U0NzlmNjZkMWIxMzRlYWVhMjI3ZWYzNzJmOWRlOTQ2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2E4ZTJhNmU5NzE0NjRjNDk5NTAzNjc2OTA5MmMyNjQxID0gJCgnPGRpdiBpZD0iaHRtbF9hOGUyYTZlOTcxNDY0YzQ5OTUwMzY3NjkwOTJjMjY0MSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+R2VvcmdldG93biwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2U0NzlmNjZkMWIxMzRlYWVhMjI3ZWYzNzJmOWRlOTQ2LnNldENvbnRlbnQoaHRtbF9hOGUyYTZlOTcxNDY0YzQ5OTUwMzY3NjkwOTJjMjY0MSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zMzYxN2Q1NDg0ZmM0MzlmYjMzYmIyYjBmODEzYzU4Ni5iaW5kUG9wdXAocG9wdXBfZTQ3OWY2NmQxYjEzNGVhZWEyMjdlZjM3MmY5ZGU5NDYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYWZjOTMwMTdjYjczNDFmYmExZmQ0YzU0YmI2Yjc4ZGEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MDg0OTI0MTA0MTU0OCwtNzMuOTM4ODU4MTUyNjkxOTVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfN2U5YTJjMTA4ODFiNDY5MmIyNzI2ODk4MDE4NTU2NTQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfN2U5Yzk5N2UzMjVjNDFkNThkODRkYTc2NTQzNjBiOGYgPSAkKCc8ZGl2IGlkPSJodG1sXzdlOWM5OTdlMzI1YzQxZDU4ZDg0ZGE3NjU0MzYwYjhmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5FYXN0IFdpbGxpYW1zYnVyZywgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzdlOWEyYzEwODgxYjQ2OTJiMjcyNjg5ODAxODU1NjU0LnNldENvbnRlbnQoaHRtbF83ZTljOTk3ZTMyNWM0MWQ1OGQ4NGRhNzY1NDM2MGI4Zik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hZmM5MzAxN2NiNzM0MWZiYTFmZDRjNTRiYjZiNzhkYS5iaW5kUG9wdXAocG9wdXBfN2U5YTJjMTA4ODFiNDY5MmIyNzI2ODk4MDE4NTU2NTQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMGNmMzMxZWJkOTJmNDQ3MTkxYzYzM2Y4YTgxZTNjMzQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MTQ4MjI5MDY1MzIwMTQsLTczLjk1ODgwODU3NTg3NTgyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzM5NTQzZDkyN2M1ZjQyYzc4YzQyOTI3OTkxZGQ3YmFhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2M3ZjhkODY1NmZhZTRhMzhhOWY1NjFkNTI0NDdjMGNhID0gJCgnPGRpdiBpZD0iaHRtbF9jN2Y4ZDg2NTZmYWU0YTM4YTlmNTYxZDUyNDQ3YzBjYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Tm9ydGggU2lkZSwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzM5NTQzZDkyN2M1ZjQyYzc4YzQyOTI3OTkxZGQ3YmFhLnNldENvbnRlbnQoaHRtbF9jN2Y4ZDg2NTZmYWU0YTM4YTlmNTYxZDUyNDQ3YzBjYSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wY2YzMzFlYmQ5MmY0NDcxOTFjNjMzZjhhODFlM2MzNC5iaW5kUG9wdXAocG9wdXBfMzk1NDNkOTI3YzVmNDJjNzhjNDI5Mjc5OTFkZDdiYWEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMmUxMjNiY2JjNTdlNDRkOGI5MjM3Njk2MTdiNGJmNzUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MTA4NjE0NzI2NTA2NCwtNzMuOTU4MDAwOTUxNTMzMzFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOTI0NjhhZDI0ZDlkNDBiNGI5NjU2MDQ0MTkxMjFkY2IgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYTAzY2I2YThlZGZhNDM3YTgwNmU5MmI5YTQ5OWE0YjkgPSAkKCc8ZGl2IGlkPSJodG1sX2EwM2NiNmE4ZWRmYTQzN2E4MDZlOTJiOWE0OTlhNGI5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Tb3V0aCBTaWRlLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOTI0NjhhZDI0ZDlkNDBiNGI5NjU2MDQ0MTkxMjFkY2Iuc2V0Q29udGVudChodG1sX2EwM2NiNmE4ZWRmYTQzN2E4MDZlOTJiOWE0OTlhNGI5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzJlMTIzYmNiYzU3ZTQ0ZDhiOTIzNzY5NjE3YjRiZjc1LmJpbmRQb3B1cChwb3B1cF85MjQ2OGFkMjRkOWQ0MGI0Yjk2NTYwNDQxOTEyMWRjYik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hMmVhMjZmZGM0YWE0MGQ1YWNjMmU0MTgxNzIxZjY2MiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYxMzA1OTc2NjY3OTQyLC03My45NjgzNjY3ODAzNTU0MV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9iODFhMjQzZTk2M2M0ZjM3YjMxNjllN2Q3MjcyODA5ZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xYWZkZjBhYTg0NWE0YTYxODkxYjk0MGZkNWU0NjIxNyA9ICQoJzxkaXYgaWQ9Imh0bWxfMWFmZGYwYWE4NDVhNGE2MTg5MWI5NDBmZDVlNDYyMTciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk9jZWFuIFBhcmt3YXksIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iODFhMjQzZTk2M2M0ZjM3YjMxNjllN2Q3MjcyODA5ZS5zZXRDb250ZW50KGh0bWxfMWFmZGYwYWE4NDVhNGE2MTg5MWI5NDBmZDVlNDYyMTcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYTJlYTI2ZmRjNGFhNDBkNWFjYzJlNDE4MTcyMWY2NjIuYmluZFBvcHVwKHBvcHVwX2I4MWEyNDNlOTYzYzRmMzdiMzE2OWU3ZDcyNzI4MDllKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzA1ZjMyMTAwMmI3YTQxODI4ZWRkZTI2OTU3N2Q1MjE4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjE0NzY4MTI2OTQyMjYsLTc0LjAzMTk3OTE0NTM3OTg0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2Y3YTI3YTg1YWUzNTQyZmI5ODE1Yjk4ODVlOGVjMDk2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzljODY3YzZhZTNhNDQzNmI4ZmE1NDQwYTYwYTFiNjA1ID0gJCgnPGRpdiBpZD0iaHRtbF85Yzg2N2M2YWUzYTQ0MzZiOGZhNTQ0MGE2MGExYjYwNSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Rm9ydCBIYW1pbHRvbiwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Y3YTI3YTg1YWUzNTQyZmI5ODE1Yjk4ODVlOGVjMDk2LnNldENvbnRlbnQoaHRtbF85Yzg2N2M2YWUzYTQ0MzZiOGZhNTQ0MGE2MGExYjYwNSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wNWYzMjEwMDJiN2E0MTgyOGVkZGUyNjk1NzdkNTIxOC5iaW5kUG9wdXAocG9wdXBfZjdhMjdhODVhZTM1NDJmYjk4MTViOTg4NWU4ZWMwOTYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOTM0MmRlY2I4MTA2NGMzYjhlNTI5MWZlYTE2ODk1OWMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MTU2MTg0MjIzMTQzMiwtNzMuOTk0Mjc5MzYyNTU5NzhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZGM0ZmIxODVhMjBlNDRhNzgyZjUzNjdjZjFhOTNhYTUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTQ0NzU5ZjNhN2M4NDU0OWFlYmNlNmU3MDQzMWFiNDUgPSAkKCc8ZGl2IGlkPSJodG1sX2U0NDc1OWYzYTdjODQ1NDlhZWJjZTZlNzA0MzFhYjQ1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DaGluYXRvd24sIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZGM0ZmIxODVhMjBlNDRhNzgyZjUzNjdjZjFhOTNhYTUuc2V0Q29udGVudChodG1sX2U0NDc1OWYzYTdjODQ1NDlhZWJjZTZlNzA0MzFhYjQ1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzkzNDJkZWNiODEwNjRjM2I4ZTUyOTFmZWExNjg5NTljLmJpbmRQb3B1cChwb3B1cF9kYzRmYjE4NWEyMGU0NGE3ODJmNTM2N2NmMWE5M2FhNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mZDRhZDgwM2Y1Y2Y0NWEzODk0NjdmZjFjNDNiODg3YyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg1MTkwMjUyNTU1MzA1LC03My45MzY5MDAyNzk4NTIzNF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xNTBkMDU3YzRkODE0NjAxOWI0NmNlMjY3Y2MxZjUzYiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xNWQzMDIzMWQ4ZjM0OTY3OGIyY2Y2ZDNhZmJiOWYxYiA9ICQoJzxkaXYgaWQ9Imh0bWxfMTVkMzAyMzFkOGYzNDk2NzhiMmNmNmQzYWZiYjlmMWIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldhc2hpbmd0b24gSGVpZ2h0cywgTWFuaGF0dGFuPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xNTBkMDU3YzRkODE0NjAxOWI0NmNlMjY3Y2MxZjUzYi5zZXRDb250ZW50KGh0bWxfMTVkMzAyMzFkOGYzNDk2NzhiMmNmNmQzYWZiYjlmMWIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZmQ0YWQ4MDNmNWNmNDVhMzg5NDY3ZmYxYzQzYjg4N2MuYmluZFBvcHVwKHBvcHVwXzE1MGQwNTdjNGQ4MTQ2MDE5YjQ2Y2UyNjdjYzFmNTNiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzA1N2ZmMjk3YjEyOTRiZGI4OWY2Y2JlMmYxZmY2YTYyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODY3NjgzOTY0NDk5MTUsLTczLjkyMTIxMDQyMjAzODk3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2UzZmY2OGFiMDgyZTRjNjdhNzk0ZTZkNWIwN2E4NTE5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2JiOTcyMTE3NDRkMTQwYmQ5MWU2Njc3Y2RkZTNhYjQ2ID0gJCgnPGRpdiBpZD0iaHRtbF9iYjk3MjExNzQ0ZDE0MGJkOTFlNjY3N2NkZGUzYWI0NiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SW53b29kLCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2UzZmY2OGFiMDgyZTRjNjdhNzk0ZTZkNWIwN2E4NTE5LnNldENvbnRlbnQoaHRtbF9iYjk3MjExNzQ0ZDE0MGJkOTFlNjY3N2NkZGUzYWI0Nik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wNTdmZjI5N2IxMjk0YmRiODlmNmNiZTJmMWZmNmE2Mi5iaW5kUG9wdXAocG9wdXBfZTNmZjY4YWIwODJlNGM2N2E3OTRlNmQ1YjA3YTg1MTkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOWM3NWEwZWRmMjJmNGQzM2I1NmI3OTMxZmEyZjIyZDcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44MjM2MDQyODQ4MTE5MzUsLTczLjk0OTY4NzkxODgzMzY2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzY2ZTgyODFhNjA5OTQ1MmViYjVkOTRkODNkY2JlZWE5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzM5MmZmYzM2NTEwMzRmYWI4NTVlOWYyMGU1OGY2ZDZlID0gJCgnPGRpdiBpZD0iaHRtbF8zOTJmZmMzNjUxMDM0ZmFiODU1ZTlmMjBlNThmNmQ2ZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SGFtaWx0b24gSGVpZ2h0cywgTWFuaGF0dGFuPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82NmU4MjgxYTYwOTk0NTJlYmI1ZDk0ZDgzZGNiZWVhOS5zZXRDb250ZW50KGh0bWxfMzkyZmZjMzY1MTAzNGZhYjg1NWU5ZjIwZTU4ZjZkNmUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOWM3NWEwZWRmMjJmNGQzM2I1NmI3OTMxZmEyZjIyZDcuYmluZFBvcHVwKHBvcHVwXzY2ZTgyODFhNjA5OTQ1MmViYjVkOTRkODNkY2JlZWE5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2I3OWVkOWExZTY2ZDRhNDc4YzM4YzE2OGJiYWIzNjZmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODE2OTM0NDI5NDk3OCwtNzMuOTU3Mzg1MzkzNTE4OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82ODZjZDdmYWUxZDY0Yzc1OWZmZDAwMWRhY2M0OTBhMiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82YWRkZWU1YzM4Njk0ZmFmOTc4OTQzOWNkM2FjZTkxMSA9ICQoJzxkaXYgaWQ9Imh0bWxfNmFkZGVlNWMzODY5NGZhZjk3ODk0MzljZDNhY2U5MTEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk1hbmhhdHRhbnZpbGxlLCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzY4NmNkN2ZhZTFkNjRjNzU5ZmZkMDAxZGFjYzQ5MGEyLnNldENvbnRlbnQoaHRtbF82YWRkZWU1YzM4Njk0ZmFmOTc4OTQzOWNkM2FjZTkxMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iNzllZDlhMWU2NmQ0YTQ3OGMzOGMxNjhiYmFiMzY2Zi5iaW5kUG9wdXAocG9wdXBfNjg2Y2Q3ZmFlMWQ2NGM3NTlmZmQwMDFkYWNjNDkwYTIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNGFmMGNiODIwMWYyNGRkNjgzYWM0MDVjMDEzOWZkNGIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44MTU5NzYwNjc0MjQxNCwtNzMuOTQzMjExMTI2MDM5MDVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMWQyNDg0ZmI0MTRkNDhhM2I0ZmEzY2NmMzY5Yzg1NWEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjE2ZmRlZDQzNWU1NGU5MjgzNDAxOGMxZTFiZjA2NjQgPSAkKCc8ZGl2IGlkPSJodG1sX2YxNmZkZWQ0MzVlNTRlOTI4MzQwMThjMWUxYmYwNjY0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DZW50cmFsIEhhcmxlbSwgTWFuaGF0dGFuPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xZDI0ODRmYjQxNGQ0OGEzYjRmYTNjY2YzNjljODU1YS5zZXRDb250ZW50KGh0bWxfZjE2ZmRlZDQzNWU1NGU5MjgzNDAxOGMxZTFiZjA2NjQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNGFmMGNiODIwMWYyNGRkNjgzYWM0MDVjMDEzOWZkNGIuYmluZFBvcHVwKHBvcHVwXzFkMjQ4NGZiNDE0ZDQ4YTNiNGZhM2NjZjM2OWM4NTVhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzZhM2IxYzEwMjhmMjQ0NmJiNmJlOWRlMWY5NDEzZTczID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzkyMjQ5NDY2NjMwMzMsLTczLjk0NDE4MjIzMTQ4NTI0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzZlMDBkNzA5ZDhjNjRjYzY4MDIwNjBjNjE3NTI1YjlmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzcyNzViNDI0MDdhYTQ2YTM4MGE3ODRkZjBiMmM1YmM5ID0gJCgnPGRpdiBpZD0iaHRtbF83Mjc1YjQyNDA3YWE0NmEzODBhNzg0ZGYwYjJjNWJjOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RWFzdCBIYXJsZW0sIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNmUwMGQ3MDlkOGM2NGNjNjgwMjA2MGM2MTc1MjViOWYuc2V0Q29udGVudChodG1sXzcyNzViNDI0MDdhYTQ2YTM4MGE3ODRkZjBiMmM1YmM5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzZhM2IxYzEwMjhmMjQ0NmJiNmJlOWRlMWY5NDEzZTczLmJpbmRQb3B1cChwb3B1cF82ZTAwZDcwOWQ4YzY0Y2M2ODAyMDYwYzYxNzUyNWI5Zik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82YmEyMzAyNzI0ZTk0MmRjOTVhZWNhZWM1NDdjNDMzYiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc3NTYzODU3MzMwMTgwNSwtNzMuOTYwNTA3NjMxMzVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjY2NTVlZDg4M2E0NGViMjhiYTA2YTNiMzcxZWE5ZjIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOWEwNGNhODNjOTUxNGY3YTlmODFjNmU5MWM0N2Y5YjIgPSAkKCc8ZGl2IGlkPSJodG1sXzlhMDRjYTgzYzk1MTRmN2E5ZjgxYzZlOTFjNDdmOWIyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5VcHBlciBFYXN0IFNpZGUsIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZjY2NTVlZDg4M2E0NGViMjhiYTA2YTNiMzcxZWE5ZjIuc2V0Q29udGVudChodG1sXzlhMDRjYTgzYzk1MTRmN2E5ZjgxYzZlOTFjNDdmOWIyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzZiYTIzMDI3MjRlOTQyZGM5NWFlY2FlYzU0N2M0MzNiLmJpbmRQb3B1cChwb3B1cF9mNjY1NWVkODgzYTQ0ZWIyOGJhMDZhM2IzNzFlYTlmMik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xODFhNTU3ODZlYjU0YWY1YThjZDQ5YWVkZjVhZDNmNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc3NTkyOTg0OTg4NDg3NSwtNzMuOTQ3MTE3ODQ0NzE4MjZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMGRjYTE2OTZmNjNhNDE5NzlmN2M4YjNkNmNkYTkwMWEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDI1OTNjYmUyOWE0NDY2MGI2ZDJmMzExZDljNmIzNDggPSAkKCc8ZGl2IGlkPSJodG1sXzAyNTkzY2JlMjlhNDQ2NjBiNmQyZjMxMWQ5YzZiMzQ4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Zb3JrdmlsbGUsIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMGRjYTE2OTZmNjNhNDE5NzlmN2M4YjNkNmNkYTkwMWEuc2V0Q29udGVudChodG1sXzAyNTkzY2JlMjlhNDQ2NjBiNmQyZjMxMWQ5YzZiMzQ4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzE4MWE1NTc4NmViNTRhZjVhOGNkNDlhZWRmNWFkM2Y0LmJpbmRQb3B1cChwb3B1cF8wZGNhMTY5NmY2M2E0MTk3OWY3YzhiM2Q2Y2RhOTAxYSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84ZTdlZTBmMTRlZjg0OWQ0YjBhNDg4MjgwZWEzZWJmOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc2ODExMjY1ODI4NzMzLC03My45NTg4NTk2ODgxMzc2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzU4M2M2ZDExMWExZTRiMWRhNzIzNDEzOGU1M2FiZmZkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2IwMTExOWM3NjZiMTRjNzc5Zjk0YWY4OGU4YjgwZjM1ID0gJCgnPGRpdiBpZD0iaHRtbF9iMDExMTljNzY2YjE0Yzc3OWY5NGFmODhlOGI4MGYzNSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TGVub3ggSGlsbCwgTWFuaGF0dGFuPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81ODNjNmQxMTFhMWU0YjFkYTcyMzQxMzhlNTNhYmZmZC5zZXRDb250ZW50KGh0bWxfYjAxMTE5Yzc2NmIxNGM3NzlmOTRhZjg4ZThiODBmMzUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOGU3ZWUwZjE0ZWY4NDlkNGIwYTQ4ODI4MGVhM2ViZjguYmluZFBvcHVwKHBvcHVwXzU4M2M2ZDExMWExZTRiMWRhNzIzNDEzOGU1M2FiZmZkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzZmZDFkNzc3OTg5MjQ0MTQ5MmNlOGYyODk1NTdkN2E2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzYyMTU5NjA1NzYyODMsLTczLjk0OTE2NzY5MjI3OTUzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzQ3ZGQ0OTJjNDE5NTQxYzc5NWVmZTY3NWViNzQzMzE0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzIzMmRmMTY5MWE3ZTQyMWQ5NGQwZWQxN2Q3OWQ0NjM0ID0gJCgnPGRpdiBpZD0iaHRtbF8yMzJkZjE2OTFhN2U0MjFkOTRkMGVkMTdkNzlkNDYzNCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Um9vc2V2ZWx0IElzbGFuZCwgTWFuaGF0dGFuPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80N2RkNDkyYzQxOTU0MWM3OTVlZmU2NzVlYjc0MzMxNC5zZXRDb250ZW50KGh0bWxfMjMyZGYxNjkxYTdlNDIxZDk0ZDBlZDE3ZDc5ZDQ2MzQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNmZkMWQ3Nzc5ODkyNDQxNDkyY2U4ZjI4OTU1N2Q3YTYuYmluZFBvcHVwKHBvcHVwXzQ3ZGQ0OTJjNDE5NTQxYzc5NWVmZTY3NWViNzQzMzE0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2YxNGMzOWQ0YjBjNzQ5MjA4YWM1M2Y2NWE1OTI0ZjY3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzg3NjU3OTk4NTM0ODU0LC03My45NzcwNTkyMzYzMDYwM10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hYTI4OTA3ZDg4MTI0MTExYmRjZjBmNTNmNjUyNTc4NSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iYmJiODgyNDlkMzk0NGI2OTQwZmVkODU4OWEwZjdiYiA9ICQoJzxkaXYgaWQ9Imh0bWxfYmJiYjg4MjQ5ZDM5NDRiNjk0MGZlZDg1ODlhMGY3YmIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlVwcGVyIFdlc3QgU2lkZSwgTWFuaGF0dGFuPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hYTI4OTA3ZDg4MTI0MTExYmRjZjBmNTNmNjUyNTc4NS5zZXRDb250ZW50KGh0bWxfYmJiYjg4MjQ5ZDM5NDRiNjk0MGZlZDg1ODlhMGY3YmIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZjE0YzM5ZDRiMGM3NDkyMDhhYzUzZjY1YTU5MjRmNjcuYmluZFBvcHVwKHBvcHVwX2FhMjg5MDdkODgxMjQxMTFiZGNmMGY1M2Y2NTI1Nzg1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2E3MjY3ZTdhOTU1YjRiOTRhMmRkYTUyYjg4ZGZlNzBiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzczNTI4ODg5NDIxNjYsLTczLjk4NTMzNzc3MDAxMjYyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2M0NWI3MTBlMzFkMzQwNDU5ZGE0YjY3ZjAzNjVhZWVhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzVmOWExODg5ZTk4MzRiOWFiZjcyZWM0OWU2MGU1ZjUxID0gJCgnPGRpdiBpZD0iaHRtbF81ZjlhMTg4OWU5ODM0YjlhYmY3MmVjNDllNjBlNWY1MSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TGluY29sbiBTcXVhcmUsIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYzQ1YjcxMGUzMWQzNDA0NTlkYTRiNjdmMDM2NWFlZWEuc2V0Q29udGVudChodG1sXzVmOWExODg5ZTk4MzRiOWFiZjcyZWM0OWU2MGU1ZjUxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2E3MjY3ZTdhOTU1YjRiOTRhMmRkYTUyYjg4ZGZlNzBiLmJpbmRQb3B1cChwb3B1cF9jNDViNzEwZTMxZDM0MDQ1OWRhNGI2N2YwMzY1YWVlYSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85YmZiMmY4ZmM1M2U0ODE2OTRmYmYxODQ5Y2VlZDcwMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc1OTEwMDg5MTQ2MjEyLC03My45OTYxMTkzNjMwOTQ3OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85MjQzMWQxZTFmNjQ0YmFlYmE0YmQyYjMzYjZhNWNkYyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lNjJmOTEyNDY5YjA0OWM3YWY3YTQ5NDFiNzdkNzgxZCA9ICQoJzxkaXYgaWQ9Imh0bWxfZTYyZjkxMjQ2OWIwNDljN2FmN2E0OTQxYjc3ZDc4MWQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNsaW50b24sIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOTI0MzFkMWUxZjY0NGJhZWJhNGJkMmIzM2I2YTVjZGMuc2V0Q29udGVudChodG1sX2U2MmY5MTI0NjliMDQ5YzdhZjdhNDk0MWI3N2Q3ODFkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzliZmIyZjhmYzUzZTQ4MTY5NGZiZjE4NDljZWVkNzAxLmJpbmRQb3B1cChwb3B1cF85MjQzMWQxZTFmNjQ0YmFlYmE0YmQyYjMzYjZhNWNkYyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mZjc4MjI2OWEzZmQ0NWIyOGU0ZDkwODY4MDNmZDkwYSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc1NDY5MTEwMjcwNjIzLC03My45ODE2Njg4MjczMDMwNF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84OGVmZDY5ODY1ZjI0ZGU3YjMzNGJhMWNjMDhlNmJlNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82NzE1ZjUxNDI0ZTc0M2E2ODM2NDYxZWJiMDRjMmYyOSA9ICQoJzxkaXYgaWQ9Imh0bWxfNjcxNWY1MTQyNGU3NDNhNjgzNjQ2MWViYjA0YzJmMjkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk1pZHRvd24sIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfODhlZmQ2OTg2NWYyNGRlN2IzMzRiYTFjYzA4ZTZiZTQuc2V0Q29udGVudChodG1sXzY3MTVmNTE0MjRlNzQzYTY4MzY0NjFlYmIwNGMyZjI5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ZmNzgyMjY5YTNmZDQ1YjI4ZTRkOTA4NjgwM2ZkOTBhLmJpbmRQb3B1cChwb3B1cF84OGVmZDY5ODY1ZjI0ZGU3YjMzNGJhMWNjMDhlNmJlNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kZTQwZDQyNjI4NTk0ZmY2ODdjOGE2YWRkYjAzOGIyYyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc0ODMwMzA3NzI1MjE3NCwtNzMuOTc4MzMyMDc5MjQxMjddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMTRmNjU1NjQ0NmZmNGJkM2JmMDU0NjUyYmIyOGRmZTkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYTBiZWJlYjJkOWM4NDcwMTljZjJmNTg3NDhlYzBmNzkgPSAkKCc8ZGl2IGlkPSJodG1sX2EwYmViZWIyZDljODQ3MDE5Y2YyZjU4NzQ4ZWMwZjc5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NdXJyYXkgSGlsbCwgTWFuaGF0dGFuPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xNGY2NTU2NDQ2ZmY0YmQzYmYwNTQ2NTJiYjI4ZGZlOS5zZXRDb250ZW50KGh0bWxfYTBiZWJlYjJkOWM4NDcwMTljZjJmNTg3NDhlYzBmNzkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZGU0MGQ0MjYyODU5NGZmNjg3YzhhNmFkZGIwMzhiMmMuYmluZFBvcHVwKHBvcHVwXzE0ZjY1NTY0NDZmZjRiZDNiZjA1NDY1MmJiMjhkZmU5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzRlMzMyZjlkNTIwOTQ0OWQ4OTViN2IxZjkwNzE0YTg3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzQ0MDM0NzA2NzQ3OTc1LC03NC4wMDMxMTYzMzQ3MjgxM10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80YmJjMmM3MDMwYWY0ZThmODM4MzMxMDZlNzk1M2VmOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83ZDdjNzY3ZGQ2YzE0OGNkOThlOTRmNDQ0ZDIwYTc0OCA9ICQoJzxkaXYgaWQ9Imh0bWxfN2Q3Yzc2N2RkNmMxNDhjZDk4ZTk0ZjQ0NGQyMGE3NDgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNoZWxzZWEsIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNGJiYzJjNzAzMGFmNGU4ZjgzODMzMTA2ZTc5NTNlZjguc2V0Q29udGVudChodG1sXzdkN2M3NjdkZDZjMTQ4Y2Q5OGU5NGY0NDRkMjBhNzQ4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzRlMzMyZjlkNTIwOTQ0OWQ4OTViN2IxZjkwNzE0YTg3LmJpbmRQb3B1cChwb3B1cF80YmJjMmM3MDMwYWY0ZThmODM4MzMxMDZlNzk1M2VmOCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xYWYxNWY0YzNkMzU0MjI5OGFiY2IzZjE0ZjRiYzMyNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcyNjkzMjg4NTM2MTI4LC03My45OTk5MTQwMjk0NTkwMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yZjEwNDM0YzgwOGE0ZjBiOGM5NmIwYmZlMDRmOGM2MCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83OTU4NmNmZTRlY2U0YzY1YjdmZjQzYmVlZmViYTMyMyA9ICQoJzxkaXYgaWQ9Imh0bWxfNzk1ODZjZmU0ZWNlNGM2NWI3ZmY0M2JlZWZlYmEzMjMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkdyZWVud2ljaCBWaWxsYWdlLCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzJmMTA0MzRjODA4YTRmMGI4Yzk2YjBiZmUwNGY4YzYwLnNldENvbnRlbnQoaHRtbF83OTU4NmNmZTRlY2U0YzY1YjdmZjQzYmVlZmViYTMyMyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xYWYxNWY0YzNkMzU0MjI5OGFiY2IzZjE0ZjRiYzMyNC5iaW5kUG9wdXAocG9wdXBfMmYxMDQzNGM4MDhhNGYwYjhjOTZiMGJmZTA0ZjhjNjApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNWZhNmE0MzViODcwNGZkZWEzYmVlYWE5ZDE5NTAzMGMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43Mjc4NDY3NzcyNzAyNDQsLTczLjk4MjIyNjE2NTA2NDE2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2YzMjA5NGJjNzIwYTRjNjhiZmQ2ODk2MWY2M2Y5OTAyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2EzNjA2MGE0YmYxNDQxZmJhZGQzNWU2YWNhMjNmMmU5ID0gJCgnPGRpdiBpZD0iaHRtbF9hMzYwNjBhNGJmMTQ0MWZiYWRkMzVlNmFjYTIzZjJlOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RWFzdCBWaWxsYWdlLCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2YzMjA5NGJjNzIwYTRjNjhiZmQ2ODk2MWY2M2Y5OTAyLnNldENvbnRlbnQoaHRtbF9hMzYwNjBhNGJmMTQ0MWZiYWRkMzVlNmFjYTIzZjJlOSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81ZmE2YTQzNWI4NzA0ZmRlYTNiZWVhYTlkMTk1MDMwYy5iaW5kUG9wdXAocG9wdXBfZjMyMDk0YmM3MjBhNGM2OGJmZDY4OTYxZjYzZjk5MDIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfY2FkM2Y5NzdmMGIxNGE4ZGJlZGRiOWZjZjk2ODViNzQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MTc4MDY3NDg5Mjc2NSwtNzMuOTgwODkwMzE5OTkyOTFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzM4OTg4Zjc5MTk5NGZkN2FiOTI4YmRmM2ZlYTJlNDcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzdjYzczZmU1NTcyNDUyODk2Y2ZiODY2ZjQ4Y2Q3NzkgPSAkKCc8ZGl2IGlkPSJodG1sXzc3Y2M3M2ZlNTU3MjQ1Mjg5NmNmYjg2NmY0OGNkNzc5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Mb3dlciBFYXN0IFNpZGUsIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzM4OTg4Zjc5MTk5NGZkN2FiOTI4YmRmM2ZlYTJlNDcuc2V0Q29udGVudChodG1sXzc3Y2M3M2ZlNTU3MjQ1Mjg5NmNmYjg2NmY0OGNkNzc5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2NhZDNmOTc3ZjBiMTRhOGRiZWRkYjlmY2Y5Njg1Yjc0LmJpbmRQb3B1cChwb3B1cF8zMzg5ODhmNzkxOTk0ZmQ3YWI5MjhiZGYzZmVhMmU0Nyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83ZGZjMTg4NDQ1ZmQ0MWYwYjVmMTQxNDUyYTk5OTcyZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcyMTUyMTk2NzQ0MzIxNiwtNzQuMDEwNjgzMjg1NTkwODddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNzk3ODRhNDQ2OGE1NDY2NmE4Y2UxZDU0MWExMDAzMmIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYjFlNTZjMGM1ZjQ3NGMyNDgzMjQzMzRhMGQzYmUxMzcgPSAkKCc8ZGl2IGlkPSJodG1sX2IxZTU2YzBjNWY0NzRjMjQ4MzI0MzM0YTBkM2JlMTM3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UcmliZWNhLCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzc5Nzg0YTQ0NjhhNTQ2NjZhOGNlMWQ1NDFhMTAwMzJiLnNldENvbnRlbnQoaHRtbF9iMWU1NmMwYzVmNDc0YzI0ODMyNDMzNGEwZDNiZTEzNyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83ZGZjMTg4NDQ1ZmQ0MWYwYjVmMTQxNDUyYTk5OTcyZi5iaW5kUG9wdXAocG9wdXBfNzk3ODRhNDQ2OGE1NDY2NmE4Y2UxZDU0MWExMDAzMmIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMGFjY2Q3ZmMwZThkNDRjNDgzYzYyNTM4OWE0ODc0NTYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MTkzMjM3OTM5NTkwNywtNzMuOTk3MzA0NjcyMDgwNzNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTJiOWQ2MjcxYjMwNDk3MTk4MDg4YzY3ZmQ2NzkyMzIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMTg1YTQ1MzFlYTdjNDE1MmE3NTg3MGQ1MDdhYjI5ZTcgPSAkKCc8ZGl2IGlkPSJodG1sXzE4NWE0NTMxZWE3YzQxNTJhNzU4NzBkNTA3YWIyOWU3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5MaXR0bGUgSXRhbHksIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTJiOWQ2MjcxYjMwNDk3MTk4MDg4YzY3ZmQ2NzkyMzIuc2V0Q29udGVudChodG1sXzE4NWE0NTMxZWE3YzQxNTJhNzU4NzBkNTA3YWIyOWU3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzBhY2NkN2ZjMGU4ZDQ0YzQ4M2M2MjUzODlhNDg3NDU2LmJpbmRQb3B1cChwb3B1cF9hMmI5ZDYyNzFiMzA0OTcxOTgwODhjNjdmZDY3OTIzMik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iM2JiYmZiODhkNDQ0MWUwYjg5OWJkNDQyMGMxMzJjNSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcyMjE4Mzg0MTMxNzk0LC03NC4wMDA2NTY2Njk1OTc1OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zMzI4MGVkYTQ5YmI0YjgzYTBlMzg1MzEwODFhMzhkNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83MTdlZDA1NDIxNjQ0ZjZjYWQ3YmM5NmFjYzBiNWVjMCA9ICQoJzxkaXYgaWQ9Imh0bWxfNzE3ZWQwNTQyMTY0NGY2Y2FkN2JjOTZhY2MwYjVlYzAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlNvaG8sIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzMyODBlZGE0OWJiNGI4M2EwZTM4NTMxMDgxYTM4ZDQuc2V0Q29udGVudChodG1sXzcxN2VkMDU0MjE2NDRmNmNhZDdiYzk2YWNjMGI1ZWMwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2IzYmJiZmI4OGQ0NDQxZTBiODk5YmQ0NDIwYzEzMmM1LmJpbmRQb3B1cChwb3B1cF8zMzI4MGVkYTQ5YmI0YjgzYTBlMzg1MzEwODFhMzhkNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84M2ZiYTgwMDJmZjE0OTI0YjgxYTU3NGFiYzAwZmYzNSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjczNDQzMzkzNTcyNDM0LC03NC4wMDYxNzk5ODEyNjgxMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hMDJjMjg2ZWE5NmQ0ZDY1OWYxNzZlMjZlZDEwMjRkMiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lY2NlMWIwN2ZiNjc0MmFhOTAwOGU2MThjNDNiNGY3NSA9ICQoJzxkaXYgaWQ9Imh0bWxfZWNjZTFiMDdmYjY3NDJhYTkwMDhlNjE4YzQzYjRmNzUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldlc3QgVmlsbGFnZSwgTWFuaGF0dGFuPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hMDJjMjg2ZWE5NmQ0ZDY1OWYxNzZlMjZlZDEwMjRkMi5zZXRDb250ZW50KGh0bWxfZWNjZTFiMDdmYjY3NDJhYTkwMDhlNjE4YzQzYjRmNzUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfODNmYmE4MDAyZmYxNDkyNGI4MWE1NzRhYmMwMGZmMzUuYmluZFBvcHVwKHBvcHVwX2EwMmMyODZlYTk2ZDRkNjU5ZjE3NmUyNmVkMTAyNGQyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzkxZmMxMzQzNDczYTQwYmVhYzMzNzMwYWUxMzczM2Y2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzk3MzA3MDQxNzAyODY1LC03My45NjQyODYxNzc0MDY1NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mMjVjZjQ0MGYyYzQ0ZDMzOTNkZmZjMGM0ZDM2ZTQ5MiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wYzJkY2QyMTMzZTg0Mzc4ODQ3NDRiOTY3NmFiMzFjNCA9ICQoJzxkaXYgaWQ9Imh0bWxfMGMyZGNkMjEzM2U4NDM3ODg0NzQ0Yjk2NzZhYjMxYzQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk1hbmhhdHRhbiBWYWxsZXksIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZjI1Y2Y0NDBmMmM0NGQzMzkzZGZmYzBjNGQzNmU0OTIuc2V0Q29udGVudChodG1sXzBjMmRjZDIxMzNlODQzNzg4NDc0NGI5Njc2YWIzMWM0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzkxZmMxMzQzNDczYTQwYmVhYzMzNzMwYWUxMzczM2Y2LmJpbmRQb3B1cChwb3B1cF9mMjVjZjQ0MGYyYzQ0ZDMzOTNkZmZjMGM0ZDM2ZTQ5Mik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iMDNhZThiZTZhNTI0NmVjYTY5ODU0NmY5ODY5YTY3OSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjgwNzk5OTczODE2NTgyNiwtNzMuOTYzODk2Mjc5MDUzMzJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDZmNDUyOTAwZmU0NDY1YWEwY2I1YTZkMWMyZmU5MjEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfM2ExMDI2ZjMzY2M4NDZkYWExMjI2ZTBkMGVlMGU3ZDMgPSAkKCc8ZGl2IGlkPSJodG1sXzNhMTAyNmYzM2NjODQ2ZGFhMTIyNmUwZDBlZTBlN2QzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Nb3JuaW5nc2lkZSBIZWlnaHRzLCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Q2ZjQ1MjkwMGZlNDQ2NWFhMGNiNWE2ZDFjMmZlOTIxLnNldENvbnRlbnQoaHRtbF8zYTEwMjZmMzNjYzg0NmRhYTEyMjZlMGQwZWUwZTdkMyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iMDNhZThiZTZhNTI0NmVjYTY5ODU0NmY5ODY5YTY3OS5iaW5kUG9wdXAocG9wdXBfZDZmNDUyOTAwZmU0NDY1YWEwY2I1YTZkMWMyZmU5MjEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMTRhODU1NGM0MmVhNGU3ZjhjNzk5N2FiMDQwODhmMWIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MzcyMDk4MzI3MTUsLTczLjk4MTM3NTk0ODMzNTQxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzg0ZjZhZWQyMTM4MTQ4YzY4Y2Q1YzFhZjBkMmE3Y2M2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzdiNDRkYWYzOGVmNjRkNTU4OTM4MGZhNzFhOWM1YTQwID0gJCgnPGRpdiBpZD0iaHRtbF83YjQ0ZGFmMzhlZjY0ZDU1ODkzODBmYTcxYTljNWE0MCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+R3JhbWVyY3ksIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfODRmNmFlZDIxMzgxNDhjNjhjZDVjMWFmMGQyYTdjYzYuc2V0Q29udGVudChodG1sXzdiNDRkYWYzOGVmNjRkNTU4OTM4MGZhNzFhOWM1YTQwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzE0YTg1NTRjNDJlYTRlN2Y4Yzc5OTdhYjA0MDg4ZjFiLmJpbmRQb3B1cChwb3B1cF84NGY2YWVkMjEzODE0OGM2OGNkNWMxYWYwZDJhN2NjNik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jZmU2OGQxZTg2NDM0YzZkYjE5ZDg3MmFkODYzMjQwMiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcxMTkzMTk4Mzk0NTY1LC03NC4wMTY4NjkzMDUwODYxN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9kZWNmZDBkOThhM2I0M2M5YTJiY2NjZTJiOTJjYTNkZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83MDc1NDlhNDA5MWQ0OWVhYTAyM2ZiYTQwNDcyM2UwYSA9ICQoJzxkaXYgaWQ9Imh0bWxfNzA3NTQ5YTQwOTFkNDllYWEwMjNmYmE0MDQ3MjNlMGEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJhdHRlcnkgUGFyayBDaXR5LCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2RlY2ZkMGQ5OGEzYjQzYzlhMmJjY2NlMmI5MmNhM2RmLnNldENvbnRlbnQoaHRtbF83MDc1NDlhNDA5MWQ0OWVhYTAyM2ZiYTQwNDcyM2UwYSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jZmU2OGQxZTg2NDM0YzZkYjE5ZDg3MmFkODYzMjQwMi5iaW5kUG9wdXAocG9wdXBfZGVjZmQwZDk4YTNiNDNjOWEyYmNjY2UyYjkyY2EzZGYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNGY0NDgwODU1Y2RkNDgyMGEwZjZlYzJmNzI1OTgxNDkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MDcxMDcxMDcyNzA0OCwtNzQuMDEwNjY1NDQ1MjEyN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9iODBjOTA3OTdjN2Y0ZDBjYTM0NWM1YzMwYWQ5YzJhMCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85ZWI3OGVlM2E4NTk0MDA5OGUyZDIyMmY0NGY4ZTc1MiA9ICQoJzxkaXYgaWQ9Imh0bWxfOWViNzhlZTNhODU5NDAwOThlMmQyMjJmNDRmOGU3NTIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZpbmFuY2lhbCBEaXN0cmljdCwgTWFuaGF0dGFuPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iODBjOTA3OTdjN2Y0ZDBjYTM0NWM1YzMwYWQ5YzJhMC5zZXRDb250ZW50KGh0bWxfOWViNzhlZTNhODU5NDAwOThlMmQyMjJmNDRmOGU3NTIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNGY0NDgwODU1Y2RkNDgyMGEwZjZlYzJmNzI1OTgxNDkuYmluZFBvcHVwKHBvcHVwX2I4MGM5MDc5N2M3ZjRkMGNhMzQ1YzVjMzBhZDljMmEwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2I1YzA1ZTgyNjY2OTQ3NjM5ZmEzMjAyZjQxMWNkMDI2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzY4NTA4NTkzMzU0OTIsLTczLjkxNTY1Mzc0MzA0MjM0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2UxMmQyYjcxNTMxZDRmMDhhMzI3ZjFlNGFiYzcwMTkzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2FkMDQyYzhiOTViNzRjOTZhMjcxMDlhMGQxNGJkNTA4ID0gJCgnPGRpdiBpZD0iaHRtbF9hZDA0MmM4Yjk1Yjc0Yzk2YTI3MTA5YTBkMTRiZDUwOCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QXN0b3JpYSwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lMTJkMmI3MTUzMWQ0ZjA4YTMyN2YxZTRhYmM3MDE5My5zZXRDb250ZW50KGh0bWxfYWQwNDJjOGI5NWI3NGM5NmEyNzEwOWEwZDE0YmQ1MDgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYjVjMDVlODI2NjY5NDc2MzlmYTMyMDJmNDExY2QwMjYuYmluZFBvcHVwKHBvcHVwX2UxMmQyYjcxNTMxZDRmMDhhMzI3ZjFlNGFiYzcwMTkzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzFjM2JiMzczZjU5MTRmMTQ5NWZlZWM3NmYxMDY5NzVmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzQ2MzQ5MDg4NjAyMjIsLTczLjkwMTg0MTY2ODM4Mjg0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzMxOGFkMjQ4YmExNDRlYTI4NzAxZjQyMDU3NmE4OGZkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzA5ODlmNzc0Mjk1NzRmZjhiMzVjZTVkZDlmYmM2YTQ5ID0gJCgnPGRpdiBpZD0iaHRtbF8wOTg5Zjc3NDI5NTc0ZmY4YjM1Y2U1ZGQ5ZmJjNmE0OSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V29vZHNpZGUsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzE4YWQyNDhiYTE0NGVhMjg3MDFmNDIwNTc2YTg4ZmQuc2V0Q29udGVudChodG1sXzA5ODlmNzc0Mjk1NzRmZjhiMzVjZTVkZDlmYmM2YTQ5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzFjM2JiMzczZjU5MTRmMTQ5NWZlZWM3NmYxMDY5NzVmLmJpbmRQb3B1cChwb3B1cF8zMThhZDI0OGJhMTQ0ZWEyODcwMWY0MjA1NzZhODhmZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84ZWI2YzZjMTYzY2U0MTFiYWU3NWU4ZTYyM2VmZTBmZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc1MTk4MTM4MDA3MzY3LC03My44ODI4MjEwOTE2NDM2NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80ZTQ5MmQzMDA4YTk0NmYxOWJjMWIzOTkwOTgxYmVkMCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hMDFhZGJjMDkzMDE0NjRlOGFjNGNhZDhmMjkzNWI0ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfYTAxYWRiYzA5MzAxNDY0ZThhYzRjYWQ4ZjI5MzViNGYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkphY2tzb24gSGVpZ2h0cywgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80ZTQ5MmQzMDA4YTk0NmYxOWJjMWIzOTkwOTgxYmVkMC5zZXRDb250ZW50KGh0bWxfYTAxYWRiYzA5MzAxNDY0ZThhYzRjYWQ4ZjI5MzViNGYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOGViNmM2YzE2M2NlNDExYmFlNzVlOGU2MjNlZmUwZmUuYmluZFBvcHVwKHBvcHVwXzRlNDkyZDMwMDhhOTQ2ZjE5YmMxYjM5OTA5ODFiZWQwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzMwNjllMTUxNzdhNDQyMTA5OTQwNWJhMzk4OGFiODE4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzQ0MDQ4NTA1MTIyMDI0LC03My44ODE2NTYyMjI4ODM4OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yOTE1OTY3MzIwYjE0NTQ5YmZmZTU2MmNjNDczZjY4YiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mMjIwMjQwODQ3Y2U0MzZjYTNkZGI5NWFmZGJkMTg1OCA9ICQoJzxkaXYgaWQ9Imh0bWxfZjIyMDI0MDg0N2NlNDM2Y2EzZGRiOTVhZmRiZDE4NTgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVsbWh1cnN0LCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzI5MTU5NjczMjBiMTQ1NDliZmZlNTYyY2M0NzNmNjhiLnNldENvbnRlbnQoaHRtbF9mMjIwMjQwODQ3Y2U0MzZjYTNkZGI5NWFmZGJkMTg1OCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zMDY5ZTE1MTc3YTQ0MjEwOTk0MDViYTM5ODhhYjgxOC5iaW5kUG9wdXAocG9wdXBfMjkxNTk2NzMyMGIxNDU0OWJmZmU1NjJjYzQ3M2Y2OGIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzM0NWQwOTQ2NTU4NDEyYWJhM2ZiZTdkNWI2YjgwMDYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42NTQyMjUyNzczODQ4NywtNzMuODM4MTM3NjQ2MDAyOF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83NmUzNzU4YmIwMjY0MWIxYjlkYTMzNmMwYjc1ZDE4NiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83MjNlZmJmZjY3Y2I0M2M0YWM0NjkxYTc3MzQ1YTk5YSA9ICQoJzxkaXYgaWQ9Imh0bWxfNzIzZWZiZmY2N2NiNDNjNGFjNDY5MWE3NzM0NWE5OWEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkhvd2FyZCBCZWFjaCwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83NmUzNzU4YmIwMjY0MWIxYjlkYTMzNmMwYjc1ZDE4Ni5zZXRDb250ZW50KGh0bWxfNzIzZWZiZmY2N2NiNDNjNGFjNDY5MWE3NzM0NWE5OWEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMzM0NWQwOTQ2NTU4NDEyYWJhM2ZiZTdkNWI2YjgwMDYuYmluZFBvcHVwKHBvcHVwXzc2ZTM3NThiYjAyNjQxYjFiOWRhMzM2YzBiNzVkMTg2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzllOWVhMzgwNzZjMDRkYmViYzczNzFhYTY3YjBmZDA0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzQyMzgxNzUwMTU2NjcsLTczLjg1NjgyNDk3MzQ1MjU4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2JlMTgzOGU3ODBjNTRjNGFhMzE4Y2RjYTEwYzM4OWJmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzdhMzAyNzgzN2VkZTQyNjY5MTg5YmE0MmVkMjY2NTFkID0gJCgnPGRpdiBpZD0iaHRtbF83YTMwMjc4MzdlZGU0MjY2OTE4OWJhNDJlZDI2NjUxZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q29yb25hLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2JlMTgzOGU3ODBjNTRjNGFhMzE4Y2RjYTEwYzM4OWJmLnNldENvbnRlbnQoaHRtbF83YTMwMjc4MzdlZGU0MjY2OTE4OWJhNDJlZDI2NjUxZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85ZTllYTM4MDc2YzA0ZGJlYmM3MzcxYWE2N2IwZmQwNC5iaW5kUG9wdXAocG9wdXBfYmUxODM4ZTc4MGM1NGM0YWEzMThjZGNhMTBjMzg5YmYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNmUwYmI0YzhmYjZhNGJmY2JhYzIzNzlmY2JmNWMyNDggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MjUyNjM3ODIxNjUwMywtNzMuODQ0NDc1MDA3ODg5ODNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWVkMDQ5OGIxZTM1NDljZjk1MTk3NTNmOGFhZDQxZWIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNjBlYjJjMjcwOTNjNDYzYTgyMjc4YTE4YWJhMWU0MmYgPSAkKCc8ZGl2IGlkPSJodG1sXzYwZWIyYzI3MDkzYzQ2M2E4MjI3OGExOGFiYTFlNDJmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Gb3Jlc3QgSGlsbHMsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYWVkMDQ5OGIxZTM1NDljZjk1MTk3NTNmOGFhZDQxZWIuc2V0Q29udGVudChodG1sXzYwZWIyYzI3MDkzYzQ2M2E4MjI3OGExOGFiYTFlNDJmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzZlMGJiNGM4ZmI2YTRiZmNiYWMyMzc5ZmNiZjVjMjQ4LmJpbmRQb3B1cChwb3B1cF9hZWQwNDk4YjFlMzU0OWNmOTUxOTc1M2Y4YWFkNDFlYik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81MzJjY2Y2NjU3OGE0YjY4OTQyZWVjMGQ1ZTFiYWFkZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcwNTE3OTAzNTQxNDgsLTczLjgyOTgxOTA1ODI1NzAzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzE4NzZjOWM1MjgzMDQ2M2RhMzhhNTkwOThmMGE4ZTM3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzMxZDU1MWVjN2ZhZTQyN2JiNWRhNmIzYTUzN2QzNTc4ID0gJCgnPGRpdiBpZD0iaHRtbF8zMWQ1NTFlYzdmYWU0MjdiYjVkYTZiM2E1MzdkMzU3OCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+S2V3IEdhcmRlbnMsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMTg3NmM5YzUyODMwNDYzZGEzOGE1OTA5OGYwYThlMzcuc2V0Q29udGVudChodG1sXzMxZDU1MWVjN2ZhZTQyN2JiNWRhNmIzYTUzN2QzNTc4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzUzMmNjZjY2NTc4YTRiNjg5NDJlZWMwZDVlMWJhYWRlLmJpbmRQb3B1cChwb3B1cF8xODc2YzljNTI4MzA0NjNkYTM4YTU5MDk4ZjBhOGUzNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jYzcxZjlmNDkxNzg0YjI1YTQxOGIwNzE2YmMxMDA2NCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY5Nzk0NzMxNDcxNzYzLC03My44MzE4MzMyMTQ0Njg4N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83ODU3ZTVjM2MzMzU0Zjc4YjM4MzRmZWY1NjAwMGRkMyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83OGNlM2QwNTIwZmQ0YTYyYWJiZWM3YjllNTRkOWI5OCA9ICQoJzxkaXYgaWQ9Imh0bWxfNzhjZTNkMDUyMGZkNGE2MmFiYmVjN2I5ZTU0ZDliOTgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJpY2htb25kIEhpbGwsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNzg1N2U1YzNjMzM1NGY3OGIzODM0ZmVmNTYwMDBkZDMuc2V0Q29udGVudChodG1sXzc4Y2UzZDA1MjBmZDRhNjJhYmJlYzdiOWU1NGQ5Yjk4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2NjNzFmOWY0OTE3ODRiMjVhNDE4YjA3MTZiYzEwMDY0LmJpbmRQb3B1cChwb3B1cF83ODU3ZTVjM2MzMzU0Zjc4YjM4MzRmZWY1NjAwMGRkMyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80NWI4ZWU1MGE2NTg0MTgwYTM2ODE0YWNmZGYwNGE0YiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc2NDQ1NDE5Njk3ODQ2LC03My44MzE3NzMwMDMyOTU4Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jMGRmYWI2NDI4MTk0ODFmYWJmMmYzNGE0YWNlMzA1NSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mNjZjZjI0OTVjMTc0YTIyYmVmNTM4MjlhM2EwMDYzZiA9ICQoJzxkaXYgaWQ9Imh0bWxfZjY2Y2YyNDk1YzE3NGEyMmJlZjUzODI5YTNhMDA2M2YiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZsdXNoaW5nLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2MwZGZhYjY0MjgxOTQ4MWZhYmYyZjM0YTRhY2UzMDU1LnNldENvbnRlbnQoaHRtbF9mNjZjZjI0OTVjMTc0YTIyYmVmNTM4MjlhM2EwMDYzZik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80NWI4ZWU1MGE2NTg0MTgwYTM2ODE0YWNmZGYwNGE0Yi5iaW5kUG9wdXAocG9wdXBfYzBkZmFiNjQyODE5NDgxZmFiZjJmMzRhNGFjZTMwNTUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDhjM2RmMmE1MmQyNGFiM2EyMDMwYzc3MTYzZjEyYTkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NTAyMTczNDYxMDUyOCwtNzMuOTM5MjAyMjM5MTU1MDVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNmI1MjZmMTRhMTIwNDFiMjk2ZjhiYjk3NmJiNTc1OTMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNWI5YjMxMWI0ODg0NDJkYWFjZTBjMTk3Njk1YzI3MWYgPSAkKCc8ZGl2IGlkPSJodG1sXzViOWIzMTFiNDg4NDQyZGFhY2UwYzE5NzY5NWMyNzFmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Mb25nIElzbGFuZCBDaXR5LCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzZiNTI2ZjE0YTEyMDQxYjI5NmY4YmI5NzZiYjU3NTkzLnNldENvbnRlbnQoaHRtbF81YjliMzExYjQ4ODQ0MmRhYWNlMGMxOTc2OTVjMjcxZik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kOGMzZGYyYTUyZDI0YWIzYTIwMzBjNzcxNjNmMTJhOS5iaW5kUG9wdXAocG9wdXBfNmI1MjZmMTRhMTIwNDFiMjk2ZjhiYjk3NmJiNTc1OTMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMGNjYTQ2YzA4OWFkNGVmOTgyZGFhNjExOTBiMDgxNzUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NDAxNzYyODM1MTkyNCwtNzMuOTI2OTE2MTc1NjE1NzddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjA0MTU4Nzk5YjQ3NDM4NWEzMDE1ZDRmMDM3OTg0ODYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDgzODcxMzcyMDBkNGRmMzk4ZTFiZTYzNzllMTNmMjQgPSAkKCc8ZGl2IGlkPSJodG1sX2Q4Mzg3MTM3MjAwZDRkZjM5OGUxYmU2Mzc5ZTEzZjI0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdW5ueXNpZGUsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNjA0MTU4Nzk5YjQ3NDM4NWEzMDE1ZDRmMDM3OTg0ODYuc2V0Q29udGVudChodG1sX2Q4Mzg3MTM3MjAwZDRkZjM5OGUxYmU2Mzc5ZTEzZjI0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzBjY2E0NmMwODlhZDRlZjk4MmRhYTYxMTkwYjA4MTc1LmJpbmRQb3B1cChwb3B1cF82MDQxNTg3OTliNDc0Mzg1YTMwMTVkNGYwMzc5ODQ4Nik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yODMyZjM1YmZhOTA0NTBkOGE2NGJiOTliOTgxYzRiNSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc2NDA3MzIzODgzMDkxLC03My44NjcwNDE0NzY1ODc3Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xZjM1ODUzODg3OTU0NzA0YTg5Y2Q4ZmVmYWIzZTFlMCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81MGQwNmFjOWVjNjY0ODMxOGY0MzY3OTEwZWQ0OGRkNCA9ICQoJzxkaXYgaWQ9Imh0bWxfNTBkMDZhYzllYzY2NDgzMThmNDM2NzkxMGVkNDhkZDQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVhc3QgRWxtaHVyc3QsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMWYzNTg1Mzg4Nzk1NDcwNGE4OWNkOGZlZmFiM2UxZTAuc2V0Q29udGVudChodG1sXzUwZDA2YWM5ZWM2NjQ4MzE4ZjQzNjc5MTBlZDQ4ZGQ0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzI4MzJmMzViZmE5MDQ1MGQ4YTY0YmI5OWI5ODFjNGI1LmJpbmRQb3B1cChwb3B1cF8xZjM1ODUzODg3OTU0NzA0YTg5Y2Q4ZmVmYWIzZTFlMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81NGE4Njg2MjgyYTY0N2E2YmZjNTgzMDUzYWRlNDFhMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcyNTQyNzM3NDA5MzYwNiwtNzMuODk2MjE3MTM2MjY4NTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjc5N2UwNGU1NWMxNGJmYzgxZTVkOGQxMGU4NTBlODEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTBhYWNmNDdjNWNkNDczN2I2YmQ1ZmVlOTFjYzEwNDMgPSAkKCc8ZGl2IGlkPSJodG1sX2UwYWFjZjQ3YzVjZDQ3MzdiNmJkNWZlZTkxY2MxMDQzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NYXNwZXRoLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzY3OTdlMDRlNTVjMTRiZmM4MWU1ZDhkMTBlODUwZTgxLnNldENvbnRlbnQoaHRtbF9lMGFhY2Y0N2M1Y2Q0NzM3YjZiZDVmZWU5MWNjMTA0Myk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81NGE4Njg2MjgyYTY0N2E2YmZjNTgzMDUzYWRlNDFhMS5iaW5kUG9wdXAocG9wdXBfNjc5N2UwNGU1NWMxNGJmYzgxZTVkOGQxMGU4NTBlODEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzdlZmI0NGIwNWMyNGExYWI0ZmRkYjhkY2Q4NWE5NTMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MDgzMjMxNTYxMzg1OCwtNzMuOTAxNDM1MTc1NTk1ODldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjRmNDA2MDZmZDQ1NDk0NjgxMzI3YmU3Nzc0ODAwMTYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMGE0ZGNiYTI5Y2Y0NDNhNDhmNTZkZWE1MTIxNDhkZjMgPSAkKCc8ZGl2IGlkPSJodG1sXzBhNGRjYmEyOWNmNDQzYTQ4ZjU2ZGVhNTEyMTQ4ZGYzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5SaWRnZXdvb2QsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNjRmNDA2MDZmZDQ1NDk0NjgxMzI3YmU3Nzc0ODAwMTYuc2V0Q29udGVudChodG1sXzBhNGRjYmEyOWNmNDQzYTQ4ZjU2ZGVhNTEyMTQ4ZGYzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzM3ZWZiNDRiMDVjMjRhMWFiNGZkZGI4ZGNkODVhOTUzLmJpbmRQb3B1cChwb3B1cF82NGY0MDYwNmZkNDU0OTQ2ODEzMjdiZTc3NzQ4MDAxNik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83NWJmNjY1NjIwZDg0NTZiYjdmODJmMTUyZjBhNzQ3MCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcwMjc2MjQyOTY3ODM4LC03My44NzA3NDE2NzQzNTYwNV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yNTNjMmY0YmEzN2E0YTE3YTA2YTIxMWU5MzY4MTNiYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mZjdmNGY0YTA0YjE0ZTYwYjE5MTkxZjE2YmY3M2NiMyA9ICQoJzxkaXYgaWQ9Imh0bWxfZmY3ZjRmNGEwNGIxNGU2MGIxOTE5MWYxNmJmNzNjYjMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkdsZW5kYWxlLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzI1M2MyZjRiYTM3YTRhMTdhMDZhMjExZTkzNjgxM2JhLnNldENvbnRlbnQoaHRtbF9mZjdmNGY0YTA0YjE0ZTYwYjE5MTkxZjE2YmY3M2NiMyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83NWJmNjY1NjIwZDg0NTZiYjdmODJmMTUyZjBhNzQ3MC5iaW5kUG9wdXAocG9wdXBfMjUzYzJmNGJhMzdhNGExN2EwNmEyMTFlOTM2ODEzYmEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNGZkNzBiNjFhMDQ0NGNjNWFlNjFlMDQ2MWI2ZTY4MzAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43Mjg5NzQwOTQ4MDczNSwtNzMuODU3ODI2ODY5MDUzN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82ZGVkOTE3ZTNiMzU0NzdkYTc2YzNmMzU3NGEwZTBlNiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mMzJmYWE3ZTYyOWM0ODkxYTYzMjQ0NmQ3NmZmNTUzZCA9ICQoJzxkaXYgaWQ9Imh0bWxfZjMyZmFhN2U2MjljNDg5MWE2MzI0NDZkNzZmZjU1M2QiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJlZ28gUGFyaywgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82ZGVkOTE3ZTNiMzU0NzdkYTc2YzNmMzU3NGEwZTBlNi5zZXRDb250ZW50KGh0bWxfZjMyZmFhN2U2MjljNDg5MWE2MzI0NDZkNzZmZjU1M2QpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNGZkNzBiNjFhMDQ0NGNjNWFlNjFlMDQ2MWI2ZTY4MzAuYmluZFBvcHVwKHBvcHVwXzZkZWQ5MTdlM2IzNTQ3N2RhNzZjM2YzNTc0YTBlMGU2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Q5NWExNDlhYmU3ZDRkNzE5OTdjNzQ4MTFkOWFlZDgyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjg5ODg2ODc5MTU3ODksLTczLjg1ODExMDQ2NTU0MzJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMmMxMTI0NjMzMzQ3NDI4NGE1MmRlYWUzNzJiNGI1MzAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDAwMDY3Y2RjZmRlNGY2YWFjZDEwYjc0ZjczZDYxNWMgPSAkKCc8ZGl2IGlkPSJodG1sX2QwMDA2N2NkY2ZkZTRmNmFhY2QxMGI3NGY3M2Q2MTVjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Xb29kaGF2ZW4sIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMmMxMTI0NjMzMzQ3NDI4NGE1MmRlYWUzNzJiNGI1MzAuc2V0Q29udGVudChodG1sX2QwMDA2N2NkY2ZkZTRmNmFhY2QxMGI3NGY3M2Q2MTVjKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Q5NWExNDlhYmU3ZDRkNzE5OTdjNzQ4MTFkOWFlZDgyLmJpbmRQb3B1cChwb3B1cF8yYzExMjQ2MzMzNDc0Mjg0YTUyZGVhZTM3MmI0YjUzMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85MWYwZmY4MzAxNjE0OWExODQxY2VlMGZkYzdmNjQ3NiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY4MDcwODQ2ODI2NTQxNSwtNzMuODQzMjAyNjYxNzM0NDddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYjMzZWY1YjNhZmVmNDM1M2I4NzIzYTY4MjZkMDdkZTYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfM2ZkZmIyNTcyMGIzNDVkYWI0YmY1YWFiNzc2NDIyOWUgPSAkKCc8ZGl2IGlkPSJodG1sXzNmZGZiMjU3MjBiMzQ1ZGFiNGJmNWFhYjc3NjQyMjllIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Pem9uZSBQYXJrLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2IzM2VmNWIzYWZlZjQzNTNiODcyM2E2ODI2ZDA3ZGU2LnNldENvbnRlbnQoaHRtbF8zZmRmYjI1NzIwYjM0NWRhYjRiZjVhYWI3NzY0MjI5ZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85MWYwZmY4MzAxNjE0OWExODQxY2VlMGZkYzdmNjQ3Ni5iaW5kUG9wdXAocG9wdXBfYjMzZWY1YjNhZmVmNDM1M2I4NzIzYTY4MjZkMDdkZTYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMGJlNjI0YWYzODM0NGZhNDk1MTRjZTUwYjQ0N2MzYzAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42Njg1NDk1Nzc2NzE5NSwtNzMuODA5ODY0Nzg2NDkwNDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfM2NlMjVlMTAwYWZmNDkzZDljMjU1Y2NlMTY0OTcwMjIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYTdlM2RiMGIyMGNmNDBiNDgwYWRhZjlmZWRmNThjZDYgPSAkKCc8ZGl2IGlkPSJodG1sX2E3ZTNkYjBiMjBjZjQwYjQ4MGFkYWY5ZmVkZjU4Y2Q2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Tb3V0aCBPem9uZSBQYXJrLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzNjZTI1ZTEwMGFmZjQ5M2Q5YzI1NWNjZTE2NDk3MDIyLnNldENvbnRlbnQoaHRtbF9hN2UzZGIwYjIwY2Y0MGI0ODBhZGFmOWZlZGY1OGNkNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wYmU2MjRhZjM4MzQ0ZmE0OTUxNGNlNTBiNDQ3YzNjMC5iaW5kUG9wdXAocG9wdXBfM2NlMjVlMTAwYWZmNDkzZDljMjU1Y2NlMTY0OTcwMjIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzY1YmJmNTg0MGZiNGYyN2IxODUxODQyOTE3YzQzZmUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43ODQ5MDI3NDkyNjAyMDUsLTczLjg0MzA0NTI4ODk2MTI1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzYwZTM5ZTQ5YzY0MDQ5NDNhMGFhZDhlM2JmZTdkMTkzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzdmYjhhZDdlNmE2ZjQ0OTFhMTk4ZTk1ZjllMThlZDQxID0gJCgnPGRpdiBpZD0iaHRtbF83ZmI4YWQ3ZTZhNmY0NDkxYTE5OGU5NWY5ZTE4ZWQ0MSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q29sbGVnZSBQb2ludCwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82MGUzOWU0OWM2NDA0OTQzYTBhYWQ4ZTNiZmU3ZDE5My5zZXRDb250ZW50KGh0bWxfN2ZiOGFkN2U2YTZmNDQ5MWExOThlOTVmOWUxOGVkNDEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzY1YmJmNTg0MGZiNGYyN2IxODUxODQyOTE3YzQzZmUuYmluZFBvcHVwKHBvcHVwXzYwZTM5ZTQ5YzY0MDQ5NDNhMGFhZDhlM2JmZTdkMTkzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Y2OGRiOGYwMTk0ODQ1MDNiNzI5MTJhNGU3MjhkYTcwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzgxMjkwNzY2MDI2OTQsLTczLjgxNDIwMjE2NjEwODYzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzA3MjUyNTY5NzdkMTRiZTA5MTdlOTJmMmQyMzZjM2EzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzgwODI4YWFhN2MzZDQ4MTc4MGNjNTE4MTI5MDM4NDhlID0gJCgnPGRpdiBpZD0iaHRtbF84MDgyOGFhYTdjM2Q0ODE3ODBjYzUxODEyOTAzODQ4ZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V2hpdGVzdG9uZSwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wNzI1MjU2OTc3ZDE0YmUwOTE3ZTkyZjJkMjM2YzNhMy5zZXRDb250ZW50KGh0bWxfODA4MjhhYWE3YzNkNDgxNzgwY2M1MTgxMjkwMzg0OGUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZjY4ZGI4ZjAxOTQ4NDUwM2I3MjkxMmE0ZTcyOGRhNzAuYmluZFBvcHVwKHBvcHVwXzA3MjUyNTY5NzdkMTRiZTA5MTdlOTJmMmQyMzZjM2EzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2UzYjg4YzUwNTgyZjRhMGNiNmRlMzc1ZGRkZjFhMjY5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzY2MDQwNjMyODEwNjQsLTczLjc3NDI3MzYzMDY4NjddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMmZmOTRlMjZiNTdmNDAzYTkxZWQ2YTBlMDJjMDIwOTIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMjg3NGRhYzM2YTc4NDFhMjgxZDI0NGNmMmVkZDlkM2IgPSAkKCc8ZGl2IGlkPSJodG1sXzI4NzRkYWMzNmE3ODQxYTI4MWQyNDRjZjJlZGQ5ZDNiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CYXlzaWRlLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzJmZjk0ZTI2YjU3ZjQwM2E5MWVkNmEwZTAyYzAyMDkyLnNldENvbnRlbnQoaHRtbF8yODc0ZGFjMzZhNzg0MWEyODFkMjQ0Y2YyZWRkOWQzYik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lM2I4OGM1MDU4MmY0YTBjYjZkZTM3NWRkZGYxYTI2OS5iaW5kUG9wdXAocG9wdXBfMmZmOTRlMjZiNTdmNDAzYTkxZWQ2YTBlMDJjMDIwOTIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNjVkMjBkNjg5MmJjNGQ4ZjgwMWM1ODBiMDY5M2NiOWIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NjE3Mjk1NDkwMzI2MiwtNzMuNzkxNzYyNDM3MjgwNjFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNzE0MmNjNWZjNzMwNDM3MzgyNDc1MWExNWFiODkxY2QgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjZlNjAwOWMxMmU0NGIyNGE3M2NiMTYwN2ZjY2UyZjYgPSAkKCc8ZGl2IGlkPSJodG1sX2Y2ZTYwMDljMTJlNDRiMjRhNzNjYjE2MDdmY2NlMmY2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5BdWJ1cm5kYWxlLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzcxNDJjYzVmYzczMDQzNzM4MjQ3NTFhMTVhYjg5MWNkLnNldENvbnRlbnQoaHRtbF9mNmU2MDA5YzEyZTQ0YjI0YTczY2IxNjA3ZmNjZTJmNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82NWQyMGQ2ODkyYmM0ZDhmODAxYzU4MGIwNjkzY2I5Yi5iaW5kUG9wdXAocG9wdXBfNzE0MmNjNWZjNzMwNDM3MzgyNDc1MWExNWFiODkxY2QpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOWMzN2E4MjYwZWQ0NDg0YTk2MjUxZjRlYjhiMWMzYmYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NzA4MjYxOTI4MjY3LC03My43Mzg4OTc3NTU4MDc0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzYyNDBmM2NmODFhZTRmZTBiZDdkNTkxYTBjOTYwOTI5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzJhMmJjYTY0Y2UwMDRhZjE5MTY4NDZhY2YwNjNkNmI0ID0gJCgnPGRpdiBpZD0iaHRtbF8yYTJiY2E2NGNlMDA0YWYxOTE2ODQ2YWNmMDYzZDZiNCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TGl0dGxlIE5lY2ssIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNjI0MGYzY2Y4MWFlNGZlMGJkN2Q1OTFhMGM5NjA5Mjkuc2V0Q29udGVudChodG1sXzJhMmJjYTY0Y2UwMDRhZjE5MTY4NDZhY2YwNjNkNmI0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzljMzdhODI2MGVkNDQ4NGE5NjI1MWY0ZWI4YjFjM2JmLmJpbmRQb3B1cChwb3B1cF82MjQwZjNjZjgxYWU0ZmUwYmQ3ZDU5MWEwYzk2MDkyOSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xMjhkN2Y1OGJiMTM0NjRhOGFjMGVjMTY5MzlmZDdjNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc2Njg0NjA5NzkwNzYzLC03My43NDI0OTgyMDcyNzMzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2UwOTkzYTNiMzgzODQyNDFiMTAzYzEwNDcwZmZkZTg5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzc3ZjY4ZmJhODBjMjQ2Y2I4NjY1OWE2YTFiYzdmMWYyID0gJCgnPGRpdiBpZD0iaHRtbF83N2Y2OGZiYTgwYzI0NmNiODY2NTlhNmExYmM3ZjFmMiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RG91Z2xhc3RvbiwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lMDk5M2EzYjM4Mzg0MjQxYjEwM2MxMDQ3MGZmZGU4OS5zZXRDb250ZW50KGh0bWxfNzdmNjhmYmE4MGMyNDZjYjg2NjU5YTZhMWJjN2YxZjIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMTI4ZDdmNThiYjEzNDY0YThhYzBlYzE2OTM5ZmQ3YzQuYmluZFBvcHVwKHBvcHVwX2UwOTkzYTNiMzgzODQyNDFiMTAzYzEwNDcwZmZkZTg5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2I3YmNkNGRkNmQwMzRlOTI4ZjJmMWE1YjA0YzAxOWE1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzQ5NDQwNzk5NzQzMzIsLTczLjcxNTQ4MTE4OTk5MTQ1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzAxYTc2ZGU2MDkyYjRiMmRhMjFjZjAwYjEwZjBhNzNiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzY0MWQyOGUxMDJhODQ2NmU4NWExOGFlNGU5NzZhODEzID0gJCgnPGRpdiBpZD0iaHRtbF82NDFkMjhlMTAyYTg0NjZlODVhMThhZTRlOTc2YTgxMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+R2xlbiBPYWtzLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzAxYTc2ZGU2MDkyYjRiMmRhMjFjZjAwYjEwZjBhNzNiLnNldENvbnRlbnQoaHRtbF82NDFkMjhlMTAyYTg0NjZlODVhMThhZTRlOTc2YTgxMyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iN2JjZDRkZDZkMDM0ZTkyOGYyZjFhNWIwNGMwMTlhNS5iaW5kUG9wdXAocG9wdXBfMDFhNzZkZTYwOTJiNGIyZGEyMWNmMDBiMTBmMGE3M2IpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYWIyMjZhOWQ2YTA0NDIxOWE1MWI2MWE1YTBiNzczNzQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43Mjg1NzMxODE3NjY3NSwtNzMuNzIwMTI4MTQ4MjY5MDNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMTlhMTkwMDk0MGEwNDI2NjgwMDNjMWRlZDljNjY1ZDkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfM2RiMjg2MDUzNmQ2NGJkN2JhZDQ4Y2E1MDQ3MDgxOWMgPSAkKCc8ZGl2IGlkPSJodG1sXzNkYjI4NjA1MzZkNjRiZDdiYWQ0OGNhNTA0NzA4MTljIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CZWxsZXJvc2UsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMTlhMTkwMDk0MGEwNDI2NjgwMDNjMWRlZDljNjY1ZDkuc2V0Q29udGVudChodG1sXzNkYjI4NjA1MzZkNjRiZDdiYWQ0OGNhNTA0NzA4MTljKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2FiMjI2YTlkNmEwNDQyMTlhNTFiNjFhNWEwYjc3Mzc0LmJpbmRQb3B1cChwb3B1cF8xOWExOTAwOTQwYTA0MjY2ODAwM2MxZGVkOWM2NjVkOSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84MWI0M2UzM2JkNWM0YWUzOGRjOWM3MmZjODJhYmQ2YiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcyMjU3ODI0NDIyODA0NiwtNzMuODIwODc3NjQ5MzM1NjZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNWMwNTc2MWNkNDdmNGFlMTg4MjJjNjI5ODc5YzNlM2IgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMWU0NGUyNmM1MzMyNDUwMDk3ZDYwNjgwZTBmNjBhZTggPSAkKCc8ZGl2IGlkPSJodG1sXzFlNDRlMjZjNTMzMjQ1MDA5N2Q2MDY4MGUwZjYwYWU4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5LZXcgR2FyZGVucyBIaWxscywgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81YzA1NzYxY2Q0N2Y0YWUxODgyMmM2Mjk4NzljM2UzYi5zZXRDb250ZW50KGh0bWxfMWU0NGUyNmM1MzMyNDUwMDk3ZDYwNjgwZTBmNjBhZTgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfODFiNDNlMzNiZDVjNGFlMzhkYzljNzJmYzgyYWJkNmIuYmluZFBvcHVwKHBvcHVwXzVjMDU3NjFjZDQ3ZjRhZTE4ODIyYzYyOTg3OWMzZTNiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzFhNmQ2NDgxMTI4ZDQwY2M4OWY5MDljYTY4NDU2NTdmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzM0Mzk0NDY1MzMxMywtNzMuNzgyNzEzMzcwMDMyNjRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMDAxOTcxNzJkZDFkNDFlMjk1YmIxZjVkYTBjNjhkNjAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMmI1MjdkNWM5Yjc3NDg0NGFiYTQ0NDJlNTI5ZjlkOTcgPSAkKCc8ZGl2IGlkPSJodG1sXzJiNTI3ZDVjOWI3NzQ4NDRhYmE0NDQyZTUyOWY5ZDk3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5GcmVzaCBNZWFkb3dzLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzAwMTk3MTcyZGQxZDQxZTI5NWJiMWY1ZGEwYzY4ZDYwLnNldENvbnRlbnQoaHRtbF8yYjUyN2Q1YzliNzc0ODQ0YWJhNDQ0MmU1MjlmOWQ5Nyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xYTZkNjQ4MTEyOGQ0MGNjODlmOTA5Y2E2ODQ1NjU3Zi5iaW5kUG9wdXAocG9wdXBfMDAxOTcxNzJkZDFkNDFlMjk1YmIxZjVkYTBjNjhkNjApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNzdlOWEwOGI5MzU5NDdiMmExMmUxM2NkMDkxYTBhNzMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MTA5MzU0NzI1MjI3MSwtNzMuODExNzQ4MjI0NTg2MzRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYjQwYzcyNjJlMDUzNDZkYzkyMDAxMGJjZjkwYTk3MDYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMGQyZGNmNWU3ODhlNGQwZmFlYWI5NWEyNDY0YTE0OWYgPSAkKCc8ZGl2IGlkPSJodG1sXzBkMmRjZjVlNzg4ZTRkMGZhZWFiOTVhMjQ2NGExNDlmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ccmlhcndvb2QsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjQwYzcyNjJlMDUzNDZkYzkyMDAxMGJjZjkwYTk3MDYuc2V0Q29udGVudChodG1sXzBkMmRjZjVlNzg4ZTRkMGZhZWFiOTVhMjQ2NGExNDlmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzc3ZTlhMDhiOTM1OTQ3YjJhMTJlMTNjZDA5MWEwYTczLmJpbmRQb3B1cChwb3B1cF9iNDBjNzI2MmUwNTM0NmRjOTIwMDEwYmNmOTBhOTcwNik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84MGI5MWU1OTNiZTE0YWRiOGFkMDZlODYzYTRmZTBiOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcwNDY1NzM2MDY4NzE3LC03My43OTY5MDE2NTg4ODI4OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hNjQyZTI4NjlmYjE0YzE1OWY2YjY4NzhiZWZmNjNmMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81YmVlYWQyNmY1MzQ0ZjMxYTVkMzg4MjBhMzY1NjhiYyA9ICQoJzxkaXYgaWQ9Imh0bWxfNWJlZWFkMjZmNTM0NGYzMWE1ZDM4ODIwYTM2NTY4YmMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkphbWFpY2EgQ2VudGVyLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2E2NDJlMjg2OWZiMTRjMTU5ZjZiNjg3OGJlZmY2M2YxLnNldENvbnRlbnQoaHRtbF81YmVlYWQyNmY1MzQ0ZjMxYTVkMzg4MjBhMzY1NjhiYyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84MGI5MWU1OTNiZTE0YWRiOGFkMDZlODYzYTRmZTBiOC5iaW5kUG9wdXAocG9wdXBfYTY0MmUyODY5ZmIxNGMxNTlmNmI2ODc4YmVmZjYzZjEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzQ1YmViZWNiODQ4NDk3OGIxZGI0OTYyODhkOWVkOTQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NDU2MTg1NzE0MTg1NSwtNzMuNzU0OTQ5NzYyMzQzMzJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYjU4ZjRlMjA2ZGRlNGMxMzg4ZTBjMDgxYTM2ZGFmNTAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjZmMjc5OGI2NDQ4NGFhZDljOTBmNTQxNTQ3OWZjMzEgPSAkKCc8ZGl2IGlkPSJodG1sX2Y2ZjI3OThiNjQ0ODRhYWQ5YzkwZjU0MTU0NzlmYzMxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5PYWtsYW5kIEdhcmRlbnMsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjU4ZjRlMjA2ZGRlNGMxMzg4ZTBjMDgxYTM2ZGFmNTAuc2V0Q29udGVudChodG1sX2Y2ZjI3OThiNjQ0ODRhYWQ5YzkwZjU0MTU0NzlmYzMxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2M0NWJlYmVjYjg0ODQ5NzhiMWRiNDk2Mjg4ZDllZDk0LmJpbmRQb3B1cChwb3B1cF9iNThmNGUyMDZkZGU0YzEzODhlMGMwODFhMzZkYWY1MCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85MDkwYjlmNjBhYTU0OTBkOWQzMmY0NDRhM2U5YWQ4ZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcxODg5MzA5MjE2NzM1NiwtNzMuNzM4NzE0ODQ1Nzg0MjRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYjg0ZmQ3MjgxNmQ0NDJiZmJhMTE0OWVmOTA1YmY3YmYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDFlZDA2MWNiYjBkNDA1NmI2NDMzMjBmMmI0ZmVkYjggPSAkKCc8ZGl2IGlkPSJodG1sXzAxZWQwNjFjYmIwZDQwNTZiNjQzMzIwZjJiNGZlZGI4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5RdWVlbnMgVmlsbGFnZSwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iODRmZDcyODE2ZDQ0MmJmYmExMTQ5ZWY5MDViZjdiZi5zZXRDb250ZW50KGh0bWxfMDFlZDA2MWNiYjBkNDA1NmI2NDMzMjBmMmI0ZmVkYjgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTA5MGI5ZjYwYWE1NDkwZDlkMzJmNDQ0YTNlOWFkOGUuYmluZFBvcHVwKHBvcHVwX2I4NGZkNzI4MTZkNDQyYmZiYTExNDllZjkwNWJmN2JmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2ZlZGRmZTBhNWYxODRjYTY5OWMwZmZlNDEzZmM0ODcxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzExMjQzNDQxOTE5MDQsLTczLjc1OTI1MDA5MzM1NTk0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzZlMjViYzM5OTY2NTRkNzg4Y2QyYmM3YWViNDViYTc2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2Q5MzU3ZTg2ZjcwNTRhZDk5Zjc0NjYyNjNjMTViZjQ2ID0gJCgnPGRpdiBpZD0iaHRtbF9kOTM1N2U4NmY3MDU0YWQ5OWY3NDY2MjYzYzE1YmY0NiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SG9sbGlzLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzZlMjViYzM5OTY2NTRkNzg4Y2QyYmM3YWViNDViYTc2LnNldENvbnRlbnQoaHRtbF9kOTM1N2U4NmY3MDU0YWQ5OWY3NDY2MjYzYzE1YmY0Nik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mZWRkZmUwYTVmMTg0Y2E2OTljMGZmZTQxM2ZjNDg3MS5iaW5kUG9wdXAocG9wdXBfNmUyNWJjMzk5NjY1NGQ3ODhjZDJiYzdhZWI0NWJhNzYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNmE1ZjEwYjFmMzcwNDI4YjkwODYwMmYwZjBiYWNkMjggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42OTY5MTEyNTM3ODk4ODUsLTczLjc5MDQyNjEzMTM1NTRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMTg2YzM5YzhmOTRmNDQ5YmI1YjA3YmM0NTg5YTY4ZjggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZGEwYjg0OWVkMDQwNDc3Nzg3ZDcxYjZlMDRjODQxMmMgPSAkKCc8ZGl2IGlkPSJodG1sX2RhMGI4NDllZDA0MDQ3Nzc4N2Q3MWI2ZTA0Yzg0MTJjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Tb3V0aCBKYW1haWNhLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzE4NmMzOWM4Zjk0ZjQ0OWJiNWIwN2JjNDU4OWE2OGY4LnNldENvbnRlbnQoaHRtbF9kYTBiODQ5ZWQwNDA0Nzc3ODdkNzFiNmUwNGM4NDEyYyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82YTVmMTBiMWYzNzA0MjhiOTA4NjAyZjBmMGJhY2QyOC5iaW5kUG9wdXAocG9wdXBfMTg2YzM5YzhmOTRmNDQ5YmI1YjA3YmM0NTg5YTY4ZjgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNDM2NGIxZjUwMWQ1NDQ0ZjgyNGQ5OTA1NmE4YjI0ZGIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42OTQ0NDUzODUyMjM1OSwtNzMuNzU4Njc2MDM3Mjc3MTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNTg3MDhiODliZDBjNDJkYjk5M2YwZjgwZmJiNTFlZjEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZWU5YThiZTE3Nzg5NGY1Zjk4OTcxODkyNzkyYjIxMWEgPSAkKCc8ZGl2IGlkPSJodG1sX2VlOWE4YmUxNzc4OTRmNWY5ODk3MTg5Mjc5MmIyMTFhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdC4gQWxiYW5zLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzU4NzA4Yjg5YmQwYzQyZGI5OTNmMGY4MGZiYjUxZWYxLnNldENvbnRlbnQoaHRtbF9lZTlhOGJlMTc3ODk0ZjVmOTg5NzE4OTI3OTJiMjExYSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80MzY0YjFmNTAxZDU0NDRmODI0ZDk5MDU2YThiMjRkYi5iaW5kUG9wdXAocG9wdXBfNTg3MDhiODliZDBjNDJkYjk5M2YwZjgwZmJiNTFlZjEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzAwODIzYTI4YzY3NDYwZjg0M2M3ODQ5MWQyMDAyYjIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42NzUyMTEzOTU5MTczMywtNzMuNzcyNTg3ODc2MjA5MDZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMTExOGQ2NGJjZGRjNGE2NmEzMzlhZmNlOTAwNjc0MzEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzUwOTE1Nzc4YjE0NGQ4NWExNTg3NjA1MDNkZTYzYzMgPSAkKCc8ZGl2IGlkPSJodG1sXzc1MDkxNTc3OGIxNDRkODVhMTU4NzYwNTAzZGU2M2MzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb2NoZGFsZSwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xMTE4ZDY0YmNkZGM0YTY2YTMzOWFmY2U5MDA2NzQzMS5zZXRDb250ZW50KGh0bWxfNzUwOTE1Nzc4YjE0NGQ4NWExNTg3NjA1MDNkZTYzYzMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMzAwODIzYTI4YzY3NDYwZjg0M2M3ODQ5MWQyMDAyYjIuYmluZFBvcHVwKHBvcHVwXzExMThkNjRiY2RkYzRhNjZhMzM5YWZjZTkwMDY3NDMxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzEwYTUzNWZmOWNhNzQxN2Y5Njk4ZjJmOTdmMjc3MDFmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjY2MjMwNDkwMzY4NTg0LC03My43NjA0MjA5MjY4MjI4N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84ZDMxZDU5M2IyOTI0MDU3YmNhYTVmZTBiZjg2M2M3MyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85Mjg1MDdjZmIxMTI0N2Q5OTJlZDI4NmI1Yjk5ODhhNCA9ICQoJzxkaXYgaWQ9Imh0bWxfOTI4NTA3Y2ZiMTEyNDdkOTkyZWQyODZiNWI5OTg4YTQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlNwcmluZ2ZpZWxkIEdhcmRlbnMsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOGQzMWQ1OTNiMjkyNDA1N2JjYWE1ZmUwYmY4NjNjNzMuc2V0Q29udGVudChodG1sXzkyODUwN2NmYjExMjQ3ZDk5MmVkMjg2YjViOTk4OGE0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzEwYTUzNWZmOWNhNzQxN2Y5Njk4ZjJmOTdmMjc3MDFmLmJpbmRQb3B1cChwb3B1cF84ZDMxZDU5M2IyOTI0MDU3YmNhYTVmZTBiZjg2M2M3Myk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kNzE5MjZkNDlmOGY0MWU2OTBjYWRlOTJmY2E3ZTY1OCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY5Mjc3NDYzOTE2MDg0NSwtNzMuNzM1MjY4NzM3MDgwMjZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOGE2NzU2ODhjNjliNDI4ZjlhOTdmZTJjM2FkYjQ4MjAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDI0MGEzMzgxMmFkNGFlMmI4YzFmNWMzODdlM2UzYjggPSAkKCc8ZGl2IGlkPSJodG1sX2QyNDBhMzM4MTJhZDRhZTJiOGMxZjVjMzg3ZTNlM2I4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DYW1icmlhIEhlaWdodHMsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOGE2NzU2ODhjNjliNDI4ZjlhOTdmZTJjM2FkYjQ4MjAuc2V0Q29udGVudChodG1sX2QyNDBhMzM4MTJhZDRhZTJiOGMxZjVjMzg3ZTNlM2I4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Q3MTkyNmQ0OWY4ZjQxZTY5MGNhZGU5MmZjYTdlNjU4LmJpbmRQb3B1cChwb3B1cF84YTY3NTY4OGM2OWI0MjhmOWE5N2ZlMmMzYWRiNDgyMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iYWJkMjFhZGQ2ZTg0NmFkOWU2NzAzNTJkOGNmY2ZlMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY1OTgxNjQzMzQyODA4NCwtNzMuNzM1MjYwNzk0MjgyNzhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMmI0ZmY4ZDgxOTUyNDI0NGJiZjY3ZGRjYmE0NWRiZWMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYjc2ZThiYTRlZGQ3NDRiNThmZTQ4ODQwZjU5MGZhYWUgPSAkKCc8ZGl2IGlkPSJodG1sX2I3NmU4YmE0ZWRkNzQ0YjU4ZmU0ODg0MGY1OTBmYWFlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb3NlZGFsZSwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yYjRmZjhkODE5NTI0MjQ0YmJmNjdkZGNiYTQ1ZGJlYy5zZXRDb250ZW50KGh0bWxfYjc2ZThiYTRlZGQ3NDRiNThmZTQ4ODQwZjU5MGZhYWUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYmFiZDIxYWRkNmU4NDZhZDllNjcwMzUyZDhjZmNmZTEuYmluZFBvcHVwKHBvcHVwXzJiNGZmOGQ4MTk1MjQyNDRiYmY2N2RkY2JhNDVkYmVjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2M0ZmNkMmVhMmYxMTQ2NDVhM2QyOTU2MGJhMzhkMTdjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjAzMTM0NDMyNTAwODk0LC03My43NTQ5Nzk2ODA0Mzg3Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lYzRmYzhmNWI2ZWU0MTExOGQ4Y2Q4YWNkZWE2YmNiZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jNjQxN2NjYmQ1OWQ0ZmQ1ODYwNDEwODJkY2I2Mjk2ZCA9ICQoJzxkaXYgaWQ9Imh0bWxfYzY0MTdjY2JkNTlkNGZkNTg2MDQxMDgyZGNiNjI5NmQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZhciBSb2NrYXdheSwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lYzRmYzhmNWI2ZWU0MTExOGQ4Y2Q4YWNkZWE2YmNiZS5zZXRDb250ZW50KGh0bWxfYzY0MTdjY2JkNTlkNGZkNTg2MDQxMDgyZGNiNjI5NmQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzRmY2QyZWEyZjExNDY0NWEzZDI5NTYwYmEzOGQxN2MuYmluZFBvcHVwKHBvcHVwX2VjNGZjOGY1YjZlZTQxMTE4ZDhjZDhhY2RlYTZiY2JlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzcwY2ViOTAxMjdkZjRlZTE4NDZhMGQxZDYyMWViODUyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjAzMDI2NTgzNTEyMzgsLTczLjgyMDA1NDg5MTEwMzJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTc2NzJmZmE0MzM2NGVmODlkMWRmODg4MTc1NTk0ZTEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfM2I5OTM0MTQxNmNhNDM3MGI3NTg4ODVlMjk5NGRmYjkgPSAkKCc8ZGl2IGlkPSJodG1sXzNiOTkzNDE0MTZjYTQzNzBiNzU4ODg1ZTI5OTRkZmI5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ccm9hZCBDaGFubmVsLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2E3NjcyZmZhNDMzNjRlZjg5ZDFkZjg4ODE3NTU5NGUxLnNldENvbnRlbnQoaHRtbF8zYjk5MzQxNDE2Y2E0MzcwYjc1ODg4NWUyOTk0ZGZiOSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83MGNlYjkwMTI3ZGY0ZWUxODQ2YTBkMWQ2MjFlYjg1Mi5iaW5kUG9wdXAocG9wdXBfYTc2NzJmZmE0MzM2NGVmODlkMWRmODg4MTc1NTk0ZTEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzQxNjAxOWRmMWY3NGVkNWJjZGE4NWQ3MjExYzExMmEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NTc0MDEyODg0NTQ1MiwtNzMuOTI1NTExOTY5OTQxNjhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNDhjM2U0NWM2ZDM5NGNiYzkwNjMwZDQzZTY5NDYxYTkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfY2Y4YWRmMGJjM2Y2NDgzMGFhNzJlMjZiMzljZjI0OTkgPSAkKCc8ZGl2IGlkPSJodG1sX2NmOGFkZjBiYzNmNjQ4MzBhYTcyZTI2YjM5Y2YyNDk5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CcmVlenkgUG9pbnQsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNDhjM2U0NWM2ZDM5NGNiYzkwNjMwZDQzZTY5NDYxYTkuc2V0Q29udGVudChodG1sX2NmOGFkZjBiYzNmNjQ4MzBhYTcyZTI2YjM5Y2YyNDk5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2M0MTYwMTlkZjFmNzRlZDViY2RhODVkNzIxMWMxMTJhLmJpbmRQb3B1cChwb3B1cF80OGMzZTQ1YzZkMzk0Y2JjOTA2MzBkNDNlNjk0NjFhOSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wYjg2YTZjYjhmNTY0ZDdmYjdjMTdlYWQ5Zjc5ZTI1OCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc3NTkyMzAxNTY0Mjg5NiwtNzMuOTAyMjg5NjAzOTE2NzNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYmQ3YjNlMjRhMzE3NDI1YWExZGU3NWFhNGVmYWVhYTUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZGQwZGUzMGNmMTdlNDAzZTlhZmI5ZDc2Mzg5ZDgxNTQgPSAkKCc8ZGl2IGlkPSJodG1sX2RkMGRlMzBjZjE3ZTQwM2U5YWZiOWQ3NjM4OWQ4MTU0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdGVpbndheSwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iZDdiM2UyNGEzMTc0MjVhYTFkZTc1YWE0ZWZhZWFhNS5zZXRDb250ZW50KGh0bWxfZGQwZGUzMGNmMTdlNDAzZTlhZmI5ZDc2Mzg5ZDgxNTQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMGI4NmE2Y2I4ZjU2NGQ3ZmI3YzE3ZWFkOWY3OWUyNTguYmluZFBvcHVwKHBvcHVwX2JkN2IzZTI0YTMxNzQyNWFhMWRlNzVhYTRlZmFlYWE1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzZkZjFlOTBmOTRmZTQ0MDg5OTA5OGZjZmU0MmNiZTU0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzkyNzgxNDAzNjAwNDgsLTczLjgwNDM2NDUxNzIwOTg4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2M2MDAwOTcyMTA1MjQ2Yjg5ODE0MDEwNTNlYzhkOTI3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzkzOTdhMDNkMDA0NTQyZjZhNDljNGJmZWY3ZWRmMDM4ID0gJCgnPGRpdiBpZD0iaHRtbF85Mzk3YTAzZDAwNDU0MmY2YTQ5YzRiZmVmN2VkZjAzOCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmVlY2hodXJzdCwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jNjAwMDk3MjEwNTI0NmI4OTgxNDAxMDUzZWM4ZDkyNy5zZXRDb250ZW50KGh0bWxfOTM5N2EwM2QwMDQ1NDJmNmE0OWM0YmZlZjdlZGYwMzgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNmRmMWU5MGY5NGZlNDQwODk5MDk4ZmNmZTQyY2JlNTQuYmluZFBvcHVwKHBvcHVwX2M2MDAwOTcyMTA1MjQ2Yjg5ODE0MDEwNTNlYzhkOTI3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzkyMjI0ZjI5Mzk1NzQ5ZTJhNmJiYzE2NWMyOTVlZjJlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzgyODQyODA2MjQ1NTU0LC03My43NzY4MDIyMjYyMTU4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzViZjZhNzhhODRjMzRmYTZiZjBiYWIyNGJkNjExOWFlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzFjMzQwMTQxNTZlMTQ5ZjA4NTA0NTNlNGNmZGYwODM5ID0gJCgnPGRpdiBpZD0iaHRtbF8xYzM0MDE0MTU2ZTE0OWYwODUwNDUzZTRjZmRmMDgzOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmF5IFRlcnJhY2UsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNWJmNmE3OGE4NGMzNGZhNmJmMGJhYjI0YmQ2MTE5YWUuc2V0Q29udGVudChodG1sXzFjMzQwMTQxNTZlMTQ5ZjA4NTA0NTNlNGNmZGYwODM5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzkyMjI0ZjI5Mzk1NzQ5ZTJhNmJiYzE2NWMyOTVlZjJlLmJpbmRQb3B1cChwb3B1cF81YmY2YTc4YTg0YzM0ZmE2YmYwYmFiMjRiZDYxMTlhZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yZWVlNTBlMDc2M2I0MTE5ODMxYzM4MGMwZjAwNDA2YSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU5NTY0MTgwNzM2ODQ5NCwtNzMuNzc2MTMyODIzOTE3MDVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYjRlYTgyZTRkZmY4NDE0MDg2NTZlYzA3ZjQzMzQ5NDIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNmZkYTEyNWZlNjU0NGYwMjhmYTY3NTA4YjQ2MzY1MTggPSAkKCc8ZGl2IGlkPSJodG1sXzZmZGExMjVmZTY1NDRmMDI4ZmE2NzUwOGI0NjM2NTE4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5FZGdlbWVyZSwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iNGVhODJlNGRmZjg0MTQwODY1NmVjMDdmNDMzNDk0Mi5zZXRDb250ZW50KGh0bWxfNmZkYTEyNWZlNjU0NGYwMjhmYTY3NTA4YjQ2MzY1MTgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMmVlZTUwZTA3NjNiNDExOTgzMWMzODBjMGYwMDQwNmEuYmluZFBvcHVwKHBvcHVwX2I0ZWE4MmU0ZGZmODQxNDA4NjU2ZWMwN2Y0MzM0OTQyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzYzNjhmM2Y2MjkyNDRjYWFiOGNjZjVkZjMxNDc1MDU3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTg5MTQzOTQzNzI5NzEsLTczLjc5MTk5MjMzMTM2OTQzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzdhODU2YTk4OWE5NDQyNjI4ZWFlMDU0YTFiZDhkN2NjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2M2NjcyZTA2NThiMTQ1NWI5ZWFlNTJiMGZmZjg0YTY3ID0gJCgnPGRpdiBpZD0iaHRtbF9jNjY3MmUwNjU4YjE0NTViOWVhZTUyYjBmZmY4NGE2NyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QXJ2ZXJuZSwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83YTg1NmE5ODlhOTQ0MjYyOGVhZTA1NGExYmQ4ZDdjYy5zZXRDb250ZW50KGh0bWxfYzY2NzJlMDY1OGIxNDU1YjllYWU1MmIwZmZmODRhNjcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNjM2OGYzZjYyOTI0NGNhYWI4Y2NmNWRmMzE0NzUwNTcuYmluZFBvcHVwKHBvcHVwXzdhODU2YTk4OWE5NDQyNjI4ZWFlMDU0YTFiZDhkN2NjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzk4ZjFmMjc0OTI5MTQ2YTFiZTZiMzJlODY5ZmUyYTYwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTgyODAxNjk2ODQ1NTg2LC03My44MjIzNjEyMTA4ODc1MV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84NzNhZmU3Yzg0ZDI0MWRkOTk4ZjhlYWEyZDlhYTM5YSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83MDExOTlhZWM1NGI0NzBhODk2NDg2NjJlMDk1ODY1ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfNzAxMTk5YWVjNTRiNDcwYTg5NjQ4NjYyZTA5NTg2NWYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJvY2thd2F5IEJlYWNoLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzg3M2FmZTdjODRkMjQxZGQ5OThmOGVhYTJkOWFhMzlhLnNldENvbnRlbnQoaHRtbF83MDExOTlhZWM1NGI0NzBhODk2NDg2NjJlMDk1ODY1Zik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85OGYxZjI3NDkyOTE0NmExYmU2YjMyZTg2OWZlMmE2MC5iaW5kUG9wdXAocG9wdXBfODczYWZlN2M4NGQyNDFkZDk5OGY4ZWFhMmQ5YWEzOWEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNzcyMWEzNjdjZjRjNGZkODk0MDA0YTUzMzczYWY0ZDkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NzIwMzY3MzAyMTcwMTUsLTczLjg1NzU0NjcyNDEwODI3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzhjOWVhMjk1YjZmZDQzODlhZjg5OTA4ZTU5OWYxYzA5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzhlNDRmN2RhMjkwZjQzZmRhZDdlOTFkMDkyZGNiZmEyID0gJCgnPGRpdiBpZD0iaHRtbF84ZTQ0ZjdkYTI5MGY0M2ZkYWQ3ZTkxZDA5MmRjYmZhMiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TmVwb25zaXQsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOGM5ZWEyOTViNmZkNDM4OWFmODk5MDhlNTk5ZjFjMDkuc2V0Q29udGVudChodG1sXzhlNDRmN2RhMjkwZjQzZmRhZDdlOTFkMDkyZGNiZmEyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzc3MjFhMzY3Y2Y0YzRmZDg5NDAwNGE1MzM3M2FmNGQ5LmJpbmRQb3B1cChwb3B1cF84YzllYTI5NWI2ZmQ0Mzg5YWY4OTkwOGU1OTlmMWMwOSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84ZTAwMmZlYzYwMTk0ZTgxYTc4MjY0ZTY2MWIzMjBiNSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc2NDEyNjEyMjYxNDA2NiwtNzMuODEyNzYyNjkxMzU4NjZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzk1YTQ4NDBmMWMwNDYxZGE4MDMyMzZjNTZlYTI0MWQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDdhYTQ5Y2U3YTliNGUxOWFmMTE3MmYxNTA2NTZkMGQgPSAkKCc8ZGl2IGlkPSJodG1sXzA3YWE0OWNlN2E5YjRlMTlhZjExNzJmMTUwNjU2ZDBkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NdXJyYXkgSGlsbCwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zOTVhNDg0MGYxYzA0NjFkYTgwMzIzNmM1NmVhMjQxZC5zZXRDb250ZW50KGh0bWxfMDdhYTQ5Y2U3YTliNGUxOWFmMTE3MmYxNTA2NTZkMGQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOGUwMDJmZWM2MDE5NGU4MWE3ODI2NGU2NjFiMzIwYjUuYmluZFBvcHVwKHBvcHVwXzM5NWE0ODQwZjFjMDQ2MWRhODAzMjM2YzU2ZWEyNDFkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzY5NjlmN2M4ZjBlMzRkNzg5YTg4NmY5N2ZjOGE0MWMxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzQxMzc4NDIxOTQ1NDM0LC03My43MDg4NDcwNTg4OTI0Nl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yMTRiYmM0MGNlMDc0OWE2YWU2ZGY2MzBkNTIxYzAxOSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yOWFiNmMzM2VjMDQ0MjY0YjQzMzkzYjEyZDczNDI2MiA9ICQoJzxkaXYgaWQ9Imh0bWxfMjlhYjZjMzNlYzA0NDI2NGI0MzM5M2IxMmQ3MzQyNjIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZsb3JhbCBQYXJrLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzIxNGJiYzQwY2UwNzQ5YTZhZTZkZjYzMGQ1MjFjMDE5LnNldENvbnRlbnQoaHRtbF8yOWFiNmMzM2VjMDQ0MjY0YjQzMzkzYjEyZDczNDI2Mik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82OTY5ZjdjOGYwZTM0ZDc4OWE4ODZmOTdmYzhhNDFjMS5iaW5kUG9wdXAocG9wdXBfMjE0YmJjNDBjZTA3NDlhNmFlNmRmNjMwZDUyMWMwMTkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZjgwZDA3NWU4YTBjNDM3NGEwMTgxMWE2MTA2OWU2ZmIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MjA5NTcyMDc2NDQ0LC03My43NjcxNDE2NjcxNDcyOV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zYzI1ZjVhMTk0Yzk0ODM1YmY0ZjQxNGJkYTc4ZTAxMCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yMTkyODFhMzg3MzA0ODNlOGM2M2E1MzU4M2JiY2ZhNSA9ICQoJzxkaXYgaWQ9Imh0bWxfMjE5MjgxYTM4NzMwNDgzZThjNjNhNTM1ODNiYmNmYTUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkhvbGxpc3dvb2QsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfM2MyNWY1YTE5NGM5NDgzNWJmNGY0MTRiZGE3OGUwMTAuc2V0Q29udGVudChodG1sXzIxOTI4MWEzODczMDQ4M2U4YzYzYTUzNTgzYmJjZmE1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Y4MGQwNzVlOGEwYzQzNzRhMDE4MTFhNjEwNjllNmZiLmJpbmRQb3B1cChwb3B1cF8zYzI1ZjVhMTk0Yzk0ODM1YmY0ZjQxNGJkYTc4ZTAxMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80NmRmMzM1NjE1YTk0YzA3ODVmOGQxN2QzNzUwZTNjYyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcxNjgwNDgzMDE0NjEzLC03My43ODcyMjY5NjkzNjY2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzRmODVmMDhlNTI3ZjQyMGU5N2NjYTc5OWY5OTNlNzEwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzEyOTM1ODA4N2QzNTRiYTg4ZTI4NjQ2MGM5YjJlM2JiID0gJCgnPGRpdiBpZD0iaHRtbF8xMjkzNTgwODdkMzU0YmE4OGUyODY0NjBjOWIyZTNiYiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SmFtYWljYSBFc3RhdGVzLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzRmODVmMDhlNTI3ZjQyMGU5N2NjYTc5OWY5OTNlNzEwLnNldENvbnRlbnQoaHRtbF8xMjkzNTgwODdkMzU0YmE4OGUyODY0NjBjOWIyZTNiYik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80NmRmMzM1NjE1YTk0YzA3ODVmOGQxN2QzNzUwZTNjYy5iaW5kUG9wdXAocG9wdXBfNGY4NWYwOGU1MjdmNDIwZTk3Y2NhNzk5Zjk5M2U3MTApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTUyZDIyY2NjMjcwNGJkZjllNTlmYWEzOWViMzliYmIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NDQ1NzIzMDkyODY3LC03My44MjU4MDkxNTExMDU1OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mMjhiZjFmMTdhYTk0MjEzYmU4MzkzZWMwYWFiMzAwMyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yMGZiODlhNzdmZmE0YmZiYmIxYjFjODViZTE4OTA2OSA9ICQoJzxkaXYgaWQ9Imh0bWxfMjBmYjg5YTc3ZmZhNGJmYmJiMWIxYzg1YmUxODkwNjkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlF1ZWVuc2Jvcm8gSGlsbCwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mMjhiZjFmMTdhYTk0MjEzYmU4MzkzZWMwYWFiMzAwMy5zZXRDb250ZW50KGh0bWxfMjBmYjg5YTc3ZmZhNGJmYmJiMWIxYzg1YmUxODkwNjkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYTUyZDIyY2NjMjcwNGJkZjllNTlmYWEzOWViMzliYmIuYmluZFBvcHVwKHBvcHVwX2YyOGJmMWYxN2FhOTQyMTNiZTgzOTNlYzBhYWIzMDAzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2FiNTIxNGNmYTNjYTRlYjZhZWEzMDJjNTJhZjA0MTMwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzIzODI0OTAxODI5MjA0LC03My43OTc2MDMwMDkxMjY3Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81Y2Y3ZGRmODBlNzM0M2VjYjM3NzI3M2RlNzBiZmRkZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wZTQyYTljMjYxZTc0MmY5OWY1MmYyMzQ2NWFhZTQ3MSA9ICQoJzxkaXYgaWQ9Imh0bWxfMGU0MmE5YzI2MWU3NDJmOTlmNTJmMjM0NjVhYWU0NzEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkhpbGxjcmVzdCwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81Y2Y3ZGRmODBlNzM0M2VjYjM3NzI3M2RlNzBiZmRkZi5zZXRDb250ZW50KGh0bWxfMGU0MmE5YzI2MWU3NDJmOTlmNTJmMjM0NjVhYWU0NzEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYWI1MjE0Y2ZhM2NhNGViNmFlYTMwMmM1MmFmMDQxMzAuYmluZFBvcHVwKHBvcHVwXzVjZjdkZGY4MGU3MzQzZWNiMzc3MjczZGU3MGJmZGRmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzg0MjM0ZWMxN2FkMDQzMDE4YjEzMjA5NDVlOTA0ZTQwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzYxNzA0NTI2MDU0MTQ2LC03My45MzE1NzUwNjA3Mjg3OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9kMjJmZGFhODYyN2E0Yzc3YWRhNGJiM2U4MWMyNTUwNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wYjYxNzUxYTc3OTg0OTRiOGJiNTllZDdiNWE0NjVlNyA9ICQoJzxkaXYgaWQ9Imh0bWxfMGI2MTc1MWE3Nzk4NDk0YjhiYjU5ZWQ3YjVhNDY1ZTciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJhdmVuc3dvb2QsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZDIyZmRhYTg2MjdhNGM3N2FkYTRiYjNlODFjMjU1MDQuc2V0Q29udGVudChodG1sXzBiNjE3NTFhNzc5ODQ5NGI4YmI1OWVkN2I1YTQ2NWU3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzg0MjM0ZWMxN2FkMDQzMDE4YjEzMjA5NDVlOTA0ZTQwLmJpbmRQb3B1cChwb3B1cF9kMjJmZGFhODYyN2E0Yzc3YWRhNGJiM2U4MWMyNTUwNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83MzIxYjhhZDViYzk0YWExYTI2ZWExYzczNWE4YzYyNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY2MzkxODQxOTI1MTM5LC03My44NDk2Mzc4MjQwMjQ0MV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83OWU4ZDczNzI2OTM0ODYxOTcwMDdlYmI0YTVlYThiMyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xNmU0ZDhmZjQxODc0YzVmYjc2ZTlhYzNlOTExZjg2YyA9ICQoJzxkaXYgaWQ9Imh0bWxfMTZlNGQ4ZmY0MTg3NGM1ZmI3NmU5YWMzZTkxMWY4NmMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxpbmRlbndvb2QsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNzllOGQ3MzcyNjkzNDg2MTk3MDA3ZWJiNGE1ZWE4YjMuc2V0Q29udGVudChodG1sXzE2ZTRkOGZmNDE4NzRjNWZiNzZlOWFjM2U5MTFmODZjKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzczMjFiOGFkNWJjOTRhYTFhMjZlYTFjNzM1YThjNjI3LmJpbmRQb3B1cChwb3B1cF83OWU4ZDczNzI2OTM0ODYxOTcwMDdlYmI0YTVlYThiMyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xNWZkYzQwOGZiMjU0Y2QzOWViNDhmMzc5MzIxN2NlZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY2Nzg4Mzg5NjYwMjQ3LC03My43NDAyNTYwNzk4OTgyMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81YmIyN2E3Yzg1NzA0NTYxOWIxMzhiYzUxMmYxMzcyOSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81ZDBjYmY2OTVmZGQ0ZTJjOGIyZGIzODg4YWFkNjIyMCA9ICQoJzxkaXYgaWQ9Imh0bWxfNWQwY2JmNjk1ZmRkNGUyYzhiMmRiMzg4OGFhZDYyMjAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxhdXJlbHRvbiwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81YmIyN2E3Yzg1NzA0NTYxOWIxMzhiYzUxMmYxMzcyOS5zZXRDb250ZW50KGh0bWxfNWQwY2JmNjk1ZmRkNGUyYzhiMmRiMzg4OGFhZDYyMjApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMTVmZGM0MDhmYjI1NGNkMzllYjQ4ZjM3OTMyMTdjZWQuYmluZFBvcHVwKHBvcHVwXzViYjI3YTdjODU3MDQ1NjE5YjEzOGJjNTEyZjEzNzI5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzVhMmJmMWNmZWI5ODQ2YmQ4NDhjMDYzYjAyY2U1ZGE1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzM2MDc0NTcwODMwNzk1LC03My44NjI1MjQ3MTQxMzc0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzc4NjdiNWEwMWQ5NTQyOTBhOTliODcxMjQ2NzM4MTVhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzE1MWIwNTBlNDBiYjQxNmNiODFlMDQ0ODA3ZWQ0ZjRmID0gJCgnPGRpdiBpZD0iaHRtbF8xNTFiMDUwZTQwYmI0MTZjYjgxZTA0NDgwN2VkNGY0ZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TGVmcmFrIENpdHksIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNzg2N2I1YTAxZDk1NDI5MGE5OWI4NzEyNDY3MzgxNWEuc2V0Q29udGVudChodG1sXzE1MWIwNTBlNDBiYjQxNmNiODFlMDQ0ODA3ZWQ0ZjRmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzVhMmJmMWNmZWI5ODQ2YmQ4NDhjMDYzYjAyY2U1ZGE1LmJpbmRQb3B1cChwb3B1cF83ODY3YjVhMDFkOTU0MjkwYTk5Yjg3MTI0NjczODE1YSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83ODAwMWI2NTlmNDA0MzZhOWIyMjg4YTJlNzc4OGU2YiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU3NjE1NTU2NTQzMTA5LC03My44NTQwMTc1MDM5MjUyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzRiNGYwNTRmNTNkMDQ1ZDhhMzdmNjc2NDU5Mzg0ZWQwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2E3YmM4ZjQ4YjM3YzQ5ZjNiMGExMjNlYmZiZTJiM2MzID0gJCgnPGRpdiBpZD0iaHRtbF9hN2JjOGY0OGIzN2M0OWYzYjBhMTIzZWJmYmUyYjNjMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmVsbGUgSGFyYm9yLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzRiNGYwNTRmNTNkMDQ1ZDhhMzdmNjc2NDU5Mzg0ZWQwLnNldENvbnRlbnQoaHRtbF9hN2JjOGY0OGIzN2M0OWYzYjBhMTIzZWJmYmUyYjNjMyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83ODAwMWI2NTlmNDA0MzZhOWIyMjg4YTJlNzc4OGU2Yi5iaW5kUG9wdXAocG9wdXBfNGI0ZjA1NGY1M2QwNDVkOGEzN2Y2NzY0NTkzODRlZDApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMmIwOWE4MDVmOTA3NDFmZjlmNjg0OWYyYmU2YTE5ODggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41ODAzNDI5NTY0NjEzMSwtNzMuODQxNTMzNzAyMjYxODZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYmE4YmM4YWQ5ZWIzNDJmNTk4NTdlY2E0ODkwZTZiNDkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDI2YmNhYWQ5NDQyNDU0ZGI3NjM1YzRhN2E3ZjJjNjEgPSAkKCc8ZGl2IGlkPSJodG1sXzAyNmJjYWFkOTQ0MjQ1NGRiNzYzNWM0YTdhN2YyYzYxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb2NrYXdheSBQYXJrLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2JhOGJjOGFkOWViMzQyZjU5ODU3ZWNhNDg5MGU2YjQ5LnNldENvbnRlbnQoaHRtbF8wMjZiY2FhZDk0NDI0NTRkYjc2MzVjNGE3YTdmMmM2MSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yYjA5YTgwNWY5MDc0MWZmOWY2ODQ5ZjJiZTZhMTk4OC5iaW5kUG9wdXAocG9wdXBfYmE4YmM4YWQ5ZWIzNDJmNTk4NTdlY2E0ODkwZTZiNDkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzg1NGM0NjAwZTY0NDUzMDhiMTA4M2Q1ZjIyYTU2MGIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41OTc3MTA2MTU2NTc2OCwtNzMuNzk2NjQ3NTA4NDQwNDddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTdkYzFlM2FkODVlNDM1NzhkNjMxN2RlMzI2YjhiN2UgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDc4ZTFhNTRkNjgxNGRlOGFlNDk3ZjdkMTgxNThlY2EgPSAkKCc8ZGl2IGlkPSJodG1sX2Q3OGUxYTU0ZDY4MTRkZThhZTQ5N2Y3ZDE4MTU4ZWNhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Tb21lcnZpbGxlLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2E3ZGMxZTNhZDg1ZTQzNTc4ZDYzMTdkZTMyNmI4YjdlLnNldENvbnRlbnQoaHRtbF9kNzhlMWE1NGQ2ODE0ZGU4YWU0OTdmN2QxODE1OGVjYSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zODU0YzQ2MDBlNjQ0NTMwOGIxMDgzZDVmMjJhNTYwYi5iaW5kUG9wdXAocG9wdXBfYTdkYzFlM2FkODVlNDM1NzhkNjMxN2RlMzI2YjhiN2UpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMWJkZjRmZGE3MDMwNGE3Y2JlYzZmODhjNGQyOWYwODQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42NjAwMDMyMjczMzYxMywtNzMuNzUxNzUzMTA3MzExNTNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZGIxNGZhMjIyOTA3NDViOTkwZThiMjgyODY0MDU1NTYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMWRjMDVlNTJiNjg2NGZkMmFmNDlkNjM1Y2YyYWE1MWIgPSAkKCc8ZGl2IGlkPSJodG1sXzFkYzA1ZTUyYjY4NjRmZDJhZjQ5ZDYzNWNmMmFhNTFiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ccm9va3ZpbGxlLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2RiMTRmYTIyMjkwNzQ1Yjk5MGU4YjI4Mjg2NDA1NTU2LnNldENvbnRlbnQoaHRtbF8xZGMwNWU1MmI2ODY0ZmQyYWY0OWQ2MzVjZjJhYTUxYik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xYmRmNGZkYTcwMzA0YTdjYmVjNmY4OGM0ZDI5ZjA4NC5iaW5kUG9wdXAocG9wdXBfZGIxNGZhMjIyOTA3NDViOTkwZThiMjgyODY0MDU1NTYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMjU3OWNlYTE0MDk2NDAyOGExNzI4YzIwMzZiNTBlMjkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MzMwMTQwNDAyNzgzNCwtNzMuNzM4ODkxOTg5MTI0ODFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMmEyMmI0ZDE3ODJhNGE4NTkyMWRjNGFjZWE3NzUwYWYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZmU2MDBkODhjZmUxNGExN2JlNTkwNWZhYjU0ZjZlZDggPSAkKCc8ZGl2IGlkPSJodG1sX2ZlNjAwZDg4Y2ZlMTRhMTdiZTU5MDVmYWI1NGY2ZWQ4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CZWxsYWlyZSwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yYTIyYjRkMTc4MmE0YTg1OTIxZGM0YWNlYTc3NTBhZi5zZXRDb250ZW50KGh0bWxfZmU2MDBkODhjZmUxNGExN2JlNTkwNWZhYjU0ZjZlZDgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMjU3OWNlYTE0MDk2NDAyOGExNzI4YzIwMzZiNTBlMjkuYmluZFBvcHVwKHBvcHVwXzJhMjJiNGQxNzgyYTRhODU5MjFkYzRhY2VhNzc1MGFmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzVlYmEzMTNmMTRmMjRlNjk5ODI4ZDMxMTRmZWI0YWMxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzU0MDcwOTk5MDQ4OSwtNzMuODU3NTE3OTA2NzY0NDddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMDUwM2EyZDkyYzVhNDhlNWJkM2ZjYjlkODdkNTQ3ODMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzQwZTQ0Nzc4NDU3NGM4ZWJhYzdkM2JkODEwNTczMGQgPSAkKCc8ZGl2IGlkPSJodG1sXzc0MGU0NDc3ODQ1NzRjOGViYWM3ZDNiZDgxMDU3MzBkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ob3J0aCBDb3JvbmEsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMDUwM2EyZDkyYzVhNDhlNWJkM2ZjYjlkODdkNTQ3ODMuc2V0Q29udGVudChodG1sXzc0MGU0NDc3ODQ1NzRjOGViYWM3ZDNiZDgxMDU3MzBkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzVlYmEzMTNmMTRmMjRlNjk5ODI4ZDMxMTRmZWI0YWMxLmJpbmRQb3B1cChwb3B1cF8wNTAzYTJkOTJjNWE0OGU1YmQzZmNiOWQ4N2Q1NDc4Myk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zMjJiMTlmMWVlN2U0OGRhODNmYjVhMTk5NTY1YWNhMyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcxNDYxMTA4MTUxMTcsLTczLjg0MTAyMjExMjM0MDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfN2I4OWUyN2QyYWExNDI4Yzk3NmY4ZGQ5MDQ4Y2UyY2EgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTA0ZDkxOGI1NWY2NGNiMzg3YjE4Yjg4YmQ4NGJkNjIgPSAkKCc8ZGl2IGlkPSJodG1sXzUwNGQ5MThiNTVmNjRjYjM4N2IxOGI4OGJkODRiZDYyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Gb3Jlc3QgSGlsbHMgR2FyZGVucywgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83Yjg5ZTI3ZDJhYTE0MjhjOTc2ZjhkZDkwNDhjZTJjYS5zZXRDb250ZW50KGh0bWxfNTA0ZDkxOGI1NWY2NGNiMzg3YjE4Yjg4YmQ4NGJkNjIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMzIyYjE5ZjFlZTdlNDhkYTgzZmI1YTE5OTU2NWFjYTMuYmluZFBvcHVwKHBvcHVwXzdiODllMjdkMmFhMTQyOGM5NzZmOGRkOTA0OGNlMmNhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Q0ODYzNjc2ODk4OTQ0NDI4ODMzMDdhYjBkMzkxODYzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjQ0OTgxNTcxMDA0NCwtNzQuMDc5MzUzMTI1MTI3OTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZGRjOGFlMzc4ZjNlNDViNTg3NzgyZjFmMzQ3OTRhNGYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNGIwYTIxYjYyZGY3NDI2ODlhMmFiNGIxMWEzZTM3MDYgPSAkKCc8ZGl2IGlkPSJodG1sXzRiMGEyMWI2MmRmNzQyNjg5YTJhYjRiMTFhM2UzNzA2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdC4gR2VvcmdlLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kZGM4YWUzNzhmM2U0NWI1ODc3ODJmMWYzNDc5NGE0Zi5zZXRDb250ZW50KGh0bWxfNGIwYTIxYjYyZGY3NDI2ODlhMmFiNGIxMWEzZTM3MDYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDQ4NjM2NzY4OTg5NDQ0Mjg4MzMwN2FiMGQzOTE4NjMuYmluZFBvcHVwKHBvcHVwX2RkYzhhZTM3OGYzZTQ1YjU4Nzc4MmYxZjM0Nzk0YTRmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzY1NTU5NWJmNGZlZTQ3Yzk5YjdmYTg2MTQxODZkMWQ3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjQwNjE0NTU5MTM1MTEsLTc0LjA4NzAxNjUwNTE2NjI1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzUxN2YxN2UyODc1YjQ0ZTA4NmVlZTNkNjJhYTQ5Mjk4ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzMxZTBhNWIyNDEyNjQzMTM5NTFkNGYwYmI1OGVhYjM4ID0gJCgnPGRpdiBpZD0iaHRtbF8zMWUwYTViMjQxMjY0MzEzOTUxZDRmMGJiNThlYWIzOCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TmV3IEJyaWdodG9uLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81MTdmMTdlMjg3NWI0NGUwODZlZWUzZDYyYWE0OTI5OC5zZXRDb250ZW50KGh0bWxfMzFlMGE1YjI0MTI2NDMxMzk1MWQ0ZjBiYjU4ZWFiMzgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNjU1NTk1YmY0ZmVlNDdjOTliN2ZhODYxNDE4NmQxZDcuYmluZFBvcHVwKHBvcHVwXzUxN2YxN2UyODc1YjQ0ZTA4NmVlZTNkNjJhYTQ5Mjk4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzk4ODZkYzM3OWMyMjRmMjhhYzJmMGI1OGY1ZThhZWI3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjI2OTI3NjI1MzgxNzYsLTc0LjA3NzkwMTkyNjYwMDY2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzU2NzdkMmRjNGYxMDQ3ZWU5MjNmNDM0MjQyODkwZTg0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzU4NDdjMzQ4ODBlZjQ2NTdhOWViZjNmODczYTZmMzZjID0gJCgnPGRpdiBpZD0iaHRtbF81ODQ3YzM0ODgwZWY0NjU3YTllYmYzZjg3M2E2ZjM2YyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U3RhcGxldG9uLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81Njc3ZDJkYzRmMTA0N2VlOTIzZjQzNDI0Mjg5MGU4NC5zZXRDb250ZW50KGh0bWxfNTg0N2MzNDg4MGVmNDY1N2E5ZWJmM2Y4NzNhNmYzNmMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTg4NmRjMzc5YzIyNGYyOGFjMmYwYjU4ZjVlOGFlYjcuYmluZFBvcHVwKHBvcHVwXzU2NzdkMmRjNGYxMDQ3ZWU5MjNmNDM0MjQyODkwZTg0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzg5MmY4ODYzZjg1NDRjN2ViY2VmNDE1ZjU2ZGU3YjIzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjE1MzA0OTQ2NTI3NjEsLTc0LjA2OTgwNTI2NzE2MTQxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzY1ZjU4MzJlOTEyMTQyY2JhMDRkZjY2OGY3NTFiODBlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2YwYzE2ZGM1ODg0YTRlMjk4ZWM0YTljZDVmODkzMDE2ID0gJCgnPGRpdiBpZD0iaHRtbF9mMGMxNmRjNTg4NGE0ZTI5OGVjNGE5Y2Q1Zjg5MzAxNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Um9zZWJhbmssIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzY1ZjU4MzJlOTEyMTQyY2JhMDRkZjY2OGY3NTFiODBlLnNldENvbnRlbnQoaHRtbF9mMGMxNmRjNTg4NGE0ZTI5OGVjNGE5Y2Q1Zjg5MzAxNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84OTJmODg2M2Y4NTQ0YzdlYmNlZjQxNWY1NmRlN2IyMy5iaW5kUG9wdXAocG9wdXBfNjVmNTgzMmU5MTIxNDJjYmEwNGRmNjY4Zjc1MWI4MGUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZmY3MDNjMzE4NTI0NDNiMzlkYzMwNjMyYmE5MWJiNDUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MzE4Nzg5MjY1NDYwNywtNzQuMTA3MTgxNzgyNjU2MV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lZTMzNzQwMzYwOWE0NGNjOWQ3YzhhNmE4NmIxZjJjZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zNDU5YWQ0M2I4NmY0YjJlOGMzMWJkYjQ4Mzk3MmQ3YyA9ICQoJzxkaXYgaWQ9Imh0bWxfMzQ1OWFkNDNiODZmNGIyZThjMzFiZGI0ODM5NzJkN2MiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldlc3QgQnJpZ2h0b24sIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2VlMzM3NDAzNjA5YTQ0Y2M5ZDdjOGE2YTg2YjFmMmNlLnNldENvbnRlbnQoaHRtbF8zNDU5YWQ0M2I4NmY0YjJlOGMzMWJkYjQ4Mzk3MmQ3Yyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mZjcwM2MzMTg1MjQ0M2IzOWRjMzA2MzJiYTkxYmI0NS5iaW5kUG9wdXAocG9wdXBfZWUzMzc0MDM2MDlhNDRjYzlkN2M4YTZhODZiMWYyY2UpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZTg0NTJlYjIyMzlkNDQ1Y2I5MTc4NDcxYTAzMGZiYzkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MjQxODQ3OTEzMTMwMDYsLTc0LjA4NzI0ODE5OTgzNzI5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzUyOTk1M2I0NGJjMzRmYTViY2FjNDJiZDljOGIwOTJlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2VhYmQ5Y2Q0NjcyYzQ3ZmU4ZTFkMmNjZTVmM2UxZGJjID0gJCgnPGRpdiBpZD0iaHRtbF9lYWJkOWNkNDY3MmM0N2ZlOGUxZDJjY2U1ZjNlMWRiYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+R3J5bWVzIEhpbGwsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzUyOTk1M2I0NGJjMzRmYTViY2FjNDJiZDljOGIwOTJlLnNldENvbnRlbnQoaHRtbF9lYWJkOWNkNDY3MmM0N2ZlOGUxZDJjY2U1ZjNlMWRiYyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lODQ1MmViMjIzOWQ0NDVjYjkxNzg0NzFhMDMwZmJjOS5iaW5kUG9wdXAocG9wdXBfNTI5OTUzYjQ0YmMzNGZhNWJjYWM0MmJkOWM4YjA5MmUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzQ0Y2NkYzQ5NDA1NGUyNGJhMTk4MTU2NDEyMWU2NWIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41OTcwNjg1MTgxNDY3MywtNzQuMTExMzI4ODE4MDA4OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8wNjgzMTRmOGQyYWI0MGJjOGY1OGUxOTJkMThjMjJhOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84ODZhY2I3OGU2NDY0OWViOTc2Mjk2ZGJmZTUwZWU1MCA9ICQoJzxkaXYgaWQ9Imh0bWxfODg2YWNiNzhlNjQ2NDllYjk3NjI5NmRiZmU1MGVlNTAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRvZHQgSGlsbCwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMDY4MzE0ZjhkMmFiNDBiYzhmNThlMTkyZDE4YzIyYTguc2V0Q29udGVudChodG1sXzg4NmFjYjc4ZTY0NjQ5ZWI5NzYyOTZkYmZlNTBlZTUwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2M0NGNjZGM0OTQwNTRlMjRiYTE5ODE1NjQxMjFlNjViLmJpbmRQb3B1cChwb3B1cF8wNjgzMTRmOGQyYWI0MGJjOGY1OGUxOTJkMThjMjJhOCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yMDdiNGE2MGNmNjA0NWRkODdjZmQ0N2JjMzRjOTg4NSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU4MDI0NzQxMzUwOTU2LC03NC4wNzk1NTI5MjUzOTgyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzkyNGE3ZDZlZDY1ODQzNGM5ZDc4ODdjYWEzOTBlMjg3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2FmZTJiNjhmNjAyNjQ1YjliYjFiZGMyYTgxNWYwM2FlID0gJCgnPGRpdiBpZD0iaHRtbF9hZmUyYjY4ZjYwMjY0NWI5YmIxYmRjMmE4MTVmMDNhZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U291dGggQmVhY2gsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzkyNGE3ZDZlZDY1ODQzNGM5ZDc4ODdjYWEzOTBlMjg3LnNldENvbnRlbnQoaHRtbF9hZmUyYjY4ZjYwMjY0NWI5YmIxYmRjMmE4MTVmMDNhZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yMDdiNGE2MGNmNjA0NWRkODdjZmQ0N2JjMzRjOTg4NS5iaW5kUG9wdXAocG9wdXBfOTI0YTdkNmVkNjU4NDM0YzlkNzg4N2NhYTM5MGUyODcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZTQ2NTI1ZWIyODM2NDkwZDlhZTQ0ZmQ3YmUwOGU0YjcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MzM2NjkzMDU1NDM2NSwtNzQuMTI5NDM0MjY3OTcwMDhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZGU4YmY0YWM0YzYwNGQ2ZGE0YjY3MDUwYWI4YzZhZTcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfM2M2MmE1Y2EzYzA1NDFmZThmYmJmZjk1ZjlmOGRjYjYgPSAkKCc8ZGl2IGlkPSJodG1sXzNjNjJhNWNhM2MwNTQxZmU4ZmJiZmY5NWY5ZjhkY2I2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Qb3J0IFJpY2htb25kLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kZThiZjRhYzRjNjA0ZDZkYTRiNjcwNTBhYjhjNmFlNy5zZXRDb250ZW50KGh0bWxfM2M2MmE1Y2EzYzA1NDFmZThmYmJmZjk1ZjlmOGRjYjYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZTQ2NTI1ZWIyODM2NDkwZDlhZTQ0ZmQ3YmUwOGU0YjcuYmluZFBvcHVwKHBvcHVwX2RlOGJmNGFjNGM2MDRkNmRhNGI2NzA1MGFiOGM2YWU3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2NiNjdhNTkzYTA5NjRlNWQ5ZDJjYmI3YjIzN2RhZGZiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjMyNTQ2MzkwNDgxMTI0LC03NC4xNTAwODUzNzA0Njk4MV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80NmE0NTU1NjdmOWY0NjM2YTJkMTE3NzAwZGIwZjkxMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xYWI1OWU3ODE3ZGI0NzQxYTdkZjk2NTJhMjQ1NWYwZSA9ICQoJzxkaXYgaWQ9Imh0bWxfMWFiNTllNzgxN2RiNDc0MWE3ZGY5NjUyYTI0NTVmMGUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk1hcmluZXImIzM5O3MgSGFyYm9yLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80NmE0NTU1NjdmOWY0NjM2YTJkMTE3NzAwZGIwZjkxMS5zZXRDb250ZW50KGh0bWxfMWFiNTllNzgxN2RiNDc0MWE3ZGY5NjUyYTI0NTVmMGUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfY2I2N2E1OTNhMDk2NGU1ZDlkMmNiYjdiMjM3ZGFkZmIuYmluZFBvcHVwKHBvcHVwXzQ2YTQ1NTU2N2Y5ZjQ2MzZhMmQxMTc3MDBkYjBmOTExKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzhkNDI1N2I3YWE4NzQ4MjY4OTFhZDFlMjEzOTQwNDk5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjM5NjgyOTc4NDU1NDIsLTc0LjE3NDY0NTMyOTkzNTQyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzI1N2Q2M2IwMDY0OTRjOGFhZWRkNjlkZGYxY2M2YWU1ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzJiOGU4MDM1YTI0NjQxMGFiZmIxMjk0YmMwNjk5ZmIyID0gJCgnPGRpdiBpZD0iaHRtbF8yYjhlODAzNWEyNDY0MTBhYmZiMTI5NGJjMDY5OWZiMiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UG9ydCBJdm9yeSwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMjU3ZDYzYjAwNjQ5NGM4YWFlZGQ2OWRkZjFjYzZhZTUuc2V0Q29udGVudChodG1sXzJiOGU4MDM1YTI0NjQxMGFiZmIxMjk0YmMwNjk5ZmIyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzhkNDI1N2I3YWE4NzQ4MjY4OTFhZDFlMjEzOTQwNDk5LmJpbmRQb3B1cChwb3B1cF8yNTdkNjNiMDA2NDk0YzhhYWVkZDY5ZGRmMWNjNmFlNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83Y2ExYmZlODdjNGU0MmM3YTRiMTJhOGE5NGU1YTgxMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYxMzMzNTkzNzY2NzQyLC03NC4xMTkxODA1ODUzNDg0Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xODY0YTY4MThlYmU0Y2QyYjhmYjE1ZWQ0ZjNjYmRkYyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mMjJmYmQwZGQxYjQ0MWE1YjNhOWQyOGM4YTc2YTM0MyA9ICQoJzxkaXYgaWQ9Imh0bWxfZjIyZmJkMGRkMWI0NDFhNWIzYTlkMjhjOGE3NmEzNDMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNhc3RsZXRvbiBDb3JuZXJzLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xODY0YTY4MThlYmU0Y2QyYjhmYjE1ZWQ0ZjNjYmRkYy5zZXRDb250ZW50KGh0bWxfZjIyZmJkMGRkMWI0NDFhNWIzYTlkMjhjOGE3NmEzNDMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfN2NhMWJmZTg3YzRlNDJjN2E0YjEyYThhOTRlNWE4MTEuYmluZFBvcHVwKHBvcHVwXzE4NjRhNjgxOGViZTRjZDJiOGZiMTVlZDRmM2NiZGRjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzczNTlmZmVmZWZmMTRiZDA4N2QzYWUxOTlmYzBlOTk2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTk0MjUyMzc5MTYxNjk1LC03NC4xNjQ5NjAzMTMyOTgyN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9kYWIzNTQyOGQwODM0MTg4OGVlYzEwNWVhMjQ1ZGJlZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wMDM0ZTYyZDM1Y2E0NWE4OGQ5YzU4ZTZkNDVlNWNiNCA9ICQoJzxkaXYgaWQ9Imh0bWxfMDAzNGU2MmQzNWNhNDVhODhkOWM1OGU2ZDQ1ZTVjYjQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5ldyBTcHJpbmd2aWxsZSwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZGFiMzU0MjhkMDgzNDE4ODhlZWMxMDVlYTI0NWRiZWUuc2V0Q29udGVudChodG1sXzAwMzRlNjJkMzVjYTQ1YTg4ZDljNThlNmQ0NWU1Y2I0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzczNTlmZmVmZWZmMTRiZDA4N2QzYWUxOTlmYzBlOTk2LmJpbmRQb3B1cChwb3B1cF9kYWIzNTQyOGQwODM0MTg4OGVlYzEwNWVhMjQ1ZGJlZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xM2ZhZDUzZTRjYWM0NDRjYTdlZjVhNmYwMmQxY2E1ZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU4NjMxMzc1MTAzMjgxLC03NC4xOTA3MzcxNzUzODExNl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lOWNhMTQ2ZTg4YzU0ZGM3ODM2ZGFiMjU1MjA5NWM4MyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mMTg1NDAxY2EzOWE0NDE1YWM2NDY0ZDU3MjA0OTQzNCA9ICQoJzxkaXYgaWQ9Imh0bWxfZjE4NTQwMWNhMzlhNDQxNWFjNjQ2NGQ1NzIwNDk0MzQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRyYXZpcywgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZTljYTE0NmU4OGM1NGRjNzgzNmRhYjI1NTIwOTVjODMuc2V0Q29udGVudChodG1sX2YxODU0MDFjYTM5YTQ0MTVhYzY0NjRkNTcyMDQ5NDM0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzEzZmFkNTNlNGNhYzQ0NGNhN2VmNWE2ZjAyZDFjYTVkLmJpbmRQb3B1cChwb3B1cF9lOWNhMTQ2ZTg4YzU0ZGM3ODM2ZGFiMjU1MjA5NWM4Myk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82ZWE2MjljNGUxOGE0YjQzYTQ3NTk5ZmE5YWE0OTAwZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU3MjU3MjMxODIwNjMyLC03NC4xMTY0Nzk0MzYwNjM4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzEwYmFjYjAwMTUwMDQ0ODdhOWY0NjgzNzJlOWM4NGQyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzAyMTY1ZGQ5NWMzMDRmOTY4NGQ0OTQyNzI3OGI4NjVmID0gJCgnPGRpdiBpZD0iaHRtbF8wMjE2NWRkOTVjMzA0Zjk2ODRkNDk0MjcyNzhiODY1ZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TmV3IERvcnAsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzEwYmFjYjAwMTUwMDQ0ODdhOWY0NjgzNzJlOWM4NGQyLnNldENvbnRlbnQoaHRtbF8wMjE2NWRkOTVjMzA0Zjk2ODRkNDk0MjcyNzhiODY1Zik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82ZWE2MjljNGUxOGE0YjQzYTQ3NTk5ZmE5YWE0OTAwZi5iaW5kUG9wdXAocG9wdXBfMTBiYWNiMDAxNTAwNDQ4N2E5ZjQ2ODM3MmU5Yzg0ZDIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNWVmMWE4MzZlZDM3NDIzMGE3YzE4ZGI5ZWU2YTI4OTkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NTg0NjIyNDMyODg4LC03NC4xMjE1NjU5Mzc3MTg5Nl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81YmNjOGJhNWY4YjE0OTRkYmZjYzU0M2VlMGMyM2RlZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xOWVlM2U0MjUwM2Y0MWQwODMxNzhhODA3NDE2M2ZhNCA9ICQoJzxkaXYgaWQ9Imh0bWxfMTllZTNlNDI1MDNmNDFkMDgzMTc4YTgwNzQxNjNmYTQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk9ha3dvb2QsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzViY2M4YmE1ZjhiMTQ5NGRiZmNjNTQzZWUwYzIzZGVmLnNldENvbnRlbnQoaHRtbF8xOWVlM2U0MjUwM2Y0MWQwODMxNzhhODA3NDE2M2ZhNCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81ZWYxYTgzNmVkMzc0MjMwYTdjMThkYjllZTZhMjg5OS5iaW5kUG9wdXAocG9wdXBfNWJjYzhiYTVmOGIxNDk0ZGJmY2M1NDNlZTBjMjNkZWYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZmMwNTk2MzBmNDNmNDhjYzkwZGI1NmJjODYyNjEyYjQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NDk0ODAyMjg3MTM2MDUsLTc0LjE0OTMyMzgxNDkwOTkyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzc0ZWMyNzA3ZGJmYzQ4NzZhZWQzMmE0MDY2MWJjYTk3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2Y1ZjlmOTk1MmU3NDQ2ZmRiNzQ3ODU2NzkyZDIxYzNkID0gJCgnPGRpdiBpZD0iaHRtbF9mNWY5Zjk5NTJlNzQ0NmZkYjc0Nzg1Njc5MmQyMWMzZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+R3JlYXQgS2lsbHMsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzc0ZWMyNzA3ZGJmYzQ4NzZhZWQzMmE0MDY2MWJjYTk3LnNldENvbnRlbnQoaHRtbF9mNWY5Zjk5NTJlNzQ0NmZkYjc0Nzg1Njc5MmQyMWMzZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mYzA1OTYzMGY0M2Y0OGNjOTBkYjU2YmM4NjI2MTJiNC5iaW5kUG9wdXAocG9wdXBfNzRlYzI3MDdkYmZjNDg3NmFlZDMyYTQwNjYxYmNhOTcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfM2FmMWM0OTVkY2Y3NGNlNWEzMWI0Yzk2Y2VkNDAyYjAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NDIyMzA3NDc0NTA3NDUsLTc0LjE2NDMzMDgwNDE5MzZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNTdiODdkOTdhNmMzNDA0Yzk5OGNiYWZkMjI4ODI5YzMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNWM0MGI4ZjcyNGM2NDA0M2I2Zjc1MTUzOTBjOGRjZjMgPSAkKCc8ZGl2IGlkPSJodG1sXzVjNDBiOGY3MjRjNjQwNDNiNmY3NTE1MzkwYzhkY2YzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5FbHRpbmd2aWxsZSwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNTdiODdkOTdhNmMzNDA0Yzk5OGNiYWZkMjI4ODI5YzMuc2V0Q29udGVudChodG1sXzVjNDBiOGY3MjRjNjQwNDNiNmY3NTE1MzkwYzhkY2YzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzNhZjFjNDk1ZGNmNzRjZTVhMzFiNGM5NmNlZDQwMmIwLmJpbmRQb3B1cChwb3B1cF81N2I4N2Q5N2E2YzM0MDRjOTk4Y2JhZmQyMjg4MjljMyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85ZmY5M2RjZTdkOGM0ZjcxOWUxZWMyM2M0ZDUxNWFhNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjUzODExNDE3NDc0NTA3LC03NC4xNzg1NDg2NjE2NTg3OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hMWUyNWExZmU4YWQ0MGM0OGUxNjM2MDJmZTM4MmViNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wN2NhOTg4ZTJjNmE0NTllODgwMmI4ZDI0Mzk4OGExZCA9ICQoJzxkaXYgaWQ9Imh0bWxfMDdjYTk4OGUyYzZhNDU5ZTg4MDJiOGQyNDM5ODhhMWQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFubmFkYWxlLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hMWUyNWExZmU4YWQ0MGM0OGUxNjM2MDJmZTM4MmViNy5zZXRDb250ZW50KGh0bWxfMDdjYTk4OGUyYzZhNDU5ZTg4MDJiOGQyNDM5ODhhMWQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOWZmOTNkY2U3ZDhjNGY3MTllMWVjMjNjNGQ1MTVhYTcuYmluZFBvcHVwKHBvcHVwX2ExZTI1YTFmZThhZDQwYzQ4ZTE2MzYwMmZlMzgyZWI3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzg5NjQ1ZDg3NTY1MTQ2YzM4NDY1ZWE2ODQ3YmNhMTM5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTQxOTY3NjIyODg4NzU1LC03NC4yMDUyNDU4MjQ4MDMyNl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9kYTc2ZTFlNmVjYzg0MjVlYjFlMjUzZjNmMzA5MTdmYiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85NzNhMTczZmYwMzk0NjIwOGMwYzU4MmEyODA1M2FmYiA9ICQoJzxkaXYgaWQ9Imh0bWxfOTczYTE3M2ZmMDM5NDYyMDhjMGM1ODJhMjgwNTNhZmIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldvb2Ryb3csIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2RhNzZlMWU2ZWNjODQyNWViMWUyNTNmM2YzMDkxN2ZiLnNldENvbnRlbnQoaHRtbF85NzNhMTczZmYwMzk0NjIwOGMwYzU4MmEyODA1M2FmYik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84OTY0NWQ4NzU2NTE0NmMzODQ2NWVhNjg0N2JjYTEzOS5iaW5kUG9wdXAocG9wdXBfZGE3NmUxZTZlY2M4NDI1ZWIxZTI1M2YzZjMwOTE3ZmIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMTIyZmQ3MmZkNGM4NGM1OGI5MDdlMTU1MzQ1ODI4NmMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41MDUzMzM3NjExNTY0MiwtNzQuMjQ2NTY5MzQyMzUyODNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMDk5NWQyZmZiNjcxNGJkMTk3MmJkMTBhZjNjZjE1NWEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZThiOWE4YWZhNTQ5NDE2M2EwNDBhOTdmYjNmMDA3M2YgPSAkKCc8ZGl2IGlkPSJodG1sX2U4YjlhOGFmYTU0OTQxNjNhMDQwYTk3ZmIzZjAwNzNmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ub3R0ZW52aWxsZSwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMDk5NWQyZmZiNjcxNGJkMTk3MmJkMTBhZjNjZjE1NWEuc2V0Q29udGVudChodG1sX2U4YjlhOGFmYTU0OTQxNjNhMDQwYTk3ZmIzZjAwNzNmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzEyMmZkNzJmZDRjODRjNThiOTA3ZTE1NTM0NTgyODZjLmJpbmRQb3B1cChwb3B1cF8wOTk1ZDJmZmI2NzE0YmQxOTcyYmQxMGFmM2NmMTU1YSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83MGJjOTgzNzg1YWU0MWJkOWQ5NDlkNGYyNTI4NDhlMCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYzNzMxNjA2NzExMDMyNiwtNzQuMDgwNTUzNTE3OTAxMTVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNzQxNDFjYmY0Mzk1NDljZGI4YmU3MmI3ZWMxMjVkMTkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTQxNmYyOWRiOGVmNGMyYTk3ODBiMTkxNzE3MjhjMTUgPSAkKCc8ZGl2IGlkPSJodG1sXzU0MTZmMjlkYjhlZjRjMmE5NzgwYjE5MTcxNzI4YzE1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ub21wa2luc3ZpbGxlLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83NDE0MWNiZjQzOTU0OWNkYjhiZTcyYjdlYzEyNWQxOS5zZXRDb250ZW50KGh0bWxfNTQxNmYyOWRiOGVmNGMyYTk3ODBiMTkxNzE3MjhjMTUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNzBiYzk4Mzc4NWFlNDFiZDlkOTQ5ZDRmMjUyODQ4ZTAuYmluZFBvcHVwKHBvcHVwXzc0MTQxY2JmNDM5NTQ5Y2RiOGJlNzJiN2VjMTI1ZDE5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzRlMWEzYmRmMzBlOTQ0YmY5OGRmNzI2MzhhOTE5Mzk5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjE5MTkzMTA3OTI2NzYsLTc0LjA5NjI5MDI5MjM1NDU4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzg0NDRmOTNmM2VlMzQxMGQ4YjhkNTkxNzkwNmVjOTY4ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2Y4MzViMDk4NjBhOTRlMzY5YzgyZDllOTRlNzA0N2EyID0gJCgnPGRpdiBpZD0iaHRtbF9mODM1YjA5ODYwYTk0ZTM2OWM4MmQ5ZTk0ZTcwNDdhMiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U2lsdmVyIExha2UsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzg0NDRmOTNmM2VlMzQxMGQ4YjhkNTkxNzkwNmVjOTY4LnNldENvbnRlbnQoaHRtbF9mODM1YjA5ODYwYTk0ZTM2OWM4MmQ5ZTk0ZTcwNDdhMik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80ZTFhM2JkZjMwZTk0NGJmOThkZjcyNjM4YTkxOTM5OS5iaW5kUG9wdXAocG9wdXBfODQ0NGY5M2YzZWUzNDEwZDhiOGQ1OTE3OTA2ZWM5NjgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMGZkOWU4NmM0ZDM1NGM5Nzk2MGU3NzM4YjhmY2Q3NzcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MTI3NjAxNTc1NjQ4OSwtNzQuMDk3MTI1NTIxNzg1M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83MWFhM2Q2YThjMmQ0MmEyODZmNjQ0OTBjZTcyMDQ2NyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lNjE4N2JkNzFkZDU0Mzk0ODgzZGU2YjY3M2MzZGQ3NyA9ICQoJzxkaXYgaWQ9Imh0bWxfZTYxODdiZDcxZGQ1NDM5NDg4M2RlNmI2NzNjM2RkNzciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlN1bm55c2lkZSwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNzFhYTNkNmE4YzJkNDJhMjg2ZjY0NDkwY2U3MjA0Njcuc2V0Q29udGVudChodG1sX2U2MTg3YmQ3MWRkNTQzOTQ4ODNkZTZiNjczYzNkZDc3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzBmZDllODZjNGQzNTRjOTc5NjBlNzczOGI4ZmNkNzc3LmJpbmRQb3B1cChwb3B1cF83MWFhM2Q2YThjMmQ0MmEyODZmNjQ0OTBjZTcyMDQ2Nyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jNDcyYzViZDY1MTY0NmI4ODYzZjY5NjM0MWU0OGE4OCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY0MzY3NTE4MzM0MDk3NCwtNzMuOTYxMDEzMTI0NjY3NzldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNzA2NjNhMjI4M2VjNDIzZjhjYjI5M2MwMGU1ZDVkN2IgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZWEwNTE4NDQyMjYzNDQwNzlkOGU5OGVlMDVhOGZhOGIgPSAkKCc8ZGl2IGlkPSJodG1sX2VhMDUxODQ0MjI2MzQ0MDc5ZDhlOThlZTA1YThmYThiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5EaXRtYXMgUGFyaywgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzcwNjYzYTIyODNlYzQyM2Y4Y2IyOTNjMDBlNWQ1ZDdiLnNldENvbnRlbnQoaHRtbF9lYTA1MTg0NDIyNjM0NDA3OWQ4ZTk4ZWUwNWE4ZmE4Yik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jNDcyYzViZDY1MTY0NmI4ODYzZjY5NjM0MWU0OGE4OC5iaW5kUG9wdXAocG9wdXBfNzA2NjNhMjI4M2VjNDIzZjhjYjI5M2MwMGU1ZDVkN2IpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMjZkMDU2MzZjZWMwNDBlYTgxZWIwMjhiM2Y5ODNlZjkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42NjA5NDY1NjE4ODExMSwtNzMuOTM3MTg2ODA1NTkzMTRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNDE2OTNiZmMyYzliNGU0NmI4NDQxN2YyZGUzNjkwOWYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTg2ZjFmNDE0Y2EyNDU3MGJmZTc3ZmVlYzE2OGJiMjggPSAkKCc8ZGl2IGlkPSJodG1sX2U4NmYxZjQxNGNhMjQ1NzBiZmU3N2ZlZWMxNjhiYjI4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5XaW5nYXRlLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNDE2OTNiZmMyYzliNGU0NmI4NDQxN2YyZGUzNjkwOWYuc2V0Q29udGVudChodG1sX2U4NmYxZjQxNGNhMjQ1NzBiZmU3N2ZlZWMxNjhiYjI4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzI2ZDA1NjM2Y2VjMDQwZWE4MWViMDI4YjNmOTgzZWY5LmJpbmRQb3B1cChwb3B1cF80MTY5M2JmYzJjOWI0ZTQ2Yjg0NDE3ZjJkZTM2OTA5Zik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xNGYxYmMyMWUwNmI0NzdmYTU4MmRkNmRkZjVkMzVkNSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY1NTU3MjMxMzI4MDc2NCwtNzMuOTI2ODgyMTI2MTY5NTVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMTQ4MzVkZTMwZmM3NGM5MjhiMmY5NzgwMmQ0Yzk2ODcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNDA5NDZhOTMzMjBjNDRjZmIxZTQwNWViYTcyODI1NDQgPSAkKCc8ZGl2IGlkPSJodG1sXzQwOTQ2YTkzMzIwYzQ0Y2ZiMWU0MDVlYmE3MjgyNTQ0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5SdWdieSwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzE0ODM1ZGUzMGZjNzRjOTI4YjJmOTc4MDJkNGM5Njg3LnNldENvbnRlbnQoaHRtbF80MDk0NmE5MzMyMGM0NGNmYjFlNDA1ZWJhNzI4MjU0NCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xNGYxYmMyMWUwNmI0NzdmYTU4MmRkNmRkZjVkMzVkNS5iaW5kUG9wdXAocG9wdXBfMTQ4MzVkZTMwZmM3NGM5MjhiMmY5NzgwMmQ0Yzk2ODcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOGRkMGFhMDI2MDUzNDIxMGE0NGZjYzNkYWU5MjM5ZTIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MDkxOTA0NDQzNDU1OCwtNzQuMDgwMTU3MzQ5MzYyOTZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYmNjMGU0ODU2MGYzNGJlY2IxYTYwMzY2NTc5NGY4YjcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNDcyMDQzZTY0MmJkNDhkNTllMjJhMjdlZWZkYjE0ZTYgPSAkKCc8ZGl2IGlkPSJodG1sXzQ3MjA0M2U2NDJiZDQ4ZDU5ZTIyYTI3ZWVmZGIxNGU2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5QYXJrIEhpbGwsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2JjYzBlNDg1NjBmMzRiZWNiMWE2MDM2NjU3OTRmOGI3LnNldENvbnRlbnQoaHRtbF80NzIwNDNlNjQyYmQ0OGQ1OWUyMmEyN2VlZmRiMTRlNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84ZGQwYWEwMjYwNTM0MjEwYTQ0ZmNjM2RhZTkyMzllMi5iaW5kUG9wdXAocG9wdXBfYmNjMGU0ODU2MGYzNGJlY2IxYTYwMzY2NTc5NGY4YjcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDhlZGJhN2VhZThhNGEzNmEzMGE0Yjk0YTczY2U1MzEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MjEwOTA0NzI3NTQwOSwtNzQuMTMzMDQxNDM5NTE3MDRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOWY0MGE1MjEwMGZiNGY3NWFlZmZkYTM4Mjc2OGUwOTcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNGNkYzY1NmZjZTAxNGZiNDg2NmZkMWFmYzY2YzA3MGEgPSAkKCc8ZGl2IGlkPSJodG1sXzRjZGM2NTZmY2UwMTRmYjQ4NjZmZDFhZmM2NmMwNzBhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5XZXN0ZXJsZWlnaCwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOWY0MGE1MjEwMGZiNGY3NWFlZmZkYTM4Mjc2OGUwOTcuc2V0Q29udGVudChodG1sXzRjZGM2NTZmY2UwMTRmYjQ4NjZmZDFhZmM2NmMwNzBhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Q4ZWRiYTdlYWU4YTRhMzZhMzBhNGI5NGE3M2NlNTMxLmJpbmRQb3B1cChwb3B1cF85ZjQwYTUyMTAwZmI0Zjc1YWVmZmRhMzgyNzY4ZTA5Nyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80MjI2MzEwMTc0YTI0NDJjOTlmZmFiYjM2ODU2MWMyZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYyMDE3MTUxMjIzMTg4NCwtNzQuMTUzMTUyNDYzODc3NjJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOGYwZTZiYjBlN2JkNDYwNDkzZGRlMDNmZjNiNzNjYWYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYjE1ZWI5YTI5M2U2NDhjOGI3YTA4OWU1NGY3ZjJlZWMgPSAkKCc8ZGl2IGlkPSJodG1sX2IxNWViOWEyOTNlNjQ4YzhiN2EwODllNTRmN2YyZWVjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5HcmFuaXRldmlsbGUsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzhmMGU2YmIwZTdiZDQ2MDQ5M2RkZTAzZmYzYjczY2FmLnNldENvbnRlbnQoaHRtbF9iMTVlYjlhMjkzZTY0OGM4YjdhMDg5ZTU0ZjdmMmVlYyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80MjI2MzEwMTc0YTI0NDJjOTlmZmFiYjM2ODU2MWMyZC5iaW5kUG9wdXAocG9wdXBfOGYwZTZiYjBlN2JkNDYwNDkzZGRlMDNmZjNiNzNjYWYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDczNDAzYTA4ODNlNDI1MTkzMTY4NDJiMGMxMTU4MmMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MzUzMjUwOTkxMTQ5MiwtNzQuMTY1MTA0MjAyNDExMjRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYmFjMTFhOTA5YjNjNDZlMjlhZTQxYzRhY2I2ZDIzNDQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYWFiMjI0MTZiOTNmNGY1OGFhMjA0ZGVlZTVlMTRjODkgPSAkKCc8ZGl2IGlkPSJodG1sX2FhYjIyNDE2YjkzZjRmNThhYTIwNGRlZWU1ZTE0Yzg5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Bcmxpbmd0b24sIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2JhYzExYTkwOWIzYzQ2ZTI5YWU0MWM0YWNiNmQyMzQ0LnNldENvbnRlbnQoaHRtbF9hYWIyMjQxNmI5M2Y0ZjU4YWEyMDRkZWVlNWUxNGM4OSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kNzM0MDNhMDg4M2U0MjUxOTMxNjg0MmIwYzExNTgyYy5iaW5kUG9wdXAocG9wdXBfYmFjMTFhOTA5YjNjNDZlMjlhZTQxYzRhY2I2ZDIzNDQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMThmODUzNWQ3NTYyNGUyOTkzNmRiMjJhNzJjNzBkZDYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41OTYzMTI1NzEyNzY3MzQsLTc0LjA2NzEyMzYzMjI1NTc0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzg2NjUwYjNmYTRhYzQ5NTQ5MzM3NDRjMWNmY2M4Yjg0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzlmMTcwNWEwZTJjOTQ5MDc4N2ExNjdlMjIzNTA0OGIxID0gJCgnPGRpdiBpZD0iaHRtbF85ZjE3MDVhMGUyYzk0OTA3ODdhMTY3ZTIyMzUwNDhiMSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QXJyb2NoYXIsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzg2NjUwYjNmYTRhYzQ5NTQ5MzM3NDRjMWNmY2M4Yjg0LnNldENvbnRlbnQoaHRtbF85ZjE3MDVhMGUyYzk0OTA3ODdhMTY3ZTIyMzUwNDhiMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xOGY4NTM1ZDc1NjI0ZTI5OTM2ZGIyMmE3MmM3MGRkNi5iaW5kUG9wdXAocG9wdXBfODY2NTBiM2ZhNGFjNDk1NDkzMzc0NGMxY2ZjYzhiODQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZjZlZDhkYTFiMDdkNDY4ZDhjZTJmZjY1ZTBhNTQ1MWMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41OTgyNjgzNTk1OTk5MSwtNzQuMDc2Njc0MzYyNzkwNV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hMWNiM2E2MjM2NGM0YWFhYjliOWFjODZiZjJmMGZhYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iMzViZTM0MzU5YjQ0N2E1ODNhMmY3ZGVlM2JjM2FhOSA9ICQoJzxkaXYgaWQ9Imh0bWxfYjM1YmUzNDM1OWI0NDdhNTgzYTJmN2RlZTNiYzNhYTkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkdyYXNtZXJlLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hMWNiM2E2MjM2NGM0YWFhYjliOWFjODZiZjJmMGZhYS5zZXRDb250ZW50KGh0bWxfYjM1YmUzNDM1OWI0NDdhNTgzYTJmN2RlZTNiYzNhYTkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZjZlZDhkYTFiMDdkNDY4ZDhjZTJmZjY1ZTBhNTQ1MWMuYmluZFBvcHVwKHBvcHVwX2ExY2IzYTYyMzY0YzRhYWFiOWI5YWM4NmJmMmYwZmFhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzU1ZGNhMDZiZDI1MTRjMGQ4ODc1NWNkYmY4OTg3MWNlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTk2MzI4OTEzNzk1MTMsLTc0LjA4NzUxMTE4MDA1NTc4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2RhMDBjNjQwYTY3ZTQwNzViNzFlOTlhYmViOWFiMDkzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzk2ZTgyOGM3YWY5NzQ4ODNhZTUzNmJjMWE1NDIyNmRhID0gJCgnPGRpdiBpZD0iaHRtbF85NmU4MjhjN2FmOTc0ODgzYWU1MzZiYzFhNTQyMjZkYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+T2xkIFRvd24sIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2RhMDBjNjQwYTY3ZTQwNzViNzFlOTlhYmViOWFiMDkzLnNldENvbnRlbnQoaHRtbF85NmU4MjhjN2FmOTc0ODgzYWU1MzZiYzFhNTQyMjZkYSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81NWRjYTA2YmQyNTE0YzBkODg3NTVjZGJmODk4NzFjZS5iaW5kUG9wdXAocG9wdXBfZGEwMGM2NDBhNjdlNDA3NWI3MWU5OWFiZWI5YWIwOTMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMDNmMTcwOTE2MWM0NDU5YThlZWJkODUwZmZlY2I0Y2UgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41ODg2NzI5NDgxOTkyNzUsLTc0LjA5NjM5OTA1MzEyNTIxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzk3NmE3NmJhYjI0NDQ0YzZiYjg1YzQ5MDdjM2Y5NDNmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzMzMjNiOTRlYTQxNTRmMzA5MWI1ZmZiMzMwNjRmYzQ3ID0gJCgnPGRpdiBpZD0iaHRtbF8zMzIzYjk0ZWE0MTU0ZjMwOTFiNWZmYjMzMDY0ZmM0NyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RG9uZ2FuIEhpbGxzLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85NzZhNzZiYWIyNDQ0NGM2YmI4NWM0OTA3YzNmOTQzZi5zZXRDb250ZW50KGh0bWxfMzMyM2I5NGVhNDE1NGYzMDkxYjVmZmIzMzA2NGZjNDcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMDNmMTcwOTE2MWM0NDU5YThlZWJkODUwZmZlY2I0Y2UuYmluZFBvcHVwKHBvcHVwXzk3NmE3NmJhYjI0NDQ0YzZiYjg1YzQ5MDdjM2Y5NDNmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Y1NGU1NGJiMWI2ZDQwNDk4ZDg5ZTdhNTEwOWY0Y2MxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTczNTI2OTA1NzQyODMsLTc0LjA5MzQ4MjY2MzAzNTkxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzI0NzlmZDM2M2ZkYzRkY2U5ZjIyMDI4ZTFjNWE2YzhmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzUwZGRlMTdkMjQ2NzRlMzA5MTg4MmE2NmEyYjEzMWQ3ID0gJCgnPGRpdiBpZD0iaHRtbF81MGRkZTE3ZDI0Njc0ZTMwOTE4ODJhNjZhMmIxMzFkNyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TWlkbGFuZCBCZWFjaCwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMjQ3OWZkMzYzZmRjNGRjZTlmMjIwMjhlMWM1YTZjOGYuc2V0Q29udGVudChodG1sXzUwZGRlMTdkMjQ2NzRlMzA5MTg4MmE2NmEyYjEzMWQ3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Y1NGU1NGJiMWI2ZDQwNDk4ZDg5ZTdhNTEwOWY0Y2MxLmJpbmRQb3B1cChwb3B1cF8yNDc5ZmQzNjNmZGM0ZGNlOWYyMjAyOGUxYzVhNmM4Zik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hNDBlNzA2YjFjNTI0YTNkYmMyMTI1NWE3YTdiMWVhNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU3NjIxNTU4NzExNzg4LC03NC4xMDU4NTU5ODU0NTQzNF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mYzlmYzcwNDliZDk0NzZlOWE0MDJiZjg5MTc0YTU0YSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83YjQ2Yzc1OWZjOTg0MTlmOWU1MmUxY2UyNjNkMzJmYSA9ICQoJzxkaXYgaWQ9Imh0bWxfN2I0NmM3NTlmYzk4NDE5ZjllNTJlMWNlMjYzZDMyZmEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkdyYW50IENpdHksIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2ZjOWZjNzA0OWJkOTQ3NmU5YTQwMmJmODkxNzRhNTRhLnNldENvbnRlbnQoaHRtbF83YjQ2Yzc1OWZjOTg0MTlmOWU1MmUxY2UyNjNkMzJmYSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hNDBlNzA2YjFjNTI0YTNkYmMyMTI1NWE3YTdiMWVhNC5iaW5kUG9wdXAocG9wdXBfZmM5ZmM3MDQ5YmQ5NDc2ZTlhNDAyYmY4OTE3NGE1NGEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfY2Q2ZmEyMDBmMjc4NGY2ODhlNTkyZDEwZmI2Zjk3ZjcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NjQyNTU0OTMwNzMzNSwtNzQuMTA0MzI3MDc0NjkxMjRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNWMwZjBkNDY2ZTlmNDdkNmFmMTJiYWQ2M2I3MDRmNTQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMjg2Y2E5NTU5ODBjNGMxNWFjZGE4MjgzODY4NjQ5ZTAgPSAkKCc8ZGl2IGlkPSJodG1sXzI4NmNhOTU1OTgwYzRjMTVhY2RhODI4Mzg2ODY0OWUwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5OZXcgRG9ycCBCZWFjaCwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNWMwZjBkNDY2ZTlmNDdkNmFmMTJiYWQ2M2I3MDRmNTQuc2V0Q29udGVudChodG1sXzI4NmNhOTU1OTgwYzRjMTVhY2RhODI4Mzg2ODY0OWUwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2NkNmZhMjAwZjI3ODRmNjg4ZTU5MmQxMGZiNmY5N2Y3LmJpbmRQb3B1cChwb3B1cF81YzBmMGQ0NjZlOWY0N2Q2YWYxMmJhZDYzYjcwNGY1NCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iZjZiZTI0NDA2ZDA0ZjU3YTQxOTFkNTY4YWJiMzRkNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU1Mzk4ODAwODU4NDYyLC03NC4xMzkxNjYyMjE3NTc2OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mMWYzZmJmMmRlZTA0YzhmODA0ZGNmNmI2YWNlODYzNiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85MDc3MWNlOWQxYTg0M2I1Yjg4ZDM2MWRjMjJhYjk2MyA9ICQoJzxkaXYgaWQ9Imh0bWxfOTA3NzFjZTlkMWE4NDNiNWI4OGQzNjFkYzIyYWI5NjMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJheSBUZXJyYWNlLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mMWYzZmJmMmRlZTA0YzhmODA0ZGNmNmI2YWNlODYzNi5zZXRDb250ZW50KGh0bWxfOTA3NzFjZTlkMWE4NDNiNWI4OGQzNjFkYzIyYWI5NjMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYmY2YmUyNDQwNmQwNGY1N2E0MTkxZDU2OGFiYjM0ZDcuYmluZFBvcHVwKHBvcHVwX2YxZjNmYmYyZGVlMDRjOGY4MDRkY2Y2YjZhY2U4NjM2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2RmZWZiMTY4ZGNlZjQ2MzFiY2UyODJkNGUwYzc3MmI3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTMxOTExOTIwNDg5NjA1LC03NC4xOTE3NDEwNTc0NzgxNF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zZDRiMzc0MzY0OWQ0ZTcxOGJkMDQ5N2Y3NTE0NTRjZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zNmQ4ZWMxMGYxOGQ0YzYyOTA0MjE3YTJkYjE3ZGJmYSA9ICQoJzxkaXYgaWQ9Imh0bWxfMzZkOGVjMTBmMThkNGM2MjkwNDIxN2EyZGIxN2RiZmEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkh1Z3Vlbm90LCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zZDRiMzc0MzY0OWQ0ZTcxOGJkMDQ5N2Y3NTE0NTRjZS5zZXRDb250ZW50KGh0bWxfMzZkOGVjMTBmMThkNGM2MjkwNDIxN2EyZGIxN2RiZmEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZGZlZmIxNjhkY2VmNDYzMWJjZTI4MmQ0ZTBjNzcyYjcuYmluZFBvcHVwKHBvcHVwXzNkNGIzNzQzNjQ5ZDRlNzE4YmQwNDk3Zjc1MTQ1NGNlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzAyYzVjOTE4Mzg0NjQ5MjA4ZTNkODA3MTRiNDZkMWViID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTI0Njk5Mzc2MTE4MTM2LC03NC4yMTk4MzEwNjYxNjc3N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9iMzQwNzEwYTBhMjQ0MzBiOGI1NTJkZTI5ZTcyNzJmMiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81MzViZGU4NDY5MDQ0MWYzOGFmMjYwNDliZTU0YjQzNCA9ICQoJzxkaXYgaWQ9Imh0bWxfNTM1YmRlODQ2OTA0NDFmMzhhZjI2MDQ5YmU1NGI0MzQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlBsZWFzYW50IFBsYWlucywgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjM0MDcxMGEwYTI0NDMwYjhiNTUyZGUyOWU3MjcyZjIuc2V0Q29udGVudChodG1sXzUzNWJkZTg0NjkwNDQxZjM4YWYyNjA0OWJlNTRiNDM0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzAyYzVjOTE4Mzg0NjQ5MjA4ZTNkODA3MTRiNDZkMWViLmJpbmRQb3B1cChwb3B1cF9iMzQwNzEwYTBhMjQ0MzBiOGI1NTJkZTI5ZTcyNzJmMik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xZTFjNzkwYmMyZTU0ODY4OTBhYzgyZGI0NjEwZTRjMCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjUwNjA4MTY1MzQ2MzA1LC03NC4yMjk1MDM1MDI2MDAyN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9iOGM3M2U4MzZiMzE0Njk0ODZlNWRiMDVjZDA2MGU5YyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hMjlmNzljMmFmYTM0MDFlOWFkNjQxMTIyNDRiYjQ0NSA9ICQoJzxkaXYgaWQ9Imh0bWxfYTI5Zjc5YzJhZmEzNDAxZTlhZDY0MTEyMjQ0YmI0NDUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJ1dGxlciBNYW5vciwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjhjNzNlODM2YjMxNDY5NDg2ZTVkYjA1Y2QwNjBlOWMuc2V0Q29udGVudChodG1sX2EyOWY3OWMyYWZhMzQwMWU5YWQ2NDExMjI0NGJiNDQ1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzFlMWM3OTBiYzJlNTQ4Njg5MGFjODJkYjQ2MTBlNGMwLmJpbmRQb3B1cChwb3B1cF9iOGM3M2U4MzZiMzE0Njk0ODZlNWRiMDVjZDA2MGU5Yyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kYWZmZTY3YWU0Zjk0N2NmYmM1N2I4YjgxNzg4NDRlMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjUzMDUzMTQ4MjgzMzE0LC03NC4yMzIxNTc3NTg5NjUyNl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82YzZkNGFjOGUzY2Q0MGI4YWVlZTgzMDY0MWExMWUzZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zNzZjNDE4MDQyYzg0ZDgwYmI0MWZkZTY0YjIxMDRkOCA9ICQoJzxkaXYgaWQ9Imh0bWxfMzc2YzQxODA0MmM4NGQ4MGJiNDFmZGU2NGIyMTA0ZDgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNoYXJsZXN0b24sIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzZjNmQ0YWM4ZTNjZDQwYjhhZWVlODMwNjQxYTExZTNkLnNldENvbnRlbnQoaHRtbF8zNzZjNDE4MDQyYzg0ZDgwYmI0MWZkZTY0YjIxMDRkOCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kYWZmZTY3YWU0Zjk0N2NmYmM1N2I4YjgxNzg4NDRlMS5iaW5kUG9wdXAocG9wdXBfNmM2ZDRhYzhlM2NkNDBiOGFlZWU4MzA2NDFhMTFlM2QpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNDc3ZTUyN2U4ZmE2NGM4NmJkYTc3NDdmZmFlYjg0ZmUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NDk0MDQwMDY1MDA3MiwtNzQuMjE1NzI4NTExMTM5NTJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNTQwMzU4ZGIzYTg1NGZkMGJlMDk3NzA1NGI4OGIzOWMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNDljOTc1YWUxMDllNGRiNGE5NTFjNTczOWU3NDUxMTIgPSAkKCc8ZGl2IGlkPSJodG1sXzQ5Yzk3NWFlMTA5ZTRkYjRhOTUxYzU3MzllNzQ1MTEyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb3NzdmlsbGUsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzU0MDM1OGRiM2E4NTRmZDBiZTA5NzcwNTRiODhiMzljLnNldENvbnRlbnQoaHRtbF80OWM5NzVhZTEwOWU0ZGI0YTk1MWM1NzM5ZTc0NTExMik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80NzdlNTI3ZThmYTY0Yzg2YmRhNzc0N2ZmYWViODRmZS5iaW5kUG9wdXAocG9wdXBfNTQwMzU4ZGIzYTg1NGZkMGJlMDk3NzA1NGI4OGIzOWMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNDQ0YTM0YzczODkwNGMxMjgyOGI1NjAyYWY5ZjRhMDggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NDkyODU4MjI3ODMyMSwtNzQuMTg1ODg2NzQ1ODM4OTNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOTU5Y2U0MzQ4NGQyNGVhYTlkYjczOTdlNDIxNjA0MDcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNWRjNjQ2MjU3YjdjNGU2NDk5ZWI2NTRiNzM0NmUxM2EgPSAkKCc8ZGl2IGlkPSJodG1sXzVkYzY0NjI1N2I3YzRlNjQ5OWViNjU0YjczNDZlMTNhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5BcmRlbiBIZWlnaHRzLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85NTljZTQzNDg0ZDI0ZWFhOWRiNzM5N2U0MjE2MDQwNy5zZXRDb250ZW50KGh0bWxfNWRjNjQ2MjU3YjdjNGU2NDk5ZWI2NTRiNzM0NmUxM2EpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNDQ0YTM0YzczODkwNGMxMjgyOGI1NjAyYWY5ZjRhMDguYmluZFBvcHVwKHBvcHVwXzk1OWNlNDM0ODRkMjRlYWE5ZGI3Mzk3ZTQyMTYwNDA3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzFhZjY2OGQ0ZjNjZTRiZDlhYzUyZTMzYmQzNzBkYTc0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTU1Mjk1MjM2MTczMTk0LC03NC4xNzA3OTQxNDc4NjA5Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84ZmMzMTMzMzVlYTc0ODUyYjU1ZThlYzJhM2I5MjYwNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kNjYwZjE4YjMxMjE0MjczODNjOTVlN2I2NTBhNjI2OCA9ICQoJzxkaXYgaWQ9Imh0bWxfZDY2MGYxOGIzMTIxNDI3MzgzYzk1ZTdiNjUwYTYyNjgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkdyZWVucmlkZ2UsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzhmYzMxMzMzNWVhNzQ4NTJiNTVlOGVjMmEzYjkyNjA3LnNldENvbnRlbnQoaHRtbF9kNjYwZjE4YjMxMjE0MjczODNjOTVlN2I2NTBhNjI2OCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xYWY2NjhkNGYzY2U0YmQ5YWM1MmUzM2JkMzcwZGE3NC5iaW5kUG9wdXAocG9wdXBfOGZjMzEzMzM1ZWE3NDg1MmI1NWU4ZWMyYTNiOTI2MDcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNzVmZDBhZjk5NTVjNDJkMTk5NmY0MDUwZmYxODBhNDkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41ODkxMzg5NDg3NTI4MSwtNzQuMTU5MDIyMDgxNTY2MDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTg5M2E1MGEwYTE5NDE4MDk1ZmQ2MWJmYTdiMjc4YTcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZWI2Y2ViMWUxMzcxNDYxZGFkYjUzNDc0MTgzZmMxMDQgPSAkKCc8ZGl2IGlkPSJodG1sX2ViNmNlYjFlMTM3MTQ2MWRhZGI1MzQ3NDE4M2ZjMTA0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IZWFydGxhbmQgVmlsbGFnZSwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTg5M2E1MGEwYTE5NDE4MDk1ZmQ2MWJmYTdiMjc4YTcuc2V0Q29udGVudChodG1sX2ViNmNlYjFlMTM3MTQ2MWRhZGI1MzQ3NDE4M2ZjMTA0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzc1ZmQwYWY5OTU1YzQyZDE5OTZmNDA1MGZmMTgwYTQ5LmJpbmRQb3B1cChwb3B1cF9hODkzYTUwYTBhMTk0MTgwOTVmZDYxYmZhN2IyNzhhNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jMTg1YmI4ZWUyNDQ0NDBkOTk2ODU4NDEwMjMxZmVmOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU5NDcyNjAyNzQ2Mjk1LC03NC4xODk1NjA0NTUxOTY5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2QzZjAwYjVkYmU2ZDRmYTY5NWYxYzRhY2IxZTM5OWE5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzczMzE0M2E5NDdlNjRmYWFiMzM1ZWNmMTliNzI3MzFjID0gJCgnPGRpdiBpZD0iaHRtbF83MzMxNDNhOTQ3ZTY0ZmFhYjMzNWVjZjE5YjcyNzMxYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2hlbHNlYSwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZDNmMDBiNWRiZTZkNGZhNjk1ZjFjNGFjYjFlMzk5YTkuc2V0Q29udGVudChodG1sXzczMzE0M2E5NDdlNjRmYWFiMzM1ZWNmMTliNzI3MzFjKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2MxODViYjhlZTI0NDQ0MGQ5OTY4NTg0MTAyMzFmZWY4LmJpbmRQb3B1cChwb3B1cF9kM2YwMGI1ZGJlNmQ0ZmE2OTVmMWM0YWNiMWUzOTlhOSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yNTIwYTM3N2Y4OTg0ZmIxOGQzYWU5ZWViNGJlZTQ3OSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYwNTc3ODY4NDUyMzU4LC03NC4xODcyNTYzODM4MTU2N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mYjVkMDhkYjIxNTY0Y2QwOWE5N2JhNTJiOTEzZTVlOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wYWY3MzU1ZWQyN2M0OTUwYjY1ZjBmN2U2NjJmNGRkNCA9ICQoJzxkaXYgaWQ9Imh0bWxfMGFmNzM1NWVkMjdjNDk1MGI2NWYwZjdlNjYyZjRkZDQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJsb29tZmllbGQsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2ZiNWQwOGRiMjE1NjRjZDA5YTk3YmE1MmI5MTNlNWU4LnNldENvbnRlbnQoaHRtbF8wYWY3MzU1ZWQyN2M0OTUwYjY1ZjBmN2U2NjJmNGRkNCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yNTIwYTM3N2Y4OTg0ZmIxOGQzYWU5ZWViNGJlZTQ3OS5iaW5kUG9wdXAocG9wdXBfZmI1ZDA4ZGIyMTU2NGNkMDlhOTdiYTUyYjkxM2U1ZTgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzgyZjQ1MWM3YmZlNGE1Njg3ZGFjNWEyY2YxMDdlMjcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MDk1OTE4MDA0MjAzLC03NC4xNTk0MDk0ODY1NzEyMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yYjM3MjVlZTZhYWY0NzNlYTM2MDI5YTJkYTFmYmJjMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mZjJjNzQ2ZDRhMzk0ZmRmYjA2ZDg3MWQzZTYwMTQwZSA9ICQoJzxkaXYgaWQ9Imh0bWxfZmYyYzc0NmQ0YTM5NGZkZmIwNmQ4NzFkM2U2MDE0MGUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJ1bGxzIEhlYWQsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzJiMzcyNWVlNmFhZjQ3M2VhMzYwMjlhMmRhMWZiYmMxLnNldENvbnRlbnQoaHRtbF9mZjJjNzQ2ZDRhMzk0ZmRmYjA2ZDg3MWQzZTYwMTQwZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jODJmNDUxYzdiZmU0YTU2ODdkYWM1YTJjZjEwN2UyNy5iaW5kUG9wdXAocG9wdXBfMmIzNzI1ZWU2YWFmNDczZWEzNjAyOWEyZGExZmJiYzEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOTBkNjg5OTA4MTM1NGUwODhlNjAwY2VmODM4NGE2MzkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43ODI2ODI1NjcxMjU3LC03My45NTMyNTY0NjgzNzExMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xZjRkMDgwZWMyODA0YmUxODE4YzlmMGUxMDBhMDE4NiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80MmI4ZGRkYjQzZTk0MTcwYjQ1YTBjYjgwYjk5MzFlMCA9ICQoJzxkaXYgaWQ9Imh0bWxfNDJiOGRkZGI0M2U5NDE3MGI0NWEwY2I4MGI5OTMxZTAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNhcm5lZ2llIEhpbGwsIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMWY0ZDA4MGVjMjgwNGJlMTgxOGM5ZjBlMTAwYTAxODYuc2V0Q29udGVudChodG1sXzQyYjhkZGRiNDNlOTQxNzBiNDVhMGNiODBiOTkzMWUwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzkwZDY4OTkwODEzNTRlMDg4ZTYwMGNlZjgzODRhNjM5LmJpbmRQb3B1cChwb3B1cF8xZjRkMDgwZWMyODA0YmUxODE4YzlmMGUxMDBhMDE4Nik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yYzhjNGMwNWM3OWY0NjQ4OWE0NzUyN2M2OTkxZGY4ZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcyMzI1OTAxODg1NzY4LC03My45ODg0MzM2ODAyMzU5N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82MWYyZDkwZGVjYzg0MDU3YWM5YzE2YWRlMWM4MjJmYyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xMTFkN2E3MWE2MWY0YzNkODA4ODUzNGMzYWUxYzM5NCA9ICQoJzxkaXYgaWQ9Imh0bWxfMTExZDdhNzFhNjFmNGMzZDgwODg1MzRjM2FlMWMzOTQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5vaG8sIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNjFmMmQ5MGRlY2M4NDA1N2FjOWMxNmFkZTFjODIyZmMuc2V0Q29udGVudChodG1sXzExMWQ3YTcxYTYxZjRjM2Q4MDg4NTM0YzNhZTFjMzk0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzJjOGM0YzA1Yzc5ZjQ2NDg5YTQ3NTI3YzY5OTFkZjhkLmJpbmRQb3B1cChwb3B1cF82MWYyZDkwZGVjYzg0MDU3YWM5YzE2YWRlMWM4MjJmYyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83ZmVkZmVjYTkyNmQ0NzA3ODI1OTViM2I4ZjQ2MzQ2NyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcxNTIyODkyMDQ2MjgyLC03NC4wMDU0MTUyOTg3MzM1NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80YTg3OGE5Y2Q1YzM0MzFhYWM1YjMwYjBiZGEyMmMzYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84NmY0NTA1OTNhNjQ0ZjllOTg0OWZjZjA2YjgzMTZlNyA9ICQoJzxkaXYgaWQ9Imh0bWxfODZmNDUwNTkzYTY0NGY5ZTk4NDlmY2YwNmI4MzE2ZTciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNpdmljIENlbnRlciwgTWFuaGF0dGFuPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80YTg3OGE5Y2Q1YzM0MzFhYWM1YjMwYjBiZGEyMmMzYS5zZXRDb250ZW50KGh0bWxfODZmNDUwNTkzYTY0NGY5ZTk4NDlmY2YwNmI4MzE2ZTcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfN2ZlZGZlY2E5MjZkNDcwNzgyNTk1YjNiOGY0NjM0NjcuYmluZFBvcHVwKHBvcHVwXzRhODc4YTljZDVjMzQzMWFhYzViMzBiMGJkYTIyYzNhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2JjZjhhNGU0ODgzMzQzYzNiM2U3NDU5NTQ1OTYzNDU2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzQ4NTA5NjY0MzEyMiwtNzMuOTg4NzEzMTMyODUyNDddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMmRjMzdiYTQzMWM0NGI4MWI1ZjMwOTExNzk5NzVkMmQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOGYxMGEzNGVlN2I3NDBlNGE5NTY1ZjEyZjYzYjM4ODggPSAkKCc8ZGl2IGlkPSJodG1sXzhmMTBhMzRlZTdiNzQwZTRhOTU2NWYxMmY2M2IzODg4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NaWR0b3duIFNvdXRoLCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzJkYzM3YmE0MzFjNDRiODFiNWYzMDkxMTc5OTc1ZDJkLnNldENvbnRlbnQoaHRtbF84ZjEwYTM0ZWU3Yjc0MGU0YTk1NjVmMTJmNjNiMzg4OCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iY2Y4YTRlNDg4MzM0M2MzYjNlNzQ1OTU0NTk2MzQ1Ni5iaW5kUG9wdXAocG9wdXBfMmRjMzdiYTQzMWM0NGI4MWI1ZjMwOTExNzk5NzVkMmQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMmVlZmQ4OGMwMzJiNDFiZWFmODhiMzRhYjYzYzdjM2UgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41Njk2MDU5NDI3NTUwNSwtNzQuMTM0MDU3Mjk4NjI1N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jZGQ4MzU5MTAzYzY0ZDJlYmNkZDgwNTUxNjYyMDhlNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84NTJiMjlkNzE1YjQ0ZmMwYTI2MGM2NDlkNzE4Y2MzYyA9ICQoJzxkaXYgaWQ9Imh0bWxfODUyYjI5ZDcxNWI0NGZjMGEyNjBjNjQ5ZDcxOGNjM2MiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJpY2htb25kIFRvd24sIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2NkZDgzNTkxMDNjNjRkMmViY2RkODA1NTE2NjIwOGU3LnNldENvbnRlbnQoaHRtbF84NTJiMjlkNzE1YjQ0ZmMwYTI2MGM2NDlkNzE4Y2MzYyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yZWVmZDg4YzAzMmI0MWJlYWY4OGIzNGFiNjNjN2MzZS5iaW5kUG9wdXAocG9wdXBfY2RkODM1OTEwM2M2NGQyZWJjZGQ4MDU1MTY2MjA4ZTcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMjhiYmYxMWQ5YmZmNDFkMTgxOWY3NDUwOWM3NmM1NzkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MDk3MTkzNDA3OTI4NCwtNzQuMDY2Njc3NjYwNjE3NzFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMjU2YTQyYWI4NDI0NGVmYjkzZGU5MjEwNmQzMTdmZTQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfY2U2NzU2YmY5MmI0NGJlZjkxZmE0NzEwODdiM2Y4NjYgPSAkKCc8ZGl2IGlkPSJodG1sX2NlNjc1NmJmOTJiNDRiZWY5MWZhNDcxMDg3YjNmODY2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TaG9yZSBBY3JlcywgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMjU2YTQyYWI4NDI0NGVmYjkzZGU5MjEwNmQzMTdmZTQuc2V0Q29udGVudChodG1sX2NlNjc1NmJmOTJiNDRiZWY5MWZhNDcxMDg3YjNmODY2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzI4YmJmMTFkOWJmZjQxZDE4MTlmNzQ1MDljNzZjNTc5LmJpbmRQb3B1cChwb3B1cF8yNTZhNDJhYjg0MjQ0ZWZiOTNkZTkyMTA2ZDMxN2ZlNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lYWM3MjUxMTYyYmM0ZjEzOWUxYWVlNGM4OTc5MDM2NiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYxOTE3ODQ1MjAyODQzLC03NC4wNzI2NDI0NDU0ODRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMGUwYjgxNWQwZTk0NDliNDlmOTUxZWY0MDIzNDZkNmQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTU2YWZhMjAxMTcyNGVhYWE4MTk4NTVjNmM0NzJkY2UgPSAkKCc8ZGl2IGlkPSJodG1sX2U1NmFmYTIwMTE3MjRlYWFhODE5ODU1YzZjNDcyZGNlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DbGlmdG9uLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wZTBiODE1ZDBlOTQ0OWI0OWY5NTFlZjQwMjM0NmQ2ZC5zZXRDb250ZW50KGh0bWxfZTU2YWZhMjAxMTcyNGVhYWE4MTk4NTVjNmM0NzJkY2UpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZWFjNzI1MTE2MmJjNGYxMzllMWFlZTRjODk3OTAzNjYuYmluZFBvcHVwKHBvcHVwXzBlMGI4MTVkMGU5NDQ5YjQ5Zjk1MWVmNDAyMzQ2ZDZkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzYzZTFhMzI5MTY4ZTRiOWE4MDdhMDUzZWJjMzVkN2UxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjA0NDczMTg5Njg3OSwtNzQuMDg0MDIzNjQ3NDAzNThdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYThjNmQ4ZDI5NDBmNDU0MmEyZDNiY2I3MWQyZjg5ZmIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfODEyZTMxMDVhY2E2NGIzZmJiNWUyMTA4ZDE3MDQ3ZTcgPSAkKCc8ZGl2IGlkPSJodG1sXzgxMmUzMTA1YWNhNjRiM2ZiYjVlMjEwOGQxNzA0N2U3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Db25jb3JkLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hOGM2ZDhkMjk0MGY0NTQyYTJkM2JjYjcxZDJmODlmYi5zZXRDb250ZW50KGh0bWxfODEyZTMxMDVhY2E2NGIzZmJiNWUyMTA4ZDE3MDQ3ZTcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNjNlMWEzMjkxNjhlNGI5YTgwN2EwNTNlYmMzNWQ3ZTEuYmluZFBvcHVwKHBvcHVwX2E4YzZkOGQyOTQwZjQ1NDJhMmQzYmNiNzFkMmY4OWZiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzM1ODgxNGYyYWNjZDRiYjdhNTllYTg1MjVhMjg0ZTkyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjA2Nzk0Mzk0ODAxLC03NC4wOTc3NjIwNjk3MjUyMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hODc4MThmZWI5YmQ0NjVmYWNjZGQ4ODM5YWE2NWZiZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zOTI0OWZlZjdhYzk0MjJiYmQ3MTVjNmNlZDg1ODI3NiA9ICQoJzxkaXYgaWQ9Imh0bWxfMzkyNDlmZWY3YWM5NDIyYmJkNzE1YzZjZWQ4NTgyNzYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVtZXJzb24gSGlsbCwgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTg3ODE4ZmViOWJkNDY1ZmFjY2RkODgzOWFhNjVmYmQuc2V0Q29udGVudChodG1sXzM5MjQ5ZmVmN2FjOTQyMmJiZDcxNWM2Y2VkODU4Mjc2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzM1ODgxNGYyYWNjZDRiYjdhNTllYTg1MjVhMjg0ZTkyLmJpbmRQb3B1cChwb3B1cF9hODc4MThmZWI5YmQ0NjVmYWNjZGQ4ODM5YWE2NWZiZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xMzg3NGY0MWYyMjQ0OGI2YTlkOTc5ODhmNjNjYmRkOSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYzNTYzMDAwNjgxMTUxLC03NC4wOTgwNTA2MjM3Mzg4N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80YmRjMTI1NGZhZDA0M2M1OTI0NDNmM2M3MTFiYzFkOSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84NWMxYjEzYTk5Yjg0MTIwYWQ3MWJmODFiNjkwNmNlNCA9ICQoJzxkaXYgaWQ9Imh0bWxfODVjMWIxM2E5OWI4NDEyMGFkNzFiZjgxYjY5MDZjZTQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJhbmRhbGwgTWFub3IsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzRiZGMxMjU0ZmFkMDQzYzU5MjQ0M2YzYzcxMWJjMWQ5LnNldENvbnRlbnQoaHRtbF84NWMxYjEzYTk5Yjg0MTIwYWQ3MWJmODFiNjkwNmNlNCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xMzg3NGY0MWYyMjQ0OGI2YTlkOTc5ODhmNjNjYmRkOS5iaW5kUG9wdXAocG9wdXBfNGJkYzEyNTRmYWQwNDNjNTkyNDQzZjNjNzExYmMxZDkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMTI1YmQ3ZWMzM2I3NDdkMzhiNWZiMThhODJkZmEyNDQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42Mzg0MzI4Mzc5NDc5NSwtNzQuMTg2MjIzMzE3NDk4MjNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjA4MWQ4MjEzMmY4NGM2OWE2YzU1MDMzYmYwOGU1YTggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZmY4ODVlODlmZDM5NDdkOGFkYzM5OWM1ZThhOTg0ODYgPSAkKCc8ZGl2IGlkPSJodG1sX2ZmODg1ZTg5ZmQzOTQ3ZDhhZGMzOTljNWU4YTk4NDg2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ib3dsYW5kIEhvb2ssIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2YwODFkODIxMzJmODRjNjlhNmM1NTAzM2JmMDhlNWE4LnNldENvbnRlbnQoaHRtbF9mZjg4NWU4OWZkMzk0N2Q4YWRjMzk5YzVlOGE5ODQ4Nik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xMjViZDdlYzMzYjc0N2QzOGI1ZmIxOGE4MmRmYTI0NC5iaW5kUG9wdXAocG9wdXBfZjA4MWQ4MjEzMmY4NGM2OWE2YzU1MDMzYmYwOGU1YTgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfY2FhNTdjNmRmOTBlNDA5YTlkZGE1ZGFiYWJhNTQxNDAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MzAxNDY3NDExOTM4MjYsLTc0LjE0MTgxNjc4OTY4ODldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZGJlNTM2ZjVjNWExNDJiNDgxM2M4Y2IyMmU3NTMwNjUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYmFkY2UyZDZjNTI0NDc2NmFmMmI0ZTY2Mzc0OTA3YjMgPSAkKCc8ZGl2IGlkPSJodG1sX2JhZGNlMmQ2YzUyNDQ3NjZhZjJiNGU2NjM3NDkwN2IzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5FbG0gUGFyaywgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZGJlNTM2ZjVjNWExNDJiNDgxM2M4Y2IyMmU3NTMwNjUuc2V0Q29udGVudChodG1sX2JhZGNlMmQ2YzUyNDQ3NjZhZjJiNGU2NjM3NDkwN2IzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2NhYTU3YzZkZjkwZTQwOWE5ZGRhNWRhYmFiYTU0MTQwLmJpbmRQb3B1cChwb3B1cF9kYmU1MzZmNWM1YTE0MmI0ODEzYzhjYjIyZTc1MzA2NSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hYTJkYzFiYjA1ZDM0ZWRiOWZmYTZhYTBmNzMxZjM2YyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY1MjExNzQ1MTc5MzQ5NCwtNzMuOTE2NjUzMzE5NzgwNDhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYzI0ZTllMzhlZjEzNGE5YzlhZGFhMDFmZWNmNWI1NzcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMjMzYzQzMWEyOWM3NDBmN2E5ZGI1MDY2Zjk0YzgzZWMgPSAkKCc8ZGl2IGlkPSJodG1sXzIzM2M0MzFhMjljNzQwZjdhOWRiNTA2NmY5NGM4M2VjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5SZW1zZW4gVmlsbGFnZSwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2MyNGU5ZTM4ZWYxMzRhOWM5YWRhYTAxZmVjZjViNTc3LnNldENvbnRlbnQoaHRtbF8yMzNjNDMxYTI5Yzc0MGY3YTlkYjUwNjZmOTRjODNlYyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hYTJkYzFiYjA1ZDM0ZWRiOWZmYTZhYTBmNzMxZjM2Yy5iaW5kUG9wdXAocG9wdXBfYzI0ZTllMzhlZjEzNGE5YzlhZGFhMDFmZWNmNWI1NzcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMTY4YTM4MDMwMDM3NDE3MWI2NzMxYzUxZjg0NjNhMjMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42NjI3NDQyNzk2OTY2LC03My44ODUxMTc3NjM3OTI5Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83ZmRjYzliNWFmMzU0MzIyOWMyNTk3YmQzMDM1ZjMyZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iODkxYThjNDQ0Zjg0MGQ5ODViNGQ4NDYzMzg3ODVlMSA9ICQoJzxkaXYgaWQ9Imh0bWxfYjg5MWE4YzQ0NGY4NDBkOTg1YjRkODQ2MzM4Nzg1ZTEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5ldyBMb3RzLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfN2ZkY2M5YjVhZjM1NDMyMjljMjU5N2JkMzAzNWYzMmUuc2V0Q29udGVudChodG1sX2I4OTFhOGM0NDRmODQwZDk4NWI0ZDg0NjMzODc4NWUxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzE2OGEzODAzMDAzNzQxNzFiNjczMWM1MWY4NDYzYTIzLmJpbmRQb3B1cChwb3B1cF83ZmRjYzliNWFmMzU0MzIyOWMyNTk3YmQzMDM1ZjMyZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kNTQwOWU5ZjBiNmI0MzJkYjg2MjkwYmI2YjJkY2IzNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYzMTMxNzU1MDM5NjY3LC03My45MDIzMzQ3NDI5NTgzNl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lOTNkNzYxYzgyZTE0NjYxYTRjMjM4YzZjODBlMzY0NCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mZTMwMDMxZjIxMTk0MjhlODU4YWMwZjYwODdkNTMxMSA9ICQoJzxkaXYgaWQ9Imh0bWxfZmUzMDAzMWYyMTE5NDI4ZTg1OGFjMGY2MDg3ZDUzMTEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlBhZXJkZWdhdCBCYXNpbiwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2U5M2Q3NjFjODJlMTQ2NjFhNGMyMzhjNmM4MGUzNjQ0LnNldENvbnRlbnQoaHRtbF9mZTMwMDMxZjIxMTk0MjhlODU4YWMwZjYwODdkNTMxMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kNTQwOWU5ZjBiNmI0MzJkYjg2MjkwYmI2YjJkY2IzNi5iaW5kUG9wdXAocG9wdXBfZTkzZDc2MWM4MmUxNDY2MWE0YzIzOGM2YzgwZTM2NDQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMDYwMWM3OGNkMjEzNDU3MjhkOTAzMzQzZjA3MWJmMDMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MTU5NzQyMzk2MjMzNiwtNzMuOTE1MTUzOTE1NTA0MDRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOGNmYTgxODM3ZmJkNGM4OTlhNzVjNWYxN2EzYmU5ODYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOTkzY2QyZDcwMDdjNGIwZmFlYTdhNWQ3MzI1YTQ5NGYgPSAkKCc8ZGl2IGlkPSJodG1sXzk5M2NkMmQ3MDA3YzRiMGZhZWE3YTVkNzMyNWE0OTRmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NaWxsIEJhc2luLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOGNmYTgxODM3ZmJkNGM4OTlhNzVjNWYxN2EzYmU5ODYuc2V0Q29udGVudChodG1sXzk5M2NkMmQ3MDA3YzRiMGZhZWE3YTVkNzMyNWE0OTRmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzA2MDFjNzhjZDIxMzQ1NzI4ZDkwMzM0M2YwNzFiZjAzLmJpbmRQb3B1cChwb3B1cF84Y2ZhODE4MzdmYmQ0Yzg5OWE3NWM1ZjE3YTNiZTk4Nik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84N2VmY2E0MGRiMWU0NjI3OTlkOTM4MWZkZWMwNjc0NiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcxMTQ1OTY0MzcwNDgyLC03My43OTY0NjQ2MjA4MTU5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mYjM0ZjM1NzdmYjk0MGI0Yjk3MGZhNjQ5YmQwZDcwNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iNzlmNWUwYmI5NGE0YTFhYTNjMjBlMjQwMDNmYzMwOCA9ICQoJzxkaXYgaWQ9Imh0bWxfYjc5ZjVlMGJiOTRhNGExYWEzYzIwZTI0MDAzZmMzMDgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkphbWFpY2EgSGlsbHMsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZmIzNGYzNTc3ZmI5NDBiNGI5NzBmYTY0OWJkMGQ3MDcuc2V0Q29udGVudChodG1sX2I3OWY1ZTBiYjk0YTRhMWFhM2MyMGUyNDAwM2ZjMzA4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzg3ZWZjYTQwZGIxZTQ2Mjc5OWQ5MzgxZmRlYzA2NzQ2LmJpbmRQb3B1cChwb3B1cF9mYjM0ZjM1NzdmYjk0MGI0Yjk3MGZhNjQ5YmQwZDcwNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zMTBlMTcwODU3ZDI0NDM2YTdkMzBkNGNjZjY5NmNhMCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjczMzUwMDI1NDI5NzU3LC03My43OTY3MTY3ODAyODM0OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9iNDM5OGU3ZjNjNTY0MDM3YjA2NWQ2ZjQ4YmQ1ZmRkZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kNjU1YTJjZjZhNzA0YTIzYTQ0MjY3MjEyYzIxODVkZSA9ICQoJzxkaXYgaWQ9Imh0bWxfZDY1NWEyY2Y2YTcwNGEyM2E0NDI2NzIxMmMyMTg1ZGUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlV0b3BpYSwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iNDM5OGU3ZjNjNTY0MDM3YjA2NWQ2ZjQ4YmQ1ZmRkZi5zZXRDb250ZW50KGh0bWxfZDY1NWEyY2Y2YTcwNGEyM2E0NDI2NzIxMmMyMTg1ZGUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMzEwZTE3MDg1N2QyNDQzNmE3ZDMwZDRjY2Y2OTZjYTAuYmluZFBvcHVwKHBvcHVwX2I0Mzk4ZTdmM2M1NjQwMzdiMDY1ZDZmNDhiZDVmZGRmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzYwMjQzNjIyNTRmNjQ0MzNhMjVmZTE3MmU2YWJmNzBlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzM0OTM2MTgwNzU0NzgsLTczLjgwNDg2MTIwMDQwNTM3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzAwZTA4ZjJmNDE5NTQ5ZThiMjJiZmM0MTYxYjM2OWFiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2Q2ZWM1MjEzYWFlZTRlYjdiZDdiYmZiZDMxNTExYzRkID0gJCgnPGRpdiBpZD0iaHRtbF9kNmVjNTIxM2FhZWU0ZWI3YmQ3YmJmYmQzMTUxMWM0ZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UG9tb25vaywgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wMGUwOGYyZjQxOTU0OWU4YjIyYmZjNDE2MWIzNjlhYi5zZXRDb250ZW50KGh0bWxfZDZlYzUyMTNhYWVlNGViN2JkN2JiZmJkMzE1MTFjNGQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNjAyNDM2MjI1NGY2NDQzM2EyNWZlMTcyZTZhYmY3MGUuYmluZFBvcHVwKHBvcHVwXzAwZTA4ZjJmNDE5NTQ5ZThiMjJiZmM0MTYxYjM2OWFiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2NhZGI2MTIxYmQzNzQ4Y2E4ODhkZjFjYjc5Nzc2ODYyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzcwMzE3MzkyOTk4MiwtNzMuODk0Njc5OTYyNzA1NzRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNDllNjIyOTYyNjk2NDFmYzg0OWE4YjMzZmRlMmM4ZWMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzI0NTlkYTA5YmQ1NDU2Njk0OGVhZTNkNjg1MWFlNjAgPSAkKCc8ZGl2IGlkPSJodG1sXzcyNDU5ZGEwOWJkNTQ1NjY5NDhlYWUzZDY4NTFhZTYwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Bc3RvcmlhIEhlaWdodHMsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNDllNjIyOTYyNjk2NDFmYzg0OWE4YjMzZmRlMmM4ZWMuc2V0Q29udGVudChodG1sXzcyNDU5ZGEwOWJkNTQ1NjY5NDhlYWUzZDY4NTFhZTYwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2NhZGI2MTIxYmQzNzQ4Y2E4ODhkZjFjYjc5Nzc2ODYyLmJpbmRQb3B1cChwb3B1cF80OWU2MjI5NjI2OTY0MWZjODQ5YThiMzNmZGUyYzhlYyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81YmNmYjBkOGRlYzY0YzY1OWNiZGI4ODg1NjQ0NDg3MiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjgzMTQyODM0MTYxNTQ4LC03My45MDExOTkwMzM4NzY2N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yMDRmY2QzODE0M2I0NWQ4OTMyZTE1MzQ0N2Y1YmM2MiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81MjFkMWZlNzFjNTE0NDkxOTI4NjU2ODQyMjQ0MmVlYiA9ICQoJzxkaXYgaWQ9Imh0bWxfNTIxZDFmZTcxYzUxNDQ5MTkyODY1Njg0MjI0NDJlZWIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNsYXJlbW9udCBWaWxsYWdlLCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMjA0ZmNkMzgxNDNiNDVkODkzMmUxNTM0NDdmNWJjNjIuc2V0Q29udGVudChodG1sXzUyMWQxZmU3MWM1MTQ0OTE5Mjg2NTY4NDIyNDQyZWViKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzViY2ZiMGQ4ZGVjNjRjNjU5Y2JkYjg4ODU2NDQ0ODcyLmJpbmRQb3B1cChwb3B1cF8yMDRmY2QzODE0M2I0NWQ4OTMyZTE1MzQ0N2Y1YmM2Mik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85MGVkMjhmOTI5MGM0YWIyODQ5M2E4NjkxOGY5ZTAxZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjgyNDc4MDQ5MDg0MjkwNSwtNzMuOTE1ODQ2NTI3NTkwMDldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOTZiNDkwMWI1YmIzNGYwYmI2YTBhOTg1ODBjYzRmZGUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzZiNWIwYzQ4ZmRkNDY3ZTg2MmQyYTBmMGY2NDYzMjIgPSAkKCc8ZGl2IGlkPSJodG1sXzc2YjViMGM0OGZkZDQ2N2U4NjJkMmEwZjBmNjQ2MzIyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Db25jb3Vyc2UgVmlsbGFnZSwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzk2YjQ5MDFiNWJiMzRmMGJiNmEwYTk4NTgwY2M0ZmRlLnNldENvbnRlbnQoaHRtbF83NmI1YjBjNDhmZGQ0NjdlODYyZDJhMGYwZjY0NjMyMik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85MGVkMjhmOTI5MGM0YWIyODQ5M2E4NjkxOGY5ZTAxZC5iaW5kUG9wdXAocG9wdXBfOTZiNDkwMWI1YmIzNGYwYmI2YTBhOTg1ODBjYzRmZGUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMWJhNjIzZmExOTRkNDg1M2FkNjIwYTliMDZmOGNiM2QgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NDM4MjYxNzY3MTY1NCwtNzMuOTE2NTU1NTE5NjQ0MTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjg4MmUwZTRmZDIyNDM5YWJjYjI0NGY4M2ExNGYyMGQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfODcxZDg3ZDhjODYxNGE3Yzg0MmI0NzkwY2FjY2JlYWUgPSAkKCc8ZGl2IGlkPSJodG1sXzg3MWQ4N2Q4Yzg2MTRhN2M4NDJiNDc5MGNhY2NiZWFlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Nb3VudCBFZGVuLCBCcm9ueDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNjg4MmUwZTRmZDIyNDM5YWJjYjI0NGY4M2ExNGYyMGQuc2V0Q29udGVudChodG1sXzg3MWQ4N2Q4Yzg2MTRhN2M4NDJiNDc5MGNhY2NiZWFlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzFiYTYyM2ZhMTk0ZDQ4NTNhZDYyMGE5YjA2ZjhjYjNkLmJpbmRQb3B1cChwb3B1cF82ODgyZTBlNGZkMjI0MzlhYmNiMjQ0ZjgzYTE0ZjIwZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hZGJjNWI4NjkyNTA0NmEwYTBiMjhhNmI3MjYxOGM0NyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg0ODg0MTYwNzI0NjY1LC03My45MDgyOTkzMDg4MTk4OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8wOWFmZWQyODNhOWU0YTMwYmMyMWNkZjAzNTRjYmViOSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mYzMzNTcwMTM3Yzk0YjM3ODQ0NTQzOThmOTllNThlYiA9ICQoJzxkaXYgaWQ9Imh0bWxfZmMzMzU3MDEzN2M5NGIzNzg0NDU0Mzk4Zjk5ZTU4ZWIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk1vdW50IEhvcGUsIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wOWFmZWQyODNhOWU0YTMwYmMyMWNkZjAzNTRjYmViOS5zZXRDb250ZW50KGh0bWxfZmMzMzU3MDEzN2M5NGIzNzg0NDU0Mzk4Zjk5ZTU4ZWIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYWRiYzViODY5MjUwNDZhMGEwYjI4YTZiNzI2MThjNDcuYmluZFBvcHVwKHBvcHVwXzA5YWZlZDI4M2E5ZTRhMzBiYzIxY2RmMDM1NGNiZWI5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2UwZDg2NWUxYTJkZjQ2Nzc5NGFhNWJjNjllMTc1MDM4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzYwMjgwMzMxMzEzNzQsLTczLjk2MzU1NjE0MDk0MzAzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzA5MjY5YjRkZDI1ZjQ2YWZhYTRkYmUxOGEwNjM5NDhjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2YwZWQzN2YxODg1ODRiNmJiZmZiYzIyMDcwMTEzZmEyID0gJCgnPGRpdiBpZD0iaHRtbF9mMGVkMzdmMTg4NTg0YjZiYmZmYmMyMjA3MDExM2ZhMiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U3V0dG9uIFBsYWNlLCBNYW5oYXR0YW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzA5MjY5YjRkZDI1ZjQ2YWZhYTRkYmUxOGEwNjM5NDhjLnNldENvbnRlbnQoaHRtbF9mMGVkMzdmMTg4NTg0YjZiYmZmYmMyMjA3MDExM2ZhMik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lMGQ4NjVlMWEyZGY0Njc3OTRhYTViYzY5ZTE3NTAzOC5iaW5kUG9wdXAocG9wdXBfMDkyNjliNGRkMjVmNDZhZmFhNGRiZTE4YTA2Mzk0OGMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTc5NTAxY2IyNDcyNGVhYWIwOWJkZjhjOGM4MmI0NGQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NDM0MTQwOTAwNzM1MzYsLTczLjk1Mzg2NzgyMTMwNzQ1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2FlNDJlYzM3NzlhMjQ0ZmU4NTM5YjA2NjA4ZTkxODczID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzI1ZjMzNzkwNjU2YjQ5MjRhOWM2YmJiZjBlOTgyNWNiID0gJCgnPGRpdiBpZD0iaHRtbF8yNWYzMzc5MDY1NmI0OTI0YTljNmJiYmYwZTk4MjVjYiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SHVudGVycyBQb2ludCwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hZTQyZWMzNzc5YTI0NGZlODUzOWIwNjYwOGU5MTg3My5zZXRDb250ZW50KGh0bWxfMjVmMzM3OTA2NTZiNDkyNGE5YzZiYmJmMGU5ODI1Y2IpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYTc5NTAxY2IyNDcyNGVhYWIwOWJkZjhjOGM4MmI0NGQuYmluZFBvcHVwKHBvcHVwX2FlNDJlYzM3NzlhMjQ0ZmU4NTM5YjA2NjA4ZTkxODczKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzMwOTU4MjUxZjhhNDRjYTFiZGQyMTU4ZGZjYjIzOTJlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzUyMDQyMzY5NTA3MjIsLTczLjk2NzcwODI0NTgxODM0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzYyMjRkMzU0ZjQyYTRlMjA5OWUwYTdkNzcwZDgwY2JhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzk1ZGFmODgzZmI5OTRhZTU5ODY5YjM5NGI2NjY2ZWFkID0gJCgnPGRpdiBpZD0iaHRtbF85NWRhZjg4M2ZiOTk0YWU1OTg2OWIzOTRiNjY2NmVhZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VHVydGxlIEJheSwgTWFuaGF0dGFuPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82MjI0ZDM1NGY0MmE0ZTIwOTllMGE3ZDc3MGQ4MGNiYS5zZXRDb250ZW50KGh0bWxfOTVkYWY4ODNmYjk5NGFlNTk4NjliMzk0YjY2NjZlYWQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMzA5NTgyNTFmOGE0NGNhMWJkZDIxNThkZmNiMjM5MmUuYmluZFBvcHVwKHBvcHVwXzYyMjRkMzU0ZjQyYTRlMjA5OWUwYTdkNzcwZDgwY2JhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2RhMTg1NWJhMDE3YTQ3NDZiYjkwMWQ0MzJhMWZlZDBlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzQ2OTE3NDEwNzQwMTk1LC03My45NzEyMTkyODcyMjI2NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jM2FlNjZhNzJmNDk0ZTk2OTYwYTgxYmRjMzE1YWYwMiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jYjIyNTk5MTc2MzQ0MzliYmFiNWIwM2UwYTEwMmNlYSA9ICQoJzxkaXYgaWQ9Imh0bWxfY2IyMjU5OTE3NjM0NDM5YmJhYjViMDNlMGExMDJjZWEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlR1ZG9yIENpdHksIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYzNhZTY2YTcyZjQ5NGU5Njk2MGE4MWJkYzMxNWFmMDIuc2V0Q29udGVudChodG1sX2NiMjI1OTkxNzYzNDQzOWJiYWI1YjAzZTBhMTAyY2VhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2RhMTg1NWJhMDE3YTQ3NDZiYjkwMWQ0MzJhMWZlZDBlLmJpbmRQb3B1cChwb3B1cF9jM2FlNjZhNzJmNDk0ZTk2OTYwYTgxYmRjMzE1YWYwMik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xM2IzY2E5M2IxM2E0NzkxOGZkNDBmMjgwYTcxNTA4YSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjczMDk5OTU1NDc3MDYxLC03My45NzQwNTE3MDQ2OTIwM10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83MjkwMjM0Mzc4ZGU0MWZmOTIwNDc4MzBmOTMwZmIxZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85MmZmNzkxYmI0MzM0NDJjOGU3OTBjOWJmYjkwZGU5ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfOTJmZjc5MWJiNDMzNDQyYzhlNzkwYzliZmI5MGRlOWYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlN0dXl2ZXNhbnQgVG93biwgTWFuaGF0dGFuPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83MjkwMjM0Mzc4ZGU0MWZmOTIwNDc4MzBmOTMwZmIxZi5zZXRDb250ZW50KGh0bWxfOTJmZjc5MWJiNDMzNDQyYzhlNzkwYzliZmI5MGRlOWYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMTNiM2NhOTNiMTNhNDc5MThmZDQwZjI4MGE3MTUwOGEuYmluZFBvcHVwKHBvcHVwXzcyOTAyMzQzNzhkZTQxZmY5MjA0NzgzMGY5MzBmYjFmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzYyNGEzNTliMTFkZjQxYjU4YzNmOWM1Y2ZhMmVjOTI4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzM5NjczMDQ3NjM4NDI2LC03My45OTA5NDcxMDUyODI2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzFhMGU1NTBiNDZmMjRkNDc4YTQ0YTZkMjBmZWVmYjQzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2MzYmUxZmE5ODkwMzRiMThhMWRlZGJiNWE4NjM3MzQyID0gJCgnPGRpdiBpZD0iaHRtbF9jM2JlMWZhOTg5MDM0YjE4YTFkZWRiYjVhODYzNzM0MiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RmxhdGlyb24sIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMWEwZTU1MGI0NmYyNGQ0NzhhNDRhNmQyMGZlZWZiNDMuc2V0Q29udGVudChodG1sX2MzYmUxZmE5ODkwMzRiMThhMWRlZGJiNWE4NjM3MzQyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzYyNGEzNTliMTFkZjQxYjU4YzNmOWM1Y2ZhMmVjOTI4LmJpbmRQb3B1cChwb3B1cF8xYTBlNTUwYjQ2ZjI0ZDQ3OGE0NGE2ZDIwZmVlZmI0Myk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80MjA4YzdmYmZhNGU0ZDQzYjljOWQ0OGE1ZWI3MzZhZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc0NTY1MTgwNjA4MDc2LC03My45MTgxOTI4NjQzMTY4Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84Y2EwMDA2N2ZlMTE0MmQzYWJkZjI3N2ZkYzY2YzNhNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wNDVhM2VkN2YwNGE0OWE1OWYyNGI1NmYzNTYzN2ZhOSA9ICQoJzxkaXYgaWQ9Imh0bWxfMDQ1YTNlZDdmMDRhNDlhNTlmMjRiNTZmMzU2MzdmYTkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlN1bm55c2lkZSBHYXJkZW5zLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzhjYTAwMDY3ZmUxMTQyZDNhYmRmMjc3ZmRjNjZjM2E0LnNldENvbnRlbnQoaHRtbF8wNDVhM2VkN2YwNGE0OWE1OWYyNGI1NmYzNTYzN2ZhOSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80MjA4YzdmYmZhNGU0ZDQzYjljOWQ0OGE1ZWI3MzZhZi5iaW5kUG9wdXAocG9wdXBfOGNhMDAwNjdmZTExNDJkM2FiZGYyNzdmZGM2NmMzYTQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfY2E5OGIyOTBhMjJmNGYxYTlmOTRlM2YyYTEyNTlmZmEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MzcyNTA3MTY5NDQ5NywtNzMuOTMyNDQyMzUyNjAxNzhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTAzNGJiNzdkMzc2NDVlMjgwMGU3M2ViYjgzZWFjZGEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYTUwOWYxOWExMGJiNDEzYmE2ZTdmZjE2MTEzYmNhMjUgPSAkKCc8ZGl2IGlkPSJodG1sX2E1MDlmMTlhMTBiYjQxM2JhNmU3ZmYxNjExM2JjYTI1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CbGlzc3ZpbGxlLCBRdWVlbnM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2EwMzRiYjc3ZDM3NjQ1ZTI4MDBlNzNlYmI4M2VhY2RhLnNldENvbnRlbnQoaHRtbF9hNTA5ZjE5YTEwYmI0MTNiYTZlN2ZmMTYxMTNiY2EyNSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jYTk4YjI5MGEyMmY0ZjFhOWY5NGUzZjJhMTI1OWZmYS5iaW5kUG9wdXAocG9wdXBfYTAzNGJiNzdkMzc2NDVlMjgwMGU3M2ViYjgzZWFjZGEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzgzMDhmYWY5MDZlNGMyYmEyZmVmZDEyMzg3ZDk5M2IgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MDMyODEwOTA5MzAxNCwtNzMuOTk1NTA3NTE4ODg0MTVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZmU4YjBiNmQ5OTUwNDM5MmE2M2NlNzg1Zjc2YmZhODAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOTZkNmVmY2M4ZDc4NDg0ODkwMTkwYmJlOTFjOTNhY2EgPSAkKCc8ZGl2IGlkPSJodG1sXzk2ZDZlZmNjOGQ3ODQ4NDg5MDE5MGJiZTkxYzkzYWNhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5GdWx0b24gRmVycnksIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mZThiMGI2ZDk5NTA0MzkyYTYzY2U3ODVmNzZiZmE4MC5zZXRDb250ZW50KGh0bWxfOTZkNmVmY2M4ZDc4NDg0ODkwMTkwYmJlOTFjOTNhY2EpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzgzMDhmYWY5MDZlNGMyYmEyZmVmZDEyMzg3ZDk5M2IuYmluZFBvcHVwKHBvcHVwX2ZlOGIwYjZkOTk1MDQzOTJhNjNjZTc4NWY3NmJmYTgwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2ViZTkwOGNiMmI3MDRhY2U4NWMyY2FkMzczMTc5MWNiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzAzMzIxNDk4ODI4NzQsLTczLjk4MTExNjAzNTkyMzkzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzZkNWEwNzMxYzU3YzQwM2Q4ZGUyYTdjZjU5MmRmMjllID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzgxZWFkZDNkNDc4MzQzOWRiM2QxMWYwOGVmZTE5MGZhID0gJCgnPGRpdiBpZD0iaHRtbF84MWVhZGQzZDQ3ODM0MzlkYjNkMTFmMDhlZmUxOTBmYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VmluZWdhciBIaWxsLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNmQ1YTA3MzFjNTdjNDAzZDhkZTJhN2NmNTkyZGYyOWUuc2V0Q29udGVudChodG1sXzgxZWFkZDNkNDc4MzQzOWRiM2QxMWYwOGVmZTE5MGZhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ViZTkwOGNiMmI3MDRhY2U4NWMyY2FkMzczMTc5MWNiLmJpbmRQb3B1cChwb3B1cF82ZDVhMDczMWM1N2M0MDNkOGRlMmE3Y2Y1OTJkZjI5ZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lMjZiMzkwNWI5ZTg0ZWEwYTlkNGEyY2MxY2RhMjIyZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjY3NTAzOTg2NTAzMjM3LC03My45MzA1MzEwODgxNzMzOF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84OWYwNDZkYmI2ZTA0OGUyYTc2NDE2NjhmNmE5YmE0MiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82MDZkZTA0ZTcwZmY0MjkyOTkzY2Q3MTM4YjZkYThiYiA9ICQoJzxkaXYgaWQ9Imh0bWxfNjA2ZGUwNGU3MGZmNDI5Mjk5M2NkNzEzOGI2ZGE4YmIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldlZWtzdmlsbGUsIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84OWYwNDZkYmI2ZTA0OGUyYTc2NDE2NjhmNmE5YmE0Mi5zZXRDb250ZW50KGh0bWxfNjA2ZGUwNGU3MGZmNDI5Mjk5M2NkNzEzOGI2ZGE4YmIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZTI2YjM5MDViOWU4NGVhMGE5ZDRhMmNjMWNkYTIyMmYuYmluZFBvcHVwKHBvcHVwXzg5ZjA0NmRiYjZlMDQ4ZTJhNzY0MTY2OGY2YTliYTQyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzI5NDBmZDA5ZWZkNDRhNWZhMmE1Yzg1MGFhOTVmMTc1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjc3ODYxMDQ3Njk1MzEsLTczLjkwMzMxNjg0ODUyNTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzM5NTBkMmNhNmQxMjRjY2ZiNTAwZjFlNWJhYjZlY2FiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzNjYjgyYzk0NTY1YzRmN2Y4N2Q3ZWQ1MDI5MDgyNWExID0gJCgnPGRpdiBpZD0iaHRtbF8zY2I4MmM5NDU2NWM0ZjdmODdkN2VkNTAyOTA4MjVhMSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QnJvYWR3YXkgSnVuY3Rpb24sIEJyb29rbHluPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zOTUwZDJjYTZkMTI0Y2NmYjUwMGYxZTViYWI2ZWNhYi5zZXRDb250ZW50KGh0bWxfM2NiODJjOTQ1NjVjNGY3Zjg3ZDdlZDUwMjkwODI1YTEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMjk0MGZkMDllZmQ0NGE1ZmEyYTVjODUwYWE5NWYxNzUuYmluZFBvcHVwKHBvcHVwXzM5NTBkMmNhNmQxMjRjY2ZiNTAwZjFlNWJhYjZlY2FiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2ZmZWY3OTA2ODVjMzQ3YjU4ODg1NjZlODMyOWZjYjZlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzAzMTc2MzI4MjI2OTIsLTczLjk4ODc1MjgwNzQ1MDRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNzI0M2NhMThhM2I0NDE0ZWE1YjkzY2Y4YWFjMDlhMTkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZWQ2OGFlZDI4ZTI2NGI3MGE4YzUzZGY4MzEwMWQyZjcgPSAkKCc8ZGl2IGlkPSJodG1sX2VkNjhhZWQyOGUyNjRiNzBhOGM1M2RmODMxMDFkMmY3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5EdW1ibywgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzcyNDNjYTE4YTNiNDQxNGVhNWI5M2NmOGFhYzA5YTE5LnNldENvbnRlbnQoaHRtbF9lZDY4YWVkMjhlMjY0YjcwYThjNTNkZjgzMTAxZDJmNyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mZmVmNzkwNjg1YzM0N2I1ODg4NTY2ZTgzMjlmY2I2ZS5iaW5kUG9wdXAocG9wdXBfNzI0M2NhMThhM2I0NDE0ZWE1YjkzY2Y4YWFjMDlhMTkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzNhZjBiYjhkZmE2NDJkZjg0ZjIxODVlOWYxYjQ0MWIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MDE4MDk1NzYzMTQ0NCwtNzQuMTIwNTkzOTk3MTgwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMjk5MDZhNGQ3MzM1NGJlNWI0MjAwZjlkMjRiMWEwNTcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfODFhN2YzZjM3MTUwNDI2Y2I2NTMwMGIxN2FmNTdiNTkgPSAkKCc8ZGl2IGlkPSJodG1sXzgxYTdmM2YzNzE1MDQyNmNiNjUzMDBiMTdhZjU3YjU5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NYW5vciBIZWlnaHRzLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yOTkwNmE0ZDczMzU0YmU1YjQyMDBmOWQyNGIxYTA1Ny5zZXRDb250ZW50KGh0bWxfODFhN2YzZjM3MTUwNDI2Y2I2NTMwMGIxN2FmNTdiNTkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzNhZjBiYjhkZmE2NDJkZjg0ZjIxODVlOWYxYjQ0MWIuYmluZFBvcHVwKHBvcHVwXzI5OTA2YTRkNzMzNTRiZTViNDIwMGY5ZDI0YjFhMDU3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzg4OTQxNzlmMDg5ZjQ3MzdhYTkxMDBmZDc5OGY1NGEwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjAzNzA2OTI2MjczNzEsLTc0LjEzMjA4NDQ3NDg0Mjk4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzFiNTJjM2Y3MTA2MTQ4N2ViMDdmNGM2Y2ZkYjZkNjY3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzllZWNkZjRjNjNlMjQyZGRhMTk2OWU0NGM0MzlkZDQ4ID0gJCgnPGRpdiBpZD0iaHRtbF85ZWVjZGY0YzYzZTI0MmRkYTE5NjllNDRjNDM5ZGQ0OCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V2lsbG93YnJvb2ssIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzFiNTJjM2Y3MTA2MTQ4N2ViMDdmNGM2Y2ZkYjZkNjY3LnNldENvbnRlbnQoaHRtbF85ZWVjZGY0YzYzZTI0MmRkYTE5NjllNDRjNDM5ZGQ0OCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84ODk0MTc5ZjA4OWY0NzM3YWE5MTAwZmQ3OThmNTRhMC5iaW5kUG9wdXAocG9wdXBfMWI1MmMzZjcxMDYxNDg3ZWIwN2Y0YzZjZmRiNmQ2NjcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYWUzNjdjNTkzN2Q5NGVjZDgwMjNjZjIyYzlhMDAzZTUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NDExMzk5MjIwOTE3NjYsLTc0LjIxNzc2NjM2MDY4NTY3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzZiMWRmZTdiNDE0YzRiOWI5ZGZiOWRlMjU0ZGRkMmFjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzQ5YzBiYTVjM2RmOTRlNWVhZmU0NzMyNDZkZjcyNDI4ID0gJCgnPGRpdiBpZD0iaHRtbF80OWMwYmE1YzNkZjk0ZTVlYWZlNDczMjQ2ZGY3MjQyOCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U2FuZHkgR3JvdW5kLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82YjFkZmU3YjQxNGM0YjliOWRmYjlkZTI1NGRkZDJhYy5zZXRDb250ZW50KGh0bWxfNDljMGJhNWMzZGY5NGU1ZWFmZTQ3MzI0NmRmNzI0MjgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYWUzNjdjNTkzN2Q5NGVjZDgwMjNjZjIyYzlhMDAzZTUuYmluZFBvcHVwKHBvcHVwXzZiMWRmZTdiNDE0YzRiOWI5ZGZiOWRlMjU0ZGRkMmFjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzRkZmRjMDQwOTMxZjQ5Nzc5M2JiNWUwODE2OTU5MDE5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTc5MTE4NzQyOTYxMjE0LC03NC4xMjcyNzI0MDYwNDk0Nl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lNjdmYWNmZjA5M2M0ZjJhODA0ZjI3NmE4YmYwZmVlNiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yODZlN2I5YjU2ZmI0MTc5YWYxNmQ2NzhhMmQyMWUxNyA9ICQoJzxkaXYgaWQ9Imh0bWxfMjg2ZTdiOWI1NmZiNDE3OWFmMTZkNjc4YTJkMjFlMTciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVnYmVydHZpbGxlLCBTdGF0ZW4gSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lNjdmYWNmZjA5M2M0ZjJhODA0ZjI3NmE4YmYwZmVlNi5zZXRDb250ZW50KGh0bWxfMjg2ZTdiOWI1NmZiNDE3OWFmMTZkNjc4YTJkMjFlMTcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNGRmZGMwNDA5MzFmNDk3NzkzYmI1ZTA4MTY5NTkwMTkuYmluZFBvcHVwKHBvcHVwX2U2N2ZhY2ZmMDkzYzRmMmE4MDRmMjc2YThiZjBmZWU2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzhhNDViNDNmZTczMDRjMTQ4MzQ2OTU3YmQ0NDAzYzU2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTY3Mzc1ODg5NTcwMzIsLTczLjg5MjEzNzYwMjMyODIyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzhlNDBkZTlmZjY5NDRlNjM5YTZjNTJjYTYxMDc5ZWRlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2E5NTRkZWVmYjU2ZTQzODU4NGZkMThlNTlhZmM4MDdjID0gJCgnPGRpdiBpZD0iaHRtbF9hOTU0ZGVlZmI1NmU0Mzg1ODRmZDE4ZTU5YWZjODA3YyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Um94YnVyeSwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84ZTQwZGU5ZmY2OTQ0ZTYzOWE2YzUyY2E2MTA3OWVkZS5zZXRDb250ZW50KGh0bWxfYTk1NGRlZWZiNTZlNDM4NTg0ZmQxOGU1OWFmYzgwN2MpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOGE0NWI0M2ZlNzMwNGMxNDgzNDY5NTdiZDQ0MDNjNTYuYmluZFBvcHVwKHBvcHVwXzhlNDBkZTlmZjY5NDRlNjM5YTZjNTJjYTYxMDc5ZWRlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2FjMzI0YTQzYTM2ZjRiYzFiNjc4MmY0MjA3ODg2ODYyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNTk4NTI1MDk1MTM3MjU1LC03My45NTkxODQ1OTQyODcwMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81ZmYwZWI0OTk2ZjM0N2Q4YjU0YzNhMjUxZTkyNTkyMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84Y2Y3NDIwZTI3MzQ0ODkwOWEzMzA0M2I1MTM1YmYzZSA9ICQoJzxkaXYgaWQ9Imh0bWxfOGNmNzQyMGUyNzM0NDg5MDlhMzMwNDNiNTEzNWJmM2UiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkhvbWVjcmVzdCwgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzVmZjBlYjQ5OTZmMzQ3ZDhiNTRjM2EyNTFlOTI1OTIxLnNldENvbnRlbnQoaHRtbF84Y2Y3NDIwZTI3MzQ0ODkwOWEzMzA0M2I1MTM1YmYzZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hYzMyNGE0M2EzNmY0YmMxYjY3ODJmNDIwNzg4Njg2Mi5iaW5kUG9wdXAocG9wdXBfNWZmMGViNDk5NmYzNDdkOGI1NGMzYTI1MWU5MjU5MjEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOGJmYmNmMDVkZjU4NGFiMjhlOTVkZDcyMzI4YjM1MDcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MTY0MTQ1MTExNTgxODUsLTczLjg4MTE0MzE5MjAwNjA0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2IxMTAzOGUyYmE2MjQ5NmRhYWFmZGU5ZjgzMjk3MmE3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzQxMjIzYWVlMGU2ODQ3YjliMzRkNjFmZGM5MTk5YmQ5ID0gJCgnPGRpdiBpZD0iaHRtbF80MTIyM2FlZTBlNjg0N2I5YjM0ZDYxZmRjOTE5OWJkOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TWlkZGxlIFZpbGxhZ2UsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjExMDM4ZTJiYTYyNDk2ZGFhYWZkZTlmODMyOTcyYTcuc2V0Q29udGVudChodG1sXzQxMjIzYWVlMGU2ODQ3YjliMzRkNjFmZGM5MTk5YmQ5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzhiZmJjZjA1ZGY1ODRhYjI4ZTk1ZGQ3MjMyOGIzNTA3LmJpbmRQb3B1cChwb3B1cF9iMTEwMzhlMmJhNjI0OTZkYWFhZmRlOWY4MzI5NzJhNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zM2FiM2FjZjNhN2E0ZGRlODY5NzBiZjk4NGYwNTUxYiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjUyNjI2NDA2NzM0ODEyLC03NC4yMDE1MjU1NjQ1NzY1OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zNjJjODM3ZjE3YWM0NDA1OTQ1NDhhZWYzMTU3N2E2ZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80YmViOGMxZGZkZDM0NDJiOTI3Yjc1OGJkMjY1MmEwNSA9ICQoJzxkaXYgaWQ9Imh0bWxfNGJlYjhjMWRmZGQzNDQyYjkyN2I3NThiZDI2NTJhMDUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlByaW5jZSYjMzk7cyBCYXksIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzM2MmM4MzdmMTdhYzQ0MDU5NDU0OGFlZjMxNTc3YTZkLnNldENvbnRlbnQoaHRtbF80YmViOGMxZGZkZDM0NDJiOTI3Yjc1OGJkMjY1MmEwNSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zM2FiM2FjZjNhN2E0ZGRlODY5NzBiZjk4NGYwNTUxYi5iaW5kUG9wdXAocG9wdXBfMzYyYzgzN2YxN2FjNDQwNTk0NTQ4YWVmMzE1NzdhNmQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfODE0MGRkNDc3ODczNGEwZWI0YjVhODI2ZGRiOWI4OTMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41NzY1MDYyOTM3OTQ4OSwtNzQuMTM3OTI2NjM3NzE1NjhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMjU2M2RiZWFhYTU1NDk2MzkwNTgyNGFjYTY5OTNmYTYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNmNhOTZmZGRiOGExNDcyMWJlOTRhMGM3NjQwNDY1NjAgPSAkKCc8ZGl2IGlkPSJodG1sXzZjYTk2ZmRkYjhhMTQ3MjFiZTk0YTBjNzY0MDQ2NTYwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5MaWdodGhvdXNlIEhpbGwsIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzI1NjNkYmVhYWE1NTQ5NjM5MDU4MjRhY2E2OTkzZmE2LnNldENvbnRlbnQoaHRtbF82Y2E5NmZkZGI4YTE0NzIxYmU5NGEwYzc2NDA0NjU2MCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84MTQwZGQ0Nzc4NzM0YTBlYjRiNWE4MjZkZGI5Yjg5My5iaW5kUG9wdXAocG9wdXBfMjU2M2RiZWFhYTU1NDk2MzkwNTgyNGFjYTY5OTNmYTYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZTEwZmEwZjI4YWRkNGFlNDg5NGNmM2Y0YjliMzIxNWYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC41MTk1NDE0NTc0ODkwOSwtNzQuMjI5NTcwODA2MjY5NDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMjg0YTg5M2NlNDY3NGFiZTlhMjMzYzJlY2MxMDk0ZjUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNmE3ZjI5ODRmMDQ0NGMyZTk5YjJjNzNhNDg4NjZmNDEgPSAkKCc8ZGl2IGlkPSJodG1sXzZhN2YyOTg0ZjA0NDRjMmU5OWIyYzczYTQ4ODY2ZjQxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5SaWNobW9uZCBWYWxsZXksIFN0YXRlbiBJc2xhbmQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzI4NGE4OTNjZTQ2NzRhYmU5YTIzM2MyZWNjMTA5NGY1LnNldENvbnRlbnQoaHRtbF82YTdmMjk4NGYwNDQ0YzJlOTliMmM3M2E0ODg2NmY0MSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lMTBmYTBmMjhhZGQ0YWU0ODk0Y2YzZjRiOWIzMjE1Zi5iaW5kUG9wdXAocG9wdXBfMjg0YTg5M2NlNDY3NGFiZTlhMjMzYzJlY2MxMDk0ZjUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNTE0OWIzNjlkN2Y4NDQzYjgyYzhlOWEyOWU5OTFmZDUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43OTA2MDE1NTY3MDE0OCwtNzMuODI2Njc3NTcxMzg2NDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNDY2MDQ2N2IzYjEzNDU4NmE3NWZmYjc1OWM5ZDBiYTcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfY2Q3MzMzY2FhMDA5NDgxM2JkYzcwYWE5ZTY5OWU5MWMgPSAkKCc8ZGl2IGlkPSJodG1sX2NkNzMzM2NhYTAwOTQ4MTNiZGM3MGFhOWU2OTllOTFjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NYWxiYSwgUXVlZW5zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80NjYwNDY3YjNiMTM0NTg2YTc1ZmZiNzU5YzlkMGJhNy5zZXRDb250ZW50KGh0bWxfY2Q3MzMzY2FhMDA5NDgxM2JkYzcwYWE5ZTY5OWU5MWMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNTE0OWIzNjlkN2Y4NDQzYjgyYzhlOWEyOWU5OTFmZDUuYmluZFBvcHVwKHBvcHVwXzQ2NjA0NjdiM2IxMzQ1ODZhNzVmZmI3NTljOWQwYmE3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2FhMDA1NWM0NjM5YjRkMjVhZTUzZDAwY2YxMTk3ZDZjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjgxOTk4OTM0NTE3MywtNzMuODkwMzQ1NzA5ODcyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzE1MDBjN2NmMDE4MTRmYjhhZjZhYjcwYjM5Zjg2NmUwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzE4YThjMmVhMTdhYjRmZjhhMjc2NzYzOGI2NWYwODJkID0gJCgnPGRpdiBpZD0iaHRtbF8xOGE4YzJlYTE3YWI0ZmY4YTI3Njc2MzhiNjVmMDgyZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SGlnaGxhbmQgUGFyaywgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzE1MDBjN2NmMDE4MTRmYjhhZjZhYjcwYjM5Zjg2NmUwLnNldENvbnRlbnQoaHRtbF8xOGE4YzJlYTE3YWI0ZmY4YTI3Njc2MzhiNjVmMDgyZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hYTAwNTVjNDYzOWI0ZDI1YWU1M2QwMGNmMTE5N2Q2Yy5iaW5kUG9wdXAocG9wdXBfMTUwMGM3Y2YwMTgxNGZiOGFmNmFiNzBiMzlmODY2ZTApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMGEzZjdlZmMwYTM5NDMwN2FmYzhhYTc2ODg5ZmI2MGIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC42MDkzNzc3MDExMzc2NiwtNzMuOTQ4NDE1MTUzMjg4OTNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWNmMjVhYTk4ZGEyNDQ3YTk5ZWRlMDM3OTlhYzhhM2UgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNjBjNjVlNmVjMDFjNGM5NjlmMDhhZDMzNWRkOWM0OGUgPSAkKCc8ZGl2IGlkPSJodG1sXzYwYzY1ZTZlYzAxYzRjOTY5ZjA4YWQzMzVkZDljNDhlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NYWRpc29uLCBCcm9va2x5bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYWNmMjVhYTk4ZGEyNDQ3YTk5ZWRlMDM3OTlhYzhhM2Uuc2V0Q29udGVudChodG1sXzYwYzY1ZTZlYzAxYzRjOTY5ZjA4YWQzMzVkZDljNDhlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzBhM2Y3ZWZjMGEzOTQzMDdhZmM4YWE3Njg4OWZiNjBiLmJpbmRQb3B1cChwb3B1cF9hY2YyNWFhOThkYTI0NDdhOTllZGUwMzc5OWFjOGEzZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wZDEzYjgyMjZhMjQ0ZmFlOWViNWYyM2U0NWM3MGEzNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg1MjcyMjk3NjMzMDE3LC03My44NjE3MjU3NzU1NTExNV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xYWJhYzc4MTg3YmU0N2RiYjY1NDNhNzIyZjE2M2U2MSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zNzFjMDBiZmQ5YTk0YzliODM0MDhiNmRhZWI5N2ZlZiA9ICQoJzxkaXYgaWQ9Imh0bWxfMzcxYzAwYmZkOWE5NGM5YjgzNDA4YjZkYWViOTdmZWYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJyb254ZGFsZSwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzFhYmFjNzgxODdiZTQ3ZGJiNjU0M2E3MjJmMTYzZTYxLnNldENvbnRlbnQoaHRtbF8zNzFjMDBiZmQ5YTk0YzliODM0MDhiNmRhZWI5N2ZlZik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wZDEzYjgyMjZhMjQ0ZmFlOWViNWYyM2U0NWM3MGEzNi5iaW5kUG9wdXAocG9wdXBfMWFiYWM3ODE4N2JlNDdkYmI2NTQzYTcyMmYxNjNlNjEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMWE0NTZkNGVlODdlNGM0ZWI4YjU4OTJhMTVjYWE0YzcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NjU3ODc4NzgwMjk4MiwtNzMuODU5MzE4NjMyMjE2NDddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOWY2ZDU0Zjk1MjM3NDA3YmE1YjE5NzVlYjgzYTRhNjMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOWQzMjYwNjNiODg0NDZjMDgyZjYxYjhlY2NkN2RjMjEgPSAkKCc8ZGl2IGlkPSJodG1sXzlkMzI2MDYzYjg4NDQ2YzA4MmY2MWI4ZWNjZDdkYzIxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5BbGxlcnRvbiwgQnJvbng8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzlmNmQ1NGY5NTIzNzQwN2JhNWIxOTc1ZWI4M2E0YTYzLnNldENvbnRlbnQoaHRtbF85ZDMyNjA2M2I4ODQ0NmMwODJmNjFiOGVjY2Q3ZGMyMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xYTQ1NmQ0ZWU4N2U0YzRlYjhiNTg5MmExNWNhYTRjNy5iaW5kUG9wdXAocG9wdXBfOWY2ZDU0Zjk1MjM3NDA3YmE1YjE5NzVlYjgzYTRhNjMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMTg4NWQxYjNlMzgyNDM5OTg4ZWRmMGVmYmQ2MzYwMTcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NzAzOTIzOTE0MTQ3LC03My45MDE1MjI2NDUxMzE0NF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9iMjJmMTNkZTA5OWY0ZDBmOWNiZjJhYzE2ZDRjOTE2MCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lYzk1ODY5ZGVhYzU0NjliYjNiZDg4NTNjYTQyNTY5YSA9ICQoJzxkaXYgaWQ9Imh0bWxfZWM5NTg2OWRlYWM1NDY5YmIzYmQ4ODUzY2E0MjU2OWEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPktpbmdzYnJpZGdlIEhlaWdodHMsIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iMjJmMTNkZTA5OWY0ZDBmOWNiZjJhYzE2ZDRjOTE2MC5zZXRDb250ZW50KGh0bWxfZWM5NTg2OWRlYWM1NDY5YmIzYmQ4ODUzY2E0MjU2OWEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMTg4NWQxYjNlMzgyNDM5OTg4ZWRmMGVmYmQ2MzYwMTcuYmluZFBvcHVwKHBvcHVwX2IyMmYxM2RlMDk5ZjRkMGY5Y2JmMmFjMTZkNGM5MTYwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2U0Y2NmYmVjYjNiMDRhZjU4NjlhNjgwYWQ0NGNkNzkyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNjQ2OTI2MDY2NTg1NzksLTczLjk0ODE3NzA5OTIwMTg0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzQ5NzYxMGVlODgzODQ4OGI4NzZkZGVhOTZiNDEyMTg5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzViYjhjMmQzZWY0YTQxYzFhM2Y0MTNjMGEzYmZjOWE5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzZmZWU2NDczNWEzMTQwZTQ5ZWYyZjVlZjhkYzc5ZGIzID0gJCgnPGRpdiBpZD0iaHRtbF82ZmVlNjQ3MzVhMzE0MGU0OWVmMmY1ZWY4ZGM3OWRiMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RXJhc211cywgQnJvb2tseW48L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzViYjhjMmQzZWY0YTQxYzFhM2Y0MTNjMGEzYmZjOWE5LnNldENvbnRlbnQoaHRtbF82ZmVlNjQ3MzVhMzE0MGU0OWVmMmY1ZWY4ZGM3OWRiMyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lNGNjZmJlY2IzYjA0YWY1ODY5YTY4MGFkNDRjZDc5Mi5iaW5kUG9wdXAocG9wdXBfNWJiOGMyZDNlZjRhNDFjMWEzZjQxM2MwYTNiZmM5YTkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNTkwZjQ1NjAxYjI4NDI1YzkyYWY3MjM4NjY2MmQyNTMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NTY2NTgwODIyNzUxOSwtNzQuMDAwMTExMzYyMDI2MzddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYzVjMTdlZjhjOWViNDUwODg4MWI1ZDJiMmRlYzY4MmUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNjlhNDMyYmRjZGVmNGQyYzgwZGNkYTBjODE2ODJhZTkgPSAkKCc8ZGl2IGlkPSJodG1sXzY5YTQzMmJkY2RlZjRkMmM4MGRjZGEwYzgxNjgyYWU5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IdWRzb24gWWFyZHMsIE1hbmhhdHRhbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYzVjMTdlZjhjOWViNDUwODg4MWI1ZDJiMmRlYzY4MmUuc2V0Q29udGVudChodG1sXzY5YTQzMmJkY2RlZjRkMmM4MGRjZGEwYzgxNjgyYWU5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzU5MGY0NTYwMWIyODQyNWM5MmFmNzIzODY2NjJkMjUzLmJpbmRQb3B1cChwb3B1cF9jNWMxN2VmOGM5ZWI0NTA4ODgxYjVkMmIyZGVjNjgyZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85ZTU3OTJkMzBkMjY0OGRkYmQxNGUyOTY4Mjc0ZDFhZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjU4NzMzNzc0MDE4NzQxLC03My44MDU1MzAwMjk2ODcxOF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9iNTUxMzExZjAyMmM0ZmQ2OWExMGFlNzc5ZjcyYTU4MiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zZmQzNDhiZWNmYjA0Y2FhYjNkYzQ2NzhkOGI2ZTI3NSA9ICQoJzxkaXYgaWQ9Imh0bWxfM2ZkMzQ4YmVjZmIwNGNhYWIzZGM0Njc4ZDhiNmUyNzUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkhhbW1lbHMsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjU1MTMxMWYwMjJjNGZkNjlhMTBhZTc3OWY3MmE1ODIuc2V0Q29udGVudChodG1sXzNmZDM0OGJlY2ZiMDRjYWFiM2RjNDY3OGQ4YjZlMjc1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzllNTc5MmQzMGQyNjQ4ZGRiZDE0ZTI5NjgyNzRkMWFmLmJpbmRQb3B1cChwb3B1cF9iNTUxMzExZjAyMmM0ZmQ2OWExMGFlNzc5ZjcyYTU4Mik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yOTc0MmFhYjIxMDk0MmY0YWZiNmNmMWZiOTZjYzhlMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYxMTMyMTY5MTI4MzgzNCwtNzMuNzY1OTY3ODE0NDU2MjddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMDg4MTUxNjEyOWEzNGQzMDg3ZTAwZDcyNjRiYTg4NWEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYTRkYzRkODFmNjZmNDE0YThjZGE0NTk3ZTU1YWIwZGYgPSAkKCc8ZGl2IGlkPSJodG1sX2E0ZGM0ZDgxZjY2ZjQxNGE4Y2RhNDU5N2U1NWFiMGRmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CYXlzd2F0ZXIsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMDg4MTUxNjEyOWEzNGQzMDg3ZTAwZDcyNjRiYTg4NWEuc2V0Q29udGVudChodG1sX2E0ZGM0ZDgxZjY2ZjQxNGE4Y2RhNDU5N2U1NWFiMGRmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzI5NzQyYWFiMjEwOTQyZjRhZmI2Y2YxZmI5NmNjOGUxLmJpbmRQb3B1cChwb3B1cF8wODgxNTE2MTI5YTM0ZDMwODdlMDBkNzI2NGJhODg1YSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lYmRlNDBjYzNjZDc0NWNjOTVlM2MyYzcyYTBkNzlmMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc1NjA5MTI5NzA5NDcwNiwtNzMuOTQ1NjMwNzAzMzQwOTFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNDk3NjEwZWU4ODM4NDg4Yjg3NmRkZWE5NmI0MTIxODkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODk4YzFkYWZjYjk1NDVlMWJhMmViODNmYWMyZWY2ZGQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYjYyZDg5YWNmNTJkNDAzOTk2YjliMDAxYmU5OWExMmYgPSAkKCc8ZGl2IGlkPSJodG1sX2I2MmQ4OWFjZjUyZDQwMzk5NmI5YjAwMWJlOTlhMTJmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5RdWVlbnNicmlkZ2UsIFF1ZWVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfODk4YzFkYWZjYjk1NDVlMWJhMmViODNmYWMyZWY2ZGQuc2V0Q29udGVudChodG1sX2I2MmQ4OWFjZjUyZDQwMzk5NmI5YjAwMWJlOTlhMTJmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ViZGU0MGNjM2NkNzQ1Y2M5NWUzYzJjNzJhMGQ3OWYxLmJpbmRQb3B1cChwb3B1cF84OThjMWRhZmNiOTU0NWUxYmEyZWI4M2ZhYzJlZjZkZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84OWIyNDUzZDNlOTA0MGJlYjQwZDBkMzI5YjNkYzZkNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjYxNzMxMDc5MjUyOTgzLC03NC4wODE3Mzk5MjIxMTk2Ml0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80OTc2MTBlZTg4Mzg0ODhiODc2ZGRlYTk2YjQxMjE4OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83ZWI5MWFmMGFkY2M0MDM1Yjk4YmZmYzEwOTM2Y2Q2OSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81MGUwN2QxOWQyYTg0Y2YyYjA5N2IyYTM2OWI2ODA2OCA9ICQoJzxkaXYgaWQ9Imh0bWxfNTBlMDdkMTlkMmE4NGNmMmIwOTdiMmEzNjliNjgwNjgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZveCBIaWxscywgU3RhdGVuIElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfN2ViOTFhZjBhZGNjNDAzNWI5OGJmZmMxMDkzNmNkNjkuc2V0Q29udGVudChodG1sXzUwZTA3ZDE5ZDJhODRjZjJiMDk3YjJhMzY5YjY4MDY4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzg5YjI0NTNkM2U5MDQwYmViNDBkMGQzMjliM2RjNmQ0LmJpbmRQb3B1cChwb3B1cF83ZWI5MWFmMGFkY2M0MDM1Yjk4YmZmYzEwOTM2Y2Q2OSk7CgogICAgICAgICAgICAKICAgICAgICAKPC9zY3JpcHQ+ onload="this.contentDocument.open();this.contentDocument.write(atob(this.getAttribute('data-html')));this.contentDocument.close();" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python
print ('Looked at Manhattan as well, as an option')
```

    Looked at Manhattan as well, as an option



```python
manhattan_data = neighborhoods[neighborhoods['Borough'] == 'Manhattan'].reset_index(drop=True)
manhattan_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Borough</th>
      <th>Neighborhood</th>
      <th>Latitude</th>
      <th>Longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Manhattan</td>
      <td>Marble Hill</td>
      <td>40.876551</td>
      <td>-73.910660</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Manhattan</td>
      <td>Chinatown</td>
      <td>40.715618</td>
      <td>-73.994279</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Manhattan</td>
      <td>Washington Heights</td>
      <td>40.851903</td>
      <td>-73.936900</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Manhattan</td>
      <td>Inwood</td>
      <td>40.867684</td>
      <td>-73.921210</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Manhattan</td>
      <td>Hamilton Heights</td>
      <td>40.823604</td>
      <td>-73.949688</td>
    </tr>
  </tbody>
</table>
</div>




```python
address = 'Manhattan, NY'

geolocator = Nominatim(user_agent="ny_explorer")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of Manhattan are {}, {}.'.format(latitude, longitude))
```

    The geograpical coordinate of Manhattan are 40.7896239, -73.9598939.



```python
print ('Created Map of Manhattan based on longitute and latitude')
```

    Created Map of Manhattan based on longitute and latitude



```python
# create map of Manhattan using latitude and longitude values
map_manhattan = folium.Map(location=[latitude, longitude], zoom_start=11)

# add markers to map
for lat, lng, label in zip(manhattan_data['Latitude'], manhattan_data['Longitude'], manhattan_data['Neighborhood']):
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='blue',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7,
        parse_html=False).add_to(map_manhattan)  
    
map_manhattan
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe src="about:blank" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" data-html=PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfZjk3MmI1YTY5ZDE4NDYxNjllYzdmNjRhNjNmNjExOGUgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwLjAlOwogICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAo8L2hlYWQ+Cjxib2R5PiAgICAKICAgIAogICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb2xpdW0tbWFwIiBpZD0ibWFwX2Y5NzJiNWE2OWQxODQ2MTY5ZWM3ZjY0YTYzZjYxMThlIiA+PC9kaXY+CiAgICAgICAgCjwvYm9keT4KPHNjcmlwdD4gICAgCiAgICAKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIG1hcF9mOTcyYjVhNjlkMTg0NjE2OWVjN2Y2NGE2M2Y2MTE4ZSA9IEwubWFwKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ21hcF9mOTcyYjVhNjlkMTg0NjE2OWVjN2Y2NGE2M2Y2MTE4ZScsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7Y2VudGVyOiBbNDAuODQ5MzA0NDUsLTczLjg3NzEzNzkxODM1MjA2XSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHpvb206IDExLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbWF4Qm91bmRzOiBib3VuZHMsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBsYXllcnM6IFtdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgd29ybGRDb3B5SnVtcDogZmFsc2UsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjcnM6IEwuQ1JTLkVQU0czODU3CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0pOwogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgdGlsZV9sYXllcl8zNTQ5NzMwZTBhMmQ0OWZjYWM1NjE2OGIyMjM4ZmQ3MSA9IEwudGlsZUxheWVyKAogICAgICAgICAgICAgICAgJ2h0dHBzOi8ve3N9LnRpbGUub3BlbnN0cmVldG1hcC5vcmcve3p9L3t4fS97eX0ucG5nJywKICAgICAgICAgICAgICAgIHsKICAiYXR0cmlidXRpb24iOiBudWxsLAogICJkZXRlY3RSZXRpbmEiOiBmYWxzZSwKICAibWF4Wm9vbSI6IDE4LAogICJtaW5ab29tIjogMSwKICAibm9XcmFwIjogZmFsc2UsCiAgInN1YmRvbWFpbnMiOiAiYWJjIgp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mOTcyYjVhNjlkMTg0NjE2OWVjN2Y2NGE2M2Y2MTE4ZSk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNDQwNGQ0MjYwN2RhNGY3MWJjMzJlMTcxOTQzMWExNzIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NzY1NTA3Nzg3OTk2NCwtNzMuOTEwNjU5NjU4NjI5ODFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZjk3MmI1YTY5ZDE4NDYxNjllYzdmNjRhNjNmNjExOGUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDQ1NDllNTgxYzM5NDliMWI2OWIyY2E0YjQ2ZTU4Y2IgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMjZiMTY3MjNjMDI3NDBiMWJjZjU5NGEzMmE4NjNkNzYgPSAkKCc8ZGl2IGlkPSJodG1sXzI2YjE2NzIzYzAyNzQwYjFiY2Y1OTRhMzJhODYzZDc2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NYXJibGUgSGlsbDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZDQ1NDllNTgxYzM5NDliMWI2OWIyY2E0YjQ2ZTU4Y2Iuc2V0Q29udGVudChodG1sXzI2YjE2NzIzYzAyNzQwYjFiY2Y1OTRhMzJhODYzZDc2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzQ0MDRkNDI2MDdkYTRmNzFiYzMyZTE3MTk0MzFhMTcyLmJpbmRQb3B1cChwb3B1cF9kNDU0OWU1ODFjMzk0OWIxYjY5YjJjYTRiNDZlNThjYik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zNzQwNzM5ODZmZmI0ZjQzYWFjYmFiYWJmNzEyZjg2NiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcxNTYxODQyMjMxNDMyLC03My45OTQyNzkzNjI1NTk3OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mOTcyYjVhNjlkMTg0NjE2OWVjN2Y2NGE2M2Y2MTE4ZSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80NzM3ZDQ0ODY0MmM0MzNhOTQzNjFlM2EyMGI3YzY3NCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iZjYzMWQzNjAyMDI0OTllYmUwZGVjZTAxZDVmNWRlNCA9ICQoJzxkaXYgaWQ9Imh0bWxfYmY2MzFkMzYwMjAyNDk5ZWJlMGRlY2UwMWQ1ZjVkZTQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNoaW5hdG93bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNDczN2Q0NDg2NDJjNDMzYTk0MzYxZTNhMjBiN2M2NzQuc2V0Q29udGVudChodG1sX2JmNjMxZDM2MDIwMjQ5OWViZTBkZWNlMDFkNWY1ZGU0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzM3NDA3Mzk4NmZmYjRmNDNhYWNiYWJhYmY3MTJmODY2LmJpbmRQb3B1cChwb3B1cF80NzM3ZDQ0ODY0MmM0MzNhOTQzNjFlM2EyMGI3YzY3NCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wOGI2NTY3OTdlZmU0NDBkYTI3MzJiZmJiZjM5NjU3ZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg1MTkwMjUyNTU1MzA1LC03My45MzY5MDAyNzk4NTIzNF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mOTcyYjVhNjlkMTg0NjE2OWVjN2Y2NGE2M2Y2MTE4ZSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jYmM3YzViYzIwZGE0Mjk5OGVhOGRjMzc3YmZiM2QxZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jZGJiNWM4ZjcxZGY0MDg2YmNlOGQ1YmZjODYwYjNhOSA9ICQoJzxkaXYgaWQ9Imh0bWxfY2RiYjVjOGY3MWRmNDA4NmJjZThkNWJmYzg2MGIzYTkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldhc2hpbmd0b24gSGVpZ2h0czwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfY2JjN2M1YmMyMGRhNDI5OThlYThkYzM3N2JmYjNkMWYuc2V0Q29udGVudChodG1sX2NkYmI1YzhmNzFkZjQwODZiY2U4ZDViZmM4NjBiM2E5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzA4YjY1Njc5N2VmZTQ0MGRhMjczMmJmYmJmMzk2NTdlLmJpbmRQb3B1cChwb3B1cF9jYmM3YzViYzIwZGE0Mjk5OGVhOGRjMzc3YmZiM2QxZik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80YTVmMWQ0NWZkYjM0ZDM1ODgyMmIxZDMzNzk3ZTE2NiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg2NzY4Mzk2NDQ5OTE1LC03My45MjEyMTA0MjIwMzg5N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mOTcyYjVhNjlkMTg0NjE2OWVjN2Y2NGE2M2Y2MTE4ZSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yZTgwZjE0OGM5NWI0NTA2YWQ5M2MwZGZkZjA5YWMxNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yY2I4NmJlZGMzNTE0ZmE5YTUwNGM4ZWVjNzg4NjNiNCA9ICQoJzxkaXYgaWQ9Imh0bWxfMmNiODZiZWRjMzUxNGZhOWE1MDRjOGVlYzc4ODYzYjQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPklud29vZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMmU4MGYxNDhjOTViNDUwNmFkOTNjMGRmZGYwOWFjMTQuc2V0Q29udGVudChodG1sXzJjYjg2YmVkYzM1MTRmYTlhNTA0YzhlZWM3ODg2M2I0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzRhNWYxZDQ1ZmRiMzRkMzU4ODIyYjFkMzM3OTdlMTY2LmJpbmRQb3B1cChwb3B1cF8yZTgwZjE0OGM5NWI0NTA2YWQ5M2MwZGZkZjA5YWMxNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mNGU2YmEwYjUxZTk0ZmJhYjQwZWE0OTcyODFmNjA1ZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjgyMzYwNDI4NDgxMTkzNSwtNzMuOTQ5Njg3OTE4ODMzNjZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZjk3MmI1YTY5ZDE4NDYxNjllYzdmNjRhNjNmNjExOGUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWFhMjA3YTNhNmZhNGVhMWIzMGU3MGMzOTA1ZTllYmMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYTEwNzgzOWE5YWEzNGRiYTliMmE5ZGI3YzFlOGEyYmEgPSAkKCc8ZGl2IGlkPSJodG1sX2ExMDc4MzlhOWFhMzRkYmE5YjJhOWRiN2MxZThhMmJhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IYW1pbHRvbiBIZWlnaHRzPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hYWEyMDdhM2E2ZmE0ZWExYjMwZTcwYzM5MDVlOWViYy5zZXRDb250ZW50KGh0bWxfYTEwNzgzOWE5YWEzNGRiYTliMmE5ZGI3YzFlOGEyYmEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZjRlNmJhMGI1MWU5NGZiYWI0MGVhNDk3MjgxZjYwNWQuYmluZFBvcHVwKHBvcHVwX2FhYTIwN2EzYTZmYTRlYTFiMzBlNzBjMzkwNWU5ZWJjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzNlYWQxODk2MjY0YjQyYWE5MGJkOWVlM2YyNTRhZGRjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODE2OTM0NDI5NDk3OCwtNzMuOTU3Mzg1MzkzNTE4OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mOTcyYjVhNjlkMTg0NjE2OWVjN2Y2NGE2M2Y2MTE4ZSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85MmFlMjIxN2EwMWI0OTNjOTk5ZjhmM2EwOGRhMzVmZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85YTc3MDg3MGQ2ZmY0NTkyYWFjMjQyOGY3N2FiYTczNCA9ICQoJzxkaXYgaWQ9Imh0bWxfOWE3NzA4NzBkNmZmNDU5MmFhYzI0MjhmNzdhYmE3MzQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk1hbmhhdHRhbnZpbGxlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85MmFlMjIxN2EwMWI0OTNjOTk5ZjhmM2EwOGRhMzVmZi5zZXRDb250ZW50KGh0bWxfOWE3NzA4NzBkNmZmNDU5MmFhYzI0MjhmNzdhYmE3MzQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfM2VhZDE4OTYyNjRiNDJhYTkwYmQ5ZWUzZjI1NGFkZGMuYmluZFBvcHVwKHBvcHVwXzkyYWUyMjE3YTAxYjQ5M2M5OTlmOGYzYTA4ZGEzNWZmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzIxNTZiNTIxM2VkYzRmMTE5OGViNjAxOTY5MmEzZjM2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODE1OTc2MDY3NDI0MTQsLTczLjk0MzIxMTEyNjAzOTA1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2Y5NzJiNWE2OWQxODQ2MTY5ZWM3ZjY0YTYzZjYxMThlKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2Y0NDZjNWVkOWVjMzRjMzU5NDcwZGUxMWIyOWQ4MzFiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzIwZDM0NTI5NGE0NTQ0MjBiZGIzYmU2NTI3MDE0NTlkID0gJCgnPGRpdiBpZD0iaHRtbF8yMGQzNDUyOTRhNDU0NDIwYmRiM2JlNjUyNzAxNDU5ZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2VudHJhbCBIYXJsZW08L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Y0NDZjNWVkOWVjMzRjMzU5NDcwZGUxMWIyOWQ4MzFiLnNldENvbnRlbnQoaHRtbF8yMGQzNDUyOTRhNDU0NDIwYmRiM2JlNjUyNzAxNDU5ZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yMTU2YjUyMTNlZGM0ZjExOThlYjYwMTk2OTJhM2YzNi5iaW5kUG9wdXAocG9wdXBfZjQ0NmM1ZWQ5ZWMzNGMzNTk0NzBkZTExYjI5ZDgzMWIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOWFjYzIzNWNiOTMyNDNlN2E5MTQyNmMyYmZlMTMxNTAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43OTIyNDk0NjY2MzAzMywtNzMuOTQ0MTgyMjMxNDg1MjRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZjk3MmI1YTY5ZDE4NDYxNjllYzdmNjRhNjNmNjExOGUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODYwYTFiZDljYjAzNDgyMjhiYWEyYjRjODUyMDZiYjMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYWJiNmJmMTE1MDNhNDc3NTgyMzRjNWFhNmRlM2QxOWEgPSAkKCc8ZGl2IGlkPSJodG1sX2FiYjZiZjExNTAzYTQ3NzU4MjM0YzVhYTZkZTNkMTlhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5FYXN0IEhhcmxlbTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfODYwYTFiZDljYjAzNDgyMjhiYWEyYjRjODUyMDZiYjMuc2V0Q29udGVudChodG1sX2FiYjZiZjExNTAzYTQ3NzU4MjM0YzVhYTZkZTNkMTlhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzlhY2MyMzVjYjkzMjQzZTdhOTE0MjZjMmJmZTEzMTUwLmJpbmRQb3B1cChwb3B1cF84NjBhMWJkOWNiMDM0ODIyOGJhYTJiNGM4NTIwNmJiMyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82MTQ4NTk3MDczZWQ0NDFjODUwM2I3NWZiNmM5MjQ1YiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc3NTYzODU3MzMwMTgwNSwtNzMuOTYwNTA3NjMxMzVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZjk3MmI1YTY5ZDE4NDYxNjllYzdmNjRhNjNmNjExOGUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjJjYjE3NDk3NThjNDk0Mjg5Yzc3ZmU2OGY5YjkyYjIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNDVlMDMwNDk2YWFlNDliNWE3YzA0NDM5MGM0NzcxNmYgPSAkKCc8ZGl2IGlkPSJodG1sXzQ1ZTAzMDQ5NmFhZTQ5YjVhN2MwNDQzOTBjNDc3MTZmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5VcHBlciBFYXN0IFNpZGU8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzYyY2IxNzQ5NzU4YzQ5NDI4OWM3N2ZlNjhmOWI5MmIyLnNldENvbnRlbnQoaHRtbF80NWUwMzA0OTZhYWU0OWI1YTdjMDQ0MzkwYzQ3NzE2Zik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82MTQ4NTk3MDczZWQ0NDFjODUwM2I3NWZiNmM5MjQ1Yi5iaW5kUG9wdXAocG9wdXBfNjJjYjE3NDk3NThjNDk0Mjg5Yzc3ZmU2OGY5YjkyYjIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzFmNGJjNzMwZTVjNGUwNWI2N2NhOTc5MDY3OTYzZWUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NzU5Mjk4NDk4ODQ4NzUsLTczLjk0NzExNzg0NDcxODI2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2Y5NzJiNWE2OWQxODQ2MTY5ZWM3ZjY0YTYzZjYxMThlKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzNlODQ4MGFkZTg2OTRmZGY4NjRhMjgyOThmZDNlMGM3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzQ0YWYzNTg3ZDU0NTQ3ZGY5Y2Q2NGIwY2ZkZjMyMTg0ID0gJCgnPGRpdiBpZD0iaHRtbF80NGFmMzU4N2Q1NDU0N2RmOWNkNjRiMGNmZGYzMjE4NCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+WW9ya3ZpbGxlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zZTg0ODBhZGU4Njk0ZmRmODY0YTI4Mjk4ZmQzZTBjNy5zZXRDb250ZW50KGh0bWxfNDRhZjM1ODdkNTQ1NDdkZjljZDY0YjBjZmRmMzIxODQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzFmNGJjNzMwZTVjNGUwNWI2N2NhOTc5MDY3OTYzZWUuYmluZFBvcHVwKHBvcHVwXzNlODQ4MGFkZTg2OTRmZGY4NjRhMjgyOThmZDNlMGM3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzAyZWQ4NmNmYTAxNTRmOWU5ZDNlYzU1YzcwMGUyNGViID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzY4MTEyNjU4Mjg3MzMsLTczLjk1ODg1OTY4ODEzNzZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZjk3MmI1YTY5ZDE4NDYxNjllYzdmNjRhNjNmNjExOGUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOWM0ODEyYzYzZDM5NDRiYzljMzkzNGExZDRlMTU2ZTkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDQ0MzU2YzQwNDg1NDg5MDlkZjFiYWQ2MDc4OTg2NDIgPSAkKCc8ZGl2IGlkPSJodG1sX2Q0NDM1NmM0MDQ4NTQ4OTA5ZGYxYmFkNjA3ODk4NjQyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5MZW5veCBIaWxsPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85YzQ4MTJjNjNkMzk0NGJjOWMzOTM0YTFkNGUxNTZlOS5zZXRDb250ZW50KGh0bWxfZDQ0MzU2YzQwNDg1NDg5MDlkZjFiYWQ2MDc4OTg2NDIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMDJlZDg2Y2ZhMDE1NGY5ZTlkM2VjNTVjNzAwZTI0ZWIuYmluZFBvcHVwKHBvcHVwXzljNDgxMmM2M2QzOTQ0YmM5YzM5MzRhMWQ0ZTE1NmU5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2U0OWE1MGNkOGM0ZTRhMmY4MzRiZmRiMmFlODgzMjRjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzYyMTU5NjA1NzYyODMsLTczLjk0OTE2NzY5MjI3OTUzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2Y5NzJiNWE2OWQxODQ2MTY5ZWM3ZjY0YTYzZjYxMThlKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzEzNGE5YWM1MWIxZTQ5ODM4MTQ3MTk2MGUyNTk4NTI3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzZjZjcwNmFmZjU1NzRkYjViMWYwNDdmOTRjNTE4NmY0ID0gJCgnPGRpdiBpZD0iaHRtbF82Y2Y3MDZhZmY1NTc0ZGI1YjFmMDQ3Zjk0YzUxODZmNCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Um9vc2V2ZWx0IElzbGFuZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMTM0YTlhYzUxYjFlNDk4MzgxNDcxOTYwZTI1OTg1Mjcuc2V0Q29udGVudChodG1sXzZjZjcwNmFmZjU1NzRkYjViMWYwNDdmOTRjNTE4NmY0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2U0OWE1MGNkOGM0ZTRhMmY4MzRiZmRiMmFlODgzMjRjLmJpbmRQb3B1cChwb3B1cF8xMzRhOWFjNTFiMWU0OTgzODE0NzE5NjBlMjU5ODUyNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82ODE5NzgxOGI0Mjk0YzcyODBmYTRhYzEzODJmMWEwNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc4NzY1Nzk5ODUzNDg1NCwtNzMuOTc3MDU5MjM2MzA2MDNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZjk3MmI1YTY5ZDE4NDYxNjllYzdmNjRhNjNmNjExOGUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOGI1ODNjMDM1YWY2NDAyZDk2NzRhMjliODgxYWQ2YzEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZGY2NTVkMjRjNjU2NGU5OGJjYTc5ODYxYjBkZWIzMGEgPSAkKCc8ZGl2IGlkPSJodG1sX2RmNjU1ZDI0YzY1NjRlOThiY2E3OTg2MWIwZGViMzBhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5VcHBlciBXZXN0IFNpZGU8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzhiNTgzYzAzNWFmNjQwMmQ5Njc0YTI5Yjg4MWFkNmMxLnNldENvbnRlbnQoaHRtbF9kZjY1NWQyNGM2NTY0ZTk4YmNhNzk4NjFiMGRlYjMwYSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82ODE5NzgxOGI0Mjk0YzcyODBmYTRhYzEzODJmMWEwNy5iaW5kUG9wdXAocG9wdXBfOGI1ODNjMDM1YWY2NDAyZDk2NzRhMjliODgxYWQ2YzEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzI2MGNmOWFjNWJjNDY2OGFlNjgyNjIxNjE3YWQ1MjQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NzM1Mjg4ODk0MjE2NiwtNzMuOTg1MzM3NzcwMDEyNjJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZjk3MmI1YTY5ZDE4NDYxNjllYzdmNjRhNjNmNjExOGUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOWJiZGM2YWQxYzM4NGVjZjgxZGIzZmY5ODFlMTExMDkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDFhOGE2MzJhZjhkNGZiNTk1ZGI5NmQzYzYzZmRjMjAgPSAkKCc8ZGl2IGlkPSJodG1sX2QxYThhNjMyYWY4ZDRmYjU5NWRiOTZkM2M2M2ZkYzIwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5MaW5jb2xuIFNxdWFyZTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOWJiZGM2YWQxYzM4NGVjZjgxZGIzZmY5ODFlMTExMDkuc2V0Q29udGVudChodG1sX2QxYThhNjMyYWY4ZDRmYjU5NWRiOTZkM2M2M2ZkYzIwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzMyNjBjZjlhYzViYzQ2NjhhZTY4MjYyMTYxN2FkNTI0LmJpbmRQb3B1cChwb3B1cF85YmJkYzZhZDFjMzg0ZWNmODFkYjNmZjk4MWUxMTEwOSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iNTg0NDNlMDFkZWM0ZWYyOTYzYTdlNTdmNWUyYjlkNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc1OTEwMDg5MTQ2MjEyLC03My45OTYxMTkzNjMwOTQ3OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mOTcyYjVhNjlkMTg0NjE2OWVjN2Y2NGE2M2Y2MTE4ZSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xOWQ2Mjk4NGIzNzU0NGRjYjE2MjI3ZDU0NTUyMTFkZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wYzNmZDU4ZTIxNzc0MTE1OTExNzBlMzBhODZhNGIzOCA9ICQoJzxkaXYgaWQ9Imh0bWxfMGMzZmQ1OGUyMTc3NDExNTkxMTcwZTMwYTg2YTRiMzgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNsaW50b248L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzE5ZDYyOTg0YjM3NTQ0ZGNiMTYyMjdkNTQ1NTIxMWRkLnNldENvbnRlbnQoaHRtbF8wYzNmZDU4ZTIxNzc0MTE1OTExNzBlMzBhODZhNGIzOCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iNTg0NDNlMDFkZWM0ZWYyOTYzYTdlNTdmNWUyYjlkNi5iaW5kUG9wdXAocG9wdXBfMTlkNjI5ODRiMzc1NDRkY2IxNjIyN2Q1NDU1MjExZGQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNmQxZTkzMjgyMDQwNGY3MmIyNWNjZjJiYWMxZWE5ZGIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NTQ2OTExMDI3MDYyMywtNzMuOTgxNjY4ODI3MzAzMDRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZjk3MmI1YTY5ZDE4NDYxNjllYzdmNjRhNjNmNjExOGUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDRkMmJhN2FjNjkxNDdmNzg0ZWY3ZTZmMzY1MjgwNGUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMTliODA0ZDBiZjE1NDY2MWEzNjVmZWNmZjc5ZWEyODAgPSAkKCc8ZGl2IGlkPSJodG1sXzE5YjgwNGQwYmYxNTQ2NjFhMzY1ZmVjZmY3OWVhMjgwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NaWR0b3duPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kNGQyYmE3YWM2OTE0N2Y3ODRlZjdlNmYzNjUyODA0ZS5zZXRDb250ZW50KGh0bWxfMTliODA0ZDBiZjE1NDY2MWEzNjVmZWNmZjc5ZWEyODApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNmQxZTkzMjgyMDQwNGY3MmIyNWNjZjJiYWMxZWE5ZGIuYmluZFBvcHVwKHBvcHVwX2Q0ZDJiYTdhYzY5MTQ3Zjc4NGVmN2U2ZjM2NTI4MDRlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzEyMDhiNzZhNzc0MTRhZDFiODM4MDdmMzQyZTdmOTgxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzQ4MzAzMDc3MjUyMTc0LC03My45NzgzMzIwNzkyNDEyN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mOTcyYjVhNjlkMTg0NjE2OWVjN2Y2NGE2M2Y2MTE4ZSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jMDZmMTg2MzA4ODA0NmQ5YjA4ZWJjMzIxYjc1YzE3OCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84YjI3MzkzOGEzNDk0OTM2YmUxOTBhMjBhMDlhNzUyYSA9ICQoJzxkaXYgaWQ9Imh0bWxfOGIyNzM5MzhhMzQ5NDkzNmJlMTkwYTIwYTA5YTc1MmEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk11cnJheSBIaWxsPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jMDZmMTg2MzA4ODA0NmQ5YjA4ZWJjMzIxYjc1YzE3OC5zZXRDb250ZW50KGh0bWxfOGIyNzM5MzhhMzQ5NDkzNmJlMTkwYTIwYTA5YTc1MmEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMTIwOGI3NmE3NzQxNGFkMWI4MzgwN2YzNDJlN2Y5ODEuYmluZFBvcHVwKHBvcHVwX2MwNmYxODYzMDg4MDQ2ZDliMDhlYmMzMjFiNzVjMTc4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzg4MDc3ZWY1ZTdkNzRkMzZiZGU1MWY3YWMwMzVhNTk4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzQ0MDM0NzA2NzQ3OTc1LC03NC4wMDMxMTYzMzQ3MjgxM10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mOTcyYjVhNjlkMTg0NjE2OWVjN2Y2NGE2M2Y2MTE4ZSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mZTJhMzliOGU3ODE0ZDRlODY0NTcyOTA5YmM0ODExOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82ZmFmMGFkNjcwMTE0ZGRiYWE2OGY3MzZhYTYwZmQzYiA9ICQoJzxkaXYgaWQ9Imh0bWxfNmZhZjBhZDY3MDExNGRkYmFhNjhmNzM2YWE2MGZkM2IiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNoZWxzZWE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2ZlMmEzOWI4ZTc4MTRkNGU4NjQ1NzI5MDliYzQ4MTE4LnNldENvbnRlbnQoaHRtbF82ZmFmMGFkNjcwMTE0ZGRiYWE2OGY3MzZhYTYwZmQzYik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84ODA3N2VmNWU3ZDc0ZDM2YmRlNTFmN2FjMDM1YTU5OC5iaW5kUG9wdXAocG9wdXBfZmUyYTM5YjhlNzgxNGQ0ZTg2NDU3MjkwOWJjNDgxMTgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMmZkODViZTkwZDdhNDM3Mjk2MDJjOWEyNWFlOWVjMDEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MjY5MzI4ODUzNjEyOCwtNzMuOTk5OTE0MDI5NDU5MDJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZjk3MmI1YTY5ZDE4NDYxNjllYzdmNjRhNjNmNjExOGUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTE4ZGQzYTViOTQ0NGFiODllNWIxMjgzZWUwZmQ0NjMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZGNiN2JkZmU1MGIxNDAzOTk0MTUyMGViNDUxYzNkNzIgPSAkKCc8ZGl2IGlkPSJodG1sX2RjYjdiZGZlNTBiMTQwMzk5NDE1MjBlYjQ1MWMzZDcyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5HcmVlbndpY2ggVmlsbGFnZTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTE4ZGQzYTViOTQ0NGFiODllNWIxMjgzZWUwZmQ0NjMuc2V0Q29udGVudChodG1sX2RjYjdiZGZlNTBiMTQwMzk5NDE1MjBlYjQ1MWMzZDcyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzJmZDg1YmU5MGQ3YTQzNzI5NjAyYzlhMjVhZTllYzAxLmJpbmRQb3B1cChwb3B1cF9hMThkZDNhNWI5NDQ0YWI4OWU1YjEyODNlZTBmZDQ2Myk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iZDJiYzg0MjMyYjA0YjgyYjZkMWYwOGFhYjlmN2QxNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcyNzg0Njc3NzI3MDI0NCwtNzMuOTgyMjI2MTY1MDY0MTZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZjk3MmI1YTY5ZDE4NDYxNjllYzdmNjRhNjNmNjExOGUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNmQxNWE0MmYwZjczNDVmNjg1YmFlYTQ4OTgzNThkZmQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYjNiZmE3OWM4MDE1NDcwY2IzZDliYWMyMWZiY2UxYWQgPSAkKCc8ZGl2IGlkPSJodG1sX2IzYmZhNzljODAxNTQ3MGNiM2Q5YmFjMjFmYmNlMWFkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5FYXN0IFZpbGxhZ2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzZkMTVhNDJmMGY3MzQ1ZjY4NWJhZWE0ODk4MzU4ZGZkLnNldENvbnRlbnQoaHRtbF9iM2JmYTc5YzgwMTU0NzBjYjNkOWJhYzIxZmJjZTFhZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iZDJiYzg0MjMyYjA0YjgyYjZkMWYwOGFhYjlmN2QxNC5iaW5kUG9wdXAocG9wdXBfNmQxNWE0MmYwZjczNDVmNjg1YmFlYTQ4OTgzNThkZmQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZTRmN2FhZmNjYTcxNGNjMzg5ZTE1YWIwOWNiZWQ5ZjcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MTc4MDY3NDg5Mjc2NSwtNzMuOTgwODkwMzE5OTkyOTFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZjk3MmI1YTY5ZDE4NDYxNjllYzdmNjRhNjNmNjExOGUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYzQ5MTZmOGRkY2FjNDg3Yzk1ZDg3OGViNGI0MzkwZWMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDliZTQxZjIyOWI2NDk0ZmI1YzM3ZDgyYzE0NzdiY2EgPSAkKCc8ZGl2IGlkPSJodG1sX2Q5YmU0MWYyMjliNjQ5NGZiNWMzN2Q4MmMxNDc3YmNhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Mb3dlciBFYXN0IFNpZGU8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2M0OTE2ZjhkZGNhYzQ4N2M5NWQ4NzhlYjRiNDM5MGVjLnNldENvbnRlbnQoaHRtbF9kOWJlNDFmMjI5YjY0OTRmYjVjMzdkODJjMTQ3N2JjYSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lNGY3YWFmY2NhNzE0Y2MzODllMTVhYjA5Y2JlZDlmNy5iaW5kUG9wdXAocG9wdXBfYzQ5MTZmOGRkY2FjNDg3Yzk1ZDg3OGViNGI0MzkwZWMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDQwNTk2ZGQ1YjMxNDcwYmJmNDkzYmVmYTQwMTYxZTIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MjE1MjE5Njc0NDMyMTYsLTc0LjAxMDY4MzI4NTU5MDg3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2Y5NzJiNWE2OWQxODQ2MTY5ZWM3ZjY0YTYzZjYxMThlKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2VkM2E2NTRlYmJlYjRlMTk5OWJjZGJiODY2NjZmNjBjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2MyMzIyNjZkNWE0ZDRiOWFhYjE5NzU3YjljMmE2ZjU0ID0gJCgnPGRpdiBpZD0iaHRtbF9jMjMyMjY2ZDVhNGQ0YjlhYWIxOTc1N2I5YzJhNmY1NCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VHJpYmVjYTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZWQzYTY1NGViYmViNGUxOTk5YmNkYmI4NjY2NmY2MGMuc2V0Q29udGVudChodG1sX2MyMzIyNjZkNWE0ZDRiOWFhYjE5NzU3YjljMmE2ZjU0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Q0MDU5NmRkNWIzMTQ3MGJiZjQ5M2JlZmE0MDE2MWUyLmJpbmRQb3B1cChwb3B1cF9lZDNhNjU0ZWJiZWI0ZTE5OTliY2RiYjg2NjY2ZjYwYyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84MDIzMGI4NTFkZmI0NTJjYmQzMTEyOTY1MjIzYjliNSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcxOTMyMzc5Mzk1OTA3LC03My45OTczMDQ2NzIwODA3M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mOTcyYjVhNjlkMTg0NjE2OWVjN2Y2NGE2M2Y2MTE4ZSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xMTA4ZDZjYmYyNmE0MTA5YWNhMDFhNGFmYTFjNmEwNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lZmE1YjVmMjEwZjU0MzM4OTdiZGY4MGQwOWI3OWMzYiA9ICQoJzxkaXYgaWQ9Imh0bWxfZWZhNWI1ZjIxMGY1NDMzODk3YmRmODBkMDliNzljM2IiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxpdHRsZSBJdGFseTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMTEwOGQ2Y2JmMjZhNDEwOWFjYTAxYTRhZmExYzZhMDcuc2V0Q29udGVudChodG1sX2VmYTViNWYyMTBmNTQzMzg5N2JkZjgwZDA5Yjc5YzNiKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzgwMjMwYjg1MWRmYjQ1MmNiZDMxMTI5NjUyMjNiOWI1LmJpbmRQb3B1cChwb3B1cF8xMTA4ZDZjYmYyNmE0MTA5YWNhMDFhNGFmYTFjNmEwNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83ZmZjYTUxODE0Mjg0NDZhODAzYzA0OTU1MjE4YjQ0YyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcyMjE4Mzg0MTMxNzk0LC03NC4wMDA2NTY2Njk1OTc1OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mOTcyYjVhNjlkMTg0NjE2OWVjN2Y2NGE2M2Y2MTE4ZSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85ZDU3OTI1NDFjZTI0NzY1YjkwNzJhOTY1ODYyOGNiZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jYzhjOTYzODU2Mjg0NmVhOWRlNWQxYWRlYzFlNWViZiA9ICQoJzxkaXYgaWQ9Imh0bWxfY2M4Yzk2Mzg1NjI4NDZlYTlkZTVkMWFkZWMxZTVlYmYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlNvaG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzlkNTc5MjU0MWNlMjQ3NjViOTA3MmE5NjU4NjI4Y2JkLnNldENvbnRlbnQoaHRtbF9jYzhjOTYzODU2Mjg0NmVhOWRlNWQxYWRlYzFlNWViZik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83ZmZjYTUxODE0Mjg0NDZhODAzYzA0OTU1MjE4YjQ0Yy5iaW5kUG9wdXAocG9wdXBfOWQ1NzkyNTQxY2UyNDc2NWI5MDcyYTk2NTg2MjhjYmQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYmY3ODlhMzdlOGZjNDVkMjkxZWFhOTg1YWUwYzFjYWQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MzQ0MzM5MzU3MjQzNCwtNzQuMDA2MTc5OTgxMjY4MTJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZjk3MmI1YTY5ZDE4NDYxNjllYzdmNjRhNjNmNjExOGUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjNlZDM3ZDkxYTJiNDM3MWI3Zjc4Mzk0NGMwODIwMTggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOThjNTdmZjYxNzUwNGIwOWExN2QzYWY1Y2ZjZGJiYzQgPSAkKCc8ZGl2IGlkPSJodG1sXzk4YzU3ZmY2MTc1MDRiMDlhMTdkM2FmNWNmY2RiYmM0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5XZXN0IFZpbGxhZ2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2YzZWQzN2Q5MWEyYjQzNzFiN2Y3ODM5NDRjMDgyMDE4LnNldENvbnRlbnQoaHRtbF85OGM1N2ZmNjE3NTA0YjA5YTE3ZDNhZjVjZmNkYmJjNCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iZjc4OWEzN2U4ZmM0NWQyOTFlYWE5ODVhZTBjMWNhZC5iaW5kUG9wdXAocG9wdXBfZjNlZDM3ZDkxYTJiNDM3MWI3Zjc4Mzk0NGMwODIwMTgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMTBiNjRhMGMwZDQzNDBiOWFjNWJmYzY4MjllMjNjZTggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43OTczMDcwNDE3MDI4NjUsLTczLjk2NDI4NjE3NzQwNjU1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2Y5NzJiNWE2OWQxODQ2MTY5ZWM3ZjY0YTYzZjYxMThlKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2Q5Y2U3ZTdhNjdlNzRlYWFiYmNhNjI4NWQ0YTliN2UzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzFmYzQ5ZjMyN2IzYjRjYTNhYmYxYTlkYjY2ZmJhM2UxID0gJCgnPGRpdiBpZD0iaHRtbF8xZmM0OWYzMjdiM2I0Y2EzYWJmMWE5ZGI2NmZiYTNlMSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TWFuaGF0dGFuIFZhbGxleTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZDljZTdlN2E2N2U3NGVhYWJiY2E2Mjg1ZDRhOWI3ZTMuc2V0Q29udGVudChodG1sXzFmYzQ5ZjMyN2IzYjRjYTNhYmYxYTlkYjY2ZmJhM2UxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzEwYjY0YTBjMGQ0MzQwYjlhYzViZmM2ODI5ZTIzY2U4LmJpbmRQb3B1cChwb3B1cF9kOWNlN2U3YTY3ZTc0ZWFhYmJjYTYyODVkNGE5YjdlMyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82MWRkOTRiMzA5OGQ0ZGY1YTJhODFmNzU2MWQyYzFiYSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjgwNzk5OTczODE2NTgyNiwtNzMuOTYzODk2Mjc5MDUzMzJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZjk3MmI1YTY5ZDE4NDYxNjllYzdmNjRhNjNmNjExOGUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNTAwNTI3MWIzYWUzNGI1NDgwNTllYmJhMGI4YjMxMDkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfM2NkNDc4OThhODI3NDk1Mjk1MDMzYTlhMGI2OTZiOWMgPSAkKCc8ZGl2IGlkPSJodG1sXzNjZDQ3ODk4YTgyNzQ5NTI5NTAzM2E5YTBiNjk2YjljIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Nb3JuaW5nc2lkZSBIZWlnaHRzPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81MDA1MjcxYjNhZTM0YjU0ODA1OWViYmEwYjhiMzEwOS5zZXRDb250ZW50KGh0bWxfM2NkNDc4OThhODI3NDk1Mjk1MDMzYTlhMGI2OTZiOWMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNjFkZDk0YjMwOThkNGRmNWEyYTgxZjc1NjFkMmMxYmEuYmluZFBvcHVwKHBvcHVwXzUwMDUyNzFiM2FlMzRiNTQ4MDU5ZWJiYTBiOGIzMTA5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2VhOThiYWYzNThlNjRhOGVhYjlkMmRkOGYxZTBhNmM4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzM3MjA5ODMyNzE1LC03My45ODEzNzU5NDgzMzU0MV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mOTcyYjVhNjlkMTg0NjE2OWVjN2Y2NGE2M2Y2MTE4ZSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9kNWM5NTgyODNjYTI0YmE0YjliZmVjNGE5NGRjN2U4MCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zN2U4YjcxZjBlOWI0MzMxYjkyMmY3ODQ2Mzc5YTYwOSA9ICQoJzxkaXYgaWQ9Imh0bWxfMzdlOGI3MWYwZTliNDMzMWI5MjJmNzg0NjM3OWE2MDkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkdyYW1lcmN5PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kNWM5NTgyODNjYTI0YmE0YjliZmVjNGE5NGRjN2U4MC5zZXRDb250ZW50KGh0bWxfMzdlOGI3MWYwZTliNDMzMWI5MjJmNzg0NjM3OWE2MDkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZWE5OGJhZjM1OGU2NGE4ZWFiOWQyZGQ4ZjFlMGE2YzguYmluZFBvcHVwKHBvcHVwX2Q1Yzk1ODI4M2NhMjRiYTRiOWJmZWM0YTk0ZGM3ZTgwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2FiNWU4NDA1MjRiMjRjODZhOGYyYjMwY2U1NGQ1MDE5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzExOTMxOTgzOTQ1NjUsLTc0LjAxNjg2OTMwNTA4NjE3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2Y5NzJiNWE2OWQxODQ2MTY5ZWM3ZjY0YTYzZjYxMThlKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2MxMTFmYjBmMjZkNzRiMDE5MjZiNDQ5NmFhZDI3YTFmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzY3OWYzNjczNzFhNzRlNTZhZjM5ZmI4ZWQ3OTRiMGNhID0gJCgnPGRpdiBpZD0iaHRtbF82NzlmMzY3MzcxYTc0ZTU2YWYzOWZiOGVkNzk0YjBjYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmF0dGVyeSBQYXJrIENpdHk8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2MxMTFmYjBmMjZkNzRiMDE5MjZiNDQ5NmFhZDI3YTFmLnNldENvbnRlbnQoaHRtbF82NzlmMzY3MzcxYTc0ZTU2YWYzOWZiOGVkNzk0YjBjYSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hYjVlODQwNTI0YjI0Yzg2YThmMmIzMGNlNTRkNTAxOS5iaW5kUG9wdXAocG9wdXBfYzExMWZiMGYyNmQ3NGIwMTkyNmI0NDk2YWFkMjdhMWYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMTRmNDgyYmMxMzkxNDk2OWIzMGM2NmJkMTI5YThkYzkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MDcxMDcxMDcyNzA0OCwtNzQuMDEwNjY1NDQ1MjEyN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mOTcyYjVhNjlkMTg0NjE2OWVjN2Y2NGE2M2Y2MTE4ZSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9kZDAyNTBmZGIwMDY0YmMyODQ4ZWM4MmJmNWZmNGM2YyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80ODNjZWJkZjNkMTM0MDFhYThjYmVkNmFkMzAyZDg1MiA9ICQoJzxkaXYgaWQ9Imh0bWxfNDgzY2ViZGYzZDEzNDAxYWE4Y2JlZDZhZDMwMmQ4NTIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZpbmFuY2lhbCBEaXN0cmljdDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZGQwMjUwZmRiMDA2NGJjMjg0OGVjODJiZjVmZjRjNmMuc2V0Q29udGVudChodG1sXzQ4M2NlYmRmM2QxMzQwMWFhOGNiZWQ2YWQzMDJkODUyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzE0ZjQ4MmJjMTM5MTQ5NjliMzBjNjZiZDEyOWE4ZGM5LmJpbmRQb3B1cChwb3B1cF9kZDAyNTBmZGIwMDY0YmMyODQ4ZWM4MmJmNWZmNGM2Yyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iNWUyYjFjNTFiNjA0OTJlYTc3NzYzMzNhOTYyNzcxZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc4MjY4MjU2NzEyNTcsLTczLjk1MzI1NjQ2ODM3MTEyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2Y5NzJiNWE2OWQxODQ2MTY5ZWM3ZjY0YTYzZjYxMThlKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2RlZTU3Y2Q4ZWE2YzRkMGNiNGNjMjg1MTcxMzczMDI2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2MzMjFiMjFjZmY1MDQwMTViMDg2OWMwMjNiZjg5NjA3ID0gJCgnPGRpdiBpZD0iaHRtbF9jMzIxYjIxY2ZmNTA0MDE1YjA4NjljMDIzYmY4OTYwNyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2FybmVnaWUgSGlsbDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZGVlNTdjZDhlYTZjNGQwY2I0Y2MyODUxNzEzNzMwMjYuc2V0Q29udGVudChodG1sX2MzMjFiMjFjZmY1MDQwMTViMDg2OWMwMjNiZjg5NjA3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2I1ZTJiMWM1MWI2MDQ5MmVhNzc3NjMzM2E5NjI3NzFmLmJpbmRQb3B1cChwb3B1cF9kZWU1N2NkOGVhNmM0ZDBjYjRjYzI4NTE3MTM3MzAyNik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85M2MzZWYzYTcyZjc0OTMyYTU4NmY4MDI0OGMxZTJjNSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjcyMzI1OTAxODg1NzY4LC03My45ODg0MzM2ODAyMzU5N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mOTcyYjVhNjlkMTg0NjE2OWVjN2Y2NGE2M2Y2MTE4ZSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83YTI0NTE4YWIyMzU0MmQ4YmJhZGI1Y2JjZmIzMDFmOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wNmI4MGJjYmRlNTQ0ZDJkOGIyYWMxYzhkOWU0NDljOCA9ICQoJzxkaXYgaWQ9Imh0bWxfMDZiODBiY2JkZTU0NGQyZDhiMmFjMWM4ZDllNDQ5YzgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5vaG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzdhMjQ1MThhYjIzNTQyZDhiYmFkYjVjYmNmYjMwMWY4LnNldENvbnRlbnQoaHRtbF8wNmI4MGJjYmRlNTQ0ZDJkOGIyYWMxYzhkOWU0NDljOCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85M2MzZWYzYTcyZjc0OTMyYTU4NmY4MDI0OGMxZTJjNS5iaW5kUG9wdXAocG9wdXBfN2EyNDUxOGFiMjM1NDJkOGJiYWRiNWNiY2ZiMzAxZjgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZTZlNmUyOWM0OTdjNGY1N2EwMDA3NDk3ZTVhYjRkNzggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MTUyMjg5MjA0NjI4MiwtNzQuMDA1NDE1Mjk4NzMzNTVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZjk3MmI1YTY5ZDE4NDYxNjllYzdmNjRhNjNmNjExOGUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfY2QyMzdmMzdhMDY4NDEyY2JlMDhmYmY2Mjk1MWRkNjggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZGRjYTJmMjRmNjk2NGEyOTg1ZjRlZjBhNzM1ZjA0MTIgPSAkKCc8ZGl2IGlkPSJodG1sX2RkY2EyZjI0ZjY5NjRhMjk4NWY0ZWYwYTczNWYwNDEyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DaXZpYyBDZW50ZXI8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2NkMjM3ZjM3YTA2ODQxMmNiZTA4ZmJmNjI5NTFkZDY4LnNldENvbnRlbnQoaHRtbF9kZGNhMmYyNGY2OTY0YTI5ODVmNGVmMGE3MzVmMDQxMik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lNmU2ZTI5YzQ5N2M0ZjU3YTAwMDc0OTdlNWFiNGQ3OC5iaW5kUG9wdXAocG9wdXBfY2QyMzdmMzdhMDY4NDEyY2JlMDhmYmY2Mjk1MWRkNjgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDhiM2I4ZWE1OTRmNGVhNGIzMTM2NmVhMzdhNzE2NTIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NDg1MDk2NjQzMTIyLC03My45ODg3MTMxMzI4NTI0N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mOTcyYjVhNjlkMTg0NjE2OWVjN2Y2NGE2M2Y2MTE4ZSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8wY2U4NmJhNjY1ZWM0OTQxOGMwM2E2MTYwNWQyNmNhOSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yZTgzZDJjNzE0NTc0YWU0YTQ2NWM5ZmM4MTJmNTRiNiA9ICQoJzxkaXYgaWQ9Imh0bWxfMmU4M2QyYzcxNDU3NGFlNGE0NjVjOWZjODEyZjU0YjYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk1pZHRvd24gU291dGg8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzBjZTg2YmE2NjVlYzQ5NDE4YzAzYTYxNjA1ZDI2Y2E5LnNldENvbnRlbnQoaHRtbF8yZTgzZDJjNzE0NTc0YWU0YTQ2NWM5ZmM4MTJmNTRiNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kOGIzYjhlYTU5NGY0ZWE0YjMxMzY2ZWEzN2E3MTY1Mi5iaW5kUG9wdXAocG9wdXBfMGNlODZiYTY2NWVjNDk0MThjMDNhNjE2MDVkMjZjYTkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMTcyMzkzYTk0YWY4NGIwYzk0MTc1YjZjYjZhMDIxMGQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NjAyODAzMzEzMTM3NCwtNzMuOTYzNTU2MTQwOTQzMDNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZjk3MmI1YTY5ZDE4NDYxNjllYzdmNjRhNjNmNjExOGUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjA3YzNjOTAxZmFkNDdiZGJiNGUxYTJhN2UwYmQyOTIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzY5YjQzOTQyNGM4NGE3Zjk2Mjk0OWRmOGYxYmE3NTcgPSAkKCc8ZGl2IGlkPSJodG1sXzc2OWI0Mzk0MjRjODRhN2Y5NjI5NDlkZjhmMWJhNzU3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdXR0b24gUGxhY2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzYwN2MzYzkwMWZhZDQ3YmRiYjRlMWEyYTdlMGJkMjkyLnNldENvbnRlbnQoaHRtbF83NjliNDM5NDI0Yzg0YTdmOTYyOTQ5ZGY4ZjFiYTc1Nyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xNzIzOTNhOTRhZjg0YjBjOTQxNzViNmNiNmEwMjEwZC5iaW5kUG9wdXAocG9wdXBfNjA3YzNjOTAxZmFkNDdiZGJiNGUxYTJhN2UwYmQyOTIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOWQ2NDRiMzRlNjk3NDlhYTg0OTMyMzdmMzE5YjI0NDggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43NTIwNDIzNjk1MDcyMiwtNzMuOTY3NzA4MjQ1ODE4MzRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZjk3MmI1YTY5ZDE4NDYxNjllYzdmNjRhNjNmNjExOGUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODc3NDM2NWI2OGZjNGZkNmFiMTM2ODA4OWQ1NWQxNTkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfN2JmMmM1ZWFjMmI5NDFjYjliYjNlNDcyZWYzODQzMDAgPSAkKCc8ZGl2IGlkPSJodG1sXzdiZjJjNWVhYzJiOTQxY2I5YmIzZTQ3MmVmMzg0MzAwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UdXJ0bGUgQmF5PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84Nzc0MzY1YjY4ZmM0ZmQ2YWIxMzY4MDg5ZDU1ZDE1OS5zZXRDb250ZW50KGh0bWxfN2JmMmM1ZWFjMmI5NDFjYjliYjNlNDcyZWYzODQzMDApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOWQ2NDRiMzRlNjk3NDlhYTg0OTMyMzdmMzE5YjI0NDguYmluZFBvcHVwKHBvcHVwXzg3NzQzNjViNjhmYzRmZDZhYjEzNjgwODlkNTVkMTU5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2NmZWRjODAyMTFlNTQxMGU5NDk4OTU5N2JjMzRiYzA0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuNzQ2OTE3NDEwNzQwMTk1LC03My45NzEyMTkyODcyMjI2NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mOTcyYjVhNjlkMTg0NjE2OWVjN2Y2NGE2M2Y2MTE4ZSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xYTAxYzg3ZWEzNmU0N2UzOTc2YmM2N2ZjMGJjZTRhYyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hY2FlN2U4OWQ5NWM0ZDdiODJlZjcyYzY3MjE5NjM0MiA9ICQoJzxkaXYgaWQ9Imh0bWxfYWNhZTdlODlkOTVjNGQ3YjgyZWY3MmM2NzIxOTYzNDIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlR1ZG9yIENpdHk8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzFhMDFjODdlYTM2ZTQ3ZTM5NzZiYzY3ZmMwYmNlNGFjLnNldENvbnRlbnQoaHRtbF9hY2FlN2U4OWQ5NWM0ZDdiODJlZjcyYzY3MjE5NjM0Mik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jZmVkYzgwMjExZTU0MTBlOTQ5ODk1OTdiYzM0YmMwNC5iaW5kUG9wdXAocG9wdXBfMWEwMWM4N2VhMzZlNDdlMzk3NmJjNjdmYzBiY2U0YWMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZTIwMjQ3ODBlMTE4NGRmZDgyNzE0ZDhkZmVjOTRkNjIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43MzA5OTk1NTQ3NzA2MSwtNzMuOTc0MDUxNzA0NjkyMDNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZjk3MmI1YTY5ZDE4NDYxNjllYzdmNjRhNjNmNjExOGUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDdkOGVjNDBlY2FjNDM2ZjhjZmZjNWY2YWViMTA0OTAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTg0NTgxMDcwM2JiNGEyODliNzJlYzUwYzhhMzZkMDEgPSAkKCc8ZGl2IGlkPSJodG1sX2U4NDU4MTA3MDNiYjRhMjg5YjcyZWM1MGM4YTM2ZDAxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdHV5dmVzYW50IFRvd248L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Q3ZDhlYzQwZWNhYzQzNmY4Y2ZmYzVmNmFlYjEwNDkwLnNldENvbnRlbnQoaHRtbF9lODQ1ODEwNzAzYmI0YTI4OWI3MmVjNTBjOGEzNmQwMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lMjAyNDc4MGUxMTg0ZGZkODI3MTRkOGRmZWM5NGQ2Mi5iaW5kUG9wdXAocG9wdXBfZDdkOGVjNDBlY2FjNDM2ZjhjZmZjNWY2YWViMTA0OTApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMmQ5YTVjYTUwYTA1NDI5ZWIyN2NkODdiM2MwNzBmNTMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC43Mzk2NzMwNDc2Mzg0MjYsLTczLjk5MDk0NzEwNTI4MjZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfZjk3MmI1YTY5ZDE4NDYxNjllYzdmNjRhNjNmNjExOGUpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOGM5MTcwZGIwZjBjNGJmMjgyYWZkMzEyZjk0MzcyNzggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfY2M3MjVhOTZmNjVlNDI3NWE2N2JkNjdmZTU3MjhiNzggPSAkKCc8ZGl2IGlkPSJodG1sX2NjNzI1YTk2ZjY1ZTQyNzVhNjdiZDY3ZmU1NzI4Yjc4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5GbGF0aXJvbjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOGM5MTcwZGIwZjBjNGJmMjgyYWZkMzEyZjk0MzcyNzguc2V0Q29udGVudChodG1sX2NjNzI1YTk2ZjY1ZTQyNzVhNjdiZDY3ZmU1NzI4Yjc4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzJkOWE1Y2E1MGEwNTQyOWViMjdjZDg3YjNjMDcwZjUzLmJpbmRQb3B1cChwb3B1cF84YzkxNzBkYjBmMGM0YmYyODJhZmQzMTJmOTQzNzI3OCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85MzE1YThlMGI2Y2Q0MjljODg3ZTJkYTFhZmRjNzUxOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjc1NjY1ODA4MjI3NTE5LC03NC4wMDAxMTEzNjIwMjYzN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9mOTcyYjVhNjlkMTg0NjE2OWVjN2Y2NGE2M2Y2MTE4ZSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hODA5MTQ0MTY1MDQ0OGZkOTMxNGE3MzIxODJjZGJlZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80ZTIxNzY2ZWQ1Njk0ZGI0YjVjZDhlNTY4MzkwZWZiMCA9ICQoJzxkaXYgaWQ9Imh0bWxfNGUyMTc2NmVkNTY5NGRiNGI1Y2Q4ZTU2ODM5MGVmYjAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkh1ZHNvbiBZYXJkczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTgwOTE0NDE2NTA0NDhmZDkzMTRhNzMyMTgyY2RiZWUuc2V0Q29udGVudChodG1sXzRlMjE3NjZlZDU2OTRkYjRiNWNkOGU1NjgzOTBlZmIwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzkzMTVhOGUwYjZjZDQyOWM4ODdlMmRhMWFmZGM3NTE4LmJpbmRQb3B1cChwb3B1cF9hODA5MTQ0MTY1MDQ0OGZkOTMxNGE3MzIxODJjZGJlZSk7CgogICAgICAgICAgICAKICAgICAgICAKPC9zY3JpcHQ+ onload="this.contentDocument.open();this.contentDocument.write(atob(this.getAttribute('data-html')));this.contentDocument.close();" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python
print ('Starting to look at other locations, Bronx')
```

    Starting to look at other locations, Bronx



```python
CLIENT_ID = 'XOMNN5V4YTDAU4HRS1NHJQMW5IYKWCWXXGCE2ZNPW4NKNU3O' # your Foursquare ID
CLIENT_SECRET = 'VMCFJQKYJT3TFKSLNMJNXNEC3EDSSLWGHUR5B3QUCODZ1K1L' # your Foursquare Secret
VERSION = '20180605' # Foursquare API version
LIMIT = 100 # A default Foursquare API limit value

print('Your credentails:')
print('CLIENT_ID: ' + CLIENT_ID)
print('CLIENT_SECRET:' + CLIENT_SECRET)
```

    Your credentails:
    CLIENT_ID: XOMNN5V4YTDAU4HRS1NHJQMW5IYKWCWXXGCE2ZNPW4NKNU3O
    CLIENT_SECRET:VMCFJQKYJT3TFKSLNMJNXNEC3EDSSLWGHUR5B3QUCODZ1K1L



```python
print ('#determining neighborhoods of Bronx, NY')
```

    #determining neighborhoods of Bronx, NY



```python
bronx_data = neighborhoods[neighborhoods['Borough'] == 'Bronx'].reset_index(drop=True)
bronx_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Borough</th>
      <th>Neighborhood</th>
      <th>Latitude</th>
      <th>Longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bronx</td>
      <td>Wakefield</td>
      <td>40.894705</td>
      <td>-73.847201</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bronx</td>
      <td>Co-op City</td>
      <td>40.874294</td>
      <td>-73.829939</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bronx</td>
      <td>Eastchester</td>
      <td>40.887556</td>
      <td>-73.827806</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Bronx</td>
      <td>Fieldston</td>
      <td>40.895437</td>
      <td>-73.905643</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bronx</td>
      <td>Riverdale</td>
      <td>40.890834</td>
      <td>-73.912585</td>
    </tr>
  </tbody>
</table>
</div>




```python
address = 'Bronx, NY'

geolocator = Nominatim(user_agent="ny_explorer")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of Manhattan are {}, {}.'.format(latitude, longitude))
```

    The geograpical coordinate of Manhattan are 40.8506558, -73.8665241.



```python
print ('Creating map of the Bronx')
```

    Creating map of the Bronx



```python
# create map of Bronx using latitude and longitude values
map_bronx = folium.Map(location=[latitude, longitude], zoom_start=11)

# add markers to map
for lat, lng, label in zip(bronx_data['Latitude'], bronx_data['Longitude'], bronx_data['Neighborhood']):
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='blue',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7,
        parse_html=False).add_to(map_bronx)  
    
map_bronx
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe src="about:blank" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" data-html=PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfNGQ2MTI4NTkxMjMzNDZmYmI1YmE0YjE3NGNhMmQyNzkgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwLjAlOwogICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAo8L2hlYWQ+Cjxib2R5PiAgICAKICAgIAogICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb2xpdW0tbWFwIiBpZD0ibWFwXzRkNjEyODU5MTIzMzQ2ZmJiNWJhNGIxNzRjYTJkMjc5IiA+PC9kaXY+CiAgICAgICAgCjwvYm9keT4KPHNjcmlwdD4gICAgCiAgICAKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIG1hcF80ZDYxMjg1OTEyMzM0NmZiYjViYTRiMTc0Y2EyZDI3OSA9IEwubWFwKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ21hcF80ZDYxMjg1OTEyMzM0NmZiYjViYTRiMTc0Y2EyZDI3OScsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7Y2VudGVyOiBbNDAuODQ5MzA0NDUsLTczLjg3NzEzNzkxODM1MjA2XSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHpvb206IDExLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbWF4Qm91bmRzOiBib3VuZHMsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBsYXllcnM6IFtdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgd29ybGRDb3B5SnVtcDogZmFsc2UsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjcnM6IEwuQ1JTLkVQU0czODU3CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0pOwogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgdGlsZV9sYXllcl83ODVkMTUzYzI1YTg0MGUxYjhhZmExYjM5YzExNTBkYiA9IEwudGlsZUxheWVyKAogICAgICAgICAgICAgICAgJ2h0dHBzOi8ve3N9LnRpbGUub3BlbnN0cmVldG1hcC5vcmcve3p9L3t4fS97eX0ucG5nJywKICAgICAgICAgICAgICAgIHsKICAiYXR0cmlidXRpb24iOiBudWxsLAogICJkZXRlY3RSZXRpbmEiOiBmYWxzZSwKICAibWF4Wm9vbSI6IDE4LAogICJtaW5ab29tIjogMSwKICAibm9XcmFwIjogZmFsc2UsCiAgInN1YmRvbWFpbnMiOiAiYWJjIgp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80ZDYxMjg1OTEyMzM0NmZiYjViYTRiMTc0Y2EyZDI3OSk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOGExMzk2MGM4Yjc5NDFkMWE3MTMwZDc5Mjc4Y2ZmMDMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44OTQ3MDUxNzY2MSwtNzMuODQ3MjAwNTIwNTQ5MDJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNGQ2MTI4NTkxMjMzNDZmYmI1YmE0YjE3NGNhMmQyNzkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZmE3YzI5YjIxMGNkNDNhYThjOWRjMTJiNTBlOTE0MzIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDQxZTJkOTFiMDA4NDI0MjgyNDY2MDY1MTVmMWNhN2IgPSAkKCc8ZGl2IGlkPSJodG1sX2Q0MWUyZDkxYjAwODQyNDI4MjQ2NjA2NTE1ZjFjYTdiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5XYWtlZmllbGQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2ZhN2MyOWIyMTBjZDQzYWE4YzlkYzEyYjUwZTkxNDMyLnNldENvbnRlbnQoaHRtbF9kNDFlMmQ5MWIwMDg0MjQyODI0NjYwNjUxNWYxY2E3Yik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84YTEzOTYwYzhiNzk0MWQxYTcxMzBkNzkyNzhjZmYwMy5iaW5kUG9wdXAocG9wdXBfZmE3YzI5YjIxMGNkNDNhYThjOWRjMTJiNTBlOTE0MzIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOTA0YjRiZjQ4YmRmNGZkZjhhZGJlODFkNzczNWI4ODcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NzQyOTQxOTMwMzAxMiwtNzMuODI5OTM5MTA4MTIzOThdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNGQ2MTI4NTkxMjMzNDZmYmI1YmE0YjE3NGNhMmQyNzkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNzYxYzFmNjk0OTM3NGZlMmE3MGM5MTgyMTEyMWFhZTMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfN2I0ZDg3NThlYjU1NGQ1NWEwZDY3NzVhZTZhYjMwNWMgPSAkKCc8ZGl2IGlkPSJodG1sXzdiNGQ4NzU4ZWI1NTRkNTVhMGQ2Nzc1YWU2YWIzMDVjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Dby1vcCBDaXR5PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83NjFjMWY2OTQ5Mzc0ZmUyYTcwYzkxODIxMTIxYWFlMy5zZXRDb250ZW50KGh0bWxfN2I0ZDg3NThlYjU1NGQ1NWEwZDY3NzVhZTZhYjMwNWMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTA0YjRiZjQ4YmRmNGZkZjhhZGJlODFkNzczNWI4ODcuYmluZFBvcHVwKHBvcHVwXzc2MWMxZjY5NDkzNzRmZTJhNzBjOTE4MjExMjFhYWUzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzc1OTVhZGJjM2YzYTQyMWU4ZDE3MWNkMmUyNTJhNDRmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODg3NTU1Njc3MzUwNzc1LC03My44Mjc4MDY0NDcxNjQxMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80ZDYxMjg1OTEyMzM0NmZiYjViYTRiMTc0Y2EyZDI3OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85OTJlOThhNDE3OTc0MDM2ODE4MzQ0MTMyOTEyNWYxMyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85Zjc5Y2JkZmVhZDE0OWQwYjRjMmYxYTQ4ZmUxNTFjNSA9ICQoJzxkaXYgaWQ9Imh0bWxfOWY3OWNiZGZlYWQxNDlkMGI0YzJmMWE0OGZlMTUxYzUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVhc3RjaGVzdGVyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85OTJlOThhNDE3OTc0MDM2ODE4MzQ0MTMyOTEyNWYxMy5zZXRDb250ZW50KGh0bWxfOWY3OWNiZGZlYWQxNDlkMGI0YzJmMWE0OGZlMTUxYzUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNzU5NWFkYmMzZjNhNDIxZThkMTcxY2QyZTI1MmE0NGYuYmluZFBvcHVwKHBvcHVwXzk5MmU5OGE0MTc5NzQwMzY4MTgzNDQxMzI5MTI1ZjEzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzU1YjNiYmI0ODVmZDQ2ZmE4YjVhNjA0ZjZjNDA3YjY4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODk1NDM3NDI2OTAzODMsLTczLjkwNTY0MjU5NTkxNjgyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzRkNjEyODU5MTIzMzQ2ZmJiNWJhNGIxNzRjYTJkMjc5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzhmOTZkNmIxZmEyYjRjYWNiNTBjODhjMTM5MmNhNGI2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2E5ZDJkMjFlODIyMTQwMjNhMmZmNTBjNmI0N2Q0ZWM2ID0gJCgnPGRpdiBpZD0iaHRtbF9hOWQyZDIxZTgyMjE0MDIzYTJmZjUwYzZiNDdkNGVjNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RmllbGRzdG9uPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84Zjk2ZDZiMWZhMmI0Y2FjYjUwYzg4YzEzOTJjYTRiNi5zZXRDb250ZW50KGh0bWxfYTlkMmQyMWU4MjIxNDAyM2EyZmY1MGM2YjQ3ZDRlYzYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNTViM2JiYjQ4NWZkNDZmYThiNWE2MDRmNmM0MDdiNjguYmluZFBvcHVwKHBvcHVwXzhmOTZkNmIxZmEyYjRjYWNiNTBjODhjMTM5MmNhNGI2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzFkOGUxY2IyY2Q2NDQxZTE5NDhjMWRlZmVmMWVjNzI0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODkwODM0NDkzODkxMzA1LC03My45MTI1ODU0NjEwODU3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzRkNjEyODU5MTIzMzQ2ZmJiNWJhNGIxNzRjYTJkMjc5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzgyYWQzNTViNmMwZTQ4YWY4MmQ2ZWEyMGM1NjU5ZThhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2EzYWM4MGEyM2FhMTQxYmVhYmE3ZDhiZjU2MWNiOTg4ID0gJCgnPGRpdiBpZD0iaHRtbF9hM2FjODBhMjNhYTE0MWJlYWJhN2Q4YmY1NjFjYjk4OCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Uml2ZXJkYWxlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84MmFkMzU1YjZjMGU0OGFmODJkNmVhMjBjNTY1OWU4YS5zZXRDb250ZW50KGh0bWxfYTNhYzgwYTIzYWExNDFiZWFiYTdkOGJmNTYxY2I5ODgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMWQ4ZTFjYjJjZDY0NDFlMTk0OGMxZGVmZWYxZWM3MjQuYmluZFBvcHVwKHBvcHVwXzgyYWQzNTViNmMwZTQ4YWY4MmQ2ZWEyMGM1NjU5ZThhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2U0MDAwMzc3NTM2OTRiNTlhNjhhY2Y5MjE0Y2FhZGZkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODgxNjg3MzcxMjA1MjEsLTczLjkwMjgxNzk4NzI0NjA0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzRkNjEyODU5MTIzMzQ2ZmJiNWJhNGIxNzRjYTJkMjc5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzNlNDQ1NDRlOTU5MjQwMjdhOTdmNWRkYzcwN2ZlMDdkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2YzZjhlODYzMGUyYjRkNGU5MGE0NWRmYjlkNTQzMjViID0gJCgnPGRpdiBpZD0iaHRtbF9mM2Y4ZTg2MzBlMmI0ZDRlOTBhNDVkZmI5ZDU0MzI1YiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+S2luZ3NicmlkZ2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzNlNDQ1NDRlOTU5MjQwMjdhOTdmNWRkYzcwN2ZlMDdkLnNldENvbnRlbnQoaHRtbF9mM2Y4ZTg2MzBlMmI0ZDRlOTBhNDVkZmI5ZDU0MzI1Yik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lNDAwMDM3NzUzNjk0YjU5YTY4YWNmOTIxNGNhYWRmZC5iaW5kUG9wdXAocG9wdXBfM2U0NDU0NGU5NTkyNDAyN2E5N2Y1ZGRjNzA3ZmUwN2QpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzJiOWFhMmRjYWQyNDViMmE2ZmUzMTliZTE1ZDgzNzEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44OTgyNzI2MTIxMzgwNSwtNzMuODY3MzE0OTY4MTQxNzZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNGQ2MTI4NTkxMjMzNDZmYmI1YmE0YjE3NGNhMmQyNzkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZGM5MjJlOTg5ODNjNDBlN2IxYTcyMDkwNTNkNzk0YWIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzgxMGZjMDUzNWVjNDg5NDg0MTU0MTg2N2UzMTI4OGUgPSAkKCc8ZGl2IGlkPSJodG1sXzc4MTBmYzA1MzVlYzQ4OTQ4NDE1NDE4NjdlMzEyODhlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Xb29kbGF3bjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZGM5MjJlOTg5ODNjNDBlN2IxYTcyMDkwNTNkNzk0YWIuc2V0Q29udGVudChodG1sXzc4MTBmYzA1MzVlYzQ4OTQ4NDE1NDE4NjdlMzEyODhlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzMyYjlhYTJkY2FkMjQ1YjJhNmZlMzE5YmUxNWQ4MzcxLmJpbmRQb3B1cChwb3B1cF9kYzkyMmU5ODk4M2M0MGU3YjFhNzIwOTA1M2Q3OTRhYik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zYmUxNjBiNWZiNDQ0ODUzYmYzYjcxNTU0MmY4YzZlNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg3NzIyNDE1NTk5NDQ2LC03My44NzkzOTA3Mzk1NjgxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzRkNjEyODU5MTIzMzQ2ZmJiNWJhNGIxNzRjYTJkMjc5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2IxMGY0ODVjNzVhZjQ1NDZiMmRlYTA5MDk0ZjAxYWM5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzQxNDg2ZmY5OTYzYTQ4YjZhMGNkZGU1OGQ3YTAwYTY5ID0gJCgnPGRpdiBpZD0iaHRtbF80MTQ4NmZmOTk2M2E0OGI2YTBjZGRlNThkN2EwMGE2OSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Tm9yd29vZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjEwZjQ4NWM3NWFmNDU0NmIyZGVhMDkwOTRmMDFhYzkuc2V0Q29udGVudChodG1sXzQxNDg2ZmY5OTYzYTQ4YjZhMGNkZGU1OGQ3YTAwYTY5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzNiZTE2MGI1ZmI0NDQ4NTNiZjNiNzE1NTQyZjhjNmU0LmJpbmRQb3B1cChwb3B1cF9iMTBmNDg1Yzc1YWY0NTQ2YjJkZWEwOTA5NGYwMWFjOSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84MmZjOTJjMDFkNTE0YWZmOTFiZTcyNTQ3Y2IwZWM3NCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg4MTAzODg3ODE5MjExLC03My44NTc0NDY0Mjk3NDIwN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80ZDYxMjg1OTEyMzM0NmZiYjViYTRiMTc0Y2EyZDI3OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lYmQ0ODFmN2UyYmQ0MGZmYTc0NmRmMzBkNDk2ZGFiMyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zNzRjZjdkMTkxNjQ0MmY3YjkxNjgxMGQ3ODcwZGViMCA9ICQoJzxkaXYgaWQ9Imh0bWxfMzc0Y2Y3ZDE5MTY0NDJmN2I5MTY4MTBkNzg3MGRlYjAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldpbGxpYW1zYnJpZGdlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lYmQ0ODFmN2UyYmQ0MGZmYTc0NmRmMzBkNDk2ZGFiMy5zZXRDb250ZW50KGh0bWxfMzc0Y2Y3ZDE5MTY0NDJmN2I5MTY4MTBkNzg3MGRlYjApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfODJmYzkyYzAxZDUxNGFmZjkxYmU3MjU0N2NiMGVjNzQuYmluZFBvcHVwKHBvcHVwX2ViZDQ4MWY3ZTJiZDQwZmZhNzQ2ZGYzMGQ0OTZkYWIzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzE4MWQ2NTNkMDMyMDQ4ZDQ4ODk4ZWMxYWZiZGIxMDFiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODY2ODU4MTA3MjUyNjk2LC03My44MzU3OTc1OTgwODExN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80ZDYxMjg1OTEyMzM0NmZiYjViYTRiMTc0Y2EyZDI3OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lMjgyN2U0ZDUwNTE0YzE3OTk0YmMyYmM1ZDFmYmJiNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zMjAwZTc0OTNmZTA0MDE1ODJiNThhYTJmN2Q1MTY2YiA9ICQoJzxkaXYgaWQ9Imh0bWxfMzIwMGU3NDkzZmUwNDAxNTgyYjU4YWEyZjdkNTE2NmIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJheWNoZXN0ZXI8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2UyODI3ZTRkNTA1MTRjMTc5OTRiYzJiYzVkMWZiYmI0LnNldENvbnRlbnQoaHRtbF8zMjAwZTc0OTNmZTA0MDE1ODJiNThhYTJmN2Q1MTY2Yik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xODFkNjUzZDAzMjA0OGQ0ODg5OGVjMWFmYmRiMTAxYi5iaW5kUG9wdXAocG9wdXBfZTI4MjdlNGQ1MDUxNGMxNzk5NGJjMmJjNWQxZmJiYjQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzc1OTc4ZmU1MDE2NDg2NmFhZmNhOWI1OWJkYmE0YmYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NTc0MTM0OTgwODg2NSwtNzMuODU0NzU1NjQwMTc5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNGQ2MTI4NTkxMjMzNDZmYmI1YmE0YjE3NGNhMmQyNzkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODkzYmIyY2JhOGY4NDE4MDlhMTk5NGIxZjNmNTg0YTUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYjZjZjk2ZmQ0ZjRiNDQxNmI4MjE5MzJhNDQ4MTUxZTYgPSAkKCc8ZGl2IGlkPSJodG1sX2I2Y2Y5NmZkNGY0YjQ0MTZiODIxOTMyYTQ0ODE1MWU2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5QZWxoYW0gUGFya3dheTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfODkzYmIyY2JhOGY4NDE4MDlhMTk5NGIxZjNmNTg0YTUuc2V0Q29udGVudChodG1sX2I2Y2Y5NmZkNGY0YjQ0MTZiODIxOTMyYTQ0ODE1MWU2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2M3NTk3OGZlNTAxNjQ4NjZhYWZjYTliNTliZGJhNGJmLmJpbmRQb3B1cChwb3B1cF84OTNiYjJjYmE4Zjg0MTgwOWExOTk0YjFmM2Y1ODRhNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iN2I2ZWQ2ODFjMmM0YmFlOWRmOTU1ODI2MGU3YTY3NiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg0NzI0NjcwNDkxODEzLC03My43ODY0ODg0NTI2NzQxM10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80ZDYxMjg1OTEyMzM0NmZiYjViYTRiMTc0Y2EyZDI3OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84MzA0Y2YwMmIwNjE0MmVmOWJiYzRiMzkwN2MxNmI2NiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85MDhmNGUzMzA5M2M0YTc1Yjg5ZjIyZjE4NmY4YWQ5YyA9ICQoJzxkaXYgaWQ9Imh0bWxfOTA4ZjRlMzMwOTNjNGE3NWI4OWYyMmYxODZmOGFkOWMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNpdHkgSXNsYW5kPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84MzA0Y2YwMmIwNjE0MmVmOWJiYzRiMzkwN2MxNmI2Ni5zZXRDb250ZW50KGh0bWxfOTA4ZjRlMzMwOTNjNGE3NWI4OWYyMmYxODZmOGFkOWMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYjdiNmVkNjgxYzJjNGJhZTlkZjk1NTgyNjBlN2E2NzYuYmluZFBvcHVwKHBvcHVwXzgzMDRjZjAyYjA2MTQyZWY5YmJjNGIzOTA3YzE2YjY2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2E4ZDMwMDRlZmZiZTQ3ODhhNzBjZWQ2NTU3ZWE5NzhkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODcwMTg1MTY0OTc1MzI1LC03My44ODU1MTIxODQxOTEzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzRkNjEyODU5MTIzMzQ2ZmJiNWJhNGIxNzRjYTJkMjc5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzIxMzExNzI3YjFlNjQ1N2NiMTNmMjgyZTU1NzhhNGM2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzBlMGUyOWQ3ZTE5NzRkYzhhZWRmODcyNGIzOTBiYTkwID0gJCgnPGRpdiBpZD0iaHRtbF8wZTBlMjlkN2UxOTc0ZGM4YWVkZjg3MjRiMzkwYmE5MCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmVkZm9yZCBQYXJrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yMTMxMTcyN2IxZTY0NTdjYjEzZjI4MmU1NTc4YTRjNi5zZXRDb250ZW50KGh0bWxfMGUwZTI5ZDdlMTk3NGRjOGFlZGY4NzI0YjM5MGJhOTApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYThkMzAwNGVmZmJlNDc4OGE3MGNlZDY1NTdlYTk3OGQuYmluZFBvcHVwKHBvcHVwXzIxMzExNzI3YjFlNjQ1N2NiMTNmMjgyZTU1NzhhNGM2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2M4ZDA1YWIyMjQyMzRhZDQ5YmEyZDVhNjkyMmQwOTZjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODU1NzI3MDc3MTk2NjQsLTczLjkxMDQxNTk2MTkxMzFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNGQ2MTI4NTkxMjMzNDZmYmI1YmE0YjE3NGNhMmQyNzkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMmYzNWI5MmFhZmIwNGRiMmJjZTY5ZWUxYjk2MTFjNzkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTgwNGIwNzk2NGY4NGEwZTg2ZmY2OTE3NTdmMjAzNDUgPSAkKCc8ZGl2IGlkPSJodG1sX2U4MDRiMDc5NjRmODRhMGU4NmZmNjkxNzU3ZjIwMzQ1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Vbml2ZXJzaXR5IEhlaWdodHM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzJmMzViOTJhYWZiMDRkYjJiY2U2OWVlMWI5NjExYzc5LnNldENvbnRlbnQoaHRtbF9lODA0YjA3OTY0Zjg0YTBlODZmZjY5MTc1N2YyMDM0NSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jOGQwNWFiMjI0MjM0YWQ0OWJhMmQ1YTY5MjJkMDk2Yy5iaW5kUG9wdXAocG9wdXBfMmYzNWI5MmFhZmIwNGRiMmJjZTY5ZWUxYjk2MTFjNzkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzBlZTMwNDUzMGIwNDI2YzlmYWU3NWZhNThkODhiMDUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NDc4OTc5MjYwNjI3MSwtNzMuOTE5NjcxNTkxMTk1NjVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNGQ2MTI4NTkxMjMzNDZmYmI1YmE0YjE3NGNhMmQyNzkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWIzM2VmYjYzYzA3NGJlMzhiMzMwMWRjMWExZTg2OGMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOTVhNmE2MmQwMTY5NDRkZTgyNmU3YmEyNTBhODk5NjQgPSAkKCc8ZGl2IGlkPSJodG1sXzk1YTZhNjJkMDE2OTQ0ZGU4MjZlN2JhMjUwYTg5OTY0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Nb3JyaXMgSGVpZ2h0czwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYWIzM2VmYjYzYzA3NGJlMzhiMzMwMWRjMWExZTg2OGMuc2V0Q29udGVudChodG1sXzk1YTZhNjJkMDE2OTQ0ZGU4MjZlN2JhMjUwYTg5OTY0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2MwZWUzMDQ1MzBiMDQyNmM5ZmFlNzVmYTU4ZDg4YjA1LmJpbmRQb3B1cChwb3B1cF9hYjMzZWZiNjNjMDc0YmUzOGIzMzAxZGMxYTFlODY4Yyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83MGU3ODE0ZTFkMmE0ZjUxOTEwZTljNDNiMzE5YjEzNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg2MDk5Njc5NjM4NjU0LC03My44OTY0MjY1NTk4MTYyM10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80ZDYxMjg1OTEyMzM0NmZiYjViYTRiMTc0Y2EyZDI3OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83NWY4NzBmMTk5Yjg0ODBlYjJkNTIxOTNhOTlkNGJhOSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82MDU2NGNhNGY0MjI0MGNkOWJjY2JhMTY1ODhkM2ZmMSA9ICQoJzxkaXYgaWQ9Imh0bWxfNjA1NjRjYTRmNDIyNDBjZDliY2NiYTE2NTg4ZDNmZjEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZvcmRoYW08L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzc1Zjg3MGYxOTliODQ4MGViMmQ1MjE5M2E5OWQ0YmE5LnNldENvbnRlbnQoaHRtbF82MDU2NGNhNGY0MjI0MGNkOWJjY2JhMTY1ODhkM2ZmMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83MGU3ODE0ZTFkMmE0ZjUxOTEwZTljNDNiMzE5YjEzNC5iaW5kUG9wdXAocG9wdXBfNzVmODcwZjE5OWI4NDgwZWIyZDUyMTkzYTk5ZDRiYTkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNTZiNDVhNjEzZDY0NDQ3YWJlYWQ0ZDc4Yjk2YTc3YzcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NDI2OTYxNTc4NjA1MywtNzMuODg3MzU2MTc1MzIzMzhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNGQ2MTI4NTkxMjMzNDZmYmI1YmE0YjE3NGNhMmQyNzkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWEyYzVlYzczZTY0NGJhMWJkN2VmYTdhMGZhY2U5OWQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfODk5YTkyY2E5ZGRkNDdiYzk1MjE3M2YxNWVhYTc1MzMgPSAkKCc8ZGl2IGlkPSJodG1sXzg5OWE5MmNhOWRkZDQ3YmM5NTIxNzNmMTVlYWE3NTMzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5FYXN0IFRyZW1vbnQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2FhMmM1ZWM3M2U2NDRiYTFiZDdlZmE3YTBmYWNlOTlkLnNldENvbnRlbnQoaHRtbF84OTlhOTJjYTlkZGQ0N2JjOTUyMTczZjE1ZWFhNzUzMyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81NmI0NWE2MTNkNjQ0NDdhYmVhZDRkNzhiOTZhNzdjNy5iaW5kUG9wdXAocG9wdXBfYWEyYzVlYzczZTY0NGJhMWJkN2VmYTdhMGZhY2U5OWQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYWFjOTgwY2ViMDczNDM1ODllZDk3MDBiZTVlMDg0YmYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44Mzk0NzUwNTY3MjY1MywtNzMuODc3NzQ0NzQ5MTA1NDVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNGQ2MTI4NTkxMjMzNDZmYmI1YmE0YjE3NGNhMmQyNzkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODdjZWZjOTE0N2JhNGMwYWJjM2U2NWI5MjUyMTQ1ZTkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOTNlZDIxYjBlNjI4NGY2YzgxMDVmZTkxOWIxZjJlZDcgPSAkKCc8ZGl2IGlkPSJodG1sXzkzZWQyMWIwZTYyODRmNmM4MTA1ZmU5MTliMWYyZWQ3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5XZXN0IEZhcm1zPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84N2NlZmM5MTQ3YmE0YzBhYmMzZTY1YjkyNTIxNDVlOS5zZXRDb250ZW50KGh0bWxfOTNlZDIxYjBlNjI4NGY2YzgxMDVmZTkxOWIxZjJlZDcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYWFjOTgwY2ViMDczNDM1ODllZDk3MDBiZTVlMDg0YmYuYmluZFBvcHVwKHBvcHVwXzg3Y2VmYzkxNDdiYTRjMGFiYzNlNjViOTI1MjE0NWU5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzZmOTY2NWFlYTU4YjQ3ZmViYTliMjQxNTU3N2FlNjYxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODM2NjIzMDEwNzA2MDU2LC03My45MjYxMDIwOTM1ODEzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzRkNjEyODU5MTIzMzQ2ZmJiNWJhNGIxNzRjYTJkMjc5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzFmYmE0YzUyODQyMTRmMmE4OGRhZjMwOWQxYjAzOWI3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2ZlNmMyZDAxMDk2OTQ2ZmVhODcyNTYwYTNkZjk0NzZhID0gJCgnPGRpdiBpZD0iaHRtbF9mZTZjMmQwMTA5Njk0NmZlYTg3MjU2MGEzZGY5NDc2YSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SGlnaCAgQnJpZGdlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xZmJhNGM1Mjg0MjE0ZjJhODhkYWYzMDlkMWIwMzliNy5zZXRDb250ZW50KGh0bWxfZmU2YzJkMDEwOTY5NDZmZWE4NzI1NjBhM2RmOTQ3NmEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNmY5NjY1YWVhNThiNDdmZWJhOWIyNDE1NTc3YWU2NjEuYmluZFBvcHVwKHBvcHVwXzFmYmE0YzUyODQyMTRmMmE4OGRhZjMwOWQxYjAzOWI3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Q0ZTFlNjdhY2NkOTQwYTE5NmRjODcxOTU0N2JiZWZhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODE5NzU0MzcwNTk0OTM2LC03My45MDk0MjE2MDc1NzQzNl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80ZDYxMjg1OTEyMzM0NmZiYjViYTRiMTc0Y2EyZDI3OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81YWEzYmRmN2U5OWM0ZjNiYjk2YWMzMmYzMTgwNzhjNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xYWFhYmExZmFhZjU0NDU0YTg5YjhmYjUwMzMzNTUxNCA9ICQoJzxkaXYgaWQ9Imh0bWxfMWFhYWJhMWZhYWY1NDQ1NGE4OWI4ZmI1MDMzMzU1MTQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk1lbHJvc2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzVhYTNiZGY3ZTk5YzRmM2JiOTZhYzMyZjMxODA3OGM0LnNldENvbnRlbnQoaHRtbF8xYWFhYmExZmFhZjU0NDU0YTg5YjhmYjUwMzMzNTUxNCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kNGUxZTY3YWNjZDk0MGExOTZkYzg3MTk1NDdiYmVmYS5iaW5kUG9wdXAocG9wdXBfNWFhM2JkZjdlOTljNGYzYmI5NmFjMzJmMzE4MDc4YzQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZTJkM2YwZTQ3NWQ2NDBkM2JmY2Q2NTcxODFlY2EyMTggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44MDYyMzg3NDkzNTE3NywtNzMuOTE2MDk5ODc0ODc1NzVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNGQ2MTI4NTkxMjMzNDZmYmI1YmE0YjE3NGNhMmQyNzkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfY2QxOTYxMWE0Nzk0NDlmZDk5MzgzZGY1ZGRkOWUwMTYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOGM1YjgxNDU4MzhjNDI1YThhZDVhYjA3NzcxMDI0ZTEgPSAkKCc8ZGl2IGlkPSJodG1sXzhjNWI4MTQ1ODM4YzQyNWE4YWQ1YWIwNzc3MTAyNGUxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Nb3R0IEhhdmVuPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jZDE5NjExYTQ3OTQ0OWZkOTkzODNkZjVkZGQ5ZTAxNi5zZXRDb250ZW50KGh0bWxfOGM1YjgxNDU4MzhjNDI1YThhZDVhYjA3NzcxMDI0ZTEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZTJkM2YwZTQ3NWQ2NDBkM2JmY2Q2NTcxODFlY2EyMTguYmluZFBvcHVwKHBvcHVwX2NkMTk2MTFhNDc5NDQ5ZmQ5OTM4M2RmNWRkZDllMDE2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzE4NjU0MjM2Mzk0YzQ4ZWZiMDQ1ZGI0YmE5ZjZjOTU4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODAxNjYzNjI3NzU2MjA2LC03My45MTMyMjEzOTM4NjEzNV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80ZDYxMjg1OTEyMzM0NmZiYjViYTRiMTc0Y2EyZDI3OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84MjI0ZmY4NjhjYTM0ZDQzODFkMzIyM2I3OGVmYzNkNiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zMWYwMzk3NzFmNDI0Y2VlYjE1ZTcwZTU0NTNlNzdjYSA9ICQoJzxkaXYgaWQ9Imh0bWxfMzFmMDM5NzcxZjQyNGNlZWIxNWU3MGU1NDUzZTc3Y2EiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlBvcnQgTW9ycmlzPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84MjI0ZmY4NjhjYTM0ZDQzODFkMzIyM2I3OGVmYzNkNi5zZXRDb250ZW50KGh0bWxfMzFmMDM5NzcxZjQyNGNlZWIxNWU3MGU1NDUzZTc3Y2EpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMTg2NTQyMzYzOTRjNDhlZmIwNDVkYjRiYTlmNmM5NTguYmluZFBvcHVwKHBvcHVwXzgyMjRmZjg2OGNhMzRkNDM4MWQzMjIzYjc4ZWZjM2Q2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2I3MjZiYjI4MGFjOTQ5ODJiNTBiYTJkMTlhY2JjMjQ2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODE1MDk5MDQ1NDU4MjIsLTczLjg5NTc4ODIwMDk0NDZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNGQ2MTI4NTkxMjMzNDZmYmI1YmE0YjE3NGNhMmQyNzkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMjNlOGU1ZTU2ZjNkNDc3YjlhMWM0ZTc5YTk4MzRjMTYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZmE5MTdkNDExMTE3NDdmM2FjMjc0NjYyMGUyOWVhNzUgPSAkKCc8ZGl2IGlkPSJodG1sX2ZhOTE3ZDQxMTExNzQ3ZjNhYzI3NDY2MjBlMjllYTc1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Mb25nd29vZDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMjNlOGU1ZTU2ZjNkNDc3YjlhMWM0ZTc5YTk4MzRjMTYuc2V0Q29udGVudChodG1sX2ZhOTE3ZDQxMTExNzQ3ZjNhYzI3NDY2MjBlMjllYTc1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2I3MjZiYjI4MGFjOTQ5ODJiNTBiYTJkMTlhY2JjMjQ2LmJpbmRQb3B1cChwb3B1cF8yM2U4ZTVlNTZmM2Q0NzdiOWExYzRlNzlhOTgzNGMxNik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85NmMwODZiOTFjYWQ0MDAzODkxYWI5MzU2OTU5YWFhNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjgwOTcyOTg3OTM4NzA5LC03My44ODMzMTUwNTk1NTI5MV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80ZDYxMjg1OTEyMzM0NmZiYjViYTRiMTc0Y2EyZDI3OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jNGE1NGY0NjliODg0OTI1YjQxNzhlM2VmYjQ5ODAzYiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kNDRmNGJhZjllYjQ0NjgxYTNlMWNjMTBjNTQwMGY4MiA9ICQoJzxkaXYgaWQ9Imh0bWxfZDQ0ZjRiYWY5ZWI0NDY4MWEzZTFjYzEwYzU0MDBmODIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkh1bnRzIFBvaW50PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jNGE1NGY0NjliODg0OTI1YjQxNzhlM2VmYjQ5ODAzYi5zZXRDb250ZW50KGh0bWxfZDQ0ZjRiYWY5ZWI0NDY4MWEzZTFjYzEwYzU0MDBmODIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTZjMDg2YjkxY2FkNDAwMzg5MWFiOTM1Njk1OWFhYTYuYmluZFBvcHVwKHBvcHVwX2M0YTU0ZjQ2OWI4ODQ5MjViNDE3OGUzZWZiNDk4MDNiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzQ1YTg3MzliYTg3OTQ1YjhhODBhMTk4NTEzZTRhMGUwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODIzNTkxOTg1ODU1MzQsLTczLjkwMTUwNjQ4OTQzMDU5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzRkNjEyODU5MTIzMzQ2ZmJiNWJhNGIxNzRjYTJkMjc5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzMzYWYxZDhkYmY0NTQ4MWU4ODFkZDNmMGY5OGRkYzAwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzViNDQ1M2RkZWNjZTRiNzU4YzAzODA4YWEyYjUzY2NiID0gJCgnPGRpdiBpZD0iaHRtbF81YjQ0NTNkZGVjY2U0Yjc1OGMwMzgwOGFhMmI1M2NjYiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TW9ycmlzYW5pYTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzNhZjFkOGRiZjQ1NDgxZTg4MWRkM2YwZjk4ZGRjMDAuc2V0Q29udGVudChodG1sXzViNDQ1M2RkZWNjZTRiNzU4YzAzODA4YWEyYjUzY2NiKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzQ1YTg3MzliYTg3OTQ1YjhhODBhMTk4NTEzZTRhMGUwLmJpbmRQb3B1cChwb3B1cF8zM2FmMWQ4ZGJmNDU0ODFlODgxZGQzZjBmOThkZGMwMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xNWFmMmRiMGM5ZGU0MzM3YTNhMTA4MGE1Y2RkMmI2MiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjgyMTAxMjE5NzkxNDAxNSwtNzMuODY1NzQ2MDk1NTQ5MjRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNGQ2MTI4NTkxMjMzNDZmYmI1YmE0YjE3NGNhMmQyNzkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfY2IyMTdmNzNkNWRkNDg2NmE3YTJhMmI5ZDA3OTU4MTAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNDdmZmQ3M2JmMTkyNGE0MTlmOTFkNmM3MTI3YmUzZTYgPSAkKCc8ZGl2IGlkPSJodG1sXzQ3ZmZkNzNiZjE5MjRhNDE5ZjkxZDZjNzEyN2JlM2U2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Tb3VuZHZpZXc8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2NiMjE3ZjczZDVkZDQ4NjZhN2EyYTJiOWQwNzk1ODEwLnNldENvbnRlbnQoaHRtbF80N2ZmZDczYmYxOTI0YTQxOWY5MWQ2YzcxMjdiZTNlNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xNWFmMmRiMGM5ZGU0MzM3YTNhMTA4MGE1Y2RkMmI2Mi5iaW5kUG9wdXAocG9wdXBfY2IyMTdmNzNkNWRkNDg2NmE3YTJhMmI5ZDA3OTU4MTApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOGFmNzBmYWVmZjExNGU1OWI0YTQ2MmIyMGVmNjZkNjcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44MDY1NTExMjAwMzU4OSwtNzMuODU0MTQ0MTYxODkyNjZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNGQ2MTI4NTkxMjMzNDZmYmI1YmE0YjE3NGNhMmQyNzkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjEzZjQ1MWI0OWM2NDc2NmE3YjJkMWNmMjc3ZmJjOWMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMjBlYmU4ZTZjMGFlNGUzNDk1YjAzYzEyNzM0MzM0NmIgPSAkKCc8ZGl2IGlkPSJodG1sXzIwZWJlOGU2YzBhZTRlMzQ5NWIwM2MxMjczNDMzNDZiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DbGFzb24gUG9pbnQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2YxM2Y0NTFiNDljNjQ3NjZhN2IyZDFjZjI3N2ZiYzljLnNldENvbnRlbnQoaHRtbF8yMGViZThlNmMwYWU0ZTM0OTViMDNjMTI3MzQzMzQ2Yik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84YWY3MGZhZWZmMTE0ZTU5YjRhNDYyYjIwZWY2NmQ2Ny5iaW5kUG9wdXAocG9wdXBfZjEzZjQ1MWI0OWM2NDc2NmE3YjJkMWNmMjc3ZmJjOWMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYmM3NzBhYmY5YTEwNDVhMjgyY2RmNDk4ZmJiMDMyNTggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44MTUxMDkyNTgwNDAwNSwtNzMuODE2MzUwMDIxNTg0NDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNGQ2MTI4NTkxMjMzNDZmYmI1YmE0YjE3NGNhMmQyNzkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDBkOGEzNmNiOGI5NGNkMjkxYTkzMDBjNjJjNjI3NzIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDhmODhhYTVlZjRhNDdhMTg5MjVkMTA1NGZhODRjOTcgPSAkKCc8ZGl2IGlkPSJodG1sXzA4Zjg4YWE1ZWY0YTQ3YTE4OTI1ZDEwNTRmYTg0Yzk3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaHJvZ3MgTmVjazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZDBkOGEzNmNiOGI5NGNkMjkxYTkzMDBjNjJjNjI3NzIuc2V0Q29udGVudChodG1sXzA4Zjg4YWE1ZWY0YTQ3YTE4OTI1ZDEwNTRmYTg0Yzk3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2JjNzcwYWJmOWExMDQ1YTI4MmNkZjQ5OGZiYjAzMjU4LmJpbmRQb3B1cChwb3B1cF9kMGQ4YTM2Y2I4Yjk0Y2QyOTFhOTMwMGM2MmM2Mjc3Mik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84OGM2YTY5MDA1NjY0NDZmYTdiOTEyZTdlMTVhMzc3MyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg0NDI0NTkzNjk0NzM3NCwtNzMuODI0MDk5MjY3NTM4NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80ZDYxMjg1OTEyMzM0NmZiYjViYTRiMTc0Y2EyZDI3OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9kYTM4NmMxYmZiMmM0ZGQyYjAwZjljMmRmOTliMDkxOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hM2M5YzhmMTFjMmQ0MjA0ODExMTVlN2U2ZWQwYWNkNCA9ICQoJzxkaXYgaWQ9Imh0bWxfYTNjOWM4ZjExYzJkNDIwNDgxMTE1ZTdlNmVkMGFjZDQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNvdW50cnkgQ2x1YjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZGEzODZjMWJmYjJjNGRkMmIwMGY5YzJkZjk5YjA5MTguc2V0Q29udGVudChodG1sX2EzYzljOGYxMWMyZDQyMDQ4MTExNWU3ZTZlZDBhY2Q0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzg4YzZhNjkwMDU2NjQ0NmZhN2I5MTJlN2UxNWEzNzczLmJpbmRQb3B1cChwb3B1cF9kYTM4NmMxYmZiMmM0ZGQyYjAwZjljMmRmOTliMDkxOCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wNTY3ODM5YmM3NGQ0NTMyYjYzNzJkZDczMjczNjE0NiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjgzNzkzNzgyMjI2NzI4NiwtNzMuODU2MDAzMTA1MzU3ODNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNGQ2MTI4NTkxMjMzNDZmYmI1YmE0YjE3NGNhMmQyNzkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzQ3MmFlYjlkYjY1NDBkZWE3NzFkZTIxYTAyODRmYTMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTRlMWU3MDEyY2VjNGM1MWJlZTBmN2U0ZWQ1ZjQ1ODcgPSAkKCc8ZGl2IGlkPSJodG1sX2U0ZTFlNzAxMmNlYzRjNTFiZWUwZjdlNGVkNWY0NTg3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5QYXJrY2hlc3RlcjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzQ3MmFlYjlkYjY1NDBkZWE3NzFkZTIxYTAyODRmYTMuc2V0Q29udGVudChodG1sX2U0ZTFlNzAxMmNlYzRjNTFiZWUwZjdlNGVkNWY0NTg3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzA1Njc4MzliYzc0ZDQ1MzJiNjM3MmRkNzMyNzM2MTQ2LmJpbmRQb3B1cChwb3B1cF8zNDcyYWViOWRiNjU0MGRlYTc3MWRlMjFhMDI4NGZhMyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yNGY4OGE2MDFjNTU0NTEwYTFjYzVjN2EyZjhiNjgxNSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg0MDYxOTQ5NjQzMjcsLTczLjg0MjE5NDA3NjA0NDQ0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzRkNjEyODU5MTIzMzQ2ZmJiNWJhNGIxNzRjYTJkMjc5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2VlYmY1NDIxODZmYjQ4ZmNiNDAwNjM3Yzk4OTI2NWUzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzllYmNiNWNjOTJkOTQ2OThhZTFhZWFhZWE3ZWFkNjY2ID0gJCgnPGRpdiBpZD0iaHRtbF85ZWJjYjVjYzkyZDk0Njk4YWUxYWVhYWVhN2VhZDY2NiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V2VzdGNoZXN0ZXIgU3F1YXJlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lZWJmNTQyMTg2ZmI0OGZjYjQwMDYzN2M5ODkyNjVlMy5zZXRDb250ZW50KGh0bWxfOWViY2I1Y2M5MmQ5NDY5OGFlMWFlYWFlYTdlYWQ2NjYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMjRmODhhNjAxYzU1NDUxMGExY2M1YzdhMmY4YjY4MTUuYmluZFBvcHVwKHBvcHVwX2VlYmY1NDIxODZmYjQ4ZmNiNDAwNjM3Yzk4OTI2NWUzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzEyMmNhZmE3MzlhZTRlYjRiZDQ5MGQ4ZDQ3ZDAwZWM3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODQzNjA4NDcxMjQ3MTgsLTczLjg2NjI5OTE4MDc1NjFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNGQ2MTI4NTkxMjMzNDZmYmI1YmE0YjE3NGNhMmQyNzkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOTc2ZGVhNWEwYzY0NDgxMGEzMzlhODMwYTYzYzI2ZTAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYTAzNGUzMjA0MDQyNGMzM2EyMzExNWZhYjZmODMxYWQgPSAkKCc8ZGl2IGlkPSJodG1sX2EwMzRlMzIwNDA0MjRjMzNhMjMxMTVmYWI2ZjgzMWFkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5WYW4gTmVzdDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOTc2ZGVhNWEwYzY0NDgxMGEzMzlhODMwYTYzYzI2ZTAuc2V0Q29udGVudChodG1sX2EwMzRlMzIwNDA0MjRjMzNhMjMxMTVmYWI2ZjgzMWFkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzEyMmNhZmE3MzlhZTRlYjRiZDQ5MGQ4ZDQ3ZDAwZWM3LmJpbmRQb3B1cChwb3B1cF85NzZkZWE1YTBjNjQ0ODEwYTMzOWE4MzBhNjNjMjZlMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mZmRiZTdjMWQ1ZDI0MjE4YTZkODE1ZGEyYmJlOTFjZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg0NzU0OTA2MzUzNjMzNCwtNzMuODUwNDAxNzgwMzA0MjFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNGQ2MTI4NTkxMjMzNDZmYmI1YmE0YjE3NGNhMmQyNzkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWZjNzEwZTA2MWRiNDU2NTg5MGFjMTRiOGE4ZWExZjQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYjYxZTFkODY5MDBjNDlkZTg1MTA5M2E5OWE1MTQ3YWYgPSAkKCc8ZGl2IGlkPSJodG1sX2I2MWUxZDg2OTAwYzQ5ZGU4NTEwOTNhOTlhNTE0N2FmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Nb3JyaXMgUGFyazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYWZjNzEwZTA2MWRiNDU2NTg5MGFjMTRiOGE4ZWExZjQuc2V0Q29udGVudChodG1sX2I2MWUxZDg2OTAwYzQ5ZGU4NTEwOTNhOTlhNTE0N2FmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ZmZGJlN2MxZDVkMjQyMThhNmQ4MTVkYTJiYmU5MWNmLmJpbmRQb3B1cChwb3B1cF9hZmM3MTBlMDYxZGI0NTY1ODkwYWMxNGI4YThlYTFmNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83ZjJlZjU5YjE3ZTg0MWE3YjdjMzdlYzNjODEyMjMyZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg1NzI3NzEwMDczODk1LC03My44ODg0NTE5NjEzNDgwNF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80ZDYxMjg1OTEyMzM0NmZiYjViYTRiMTc0Y2EyZDI3OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8wMDZkNWFiZTQzNDI0NDcyYWExMjNhMmRiN2E1MzNmOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kZmU4Zjc5NmQ5NmI0MWNmODM0ODZmNGQ1N2MxNGRjMSA9ICQoJzxkaXYgaWQ9Imh0bWxfZGZlOGY3OTZkOTZiNDFjZjgzNDg2ZjRkNTdjMTRkYzEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJlbG1vbnQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzAwNmQ1YWJlNDM0MjQ0NzJhYTEyM2EyZGI3YTUzM2Y4LnNldENvbnRlbnQoaHRtbF9kZmU4Zjc5NmQ5NmI0MWNmODM0ODZmNGQ1N2MxNGRjMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83ZjJlZjU5YjE3ZTg0MWE3YjdjMzdlYzNjODEyMjMyZS5iaW5kUG9wdXAocG9wdXBfMDA2ZDVhYmU0MzQyNDQ3MmFhMTIzYTJkYjdhNTMzZjgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZjg2NDAzMDljNzI5NDI1MWFlZmJjMGYzOTlhMmE5NWIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44ODEzOTQ5NzcyNzA4NiwtNzMuOTE3MTkwNDgyMTAzOTNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNGQ2MTI4NTkxMjMzNDZmYmI1YmE0YjE3NGNhMmQyNzkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNzE5MzBhZDMzYjgyNDdlM2I2YjI1OGU3NmYyYjUxZjggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMzIyYTc4OTVlNGNkNGVkZWE3NDYxYmExZGI1MjVmODkgPSAkKCc8ZGl2IGlkPSJodG1sXzMyMmE3ODk1ZTRjZDRlZGVhNzQ2MWJhMWRiNTI1Zjg5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TcHV5dGVuIER1eXZpbDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNzE5MzBhZDMzYjgyNDdlM2I2YjI1OGU3NmYyYjUxZjguc2V0Q29udGVudChodG1sXzMyMmE3ODk1ZTRjZDRlZGVhNzQ2MWJhMWRiNTI1Zjg5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Y4NjQwMzA5YzcyOTQyNTFhZWZiYzBmMzk5YTJhOTViLmJpbmRQb3B1cChwb3B1cF83MTkzMGFkMzNiODI0N2UzYjZiMjU4ZTc2ZjJiNTFmOCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84ZDMzZWFmYWE4Nzc0OWYwYWY0ZGNjN2YyODhjMWY5NyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjkwODU0MjgyOTUwNjY2LC03My45MDQ1MzA1NDkwODkyN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80ZDYxMjg1OTEyMzM0NmZiYjViYTRiMTc0Y2EyZDI3OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83MzlkNjU4ZjU5ZmQ0ZTZiYWRlNDE4YzViZDdjYTU2NCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yOGJiYTQ5YjdhMWI0MzViOTUyYzU0MDQ1ODM1NjdhOCA9ICQoJzxkaXYgaWQ9Imh0bWxfMjhiYmE0OWI3YTFiNDM1Yjk1MmM1NDA0NTgzNTY3YTgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5vcnRoIFJpdmVyZGFsZTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNzM5ZDY1OGY1OWZkNGU2YmFkZTQxOGM1YmQ3Y2E1NjQuc2V0Q29udGVudChodG1sXzI4YmJhNDliN2ExYjQzNWI5NTJjNTQwNDU4MzU2N2E4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzhkMzNlYWZhYTg3NzQ5ZjBhZjRkY2M3ZjI4OGMxZjk3LmJpbmRQb3B1cChwb3B1cF83MzlkNjU4ZjU5ZmQ0ZTZiYWRlNDE4YzViZDdjYTU2NCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84MGQ3YmJjMjU0MGU0ZWMyYmIxODg4ZmFhYjBiZDhkNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg1MDY0MTQwOTQwMzM1LC03My44MzIwNzM3ODI0MDQ3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzRkNjEyODU5MTIzMzQ2ZmJiNWJhNGIxNzRjYTJkMjc5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzVkYWQ3MjYzMjk4YzQxZTA5ZmQwYWZkNDQ1Yjk4NzI3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzZlZmE3MzIyYThjYTRkNjA4YTY3MWE2YmE1NTczMzA4ID0gJCgnPGRpdiBpZD0iaHRtbF82ZWZhNzMyMmE4Y2E0ZDYwOGE2NzFhNmJhNTU3MzMwOCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UGVsaGFtIEJheTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNWRhZDcyNjMyOThjNDFlMDlmZDBhZmQ0NDViOTg3Mjcuc2V0Q29udGVudChodG1sXzZlZmE3MzIyYThjYTRkNjA4YTY3MWE2YmE1NTczMzA4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzgwZDdiYmMyNTQwZTRlYzJiYjE4ODhmYWFiMGJkOGQ2LmJpbmRQb3B1cChwb3B1cF81ZGFkNzI2MzI5OGM0MWUwOWZkMGFmZDQ0NWI5ODcyNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lYWQwOGZmOWQxMDA0OWMzOTA1MzNlZjU4OTY3ZTY0MSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjgyNjU3OTUxNjg2OTIyLC03My44MjYyMDI3NTk5NDA3M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80ZDYxMjg1OTEyMzM0NmZiYjViYTRiMTc0Y2EyZDI3OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zNmVhN2NhNmVhMDE0YmRkYmUwMDVlMDcwMWEyZTc3MCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80MmYxMDRhNjIxYjA0YTc0OTA4NDY5YjMzNjVjN2NmNCA9ICQoJzxkaXYgaWQ9Imh0bWxfNDJmMTA0YTYyMWIwNGE3NDkwODQ2OWIzMzY1YzdjZjQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlNjaHV5bGVydmlsbGU8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzM2ZWE3Y2E2ZWEwMTRiZGRiZTAwNWUwNzAxYTJlNzcwLnNldENvbnRlbnQoaHRtbF80MmYxMDRhNjIxYjA0YTc0OTA4NDY5YjMzNjVjN2NmNCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lYWQwOGZmOWQxMDA0OWMzOTA1MzNlZjU4OTY3ZTY0MS5iaW5kUG9wdXAocG9wdXBfMzZlYTdjYTZlYTAxNGJkZGJlMDA1ZTA3MDFhMmU3NzApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfY2IxNzVkZDAwYTNkNDgwY2IyYTY5YjE5ZDQxYmQzYjkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44MjE5ODYxMTgxNjM0OTQsLTczLjgxMzg4NTE0NDI4NjE5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzRkNjEyODU5MTIzMzQ2ZmJiNWJhNGIxNzRjYTJkMjc5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzRlN2I5MTEzOGQ1NTQxMjZhNDgxZDVhNzkxYThiZDRjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2JlNzVlZjdkNWFkMTQ4N2M4M2U3ZDFlN2Q1OTNkYzA5ID0gJCgnPGRpdiBpZD0iaHRtbF9iZTc1ZWY3ZDVhZDE0ODdjODNlN2QxZTdkNTkzZGMwOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RWRnZXdhdGVyIFBhcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzRlN2I5MTEzOGQ1NTQxMjZhNDgxZDVhNzkxYThiZDRjLnNldENvbnRlbnQoaHRtbF9iZTc1ZWY3ZDVhZDE0ODdjODNlN2QxZTdkNTkzZGMwOSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jYjE3NWRkMDBhM2Q0ODBjYjJhNjliMTlkNDFiZDNiOS5iaW5kUG9wdXAocG9wdXBfNGU3YjkxMTM4ZDU1NDEyNmE0ODFkNWE3OTFhOGJkNGMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOTQyYTExN2Y0NzhjNDIwMGFmNWNiMWVlMTk2NjFhOWUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44MTkwMTQzNzY5ODgzMTQsLTczLjg0ODAyNzI5NTgyNzM1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzRkNjEyODU5MTIzMzQ2ZmJiNWJhNGIxNzRjYTJkMjc5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzMwYTcxMjg5ZGM5NDQ1ZTM5YmUwOGQ2YzM4NDgzZGI4ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzJkZTE1NjI3YTZmOTQxODg5Y2VjOTAyMWExMGQwYTIxID0gJCgnPGRpdiBpZD0iaHRtbF8yZGUxNTYyN2E2Zjk0MTg4OWNlYzkwMjFhMTBkMGEyMSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2FzdGxlIEhpbGw8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzMwYTcxMjg5ZGM5NDQ1ZTM5YmUwOGQ2YzM4NDgzZGI4LnNldENvbnRlbnQoaHRtbF8yZGUxNTYyN2E2Zjk0MTg4OWNlYzkwMjFhMTBkMGEyMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85NDJhMTE3ZjQ3OGM0MjAwYWY1Y2IxZWUxOTY2MWE5ZS5iaW5kUG9wdXAocG9wdXBfMzBhNzEyODlkYzk0NDVlMzliZTA4ZDZjMzg0ODNkYjgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTMwYjY0NzNkMjNjNGE3OWI0YzA0MzZhNWRhMDgxNmQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NzEzNzA3ODE5MjM3MSwtNzMuODYzMzIzNjE2NTI3NzddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNGQ2MTI4NTkxMjMzNDZmYmI1YmE0YjE3NGNhMmQyNzkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMjQ3MjRiN2I4ZjIyNGFkMGJkN2RhMjVmZmNjYTlkMmUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMTA3ZDlhMzQ5NGQwNGM0YTk4YmExNDJmZTdjMDI2ZmYgPSAkKCc8ZGl2IGlkPSJodG1sXzEwN2Q5YTM0OTRkMDRjNGE5OGJhMTQyZmU3YzAyNmZmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5PbGludmlsbGU8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzI0NzI0YjdiOGYyMjRhZDBiZDdkYTI1ZmZjY2E5ZDJlLnNldENvbnRlbnQoaHRtbF8xMDdkOWEzNDk0ZDA0YzRhOThiYTE0MmZlN2MwMjZmZik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hMzBiNjQ3M2QyM2M0YTc5YjRjMDQzNmE1ZGEwODE2ZC5iaW5kUG9wdXAocG9wdXBfMjQ3MjRiN2I4ZjIyNGFkMGJkN2RhMjVmZmNjYTlkMmUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZTA1Njk1Y2ExMDFiNDU3MTg0OGY5MWYyMmVjODYxOGYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NjI5NjU2MjQ3Nzk5OCwtNzMuODQxNjExOTQ4MzEyMjNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNGQ2MTI4NTkxMjMzNDZmYmI1YmE0YjE3NGNhMmQyNzkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMjZmZThmZGYzYTQ4NGVkY2FjNGE0N2RiMTNiOGEwZDQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYjEwZWJlNTIwZWFlNDI5MmI2MjNhMDZkMWVkZDAwMzkgPSAkKCc8ZGl2IGlkPSJodG1sX2IxMGViZTUyMGVhZTQyOTJiNjIzYTA2ZDFlZGQwMDM5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5QZWxoYW0gR2FyZGVuczwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMjZmZThmZGYzYTQ4NGVkY2FjNGE0N2RiMTNiOGEwZDQuc2V0Q29udGVudChodG1sX2IxMGViZTUyMGVhZTQyOTJiNjIzYTA2ZDFlZGQwMDM5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2UwNTY5NWNhMTAxYjQ1NzE4NDhmOTFmMjJlYzg2MThmLmJpbmRQb3B1cChwb3B1cF8yNmZlOGZkZjNhNDg0ZWRjYWM0YTQ3ZGIxM2I4YTBkNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83YzYyYzRiMzI3NGE0ZmVhYTg2ODBiMWEwM2E3OTFiNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjgzNDI4MzgwNzMzODUxLC03My45MTU1ODk0MTc3MzQ0NF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80ZDYxMjg1OTEyMzM0NmZiYjViYTRiMTc0Y2EyZDI3OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zYzE0ZGFlMDhjNTk0NzNiYTFiYjNkMzZiMGU1ZjM5MSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82OThlMjQzMjk3YWI0MmNlYWI0NjE4OTVjOWYzYjdhMSA9ICQoJzxkaXYgaWQ9Imh0bWxfNjk4ZTI0MzI5N2FiNDJjZWFiNDYxODk1YzlmM2I3YTEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNvbmNvdXJzZTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfM2MxNGRhZTA4YzU5NDczYmExYmIzZDM2YjBlNWYzOTEuc2V0Q29udGVudChodG1sXzY5OGUyNDMyOTdhYjQyY2VhYjQ2MTg5NWM5ZjNiN2ExKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzdjNjJjNGIzMjc0YTRmZWFhODY4MGIxYTAzYTc5MWI2LmJpbmRQb3B1cChwb3B1cF8zYzE0ZGFlMDhjNTk0NzNiYTFiYjNkMzZiMGU1ZjM5MSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wYmI5MjEwNDc5NWQ0YTA4ODg4MGVhN2Q0Y2E0NzJjMCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjgyOTc3NDI5Nzg3MTYxLC03My44NTA1MzUyNDQ1MTkzNV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80ZDYxMjg1OTEyMzM0NmZiYjViYTRiMTc0Y2EyZDI3OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mZGZjNGVkMmU2M2Q0MWVlYjcyOGY5MjcwMGQwNzEyZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82ZTllOTI0NzU2YTY0MDNjOWNmYzQ4ZmY2NGQ2ODFmYyA9ICQoJzxkaXYgaWQ9Imh0bWxfNmU5ZTkyNDc1NmE2NDAzYzljZmM0OGZmNjRkNjgxZmMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlVuaW9ucG9ydDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZmRmYzRlZDJlNjNkNDFlZWI3MjhmOTI3MDBkMDcxMmQuc2V0Q29udGVudChodG1sXzZlOWU5MjQ3NTZhNjQwM2M5Y2ZjNDhmZjY0ZDY4MWZjKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzBiYjkyMTA0Nzk1ZDRhMDg4ODgwZWE3ZDRjYTQ3MmMwLmJpbmRQb3B1cChwb3B1cF9mZGZjNGVkMmU2M2Q0MWVlYjcyOGY5MjcwMGQwNzEyZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mMDc1Zjc5OWMyNDY0MjYyYmVkMTY0MWM5ZjA0YzNkMiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg4NDU2MTMwMzAzNzMyLC03My44NDgwODI3MTg3NzE2OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80ZDYxMjg1OTEyMzM0NmZiYjViYTRiMTc0Y2EyZDI3OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jMDY3ZWNmMTJmM2Y0NDk0YjA3ODkzMGNjOTY0YjY0YiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yZTRkMzc3MWVkNmE0OTAzODM3ZjA3NTllZWU1MTYyYiA9ICQoJzxkaXYgaWQ9Imh0bWxfMmU0ZDM3NzFlZDZhNDkwMzgzN2YwNzU5ZWVlNTE2MmIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVkZW53YWxkPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jMDY3ZWNmMTJmM2Y0NDk0YjA3ODkzMGNjOTY0YjY0Yi5zZXRDb250ZW50KGh0bWxfMmU0ZDM3NzFlZDZhNDkwMzgzN2YwNzU5ZWVlNTE2MmIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZjA3NWY3OTljMjQ2NDI2MmJlZDE2NDFjOWYwNGMzZDIuYmluZFBvcHVwKHBvcHVwX2MwNjdlY2YxMmYzZjQ0OTRiMDc4OTMwY2M5NjRiNjRiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2UyNzcxZjVjODBhYzQ0ZWRhNWFlY2QyMzUyOWM0NDFhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODMxNDI4MzQxNjE1NDgsLTczLjkwMTE5OTAzMzg3NjY3XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzRkNjEyODU5MTIzMzQ2ZmJiNWJhNGIxNzRjYTJkMjc5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzUyMzA1YzA5NjkxZDRmYWY4NGVhZDE1YTFlMGY4ZDBhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzM2MGQwNzZkNmJkYzQ4NzRiYTBjZDE0NzMyYzMzMTcxID0gJCgnPGRpdiBpZD0iaHRtbF8zNjBkMDc2ZDZiZGM0ODc0YmEwY2QxNDczMmMzMzE3MSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2xhcmVtb250IFZpbGxhZ2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzUyMzA1YzA5NjkxZDRmYWY4NGVhZDE1YTFlMGY4ZDBhLnNldENvbnRlbnQoaHRtbF8zNjBkMDc2ZDZiZGM0ODc0YmEwY2QxNDczMmMzMzE3MSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lMjc3MWY1YzgwYWM0NGVkYTVhZWNkMjM1MjljNDQxYS5iaW5kUG9wdXAocG9wdXBfNTIzMDVjMDk2OTFkNGZhZjg0ZWFkMTVhMWUwZjhkMGEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNjZjMmZiNDEzNDMwNDBkNDk5ODU3ZTRlNjhhMGVhZTAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44MjQ3ODA0OTA4NDI5MDUsLTczLjkxNTg0NjUyNzU5MDA5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzRkNjEyODU5MTIzMzQ2ZmJiNWJhNGIxNzRjYTJkMjc5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzZiMGRjYTA0NWVmOTRiODM5MWE4MmJmYmM2ZmVkOTc2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzUxMTUwMGE5MDc2ODRlOTRhYzllNWNhZjdjMTJhOWZmID0gJCgnPGRpdiBpZD0iaHRtbF81MTE1MDBhOTA3Njg0ZTk0YWM5ZTVjYWY3YzEyYTlmZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q29uY291cnNlIFZpbGxhZ2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzZiMGRjYTA0NWVmOTRiODM5MWE4MmJmYmM2ZmVkOTc2LnNldENvbnRlbnQoaHRtbF81MTE1MDBhOTA3Njg0ZTk0YWM5ZTVjYWY3YzEyYTlmZik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82NmMyZmI0MTM0MzA0MGQ0OTk4NTdlNGU2OGEwZWFlMC5iaW5kUG9wdXAocG9wdXBfNmIwZGNhMDQ1ZWY5NGI4MzkxYTgyYmZiYzZmZWQ5NzYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOTEyNDgwMGEwMjU3NDkxODk3MDIxNDBjOWZlOGQ1ZGIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NDM4MjYxNzY3MTY1NCwtNzMuOTE2NTU1NTE5NjQ0MTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNGQ2MTI4NTkxMjMzNDZmYmI1YmE0YjE3NGNhMmQyNzkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWE5NzM0MDA3YTc4NDI2OWJiYzg1OTYyZDlmZjhjOTggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMTk2MDhkZWQwODg5NDVhMWI1YWE4NTU2NWI4NGJkZmYgPSAkKCc8ZGl2IGlkPSJodG1sXzE5NjA4ZGVkMDg4OTQ1YTFiNWFhODU1NjViODRiZGZmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Nb3VudCBFZGVuPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hYTk3MzQwMDdhNzg0MjY5YmJjODU5NjJkOWZmOGM5OC5zZXRDb250ZW50KGh0bWxfMTk2MDhkZWQwODg5NDVhMWI1YWE4NTU2NWI4NGJkZmYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTEyNDgwMGEwMjU3NDkxODk3MDIxNDBjOWZlOGQ1ZGIuYmluZFBvcHVwKHBvcHVwX2FhOTczNDAwN2E3ODQyNjliYmM4NTk2MmQ5ZmY4Yzk4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2I1MzU5Yzg5ZTRhZDQxNGRiNzZlN2RlNTY5NmI5ZjJmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODQ4ODQxNjA3MjQ2NjUsLTczLjkwODI5OTMwODgxOTg4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzRkNjEyODU5MTIzMzQ2ZmJiNWJhNGIxNzRjYTJkMjc5KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzJkOTZkZmRmNGU2YzQ1MzZhODRjY2ZmYzMyZjIxZjQ3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzgwYjE0NDUyMmVkNzRlMjdhYzQ4Y2IzYWU1ZDVlN2E1ID0gJCgnPGRpdiBpZD0iaHRtbF84MGIxNDQ1MjJlZDc0ZTI3YWM0OGNiM2FlNWQ1ZTdhNSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+TW91bnQgSG9wZTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMmQ5NmRmZGY0ZTZjNDUzNmE4NGNjZmZjMzJmMjFmNDcuc2V0Q29udGVudChodG1sXzgwYjE0NDUyMmVkNzRlMjdhYzQ4Y2IzYWU1ZDVlN2E1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2I1MzU5Yzg5ZTRhZDQxNGRiNzZlN2RlNTY5NmI5ZjJmLmJpbmRQb3B1cChwb3B1cF8yZDk2ZGZkZjRlNmM0NTM2YTg0Y2NmZmMzMmYyMWY0Nyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80N2ExZGViYmUyNDU0NDc4ODA2YjkzNGJkZjE0N2Y2ZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg1MjcyMjk3NjMzMDE3LC03My44NjE3MjU3NzU1NTExNV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80ZDYxMjg1OTEyMzM0NmZiYjViYTRiMTc0Y2EyZDI3OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zMTAxMjhmMmEwMzU0ZmUyODdlM2Q5MTQ5M2M3NWEwNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80MzQ5OGUwMjFiODU0OGQzYjY0YmRkNGRiMDFjOTljMiA9ICQoJzxkaXYgaWQ9Imh0bWxfNDM0OThlMDIxYjg1NDhkM2I2NGJkZDRkYjAxYzk5YzIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJyb254ZGFsZTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzEwMTI4ZjJhMDM1NGZlMjg3ZTNkOTE0OTNjNzVhMDQuc2V0Q29udGVudChodG1sXzQzNDk4ZTAyMWI4NTQ4ZDNiNjRiZGQ0ZGIwMWM5OWMyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzQ3YTFkZWJiZTI0NTQ0Nzg4MDZiOTM0YmRmMTQ3ZjZkLmJpbmRQb3B1cChwb3B1cF8zMTAxMjhmMmEwMzU0ZmUyODdlM2Q5MTQ5M2M3NWEwNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83YTE1MGEzYzJmYTU0NGMwYTllMDIzMjVjODM5ZDUzMiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg2NTc4Nzg3ODAyOTgyLC03My44NTkzMTg2MzIyMTY0N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF80ZDYxMjg1OTEyMzM0NmZiYjViYTRiMTc0Y2EyZDI3OSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yNWNkN2NkMjEwYzI0ZTQ4ODljZTVmMGY5Y2Y1MTMwOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mYTg3ZWUzNTEwNmE0MzQ5ODI2Y2M4NGU3MjFjOTk3MSA9ICQoJzxkaXYgaWQ9Imh0bWxfZmE4N2VlMzUxMDZhNDM0OTgyNmNjODRlNzIxYzk5NzEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFsbGVydG9uPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yNWNkN2NkMjEwYzI0ZTQ4ODljZTVmMGY5Y2Y1MTMwOC5zZXRDb250ZW50KGh0bWxfZmE4N2VlMzUxMDZhNDM0OTgyNmNjODRlNzIxYzk5NzEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfN2ExNTBhM2MyZmE1NDRjMGE5ZTAyMzI1YzgzOWQ1MzIuYmluZFBvcHVwKHBvcHVwXzI1Y2Q3Y2QyMTBjMjRlNDg4OWNlNWYwZjljZjUxMzA4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2MxNmVmZDY5YWE2ZDQ3NzE4NzY2MjQ4MTNiOGQzODI5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODcwMzkyMzkxNDE0NywtNzMuOTAxNTIyNjQ1MTMxNDRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNGQ2MTI4NTkxMjMzNDZmYmI1YmE0YjE3NGNhMmQyNzkpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjgxMmYxNGQ4MzJkNDBjYmJmMjlhMTYzMzc2NTRhNTcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNDM0ZDEwNzg4NzM2NDhjMmFkN2QwNTRjNjMxZjZlYWYgPSAkKCc8ZGl2IGlkPSJodG1sXzQzNGQxMDc4ODczNjQ4YzJhZDdkMDU0YzYzMWY2ZWFmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5LaW5nc2JyaWRnZSBIZWlnaHRzPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82ODEyZjE0ZDgzMmQ0MGNiYmYyOWExNjMzNzY1NGE1Ny5zZXRDb250ZW50KGh0bWxfNDM0ZDEwNzg4NzM2NDhjMmFkN2QwNTRjNjMxZjZlYWYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzE2ZWZkNjlhYTZkNDc3MTg3NjYyNDgxM2I4ZDM4MjkuYmluZFBvcHVwKHBvcHVwXzY4MTJmMTRkODMyZDQwY2JiZjI5YTE2MzM3NjU0YTU3KTsKCiAgICAgICAgICAgIAogICAgICAgIAo8L3NjcmlwdD4= onload="this.contentDocument.open();this.contentDocument.write(atob(this.getAttribute('data-html')));this.contentDocument.close();" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python
CLIENT_ID = 'XOMNN5V4YTDAU4HRS1NHJQMW5IYKWCWXXGCE2ZNPW4NKNU3O' # your Foursquare ID
CLIENT_SECRET = 'VMCFJQKYJT3TFKSLNMJNXNEC3EDSSLWGHUR5B3QUCODZ1K1L' # your Foursquare Secret
VERSION = '20180604'
LIMIT = 30
print('Your credentails:')
print('CLIENT_ID: ' + CLIENT_ID)
print('CLIENT_SECRET:' + CLIENT_SECRET)
```

    Your credentails:
    CLIENT_ID: XOMNN5V4YTDAU4HRS1NHJQMW5IYKWCWXXGCE2ZNPW4NKNU3O
    CLIENT_SECRET:VMCFJQKYJT3TFKSLNMJNXNEC3EDSSLWGHUR5B3QUCODZ1K1L



```python
print ('Interest of type of restaurant is Chinese or Italian, analyzing current population of restaurants')
```

    Interest of type of restaurant is Chinese or Italian, analyzing current population of restaurants



```python
address = 'Bronx Zoo, NY'

geolocator = Nominatim(user_agent="foursquare_agent")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print(latitude, longitude)
```

    40.84930445 -73.87713791835206



```python
search_query = 'Chinese'
radius = 800
print(search_query + ' .... OK!')
```

    Chinese .... OK!



```python
print ('Using Foursquare to gather restaurant information within 800 radius')
```

    Using Foursquare to gather restaurant information within 800 radius



```python
url = 'https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&ll={},{}&v={}&query={}&radius={}&limit={}'.format(CLIENT_ID, CLIENT_SECRET, latitude, longitude, VERSION, search_query, radius, LIMIT)
url
```




    'https://api.foursquare.com/v2/venues/search?client_id=XOMNN5V4YTDAU4HRS1NHJQMW5IYKWCWXXGCE2ZNPW4NKNU3O&client_secret=VMCFJQKYJT3TFKSLNMJNXNEC3EDSSLWGHUR5B3QUCODZ1K1L&ll=40.84930445,-73.87713791835206&v=20180604&query=Chinese&radius=800&limit=30'




```python
results = requests.get(url).json()
results
```




    {'meta': {'code': 200, 'requestId': '5fb4bd342158a34dc8b9790b'},
     'response': {'venues': [{'id': '4ed4326f2c5b695abedee221',
        'name': 'Lung Fong Chinese Restaurant',
        'location': {'address': '870 E 180th St, Bronx, NY 10460',
         'lat': 40.845089,
         'lng': -73.88315300000001,
         'labeledLatLngs': [{'label': 'display',
           'lat': 40.845089,
           'lng': -73.88315300000001},
          {'label': 'entrance', 'lat': 40.845168, 'lng': -73.883094}],
         'distance': 690,
         'postalCode': '10460',
         'cc': 'US',
         'city': 'Bronx',
         'state': 'NY',
         'country': 'United States',
         'formattedAddress': ['870 E 180th St, Bronx, NY 10460',
          'Bronx, NY 10460',
          'United States']},
        'categories': [{'id': '4bf58dd8d48988d145941735',
          'name': 'Chinese Restaurant',
          'pluralName': 'Chinese Restaurants',
          'shortName': 'Chinese',
          'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/asian_',
           'suffix': '.png'},
          'primary': True}],
        'referralId': 'v-1605680436',
        'hasPerk': False},
       {'id': '4f32777919836c91c7da98c4',
        'name': 'Dragon Sea Chinese Restaurant',
        'location': {'address': '2302 Crotona Ave',
         'lat': 40.8519,
         'lng': -73.884394,
         'labeledLatLngs': [{'label': 'display',
           'lat': 40.8519,
           'lng': -73.884394}],
         'distance': 675,
         'postalCode': '10458',
         'cc': 'US',
         'city': 'Bronx',
         'state': 'NY',
         'country': 'United States',
         'formattedAddress': ['2302 Crotona Ave',
          'Bronx, NY 10458',
          'United States']},
        'categories': [{'id': '4bf58dd8d48988d1ce941735',
          'name': 'Seafood Restaurant',
          'pluralName': 'Seafood Restaurants',
          'shortName': 'Seafood',
          'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/seafood_',
           'suffix': '.png'},
          'primary': True}],
        'referralId': 'v-1605680436',
        'hasPerk': False},
       {'id': '4ea229f77ee52a35dcca6aa5',
        'name': '653 Lucky Chinese Restaurant',
        'location': {'address': '653 E 182nd St',
         'lat': 40.851396,
         'lng': -73.888245,
         'labeledLatLngs': [{'label': 'display',
           'lat': 40.851396,
           'lng': -73.888245},
          {'label': 'entrance', 'lat': 40.851234, 'lng': -73.888328}],
         'distance': 963,
         'postalCode': '10457',
         'cc': 'US',
         'city': 'Bronx',
         'state': 'NY',
         'country': 'United States',
         'formattedAddress': ['653 E 182nd St',
          'Bronx, NY 10457',
          'United States']},
        'categories': [{'id': '4bf58dd8d48988d142941735',
          'name': 'Asian Restaurant',
          'pluralName': 'Asian Restaurants',
          'shortName': 'Asian',
          'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/asian_',
           'suffix': '.png'},
          'primary': True}],
        'referralId': 'v-1605680436',
        'hasPerk': False},
       {'id': '4f4348da19834bc91f55b4f0',
        'name': 'Lucky Chinese Restaurant',
        'location': {'address': '653 E 182nd St',
         'lat': 40.851396,
         'lng': -73.888245,
         'labeledLatLngs': [{'label': 'display',
           'lat': 40.851396,
           'lng': -73.888245},
          {'label': 'entrance', 'lat': 40.851234, 'lng': -73.888328}],
         'distance': 963,
         'postalCode': '10457',
         'cc': 'US',
         'city': 'Bronx',
         'state': 'NY',
         'country': 'United States',
         'formattedAddress': ['653 E 182nd St',
          'Bronx, NY 10457',
          'United States']},
        'categories': [{'id': '4bf58dd8d48988d145941735',
          'name': 'Chinese Restaurant',
          'pluralName': 'Chinese Restaurants',
          'shortName': 'Chinese',
          'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/asian_',
           'suffix': '.png'},
          'primary': True}],
        'referralId': 'v-1605680436',
        'hasPerk': False}]}}




```python
print ('Chinese restaurant results obtained')
```

    Chinese restaurant results obtained



```python
# assign relevant part of JSON to venues
venues = results['response']['venues']

# tranform venues into a dataframe
dataframe = json_normalize(venues)
dataframe.head()
```

    /home/jupyterlab/conda/envs/python/lib/python3.6/site-packages/ipykernel_launcher.py:5: FutureWarning: pandas.io.json.json_normalize is deprecated, use pandas.json_normalize instead
      """





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>categories</th>
      <th>referralId</th>
      <th>hasPerk</th>
      <th>location.address</th>
      <th>location.lat</th>
      <th>location.lng</th>
      <th>location.labeledLatLngs</th>
      <th>location.distance</th>
      <th>location.postalCode</th>
      <th>location.cc</th>
      <th>location.city</th>
      <th>location.state</th>
      <th>location.country</th>
      <th>location.formattedAddress</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4ed4326f2c5b695abedee221</td>
      <td>Lung Fong Chinese Restaurant</td>
      <td>[{'id': '4bf58dd8d48988d145941735', 'name': 'C...</td>
      <td>v-1605680436</td>
      <td>False</td>
      <td>870 E 180th St, Bronx, NY 10460</td>
      <td>40.845089</td>
      <td>-73.883153</td>
      <td>[{'label': 'display', 'lat': 40.845089, 'lng':...</td>
      <td>690</td>
      <td>10460</td>
      <td>US</td>
      <td>Bronx</td>
      <td>NY</td>
      <td>United States</td>
      <td>[870 E 180th St, Bronx, NY 10460, Bronx, NY 10...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4f32777919836c91c7da98c4</td>
      <td>Dragon Sea Chinese Restaurant</td>
      <td>[{'id': '4bf58dd8d48988d1ce941735', 'name': 'S...</td>
      <td>v-1605680436</td>
      <td>False</td>
      <td>2302 Crotona Ave</td>
      <td>40.851900</td>
      <td>-73.884394</td>
      <td>[{'label': 'display', 'lat': 40.8519, 'lng': -...</td>
      <td>675</td>
      <td>10458</td>
      <td>US</td>
      <td>Bronx</td>
      <td>NY</td>
      <td>United States</td>
      <td>[2302 Crotona Ave, Bronx, NY 10458, United Sta...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4ea229f77ee52a35dcca6aa5</td>
      <td>653 Lucky Chinese Restaurant</td>
      <td>[{'id': '4bf58dd8d48988d142941735', 'name': 'A...</td>
      <td>v-1605680436</td>
      <td>False</td>
      <td>653 E 182nd St</td>
      <td>40.851396</td>
      <td>-73.888245</td>
      <td>[{'label': 'display', 'lat': 40.851396, 'lng':...</td>
      <td>963</td>
      <td>10457</td>
      <td>US</td>
      <td>Bronx</td>
      <td>NY</td>
      <td>United States</td>
      <td>[653 E 182nd St, Bronx, NY 10457, United States]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4f4348da19834bc91f55b4f0</td>
      <td>Lucky Chinese Restaurant</td>
      <td>[{'id': '4bf58dd8d48988d145941735', 'name': 'C...</td>
      <td>v-1605680436</td>
      <td>False</td>
      <td>653 E 182nd St</td>
      <td>40.851396</td>
      <td>-73.888245</td>
      <td>[{'label': 'display', 'lat': 40.851396, 'lng':...</td>
      <td>963</td>
      <td>10457</td>
      <td>US</td>
      <td>Bronx</td>
      <td>NY</td>
      <td>United States</td>
      <td>[653 E 182nd St, Bronx, NY 10457, United States]</td>
    </tr>
  </tbody>
</table>
</div>




```python
print ('Formatting into categories in dataframe columns, so results easily analyzed')
```

    Formatting into categories in dataframe columns, so results easily analyzed



```python
# keep only columns that include venue name, and anything that is associated with location
filtered_columns = ['name', 'categories'] + [col for col in dataframe.columns if col.startswith('location.')] + ['id']
dataframe_filtered = dataframe.loc[:, filtered_columns]

# function that extracts the category of the venue
def get_category_type(row):
    try:
        categories_list = row['categories']
    except:
        categories_list = row['venue.categories']
        
    if len(categories_list) == 0:
        return None
    else:
        return categories_list[0]['name']

# filter the category for each row
dataframe_filtered['categories'] = dataframe_filtered.apply(get_category_type, axis=1)

# clean column names by keeping only last term
dataframe_filtered.columns = [column.split('.')[-1] for column in dataframe_filtered.columns]

dataframe_filtered
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>categories</th>
      <th>address</th>
      <th>lat</th>
      <th>lng</th>
      <th>labeledLatLngs</th>
      <th>distance</th>
      <th>postalCode</th>
      <th>cc</th>
      <th>city</th>
      <th>state</th>
      <th>country</th>
      <th>formattedAddress</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Lung Fong Chinese Restaurant</td>
      <td>Chinese Restaurant</td>
      <td>870 E 180th St, Bronx, NY 10460</td>
      <td>40.845089</td>
      <td>-73.883153</td>
      <td>[{'label': 'display', 'lat': 40.845089, 'lng':...</td>
      <td>690</td>
      <td>10460</td>
      <td>US</td>
      <td>Bronx</td>
      <td>NY</td>
      <td>United States</td>
      <td>[870 E 180th St, Bronx, NY 10460, Bronx, NY 10...</td>
      <td>4ed4326f2c5b695abedee221</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Dragon Sea Chinese Restaurant</td>
      <td>Seafood Restaurant</td>
      <td>2302 Crotona Ave</td>
      <td>40.851900</td>
      <td>-73.884394</td>
      <td>[{'label': 'display', 'lat': 40.8519, 'lng': -...</td>
      <td>675</td>
      <td>10458</td>
      <td>US</td>
      <td>Bronx</td>
      <td>NY</td>
      <td>United States</td>
      <td>[2302 Crotona Ave, Bronx, NY 10458, United Sta...</td>
      <td>4f32777919836c91c7da98c4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>653 Lucky Chinese Restaurant</td>
      <td>Asian Restaurant</td>
      <td>653 E 182nd St</td>
      <td>40.851396</td>
      <td>-73.888245</td>
      <td>[{'label': 'display', 'lat': 40.851396, 'lng':...</td>
      <td>963</td>
      <td>10457</td>
      <td>US</td>
      <td>Bronx</td>
      <td>NY</td>
      <td>United States</td>
      <td>[653 E 182nd St, Bronx, NY 10457, United States]</td>
      <td>4ea229f77ee52a35dcca6aa5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Lucky Chinese Restaurant</td>
      <td>Chinese Restaurant</td>
      <td>653 E 182nd St</td>
      <td>40.851396</td>
      <td>-73.888245</td>
      <td>[{'label': 'display', 'lat': 40.851396, 'lng':...</td>
      <td>963</td>
      <td>10457</td>
      <td>US</td>
      <td>Bronx</td>
      <td>NY</td>
      <td>United States</td>
      <td>[653 E 182nd St, Bronx, NY 10457, United States]</td>
      <td>4f4348da19834bc91f55b4f0</td>
    </tr>
  </tbody>
</table>
</div>




```python
dataframe_filtered.name
```




    0     Lung Fong Chinese Restaurant
    1    Dragon Sea Chinese Restaurant
    2     653 Lucky Chinese Restaurant
    3         Lucky Chinese Restaurant
    Name: name, dtype: object




```python
print ('4 restaurants determined')
```

    4 restaurants determined



```python
venues_map = folium.Map(location=[latitude, longitude], zoom_start=13) # generate map centred around Bronz Zoo, NY

# add a red circle marker to represent the Bronx Zoo
folium.CircleMarker(
    [latitude, longitude],
    radius=10,
    color='red',
    popup='Bronz Zoo - Bronx',
    fill = True,
    fill_color = 'red',
    fill_opacity = 0.6
).add_to(venues_map)

# add the other restaurants as blue circle markers
for lat, lng, label in zip(dataframe_filtered.lat, dataframe_filtered.lng, dataframe_filtered.categories):
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        color='blue',
        popup=label,
        fill = True,
        fill_color='blue',
        fill_opacity=0.6
    ).add_to(venues_map)

# display map
venues_map
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe src="about:blank" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" data-html=PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfN2VhYjlmYWNiOTNhNGVjMjkzMmMyZWZkZjAyOTI4YmEgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwLjAlOwogICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAo8L2hlYWQ+Cjxib2R5PiAgICAKICAgIAogICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb2xpdW0tbWFwIiBpZD0ibWFwXzdlYWI5ZmFjYjkzYTRlYzI5MzJjMmVmZGYwMjkyOGJhIiA+PC9kaXY+CiAgICAgICAgCjwvYm9keT4KPHNjcmlwdD4gICAgCiAgICAKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIG1hcF83ZWFiOWZhY2I5M2E0ZWMyOTMyYzJlZmRmMDI5MjhiYSA9IEwubWFwKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ21hcF83ZWFiOWZhY2I5M2E0ZWMyOTMyYzJlZmRmMDI5MjhiYScsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7Y2VudGVyOiBbNDAuODQ5MzA0NDUsLTczLjg3NzEzNzkxODM1MjA2XSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHpvb206IDEzLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbWF4Qm91bmRzOiBib3VuZHMsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBsYXllcnM6IFtdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgd29ybGRDb3B5SnVtcDogZmFsc2UsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjcnM6IEwuQ1JTLkVQU0czODU3CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0pOwogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgdGlsZV9sYXllcl9mYzQ1ZjQ5MjE3ZTI0NzZkYWI4ZmFkMGMyODJkNDA4NCA9IEwudGlsZUxheWVyKAogICAgICAgICAgICAgICAgJ2h0dHBzOi8ve3N9LnRpbGUub3BlbnN0cmVldG1hcC5vcmcve3p9L3t4fS97eX0ucG5nJywKICAgICAgICAgICAgICAgIHsKICAiYXR0cmlidXRpb24iOiBudWxsLAogICJkZXRlY3RSZXRpbmEiOiBmYWxzZSwKICAibWF4Wm9vbSI6IDE4LAogICJtaW5ab29tIjogMSwKICAibm9XcmFwIjogZmFsc2UsCiAgInN1YmRvbWFpbnMiOiAiYWJjIgp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZWFiOWZhY2I5M2E0ZWMyOTMyYzJlZmRmMDI5MjhiYSk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNDNlYjRiOTQ2M2RjNDUzNThmMDI3ZTE5MjEyYWFmY2UgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NDkzMDQ0NSwtNzMuODc3MTM3OTE4MzUyMDZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAicmVkIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAicmVkIiwKICAiZmlsbE9wYWNpdHkiOiAwLjYsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiAxMCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZWFiOWZhY2I5M2E0ZWMyOTMyYzJlZmRmMDI5MjhiYSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mYjM1MTA3ZWQ3YzA0YTQ5YmMwM2E5OTkzMjMxZDk3YSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wMDc1ZjNiYzgzNTg0YTc0YjkyOWQ1OGNjZTg0ZDk3MCA9ICQoJzxkaXYgaWQ9Imh0bWxfMDA3NWYzYmM4MzU4NGE3NGI5MjlkNThjY2U4NGQ5NzAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJyb256IFpvbyAtIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mYjM1MTA3ZWQ3YzA0YTQ5YmMwM2E5OTkzMjMxZDk3YS5zZXRDb250ZW50KGh0bWxfMDA3NWYzYmM4MzU4NGE3NGI5MjlkNThjY2U4NGQ5NzApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNDNlYjRiOTQ2M2RjNDUzNThmMDI3ZTE5MjEyYWFmY2UuYmluZFBvcHVwKHBvcHVwX2ZiMzUxMDdlZDdjMDRhNDliYzAzYTk5OTMyMzFkOTdhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzNiZWViMjEyNGQyMjRiNTc5ZTU0OGQ3YjNlOTk3ZDc4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODQ1MDg5LC03My44ODMxNTMwMDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiYmx1ZSIsCiAgImZpbGxPcGFjaXR5IjogMC42LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZWFiOWZhY2I5M2E0ZWMyOTMyYzJlZmRmMDI5MjhiYSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82YTkyN2MyNDMwODQ0ZmRlOGZiMGNkNzQxMDZlNjVhOSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83N2M2ZDhlNWQzMzc0NGQzYTRiNGFiN2Y4YjkxMjJkMCA9ICQoJzxkaXYgaWQ9Imh0bWxfNzdjNmQ4ZTVkMzM3NDRkM2E0YjRhYjdmOGI5MTIyZDAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNoaW5lc2UgUmVzdGF1cmFudDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNmE5MjdjMjQzMDg0NGZkZThmYjBjZDc0MTA2ZTY1YTkuc2V0Q29udGVudChodG1sXzc3YzZkOGU1ZDMzNzQ0ZDNhNGI0YWI3ZjhiOTEyMmQwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzNiZWViMjEyNGQyMjRiNTc5ZTU0OGQ3YjNlOTk3ZDc4LmJpbmRQb3B1cChwb3B1cF82YTkyN2MyNDMwODQ0ZmRlOGZiMGNkNzQxMDZlNjVhOSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wY2JkZmQ4ZTkwZWQ0NGVjODUyYzRjOWVmMzNlY2NlZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg1MTksLTczLjg4NDM5NF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiYmx1ZSIsCiAgImZpbGxPcGFjaXR5IjogMC42LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZWFiOWZhY2I5M2E0ZWMyOTMyYzJlZmRmMDI5MjhiYSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9kYzE1MDY2YzcxMmQ0ZTU2OTI0NDE2ODc1ZDhiODRlNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wN2VkMGZjOTkxOWI0OWM1ODA5NmRlNzRlYjY3NzRkNyA9ICQoJzxkaXYgaWQ9Imh0bWxfMDdlZDBmYzk5MTliNDljNTgwOTZkZTc0ZWI2Nzc0ZDciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlNlYWZvb2QgUmVzdGF1cmFudDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZGMxNTA2NmM3MTJkNGU1NjkyNDQxNjg3NWQ4Yjg0ZTcuc2V0Q29udGVudChodG1sXzA3ZWQwZmM5OTE5YjQ5YzU4MDk2ZGU3NGViNjc3NGQ3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzBjYmRmZDhlOTBlZDQ0ZWM4NTJjNGM5ZWYzM2VjY2VlLmJpbmRQb3B1cChwb3B1cF9kYzE1MDY2YzcxMmQ0ZTU2OTI0NDE2ODc1ZDhiODRlNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81ODdjZDBlMTRhNjE0NGQwYmEzN2I0MTg0MzM3ODEyOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg1MTM5NiwtNzMuODg4MjQ1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICJibHVlIiwKICAiZmlsbE9wYWNpdHkiOiAwLjYsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdlYWI5ZmFjYjkzYTRlYzI5MzJjMmVmZGYwMjkyOGJhKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2JkOTFmN2ExYjhiYTRhM2ZhYjVkZDYyNzllNGMyNDJmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzkzZWM0OWExZDBkMjQzNDRhZTBlMmE5NjA2NDUzNjk2ID0gJCgnPGRpdiBpZD0iaHRtbF85M2VjNDlhMWQwZDI0MzQ0YWUwZTJhOTYwNjQ1MzY5NiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QXNpYW4gUmVzdGF1cmFudDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYmQ5MWY3YTFiOGJhNGEzZmFiNWRkNjI3OWU0YzI0MmYuc2V0Q29udGVudChodG1sXzkzZWM0OWExZDBkMjQzNDRhZTBlMmE5NjA2NDUzNjk2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzU4N2NkMGUxNGE2MTQ0ZDBiYTM3YjQxODQzMzc4MTI4LmJpbmRQb3B1cChwb3B1cF9iZDkxZjdhMWI4YmE0YTNmYWI1ZGQ2Mjc5ZTRjMjQyZik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84ODc3MjJjMDQ1MjQ0OWIzOTYxODQ4YTdhZGE4ZmU4NCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQwLjg1MTM5NiwtNzMuODg4MjQ1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICJibHVlIiwKICAiZmlsbE9wYWNpdHkiOiAwLjYsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdlYWI5ZmFjYjkzYTRlYzI5MzJjMmVmZGYwMjkyOGJhKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzIxMTJkZmE2Mjc2NDRmOWZiZGQ0NDhjNWVjNGI5MWY5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2EyZWE3OTBlODU2NDRkMGI5NWE0NTI2ZDRlZjI5ZWRiID0gJCgnPGRpdiBpZD0iaHRtbF9hMmVhNzkwZTg1NjQ0ZDBiOTVhNDUyNmQ0ZWYyOWVkYiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2hpbmVzZSBSZXN0YXVyYW50PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yMTEyZGZhNjI3NjQ0ZjlmYmRkNDQ4YzVlYzRiOTFmOS5zZXRDb250ZW50KGh0bWxfYTJlYTc5MGU4NTY0NGQwYjk1YTQ1MjZkNGVmMjllZGIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfODg3NzIyYzA0NTI0NDliMzk2MTg0OGE3YWRhOGZlODQuYmluZFBvcHVwKHBvcHVwXzIxMTJkZmE2Mjc2NDRmOWZiZGQ0NDhjNWVjNGI5MWY5KTsKCiAgICAgICAgICAgIAogICAgICAgIAo8L3NjcmlwdD4= onload="this.contentDocument.open();this.contentDocument.write(atob(this.getAttribute('data-html')));this.contentDocument.close();" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python
print ('Mapped the venues')
```

    Mapped the venues



```python
address = 'Bronx Zoo, NY'

geolocator = Nominatim(user_agent="foursquare_agent")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print(latitude, longitude)
```

    40.84930445 -73.87713791835206



```python
#determine how many Italian restaurants around Zoo
```


```python
search_query = 'Italian'
radius = 800
print(search_query + ' .... OK!')
```

    Italian .... OK!



```python
print ('Now searching for Italian restaurants close to Bronx Zoo')
```

    Now searching for Italian restaurants close to Bronx Zoo



```python
url = 'https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&ll={},{}&v={}&query={}&radius={}&limit={}'.format(CLIENT_ID, CLIENT_SECRET, latitude, longitude, VERSION, search_query, radius, LIMIT)
url
```




    'https://api.foursquare.com/v2/venues/search?client_id=XOMNN5V4YTDAU4HRS1NHJQMW5IYKWCWXXGCE2ZNPW4NKNU3O&client_secret=VMCFJQKYJT3TFKSLNMJNXNEC3EDSSLWGHUR5B3QUCODZ1K1L&ll=40.84930445,-73.87713791835206&v=20180604&query=Italian&radius=800&limit=30'




```python
results = requests.get(url).json()
results
```




    {'meta': {'code': 200, 'requestId': '5fb4cb04a0021654caf11560'},
     'response': {'venues': [{'id': '4bc33005abf49521fe5cc393',
        'name': 'Joes Italian Deli',
        'location': {'address': '685 E 187th St',
         'crossStreet': 'Cambreleng Ave.',
         'lat': 40.85439129501429,
         'lng': -73.8853668865723,
         'labeledLatLngs': [{'label': 'display',
           'lat': 40.85439129501429,
           'lng': -73.8853668865723},
          {'label': 'entrance', 'lat': 40.854473, 'lng': -73.885095}],
         'distance': 894,
         'postalCode': '10458',
         'cc': 'US',
         'city': 'Bronx',
         'state': 'NY',
         'country': 'United States',
         'formattedAddress': ['685 E 187th St (Cambreleng Ave.)',
          'Bronx, NY 10458',
          'United States']},
        'categories': [{'id': '4bf58dd8d48988d146941735',
          'name': 'Deli / Bodega',
          'pluralName': 'Delis / Bodegas',
          'shortName': 'Deli / Bodega',
          'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/deli_',
           'suffix': '.png'},
          'primary': True}],
        'venuePage': {'id': '80196593'},
        'referralId': 'v-1605683972',
        'hasPerk': False},
       {'id': '4b3957bbf964a520fd5a25e3',
        'name': "Passo's Italian Deli",
        'location': {'address': 'Garden Street',
         'crossStreet': '11th Street',
         'lat': 40.848891,
         'lng': -73.88353,
         'labeledLatLngs': [{'label': 'display',
           'lat': 40.848891,
           'lng': -73.88353}],
         'distance': 540,
         'cc': 'US',
         'city': 'New York',
         'state': 'NY',
         'country': 'United States',
         'formattedAddress': ['Garden Street (11th Street)',
          'New York, NY',
          'United States']},
        'categories': [],
        'referralId': 'v-1605683972',
        'hasPerk': False}]}}




```python
print ('results obtained, 2 restaurants')
```

    results obtained, 2 restaurants



```python
# assign relevant part of JSON to venues
venues = results['response']['venues']

# tranform venues into a dataframe
dataframe = json_normalize(venues)
dataframe.head()
```

    /home/jupyterlab/conda/envs/python/lib/python3.6/site-packages/ipykernel_launcher.py:5: FutureWarning: pandas.io.json.json_normalize is deprecated, use pandas.json_normalize instead
      """





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>categories</th>
      <th>referralId</th>
      <th>hasPerk</th>
      <th>location.address</th>
      <th>location.crossStreet</th>
      <th>location.lat</th>
      <th>location.lng</th>
      <th>location.labeledLatLngs</th>
      <th>location.distance</th>
      <th>location.postalCode</th>
      <th>location.cc</th>
      <th>location.city</th>
      <th>location.state</th>
      <th>location.country</th>
      <th>location.formattedAddress</th>
      <th>venuePage.id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4bc33005abf49521fe5cc393</td>
      <td>Joes Italian Deli</td>
      <td>[{'id': '4bf58dd8d48988d146941735', 'name': 'D...</td>
      <td>v-1605683972</td>
      <td>False</td>
      <td>685 E 187th St</td>
      <td>Cambreleng Ave.</td>
      <td>40.854391</td>
      <td>-73.885367</td>
      <td>[{'label': 'display', 'lat': 40.85439129501429...</td>
      <td>894</td>
      <td>10458</td>
      <td>US</td>
      <td>Bronx</td>
      <td>NY</td>
      <td>United States</td>
      <td>[685 E 187th St (Cambreleng Ave.), Bronx, NY 1...</td>
      <td>80196593</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4b3957bbf964a520fd5a25e3</td>
      <td>Passo's Italian Deli</td>
      <td>[]</td>
      <td>v-1605683972</td>
      <td>False</td>
      <td>Garden Street</td>
      <td>11th Street</td>
      <td>40.848891</td>
      <td>-73.883530</td>
      <td>[{'label': 'display', 'lat': 40.848891, 'lng':...</td>
      <td>540</td>
      <td>NaN</td>
      <td>US</td>
      <td>New York</td>
      <td>NY</td>
      <td>United States</td>
      <td>[Garden Street (11th Street), New York, NY, Un...</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
print ('formatting into dataframe columns')
```

    formatting into dataframe columns



```python
# keep only columns that include venue name, and anything that is associated with location
filtered_columns = ['name', 'categories'] + [col for col in dataframe.columns if col.startswith('location.')] + ['id']
dataframe_filtered = dataframe.loc[:, filtered_columns]

# function that extracts the category of the venue
def get_category_type(row):
    try:
        categories_list = row['categories']
    except:
        categories_list = row['venue.categories']
        
    if len(categories_list) == 0:
        return None
    else:
        return categories_list[0]['name']

# filter the category for each row
dataframe_filtered['categories'] = dataframe_filtered.apply(get_category_type, axis=1)

# clean column names by keeping only last term
dataframe_filtered.columns = [column.split('.')[-1] for column in dataframe_filtered.columns]

dataframe_filtered
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>categories</th>
      <th>address</th>
      <th>crossStreet</th>
      <th>lat</th>
      <th>lng</th>
      <th>labeledLatLngs</th>
      <th>distance</th>
      <th>postalCode</th>
      <th>cc</th>
      <th>city</th>
      <th>state</th>
      <th>country</th>
      <th>formattedAddress</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Joes Italian Deli</td>
      <td>Deli / Bodega</td>
      <td>685 E 187th St</td>
      <td>Cambreleng Ave.</td>
      <td>40.854391</td>
      <td>-73.885367</td>
      <td>[{'label': 'display', 'lat': 40.85439129501429...</td>
      <td>894</td>
      <td>10458</td>
      <td>US</td>
      <td>Bronx</td>
      <td>NY</td>
      <td>United States</td>
      <td>[685 E 187th St (Cambreleng Ave.), Bronx, NY 1...</td>
      <td>4bc33005abf49521fe5cc393</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Passo's Italian Deli</td>
      <td>None</td>
      <td>Garden Street</td>
      <td>11th Street</td>
      <td>40.848891</td>
      <td>-73.883530</td>
      <td>[{'label': 'display', 'lat': 40.848891, 'lng':...</td>
      <td>540</td>
      <td>NaN</td>
      <td>US</td>
      <td>New York</td>
      <td>NY</td>
      <td>United States</td>
      <td>[Garden Street (11th Street), New York, NY, Un...</td>
      <td>4b3957bbf964a520fd5a25e3</td>
    </tr>
  </tbody>
</table>
</div>




```python
dataframe_filtered.name
```




    0       Joes Italian Deli
    1    Passo's Italian Deli
    Name: name, dtype: object




```python
print ('Mapping Italian restaurants to Bronx Zoo')
```

    Mapping Italian restaurants to Bronx Zoo



```python
venues_map = folium.Map(location=[latitude, longitude], zoom_start=13) # generate map centred around Bronz Zoo, NY

# add a red circle marker to represent the Bronx Zoo
folium.CircleMarker(
    [latitude, longitude],
    radius=10,
    color='red',
    popup='Bronz Zoo - Bronx',
    fill = True,
    fill_color = 'red',
    fill_opacity = 0.6
).add_to(venues_map)

# add the other Italian restaurants as blue circle markers
for lat, lng, label in zip(dataframe_filtered.lat, dataframe_filtered.lng, dataframe_filtered.categories):
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        color='blue',
        popup=label,
        fill = True,
        fill_color='blue',
        fill_opacity=0.6
    ).add_to(venues_map)

# display map
venues_map
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe src="about:blank" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" data-html=PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfOThiMGVhMzIzOGM1NGI3ZGFlNWIxNmE5ZjA0ZTZmNGEgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwLjAlOwogICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAo8L2hlYWQ+Cjxib2R5PiAgICAKICAgIAogICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb2xpdW0tbWFwIiBpZD0ibWFwXzk4YjBlYTMyMzhjNTRiN2RhZTViMTZhOWYwNGU2ZjRhIiA+PC9kaXY+CiAgICAgICAgCjwvYm9keT4KPHNjcmlwdD4gICAgCiAgICAKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIG1hcF85OGIwZWEzMjM4YzU0YjdkYWU1YjE2YTlmMDRlNmY0YSA9IEwubWFwKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ21hcF85OGIwZWEzMjM4YzU0YjdkYWU1YjE2YTlmMDRlNmY0YScsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7Y2VudGVyOiBbNDAuODQ5MzA0NDUsLTczLjg3NzEzNzkxODM1MjA2XSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHpvb206IDEzLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbWF4Qm91bmRzOiBib3VuZHMsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBsYXllcnM6IFtdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgd29ybGRDb3B5SnVtcDogZmFsc2UsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBjcnM6IEwuQ1JTLkVQU0czODU3CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0pOwogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgdGlsZV9sYXllcl9hMTA2YjdmOWIxZDY0NWY5OTI5MmRjNDg1YmNlMTFlZCA9IEwudGlsZUxheWVyKAogICAgICAgICAgICAgICAgJ2h0dHBzOi8ve3N9LnRpbGUub3BlbnN0cmVldG1hcC5vcmcve3p9L3t4fS97eX0ucG5nJywKICAgICAgICAgICAgICAgIHsKICAiYXR0cmlidXRpb24iOiBudWxsLAogICJkZXRlY3RSZXRpbmEiOiBmYWxzZSwKICAibWF4Wm9vbSI6IDE4LAogICJtaW5ab29tIjogMSwKICAibm9XcmFwIjogZmFsc2UsCiAgInN1YmRvbWFpbnMiOiAiYWJjIgp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OGIwZWEzMjM4YzU0YjdkYWU1YjE2YTlmMDRlNmY0YSk7CiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMjZkYjRiM2QxMjg4NDdmMDk0MmI4OTcxNGM0ZmU4MjEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0MC44NDkzMDQ0NSwtNzMuODc3MTM3OTE4MzUyMDZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAicmVkIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAicmVkIiwKICAiZmlsbE9wYWNpdHkiOiAwLjYsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiAxMCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OGIwZWEzMjM4YzU0YjdkYWU1YjE2YTlmMDRlNmY0YSk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80NzU0YWQxMGI0OWU0ZWI2YjIxYTM4Njc0NDMzNGIwYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xOTNmMGEwZDdjYWI0ZTc2YWE4YzJkNWZmNmU4YzgxNyA9ICQoJzxkaXYgaWQ9Imh0bWxfMTkzZjBhMGQ3Y2FiNGU3NmFhOGMyZDVmZjZlOGM4MTciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJyb256IFpvbyAtIEJyb254PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80NzU0YWQxMGI0OWU0ZWI2YjIxYTM4Njc0NDMzNGIwYS5zZXRDb250ZW50KGh0bWxfMTkzZjBhMGQ3Y2FiNGU3NmFhOGMyZDVmZjZlOGM4MTcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMjZkYjRiM2QxMjg4NDdmMDk0MmI4OTcxNGM0ZmU4MjEuYmluZFBvcHVwKHBvcHVwXzQ3NTRhZDEwYjQ5ZTRlYjZiMjFhMzg2NzQ0MzM0YjBhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzUyMDA0YmUwYWI2NzRlNmNiMzMzOTI4NDc3NjFhYTE0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODU0MzkxMjk1MDE0MjksLTczLjg4NTM2Njg4NjU3MjNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogImJsdWUiLAogICJmaWxsT3BhY2l0eSI6IDAuNiwKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOThiMGVhMzIzOGM1NGI3ZGFlNWIxNmE5ZjA0ZTZmNGEpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYjhlYmUyMDY1OTViNDQyY2I2NGY0NTQ2YmFlOGY3ZWYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNDMyNDY2ZjcwMjhmNDY1M2JmZGVmMGRiMWE5NWNiZjEgPSAkKCc8ZGl2IGlkPSJodG1sXzQzMjQ2NmY3MDI4ZjQ2NTNiZmRlZjBkYjFhOTVjYmYxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5EZWxpIC8gQm9kZWdhPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iOGViZTIwNjU5NWI0NDJjYjY0ZjQ1NDZiYWU4ZjdlZi5zZXRDb250ZW50KGh0bWxfNDMyNDY2ZjcwMjhmNDY1M2JmZGVmMGRiMWE5NWNiZjEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNTIwMDRiZTBhYjY3NGU2Y2IzMzM5Mjg0Nzc2MWFhMTQuYmluZFBvcHVwKHBvcHVwX2I4ZWJlMjA2NTk1YjQ0MmNiNjRmNDU0NmJhZThmN2VmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzQ1YWY1OTcxM2MyMjQzNDRhZDMzMWYxMTQ1Mjc5NmVjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDAuODQ4ODkxLC03My44ODM1M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiYmx1ZSIsCiAgImZpbGxPcGFjaXR5IjogMC42LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85OGIwZWEzMjM4YzU0YjdkYWU1YjE2YTlmMDRlNmY0YSk7CiAgICAgICAgICAgIAo8L3NjcmlwdD4= onload="this.contentDocument.open();this.contentDocument.write(atob(this.getAttribute('data-html')));this.contentDocument.close();" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>




```python
print ('There are only 2 Italian restaurants clost to the Bronz Zoo, compared to 4 Chinese Restaturants') 
```

    There are only 2 Italian restaurants clost to the Bronz Zoo, compared to 4 Chinese Restaturants



```python
print ('Discussion Section')
print ()
print ()
print ('The purpose of the project was to analyze which type of restaurant to open in the Bronx Zoo area, Chinese or Italian')
print ('Each type of restaurant venue was determine how many were already in the area')
print ('By determing how many, it allowed a decision to be made which type of restaurant to proceed to open')
print ()
print ()
print ('Results Section')
print ('Based on the analyzes of this project it was determined, that there are 2 Italian and 4 Chinese restaurants close to the Bronx Zoo')
print ('Based on the number of restuarants in the area, the conclusion would be to proceed t0 open up an Italian restaurant. ')
print ('Due to the number of chinese restaurants in the area, it is not recommended to open a Chinese restaurant')
print ('As the conclusion is directly based on the number of restaurants, it does not take into the factor of size or rating of each one of the restaurants')


```

    Discussion Section
    
    
    The purpose of the project was to analyze which type of restaurant to open in the Bronx Zoo area, Chinese or Italian
    Each type of restaurant venue was determine how many were already in the area
    By determing how many, it allowed a decision to be made which type of restaurant to proceed to open
    
    
    Results Section
    Based on the analyzes of this project it was determined, that there are 2 Italian and 4 Chinese restaurants close to the Bronx Zoo
    Based on the number of restuarants in the area, the conclusion would be to proceed t0 open up an Italian restaurant. 
    Due to the number of chinese restaurants in the area, it is not recommended to open a Chinese restaurant
    As the conclusion is directly based on the number of restaurants, it does not take into the factor of size or rating of each one of the restaurants



```python

```
