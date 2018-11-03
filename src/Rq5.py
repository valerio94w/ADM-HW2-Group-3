# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 15:51:30 2018

@author: ValerioV
"""

import pandas as pd
import IPython.nbformat.current as nbf

# In[1]
Location_Jan = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-01.csv"
Location_Feb = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-02.csv"
Location_Mar = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-03.csv"
Location_Apr = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-04.csv"
Location_May = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-05.csv"
Location_Jun = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-06.csv"

# In[2]:
# Load January
nytaxi = pd.read_csv(Location_Jan, usecols=[1,2,4,7]) 

# In[3]
# Load and concatenate other months
nytaxi = pd.concat([nytaxi, pd.read_csv(Location_Feb, usecols=[1,2,4,7])])
nytaxi = pd.concat([nytaxi, pd.read_csv(Location_Mar, usecols=[1,2,4,7])])
nytaxi = pd.concat([nytaxi, pd.read_csv(Location_Apr, usecols=[1,2,4,7])])
nytaxi = pd.concat([nytaxi, pd.read_csv(Location_May, usecols=[1,2,4,7])])
nytaxi = pd.concat([nytaxi, pd.read_csv(Location_Jun, usecols=[1,2,4,7])])

# In[4]
Location_2 =r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\taxi_zone_lookup.csv"     #here is where i save new vork borough data

# In[5]
nyBorough =pd.read_csv(Location_2, usecols=[0,1])

# In[6]
#i do this join to obtain a dataset which help me to know the name of borough where trip starts
nytaxi = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')

# In[7]
# modify type of tpep_pickup_datetime to DateTime
nytaxi.tpep_pickup_datetime = pd.to_datetime(nytaxi.tpep_pickup_datetime) 

# In[8]
# modify type of tpep_dropoff_datetime to DateTime
nytaxi.tpep_dropoff_datetime = pd.to_datetime(nytaxi.tpep_dropoff_datetime)

# In[9]
# it computes trip duration
nytaxi['trip_duration'] = (nytaxi.tpep_dropoff_datetime - nytaxi.tpep_pickup_datetime).dt.total_seconds()

# In[10]
# it makes a plot where we can see relationship between trip duration and trip distance
# there are a lot of outliers
nytaxi.plot.hexbin(x='trip_duration', y='trip_distance')

# In[11]
# I clone the dataframe to make cleanings
nytaxi_clean = nytaxi
 
# In[12]
# I remove all the trips lasting less than 0 seconds and the ones lasting 0 seconds
nytaxi_clean = nytaxi_clean.drop(nytaxi_clean[(nytaxi_clean.trip_duration<=0)].index)
# I remove all the trips with trip distance higher than 25000
nytaxi_clean = nytaxi_clean.drop(nytaxi_clean[(nytaxi_clean.trip_distance > 25000)].index)
nytaxi_clean.plot.hexbin(x='trip_duration', y='trip_distance')

# In[13]
# I remove all the trips lasting more than 100000 seconds
nytaxi_clean = nytaxi_clean.drop(nytaxi_clean[(nytaxi_clean.trip_duration > 100000)].index)
# I remove all the trips with trip distance higher than 400
nytaxi_clean = nytaxi_clean.drop(nytaxi_clean[(nytaxi_clean.trip_distance > 400)].index)
nytaxi_clean.plot.hexbin(x='trip_duration', y='trip_distance')

# In[14]
# In order to clean the data, let's plot the trip_duration distribution
nytaxi_clean.trip_duration.plot.hist(100)

# In[15]
# Let's do a first cut to trip_duration 5000
nytaxi_clean = nytaxi_clean.drop(nytaxi_clean[(nytaxi_clean.trip_duration > 5000)].index)
nytaxi_clean.trip_duration.plot.hist(100)

# In[16]
# Now let's plot the trip_distance distribution
nytaxi_clean.trip_distance.plot.hist(100)

# In[17]
# Let's do a first cut to trip_distance 35
nytaxi_clean = nytaxi_clean.drop(nytaxi_clean[(nytaxi_clean.trip_distance > 35)].index)
nytaxi_clean.trip_distance.plot.hist(100)

# In[18]
# Let's see the new heatmap plot
nytaxi_clean.plot.hexbin(x='trip_duration', y='trip_distance')

# In[19]
# The plot is not clear, let's investigate the heatmaps for each Borough
nytaxi_clean[nytaxi_clean.Borough == 'Queens'].plot(kind='hexbin',x='trip_duration', y='trip_distance',gridsize=30, title='Queens')
nytaxi_clean[nytaxi_clean.Borough == 'Manhattan'].plot(kind='hexbin',x='trip_duration', y='trip_distance',gridsize=30, title='Manhattan')
nytaxi_clean[nytaxi_clean.Borough == 'EWR'].plot(kind='hexbin',x='trip_duration', y='trip_distance',gridsize=30, title='EWR')
nytaxi_clean[nytaxi_clean.Borough == 'Staten Island'].plot(kind='hexbin',x='trip_duration', y='trip_distance',gridsize=30, title='Staten Island')
nytaxi_clean[nytaxi_clean.Borough == 'Brooklyn'].plot(kind='hexbin',x='trip_duration', y='trip_distance',gridsize=30, title='Brooklyn')
nytaxi_clean[nytaxi_clean.Borough == 'Bronx'].plot(kind='hexbin',x='trip_duration', y='trip_distance',gridsize=30, title='Bronx')
nytaxi_clean[nytaxi_clean.Borough == 'Unknown'].plot(kind='hexbin',x='trip_duration', y='trip_distance',gridsize=30, title='Unknown')

# In[20]
# Queens is the borough with the mean trip_distance higher
# But there is also a strange concentration of trip lasting only few seconds
# Let's plot the distribution of the duration for Queens
nytaxi_clean[nytaxi_clean.Borough == 'Queens'].trip_duration.hist(bins=100)

# In[21]
# Let's remove trips with duration less than 60 seconds
nytaxi_clean = nytaxi_clean.drop(nytaxi_clean[(nytaxi_clean.trip_duration <60)].index)
nytaxi_clean[nytaxi_clean.Borough == 'Queens'].trip_duration.hist(bins=100)

# In[22]
# Let's replot everything with new scales
nytaxi_clean[nytaxi_clean.Borough == 'Queens'].plot(kind='hexbin',x='trip_duration', y='trip_distance',gridsize=30, title='Queens')
nytaxi_clean[nytaxi_clean.Borough == 'Manhattan'].plot(kind='hexbin',x='trip_duration', y='trip_distance', title='Manhattan', xlim=(0,1800), ylim=(0,10))
nytaxi_clean[nytaxi_clean.Borough == 'EWR'].plot(kind='hexbin',x='trip_duration', y='trip_distance', title='EWR', xlim=(0,400), ylim=(0,3))
nytaxi_clean[nytaxi_clean.Borough == 'Staten Island'].plot(kind='hexbin',x='trip_duration', y='trip_distance',gridsize=30, title='Staten Island', xlim=(0,4000), ylim=(0,25))
nytaxi_clean[nytaxi_clean.Borough == 'Brooklyn'].plot(kind='hexbin',x='trip_duration', y='trip_distance', title='Brooklyn', xlim=(0,1300), ylim=(0,6))
nytaxi_clean[nytaxi_clean.Borough == 'Bronx'].plot(kind='hexbin',x='trip_duration', y='trip_distance', title='Bronx', xlim=(0,1300), ylim=(0,6))
nytaxi_clean[nytaxi_clean.Borough == 'Unknown'].plot(kind='hexbin',x='trip_duration', y='trip_distance', title='Unknown', xlim=(0,1300), ylim=(0,5))

# In[23]
# In the EWR plot we see that data is pushed close to trip_distance = 0
# Doing an histogram for trip_distance for EWR on the full dataframe nytaxi
# It's clear that almost all the trips have trip_distance = 0
# We guess this is because trips to/from the airport have a fixed tariff
# Thus the drivers do not register the trip distance but only the price
nytaxi[nytaxi.Borough == 'EWR'].trip_distance.hist(bins=100)

# In[24]
# Because of this, we decide to remove all the trips starting from EWR
nytaxi_clean = nytaxi_clean.drop(nytaxi_clean[(nytaxi_clean.Borough == "EWR")].index)


# In[17]
# it shows if exist correlation between trip duration and trip distance
nytaxi_clean['trip_duration'].corr(nytaxi_clean['trip_distance'])