# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 12:57:54 2018

@author: mikyl
"""

# In[1]:
import pandas as pd
from scipy.stats import ttest_ind

pd.set_option("display.max_columns",10)

# In[2]:
Location = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-01.csv"   #here is where i save january data

# In[3]:
nytaxi =pd.read_csv(Location, usecols=[1,2,4,7,8,10,16])           #with command usecols i use only columns that i need to solve RQ2

# In[4]:
nytaxi[:3]       

# In[5]:
Location_2 =r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\taxi_zone_lookup.csv"     #here is where i save new vork borough data

# In[6]:
nyBorough =pd.read_csv(Location_2, usecols=[0,1])          

# In[7]:
nyBorough[:3]

# In[8]:
df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')

taxi_and_Borough = df_full

# In[9]
# Let's check the mean values for all the columns by Borough
grouped_mean_full = df_full.groupby(['Borough']).mean()
grouped_mean_full= grouped_mean_full.drop(columns=['PULocationID','DOLocationID'])
print(grouped_mean_full)
# Queens has the highest average on 'trip_distance'
# EWR has the highest fare amount average

# In[10]
# Here we check the distribution of the feature 'trip_distance'
taxi_and_Borough['trip_distance'].plot.box()

# In[11]
# Let's investigate Queens trip_distance
queens = df_full[df_full.Borough == "Queens"] # Select all trips from Queens
queens['trip_distance'].plot.box()
# We can remove outliars with trip_distance > 80

# In[12]
# Let's investigate EWR fare_amount
ewr = df_full[df_full.Borough == "EWR"] # Select all trips from Queens
ewr['fare_amount'].plot.box()
# We can remove outliars with fare_amount > 200

# In[13]
taxi_and_Borough = taxi_and_Borough.drop(taxi_and_Borough[taxi_and_Borough.Borough == 'Unknown'].index) # remove rows with unknown Borough
taxi_and_Borough = taxi_and_Borough.drop(taxi_and_Borough[taxi_and_Borough.trip_distance == 0].index) # remove rows with trip distance = 0
taxi_and_Borough = taxi_and_Borough.drop(taxi_and_Borough[taxi_and_Borough.fare_amount <= 0].index) # remove rows with trip cost < 0
taxi_and_Borough = taxi_and_Borough.drop(taxi_and_Borough[taxi_and_Borough.fare_amount > 200].index) # remove rows with trip cost > 25
taxi_and_Borough = taxi_and_Borough.drop(taxi_and_Borough[taxi_and_Borough.trip_distance > 6].index) # remove rows with trip distance > 6
taxi_and_Borough = taxi_and_Borough.drop(taxi_and_Borough[taxi_and_Borough.total_amount < 2.5].index) # remove rows with total amount < 2.5, less than the minimum fee


# In[14]
fare_mean = taxi_and_Borough.fare_amount.mean()
fare_std = taxi_and_Borough.fare_amount.std()

# In[15]
taxi_and_Borough['price_per_mile'] = taxi_and_Borough.fare_amount / taxi_and_Borough.trip_distance

# In[16]
grouped_mean = taxi_and_Borough.groupby(['Borough']).mean()
grouped_mean = grouped_mean.drop(columns=['PULocationID','DOLocationID'])
grouped_std = taxi_and_Borough.groupby(['Borough']).std()
grouped_std = grouped_std.drop(columns=['PULocationID','DOLocationID'])

# In[17]
# EWR has incredibly high mean for 'price_per_mile'. Let's investigate
taxi_and_Borough.price_per_mile.plot.box();

# In[18]
# There are some outliers due to high cost and small distance. We'll cut them out
taxi_and_Borough = taxi_and_Borough.drop(taxi_and_Borough[taxi_and_Borough.trip_distance < 0.6].index) # remove rows with 'price_per_mile' > 12000
taxi_and_Borough.price_per_mile.plot.box();

# In[19]
grouped = taxi_and_Borough.groupby(by='Borough')
axes = grouped.plot(kind='hist', y="price_per_mile",bins=60, sharex=True, subplots=True )
# https://github.com/pandas-dev/pandas/pull/8018
# In[20]
# H0 = means are the same
# H1 = means are different
ttest_ind(taxi_and_Borough[taxi_and_Borough.Borough == 'Manhattan']['price_per_mile'], taxi_and_Borough[taxi_and_Borough.Borough == 'Queens']['price_per_mile'])