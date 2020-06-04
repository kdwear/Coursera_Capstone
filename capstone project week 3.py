#!/usr/bin/env python
# coding: utf-8

# In[ ]:






from pandas.io.html import read_html

Toronto_Neighborhoods = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'

Neighborhood = read_html(Toronto_Neighborhoods, attrs={'class':'wikitable'})

canada_data = Neighborhood[0]

Neighborhood[0].head()


# In[ ]:





# In[2]:


import random # library for random number generation
import numpy as np # library for vectorized computation
import pandas as pd # library to process data as dataframes

import matplotlib.pyplot as plt # plotting library
# backend for rendering plots within the browser
get_ipython().run_line_magic('matplotlib', 'inline')

from sklearn.cluster import KMeans 
from sklearn.datasets.samples_generator import make_blobs

print('Libraries imported.')


# In[ ]:


import pandas as pd
get_ipython().system('conda install -c conda lxml')
get_ipython().system('pip install et_xmlfile')
get_ipython().system('pip install bs4')
get_ipython().system('pip install html5lib')
get_ipython().system('pip install lxml')
import bs4.builder._lxml
from lxml import etree
import requests
from bs4 import BeautifulSoup
print('installs completed')


# In[3]:




from pandas.io.html import read_html

Toronto_Neighborhoods = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'

Neighborhood = read_html(Toronto_Neighborhoods, attrs={'class':'wikitable'})

canada_data = Neighborhood[0]

Neighborhood[0].head()


# In[2]:


import pandas as pd 
get_ipython().system('pip install -c conda lxml')
get_ipython().system('pip install et_xmlfile')
get_ipython().system('pip install bs4')
get_ipython().system('pip install html5lib')
get_ipython().system('pip install lxml')
import bs4.builder._lxml
from lxml import etree
 




# In[4]:


canada_data


# In[5]:


get_ipython().system('pip install geocoder')
import pandas as pd
postal_data =pd.read_csv('http://cocl.us/Geospatial_data')
postal_data.head()


# In[ ]:


import geocoder # import geocoder
# initialize your variable to None
lat_lng_coords = None

# loop until you get the coordinates
while(lat_lng_coords is None):
  g = geocoder.google('{}, Toronto, Ontario'.format(postal_data))
  lat_lng_coords = g.latlng
latitude = lat_lng_coords[0]
longitude = lat_lng_coords[1]


# In[6]:


print (pd.merge(canada_data, postal_data, on='Postal Code'))


# In[8]:


df_inner = pd.merge(canada_data, postal_data, on='Postal Code', how='inner')
df_inner


# In[ ]:





# In[11]:


#segmenting and clustering only Borough of Etobicoke

Etobicoke_data = df_inner[df_inner['Borough'] == 'Etobicoke'].reset_index(drop=True)
Etobicoke_data.head()


# In[ ]:





# In[12]:


# number of dataframes for Etobicoke
print('The dataframe has {} boroughs and {} neighborhoods.'.format(
        len(df_inner['Borough'].unique()),
        df_inner.shape[0]
    )
)


# In[ ]:





# In[13]:


import numpy as np # library to handle data in a vectorized manner

import pandas as pd # library for data analsysis
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

import json # library to handle JSON files

get_ipython().system("conda install -c conda-forge geopy --yes # uncomment this line if you haven't completed the Foursquare API lab")
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


# In[ ]:





# In[15]:


address = 'Toronto, ON'

geolocator = Nominatim(user_agent="ny_explorer")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of Toronto are {}, {}.'.format(latitude, longitude))


# In[ ]:





# In[16]:


# create map of Toronto using latitude and longitude values
map_toronto = folium.Map(location=[latitude, longitude], zoom_start=10)

# add markers to map
for lat, lng, borough, neighborhood in zip(df_inner['Latitude'], df_inner['Longitude'], df_inner['Borough'], df_inner['Neighborhood']):
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
    
map_toronto


# In[ ]:





# In[17]:


# obtainging Etobicoke geogrpical coordinates
address = 'Etobicoke, ON'

geolocator = Nominatim(user_agent="ny_explorer")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of Etobicoke are {}, {}.'.format(latitude, longitude))


# In[ ]:





# In[18]:


# create map of Etobicoke using latitude and longitude values
# used Etobicoke to show how close it was to Toronto
map_etobicoke = folium.Map(location=[latitude, longitude], zoom_start=10)

# add markers to map
for lat, lng, borough, neighborhood in zip(df_inner['Latitude'], df_inner['Longitude'], df_inner['Borough'], df_inner['Neighborhood']):
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
    
map_etobicoke


# In[ ]:





# In[19]:


CLIENT_ID = 'XOMNN5V4YTDAU4HRS1NHJQMW5IYKWCWXXGCE2ZNPW4NKNU3O' # your Foursquare ID
CLIENT_SECRET = 'VMCFJQKYJT3TFKSLNMJNXNEC3EDSSLWGHUR5B3QUCODZ1K1L' # your Foursquare Secret
VERSION = '20180605' # Foursquare API version

print('Your credentails:')
print('CLIENT_ID: ' + CLIENT_ID)
print('CLIENT_SECRET:' + CLIENT_SECRET)


# In[ ]:





# In[21]:


# Etocbicoke neighborhood - Humber Valley Village
Etobicoke_data.loc[0, 'Neighborhood']


# In[ ]:




