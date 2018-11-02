#!/usr/bin/env python
# coding: utf-8

# In[1]:
import pandas as pd

# In[2]:
from pandas import DataFrame, read_csv

# In[2]:
Location = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-01.csv"   #here is where i save january data

# In[3]:
nytaxi =pd.read_csv(Location, usecols=[1,3,7])           #with command usecols i use only columns that i need to solve RQ2

# In[4]:
nytaxi[:3]       

# In[5]:
Location_2 =r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\taxi_zone_lookup.csv"     #here is where i save new vork borough data

# In[6]:
nyBorough =pd.read_csv(Location_2, usecols=[0,1])          

# In[7]:
nyBorough[:3]

# In[8]:
taxi_and_Borough=nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')    #  join two datasets

# In[9]:
taxi_and_Borough.tpep_pickup_datetime = pd.to_datetime(taxi_and_Borough.tpep_pickup_datetime) # modify type of tpep_pickup_datetime to DateTime

# In[4]:
taxi_and_Borough = taxi_and_Borough[(taxi_and_Borough['tpep_pickup_datetime'].dt.year == 2018) & (taxi_and_Borough['tpep_pickup_datetime'].dt.month == 1)] # remove trips started before 2018 and after Jann 2018

# In[10]:
taxi_and_Borough[:3]

# In[11]
df_grouped = taxi_and_Borough.groupby([taxi_and_Borough.tpep_pickup_datetime.dt.hour,'Borough'])['passenger_count'].count() # group by hour of the day and borough, and count passengers
df_grouped = df_grouped.unstack()

# In[12]
df_grouped[:3]

# In[13]
df_grouped = df_grouped.drop('Unknown', axis=1)

# In[13]
df_grouped.plot.bar(stacked=True);

# In[14]
df_grouped.plot(subplots=True,figsize=(5,4))