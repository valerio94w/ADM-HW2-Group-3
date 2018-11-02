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
Location_Jan = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-01.csv"
Location_Feb = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-02.csv"
Location_Mar = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-03.csv"
Location_Apr = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-04.csv"
Location_May = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-05.csv"
Location_Jun = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-06.csv"

# In[3]:
# Load January
nytaxi = pd.read_csv(Location_Jan, usecols=[1,2,4,7,8,10,16]) 

# In[4]
# Load and concatenate other months
nytaxi = pd.concat([nytaxi, pd.read_csv(Location_Feb, usecols=[1,2,4,7,8,10,16])])
nytaxi = pd.concat([nytaxi, pd.read_csv(Location_Mar, usecols=[1,2,4,7,8,10,16])])
nytaxi = pd.concat([nytaxi, pd.read_csv(Location_Apr, usecols=[1,2,4,7,8,10,16])])
nytaxi = pd.concat([nytaxi, pd.read_csv(Location_May, usecols=[1,2,4,7,8,10,16])])
nytaxi = pd.concat([nytaxi, pd.read_csv(Location_Jun, usecols=[1,2,4,7,8,10,16])])

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

# In[9]
# Convert dates to datetime type
df_full.tpep_pickup_datetime = pd.to_datetime(df_full.tpep_pickup_datetime)
df_full.tpep_dropoff_datetime = pd.to_datetime(df_full.tpep_dropoff_datetime)

# In[10]
# We clone the full dataframe to make cleanings on it
df_clean = df_full

# In[11]
# Let's start cleaning up the data
# First thing is to remove all the trips with 'tpep_pickup' < 2018
df_clean = df_clean[df_clean.tpep_pickup_datetime.dt.year > 2017]
df_clean = df_clean[df_clean.tpep_pickup_datetime.dt.year < 2019]

# In[12]
# Let's create a new column 'trip_duration' with the trip duration in seconds, we'll need it later
df_clean['trip_duration'] = (df_clean.tpep_dropoff_datetime - df_clean.tpep_pickup_datetime).dt.total_seconds()
# Remove all the trips with duration null or negative
df_clean = df_clean[df_clean.trip_duration > 0]

# In[13]
# Let's check the mean values for all the columns by Borough
grouped_mean_full = df_clean.groupby(['Borough']).mean()
grouped_mean_full= grouped_mean_full.drop(columns=['PULocationID','DOLocationID']) # Remove not relevant columns
print(grouped_mean_full)
# Queens has the highest average on 'trip_distance'
# EWR has the highest 'fare_amount' average
# Queens has the highest mean 'trip_duration'

# In[14]
# It's time to start exploring the data
# Here we check the distribution of the feature 'trip_distance'
df_clean['trip_distance'].plot.box()

# In[15]
# There is a clear outlier standing at around 'trip_distance' = 18000.
# Let's cut it out
df_clean = df_clean[df_clean.trip_distance < 25000]
df_clean['trip_distance'].plot.box()

# In[16]
# Again, there are values above 400 miles. Let's cut them out
df_clean = df_clean[df_clean.trip_distance < 400]
df_clean['trip_distance'].plot.box()

# In[17]
# Plot is still too unbalanced, let's try making a new cut at 150 miles
df_clean = df_clean[df_clean.trip_distance < 150]
df_clean['trip_distance'].plot.box()

# In[18]
# Let's investigate Queens trip_distance because it's the borough with the highest average
queens = df_clean[df_clean.Borough == "Queens"] # Select all trips from Queens
queens['trip_distance'].plot.hist(bins=80)

# In[19]
# Analyzing the boxplot we decide to cut out all the trips with distance > 35
# This seems a reasonable value to say that trips inside New York hardly can conver more than these miles
# We can also cut out trips with distance less or equal to zero
df_clean = df_clean.drop(df_clean[df_clean.trip_distance <= 0].index) # remove rows with trip distance <= 0
df_clean = df_clean.drop(df_clean[df_clean.trip_distance > 35].index) # remove rows with trip distance > 60

# In[20]
# We can remove trips with 'total_amount' < 2.50 because is the minimum fee when you call a Taxi in New York
df_clean = df_clean.drop(df_clean[df_clean.total_amount < 2.5].index) # remove rows with total amount < 2.5, less than the minimum fee

# In[21]
# Let's investigate the feature 'fare_amount'
df_clean['fare_amount'].plot.box()

# In[22]
# We can clearly see two outliers staind at around 200000. We cut them out
# Together with the values below or equal to zero
df_clean = df_clean.drop(df_clean[df_clean.fare_amount <= 0].index) # remove rows with fare_amount <= 0
df_clean = df_clean.drop(df_clean[df_clean.fare_amount > 50000].index) # remove rows with fare_amount > 50000
df_clean['fare_amount'].plot.box()

# In[23]
# We see other outliers above 2000, we can remove them
df_clean = df_clean.drop(df_clean[df_clean.fare_amount > 2000].index) # remove rows with fare_amount > 2000
df_clean['fare_amount'].plot.box()

# In[24]
# We do another cut at 800
df_clean = df_clean.drop(df_clean[df_clean.fare_amount > 800].index) # remove rows with fare_amount > 800
df_clean['fare_amount'].plot.box()

# In[25]
# The plot is still unbalanced, we do another cut at 300
df_clean = df_clean.drop(df_clean[df_clean.fare_amount > 300].index) # remove rows with fare_amount > 300
df_clean['fare_amount'].plot.box()

# In[26]
# To make the things clearer, let's investigate the 'fare_amount' in EWR, the borough with the highest average
ewr = df_clean[df_clean.Borough == "EWR"] # Select all trips from EWR
ewr['fare_amount'].plot.hist(bins=50)

# In[27]
# Around 150 there is a slightly higher frequency of occurrencies that might be relevant
# So we decide to cut starting from 175
df_clean = df_clean.drop(df_clean[df_clean.fare_amount > 175].index) # remove rows with fare_amount > 175

# In[28]
# We create a new column 'trip_duration' with the duration of the trip in seconds (we will need this also later)
df_clean['trip_duration'] = (df_clean.tpep_dropoff_datetime - df_clean.tpep_pickup_datetime).dt.total_seconds()
df_clean.trip_duration.plot.box()

# In[29]
# There are three outliers, we remove them
# We remove also trips with duration lower or equal to 0
df_clean = df_clean.drop(df_clean[df_clean.trip_duration <= 0].index) # remove rows with fare_amount > 300
df_clean = df_clean.drop(df_clean[df_clean.trip_duration > 100000].index) # remove rows with fare_amount > 300
df_clean.trip_duration.plot.box()

# In[28]
# In the dataset we have many rows with 'Unknown' borough.
# We want to try to re-allocate the trips to the borough with the closest behaviour
# Let's recalculate the means and the stds for the boroughs
grouped_mean_full = df_clean.groupby(['Borough']).mean()
grouped_mean_full= grouped_mean_full.drop(columns=['PULocationID','DOLocationID']) # Remove not relevant columns
print(grouped_mean_full)

# In[29]
# According to the means, Unknown seems to be close to Manhattan.
# Let's compare some distributions

unknown = df_clean[df_clean.Borough == "Unknown"] # Select all trips from Unknown
manhattan = df_clean[df_clean.Borough == "Manhattan"] # Select all trips from Manhattan



# In[28]
# We remove also all the rows with unknown borough
#df_clean = df_clean.drop(df_clean[df_clean.Borough == 'Unknown'].index)

# In[20]
fare_mean = df_clean.fare_amount.mean()
fare_std = df_clean.fare_amount.std()

# In[21]
df_clean['price_per_mile'] = df_clean.fare_amount / df_clean.trip_distance

# In[22]
grouped_mean = df_clean.groupby(['Borough']).mean()
grouped_mean = grouped_mean.drop(columns=['PULocationID','DOLocationID'])
grouped_std = df_clean.groupby(['Borough']).std()
grouped_std = grouped_std.drop(columns=['PULocationID','DOLocationID'])

# In[23]
# EWR has incredibly high mean for 'price_per_mile'. Let's investigate
df_clean.price_per_mile.plot.box();

# In[24]
# There are some outliers due to high cost and small distance. We'll cut them out
df_clean = df_clean.drop(df_clean[df_clean.trip_distance < 0.6].index) # remove rows with 'price_per_mile' > 12000
df_clean.price_per_mile.plot.box();

# In[25]
grouped = df_clean.groupby(by='Borough')
axes = grouped.plot(kind='hist', y="price_per_mile",bins=60, sharex=True, subplots=True )
# https://github.com/pandas-dev/pandas/pull/8018

# In[26]
# H0 = means are the same
# H1 = means are different

ttest_matrix = pd.DataFrame(index=df_clean.Borough.unique(), columns=df_clean.Borough.unique())

for col1 in df_clean.Borough.unique():
    for col2 in df_clean.Borough.unique():
        ttest_matrix.loc[col1,col2] = ttest_ind(df_clean[df_clean.Borough == col1]['price_per_mile'], df_clean[df_clean.Borough == col2]['price_per_mile']).pvalue
        
# In[27]
ttest_matrix = ttest_matrix.apply(pd.to_numeric)
print(ttest_matrix)

# We consider pvalue = 0.05 as a treshold to reject the H0.
# Pvalues higher than 0.05 mean that Boroughs have the same mean (we accept the H0)
# Pvalues lower than 0.05 mean that Boroughs have different mean (we reject the H0)

# In[28]
# We create a new column 'trip_duration' with the duration of the trip in seconds
df_clean['trip_duration'] = (df_clean.tpep_dropoff_datetime - df_clean.tpep_pickup_datetime).dt.total_seconds()
df_clean.trip_duration.plot.box()

# In[29]
# We need to remove all the rows with a negative duration

# In[29]
# We create a new column with 'ppm_adj'
df_clean['ppm_adj'] = df_clean.fare_amount/df_clean.trip_duration

# In[30]
# Let's update the tables with mean and std with the new columns
grouped_mean = df_clean.groupby(['Borough']).mean()
grouped_mean = grouped_mean.drop(columns=['PULocationID','DOLocationID'])
grouped_std = df_clean.groupby(['Borough']).std()
grouped_std = grouped_std.drop(columns=['PULocationID','DOLocationID'])

# In[31]
# Plot the distribution for all the boroughs
grouped = df_clean.groupby(by='Borough')
axes = grouped.plot(kind='hist', y="ppm_adj",bins=60, sharex=True, subplots=True )
# https://github.com/pandas-dev/pandas/pull/8018

# In[32]
# In[26]
# H0 = means are the same
# H1 = means are different

ttest_matrix_adj = pd.DataFrame(index=df_clean.Borough.unique(), columns=df_clean.Borough.unique())

for col1 in df_clean.Borough.unique():
    for col2 in df_clean.Borough.unique():
        ttest_matrix_adj.loc[col1,col2] = ttest_ind(df_clean[df_clean.Borough == col1]['ppm_adj'], df_clean[df_clean.Borough == col2]['ppm_adj']).pvalue
        
# In[27]
ttest_matrix_adj = ttest_matrix_adj.apply(pd.to_numeric)
print(ttest_matrix_adj)

# We consider pvalue = 0.05 as a treshold to reject the H0.
# Pvalues higher than 0.05 mean that Boroughs have the same mean (we accept the H0)
# Pvalues lower than 0.05 mean that Boroughs have different mean (we reject the H0)

# It happened that now all the boroughs seem correlated, thus there are not more expensive boroughs
