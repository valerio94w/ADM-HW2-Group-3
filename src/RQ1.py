#!/usr/bin/env python
# coding: utf-8

# In[1]:
import pandas as pd

# In[2]:
from pandas import DataFrame, read_csv

# In[2]:
Location = r"F:\Valerio\yellow_tripdata_2018-01.csv"   #here is where i save january data

# In[3]:
nytaxi =pd.read_csv(Location, usecols=[1,5])           #whit command usecols i use only columns that i need to solve RQ1

# In[5]:
nytaxi[:3]       

# In[4]:
Location_2 =r"C:\Users\ValerioV\Downloads\taxi _zone_lookup.csv"     #here is where i save new vork borough data

# In[6]:
nyBorough =pd.read_csv(Location_2, usecols=[0,1])          

# In[29]:
nyBorough[:3]

# In[9]:
taxi_and_Borough=nytaxi.join(nyBorough.set_index('LocationID'), on='RatecodeID')    #  join two datasets

# In[10]:
taxi_and_Borough[:3]

# In[12]:
number_of_times = len(taxi_and_Borough)  #counts number of times that taxis are used in the month

# In[13]:
monthly_average = number_of_times/31  #shows the average number of trips recorded each day

# In[14]:
monthly_average

# In[15]:
Borough_grouped = taxi_and_Borough.groupby('Borough')   #groups data by borough

# In[25]:
Borough_grouped

# In[20]:


# In[ ]:


# In[26]:

for name in Borough_grouped:
    print(name)
    print(len(name))

# In[27]:
Borough_grouped.describe()  #shows how many taxis are used by borough-------there's an error: boroughs are 6 and not 5!! i'm tryng to solve this problem