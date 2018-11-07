# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
# In[1]:
import pandas as pd
import folium as folium

# In[3]:
Location_Jan = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-01.csv"
Location_Feb = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-02.csv"
Location_Mar = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-03.csv"
Location_Apr = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-04.csv"
Location_May = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-05.csv"
Location_Jun = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-06.csv"

# In[2]:
# Load January
nytaxi = pd.read_csv(Location_Jan, usecols=[1,2,3,7,8]) 

# In[3]
# Load and concatenate other months
nytaxi = pd.concat([nytaxi, pd.read_csv(Location_Feb, usecols=[1,2,3,7,8])])
nytaxi = pd.concat([nytaxi, pd.read_csv(Location_Mar, usecols=[1,2,3,7,8])])
nytaxi = pd.concat([nytaxi, pd.read_csv(Location_Apr, usecols=[1,2,3,7,8])])
nytaxi = pd.concat([nytaxi, pd.read_csv(Location_May, usecols=[1,2,3,7,8])])
nytaxi = pd.concat([nytaxi, pd.read_csv(Location_Jun, usecols=[1,2,3,7,8])])


# In[10]
df_grouped_pu = nytaxi.groupby(['PULocationID']).count() 
df_grouped_pu = df_grouped_pu['passenger_count']
df_grouped_pu = df_grouped_pu.order(ascending=False)

# In[10]
df_grouped_do = nytaxi.groupby(['DOLocationID']).count() 
df_grouped_do.columns = ['count']
df_grouped_do = df_grouped_do.order(ascending=False)

# In[10]
ny_json= r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\taxi_zones.json"

# In[]
taxiMap_pu = folium.Map(location=[40.7142700,-74.0059700], zoom_start=11)

# In[]
taxiMap_pu.choropleth(geo_data=ny_json,
                     fill_color='YlGn', fill_opacity=0.8, line_opacity=0.5,
                     data = df_grouped_pu,
                     key_on='feature.properties.LocationID',
                     columns = [df_grouped_pu.index,0],
                     legend_name = 'Taxis trips'
                     ) 

# In[]
#Output the map to an .html file:
taxiMap_pu.save(outfile=r'C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\src\map_pu.html')

# In[]
taxiMap_do = folium.Map(location=[40.7142700,-74.0059700], 
                     zoom_start=10.5)

# In[]
taxiMap_do.choropleth(geo_data=ny_json,
                     fill_color='YlGn', fill_opacity=0.8, line_opacity=0.5,
                     data = df_grouped_do,
                     key_on='feature.properties.LocationID',
                     columns = [df_grouped_do.index,'count'],
                     legend_name = 'Taxis trips',
                     ) 

# In[]
#Output the map to an .html file:
taxiMap_do.save(outfile=r'C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\src\map_do.html')

# In[]
nytaxi_january['PU_DO'] = nytaxi_january["PULocationID"].map(str).add('p-d').add(nytaxi_january["DOLocationID"].map(str))

# In[]
new_grouped = nytaxi_january.groupby(['PU_DO']).count()

# In[]
new_grouped = new_grouped.drop(columns=['tpep_pickup_datetime','tpep_dropoff_datetime','PULocationID','DOLocationID','PU-DO'])

# In[]
new_grouped = new_grouped.sort_values(by='passenger_count', ascending=False)

# In[]

new_grouped[0:10].plot.bar()
