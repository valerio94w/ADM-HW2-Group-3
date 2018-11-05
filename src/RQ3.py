
# coding: utf-8
"""
Created on Thu Nov  1 09:20:15 2018
@author: Pavanalikana

"""

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
import seaborn as sns


# In[5]:


Location = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-01.csv"  #the location of january data



# In[7]:


Location_1 = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\taxi_zone_lookup.csv" #the location of new vork borough data


# In[8]:


nytaxi =pd.read_csv(Location, usecols=[1,2,3,4,7,8,9,10]) 


# In[9]:


nytaxi[:10]


# In[10]:


nyBorough =pd.read_csv(Location_1, usecols=[0,1,2,3]) 


# In[11]:


nyBorough[:10]


# In[12]:


mergedata = pd.merge(nytaxi, nyBorough, left_on = "PULocationID", right_on = "LocationID").drop("LocationID", axis = 1)   #Merge the two csv files and store the data into new df(DataFrame)


# In[13]:


mergedata


# In[14]:


mergedata['passenger_count'].value_counts()


# In[15]:


mergedata['passenger_count'].describe()


# In[16]:


plt.figure(figsize = (6,4))
sns.countplot(mergedata['passenger_count'])
plt.xlabel("People")
plt.show()


# In[17]:


mergedata['tpep_pickup_datetime'] = pd.to_datetime(mergedata['tpep_pickup_datetime'])
mergedata['tpep_dropoff_datetime'] = pd.to_datetime(mergedata['tpep_dropoff_datetime'])

mergedata['weekday'] = mergedata['tpep_pickup_datetime'].dt.weekday_name
mergedata['month'] = mergedata['tpep_pickup_datetime'].dt.month
mergedata['weekday_num'] = mergedata['tpep_pickup_datetime'].dt.weekday
mergedata['pickup_hour'] = mergedata['tpep_pickup_datetime'].dt.hour
mergedata['day'] = mergedata['tpep_pickup_datetime'].dt.date


# In[18]:


plt.figure(figsize = (20,3))
sns.countplot(mergedata.weekday_num)
plt.show()


# In[19]:


mergedata['trip_duration'] = (mergedata.tpep_dropoff_datetime - mergedata.tpep_pickup_datetime).dt.total_seconds()


# In[20]:


mergedata.head()


# In[21]:


plt.figure(figsize = (20,5))
sns.boxplot(mergedata['trip_duration'])
plt.show()


# In[23]:


ManhattanMD = mergedata[mergedata['Borough'] == 'Manhattan']


# In[25]:


QueensMD = mergedata[mergedata['Borough'] == 'Queens']


# In[27]:


BrooklynMD = mergedata[mergedata['Borough'] == 'Brooklyn']


# In[29]:


plt.figure(figsize = (20,5))
sns.boxplot(ManhattanMD['trip_duration'])
plt.show()    #Manhattan Trip Duration


# In[31]:


plt.figure(figsize = (20,5))
sns.boxplot(BrooklynMD['trip_duration'])
plt.show()


# In[35]:


#Trips that took more than 5000 Seconds Brooklyn
BrooklynMD[BrooklynMD.trip_duration> 5000].head()


# In[38]:


#Trips that took more than 10000 Seconds Manhattan
ManhattanMD[ManhattanMD.trip_duration> 10000].head()


# In[41]:


#Trips that took more than 7000 Seconds Queens
QueensMD[QueensMD.trip_duration> 7000].head()


# In[64]:


plt.figure(figsize = (6,4))
mergedata.trip_duration.groupby(pd.cut(mergedata.trip_duration,np.arange(0,10000,400))).count().plot(kind='barh')
plt.title("Trip duration Every 8 Minutes")
plt.show()


# In[71]:


plt.figure(figsize = (6,4))
plt.title(" Manhattan Trip duration Every 10 Minutes")

ManhattanMD.trip_duration.groupby(pd.cut(ManhattanMD.trip_duration,np.arange(0,10000,500))).count().plot(kind='bar')
plt.show()


# In[72]:


plt.figure(figsize = (6,4))
plt.title(" Brooklyn Trip duration Every 20 Minutes")
BrooklynMD.trip_duration.groupby(pd.cut(BrooklynMD.trip_duration,np.arange(0,10000,500))).count().plot(kind='bar')
plt.show()


# In[73]:


plt.figure(figsize = (6,4))
plt.title(" Queens Trip duration Every 20 Minutes")

QueensMD.trip_duration.groupby(pd.cut(QueensMD.trip_duration,np.arange(0,10000,500))).count().plot(kind='bar')
plt.show()

