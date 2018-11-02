# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 15:51:30 2018

@author: ValerioV
"""

import pandas as pd
# In[2]:
from pandas import DataFrame, read_csv
# In[]
Location = r"F:\Valerio\yellow_tripdata_2018-01.csv"   #here is where i save january data

# In[5]:

nytaxi_january =pd.read_csv(Location, usecols=[1,2,4,7])

# In[]
nytaxi_january.tpep_pickup_datetime = pd.to_datetime(nytaxi_january.tpep_pickup_datetime) 

# modify type of tpep_pickup_datetime to DateTime

# In[]
nytaxi_january.tpep_dropoff_datetime = pd.to_datetime(nytaxi_january.tpep_dropoff_datetime)
 # modify type of tpep_dropoff_datetime to DateTime

# In[]
nytaxi_january['trip_duration'] = (nytaxi_january.tpep_dropoff_datetime - nytaxi_january.tpep_pickup_datetime).dt.total_seconds() 

# it computes trip duration (for trip started in january)

# In[]

Location_february =r"F:\Valerio\yellow_tripdata_2018-02.csv"

# In[]
ny_taxi_february =pd.read_csv(Location_february, usecols=[1,2,4,7])

# In[]

Location_3="F:\Valerio\yellow_tripdata_2018-03.csv"

# In[]

nytaxi_march =pd.read_csv(Location_3, usecols=[1,2,4,7])

# In[]
Location_4="F:\Valerio\yellow_tripdata_2018-04.csv"

# In[]
nytaxi_april=pd.read_csv(Location_4, usecols=[1,2,4,7])

# In[]

Location_5="F:\Valerio\yellow_tripdata_2018-05.csv"

# In[]

nytaxi_may =pd.read_csv(Location_5, usecols=[1,2,4,7])

# In[]

Location_6="F:\Valerio\yellow_tripdata_2018-06.csv"

# In[]

nytaxi_july=pd.read_csv(Location_6, usecols=[1,2,4,7])

# In[]
ny_taxi_february.tpep_pickup_datetime = pd.to_datetime(ny_taxi_february.tpep_pickup_datetime) 

# modify type of tpep_pickup_datetime to DateTime
# In[]

ny_taxi_february.tpep_dropoff_datetime = pd.to_datetime(ny_taxi_february.tpep_dropoff_datetime) 

# modify type of tpep_dropoff_datetime to DateTime

# In[]

ny_taxi_february['trip_duration'] = (ny_taxi_february.tpep_dropoff_datetime - ny_taxi_february.tpep_pickup_datetime).dt.total_seconds() 

# it computes trip duration (for trip started in february)

# In[]
nytaxi_march.tpep_pickup_datetime = pd.to_datetime(nytaxi_march.tpep_pickup_datetime) 

# modify type of tpep_pickup_datetime to DateTime

# In[]
nytaxi_march.tpep_dropoff_datetime = pd.to_datetime(nytaxi_march.tpep_dropoff_datetime) 

# modify type of tpep_dropoff_datetime to DateTime

# In[]
nytaxi_march['trip_duration'] = (nytaxi_march.tpep_dropoff_datetime - nytaxi_march.tpep_pickup_datetime).dt.total_seconds() 

# it computes trip duration (for trip started in march)

# In[]
nytaxi_april.tpep_pickup_datetime = pd.to_datetime(nytaxi_april.tpep_pickup_datetime) 

# modify type of tpep_pickup_datetime to DateTime
# In[]
nytaxi_april.tpep_dropoff_datetime = pd.to_datetime(nytaxi_april.tpep_dropoff_datetime) 

# modify type of tpep_dropoff_datetime to DateTime

# In[]
nytaxi_april['trip_duration'] = (nytaxi_april.tpep_dropoff_datetime - nytaxi_april.tpep_pickup_datetime).dt.total_seconds() 

# it computes trip duration (for trip started in april)

# In[]
nytaxi_may.tpep_pickup_datetime = pd.to_datetime(nytaxi_may.tpep_pickup_datetime) 

# modify type of tpep_pickup_datetime to DateTime

# In[]
nytaxi_may.tpep_dropoff_datetime = pd.to_datetime(nytaxi_may.tpep_dropoff_datetime) 

# modify type of tpep_dropoff_datetime to DateTime

# In[]
nytaxi_may['trip_duration'] = (nytaxi_may.tpep_dropoff_datetime - nytaxi_may.tpep_pickup_datetime).dt.total_seconds() 

# it computes trip duration (for trip started in may)


# In[]
nytaxi_july.tpep_pickup_datetime = pd.to_datetime(nytaxi_july.tpep_pickup_datetime)

# modify type of tpep_pickup_datetime to DateTime

# In[]
nytaxi_july.tpep_dropoff_datetime = pd.to_datetime(nytaxi_july.tpep_dropoff_datetime) # modify type of tpep_dropoff_datetime to DateTime

# modify type of tpep_dropoff_datetime to DateTime


# In[]
nytaxi_july['trip_duration'] = (nytaxi_july.tpep_dropoff_datetime - nytaxi_july.tpep_pickup_datetime).dt.total_seconds() 

#it shows duration trip (for trips started in july)


# In[]

nytaxi=pd.concat([nytaxi_january,ny_taxi_february,nytaxi_march,nytaxi_april,nytaxi_may,nytaxi_july], axis=1,join='inner')

#now i obtain one dataset from the concatenation of monthly datasets. In the colmun called 'trip_duration' i've the duration of all trips and the month which this trip is done

# In[]
Location_2 = r"C:\Users\ValerioV\Downloads\taxi _zone_lookup.csv"

# In[]
nyBorough =pd.read_csv(Location_2, usecols=[0,1])

# In[]

nytaxi = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')

#i do this join to obtain a dataset which help me to know the name of borough where trip starts

# In[]
nytaxi.plot.scatter(x='trip_duration', y='trip_distance')
 
# it makes a plot where we can see relationship between trip duration and trip distance
# there are a lot of outliers
 # In[]

nytaxi = nytaxi.drop(nytaxi[(nytaxi.trip_duration<=0)].index)
 
#i consider only trips which last at least 30 seconds

# In[]

nytaxi = nytaxi.drop(nytaxi[(nytaxi.trip_duration>10000)].index)

#i delete trips which last plus than 10000 seconds 

# In[]
nytaxi = nytaxi.drop(nytaxi[(nytaxi.trip_distance>100)].index)

#i delete trips which distance upper than 100 mile

# In[]
nytaxi = nytaxi.drop(nytaxi[(nytaxi.trip_distance < 0.6)].index)

#i delete trips which duration lower than 0,60 mile

# In[]

nytaxi = nytaxi.drop('Unknown', axis=1)

# delete trip which start from unknown borough

# In[]

nytaxi.plot.scatter(x='trip_duration', y='trip_distance')

#now we can see better way the plot

# In[]
nytaxi['trip_duration'].corr(nytaxi['trip_distance'])

#it shows if exist correlation between trip duration and trip distance

#show results by borough

Borough_grouped= nytaxi.groupby('Borough',axis=1)

# group data by borough

# In[]

Borough_grouped.plot(kind='scatter',x='trip_duration', y='trip_distance', c='Borough')

# In[]

Borough_grouped.plot.scatter(x='trip_duration', y='trip_distance', c='Borough')
