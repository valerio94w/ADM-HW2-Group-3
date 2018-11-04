# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
# In[1]:
import pandas as pd

# In[2]:
from pandas import DataFrame, read_csv

# In[3]
import json


# In[12]
import folium as folium

# In[]
from IPython.display import HTML
# In[3]:
Location = "F:\Valerio\yellow_tripdata_2018-01.csv"

# In[5]:
nytaxi_january =pd.read_csv(Location, usecols=[1,7])

# In[7]:
Location_taxi_zone =r"C:\Users\ValerioV\Downloads\taxi _zone_lookup.csv"

# In[8]:
nyBorough =pd.read_csv(Location_taxi_zone, usecols=[0,1])

# In[9]
taxi_and_Borough_january=nytaxi_january.join(nyBorough.set_index('LocationID'), on='PULocationID')

# In[10]
df_grouped = taxi_and_Borough_january.groupby(['PULocationID']).count() 

# In[]
df_grouped.reset_index(level='PULocationID')
# In[]
df_grouped = df_grouped.unstack()

# In[]
df_grouped
# In[10]
nytaxijason= r"C:\Users\ValerioV\Downloads\Valerio\Università\Data science\taxi_zones.json"

# In[11]

# In[]
taxiMap = folium.Map(location=[40.7142700,-74.0059700], 
                     zoom_start=10.5)
# In[]

taxiMap.choropleth(geo_data=r"C:\Users\ValerioV\Downloads\Valerio\Università\Data science\taxi_zones.json",
                   
                   fill_opacity  = 0.3, line_opacity=0.5
                     ) 

# In[]
taxiMap.choropleth(geo_data=nytaxijason,
                     fill_color='YlGn', fill_opacity=0.3, line_opacity=0.5,
                     data = df_grouped,
                     key_on='feature.properties.LocationID',
                     threshold_scale = [0,200000,400000],
                     columns = [df_grouped.index,'Borough'],
                     legend_name = 'Taxis trips'
                     ) 

# In[]
#Output the map to an .html file:
taxiMap.save(outfile='testScores1.html')

# In[]
# In[]

