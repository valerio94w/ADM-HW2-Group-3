# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 12:57:54 2018

@author: mikyl
"""
# <markdowncell>
# Let's import all the needed libraries

# <codecell>
import pandas as pd
import scipy.stats as stats
from matplotlib import pyplot
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns",10)

# <codecell>
Location_Jan = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-01.csv"
Location_Feb = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-02.csv"
Location_Mar = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-03.csv"
Location_Apr = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-04.csv"
Location_May = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-05.csv"
Location_Jun = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-06.csv"

# <codecell>
# Load all the datasets
nytaxi = pd.read_csv(Location_Jan, usecols=[1,2,4,7,8,10,16]) 
nytaxi = pd.concat([nytaxi, pd.read_csv(Location_Feb, usecols=[1,2,4,7,8,10,16])])
nytaxi = pd.concat([nytaxi, pd.read_csv(Location_Mar, usecols=[1,2,4,7,8,10,16])])
nytaxi = pd.concat([nytaxi, pd.read_csv(Location_Apr, usecols=[1,2,4,7,8,10,16])])
nytaxi = pd.concat([nytaxi, pd.read_csv(Location_May, usecols=[1,2,4,7,8,10,16])])
nytaxi = pd.concat([nytaxi, pd.read_csv(Location_Jun, usecols=[1,2,4,7,8,10,16])])     

# <codecell>
Location_2 =r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\taxi_zone_lookup.csv"     #here is where i save new vork borough data

# <codecell>
nyBorough =pd.read_csv(Location_2, usecols=[0,1])          

# <codecell>
df_full = nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')

# <codecell>
# Convert dates to datetime type
df_full.tpep_pickup_datetime = pd.to_datetime(df_full.tpep_pickup_datetime)
df_full.tpep_dropoff_datetime = pd.to_datetime(df_full.tpep_dropoff_datetime)

# <codecell>
# We clone the full dataframe to make cleanings on it
df_clean = df_full

# <codecell>
# Let's start cleaning up the data
# First thing is to remove all the trips with 'tpep_pickup' < 2017 and > 2019, errors
df_clean = df_clean[df_clean.tpep_pickup_datetime.dt.year > 2017]
df_clean = df_clean[df_clean.tpep_pickup_datetime.dt.year < 2019]

# <codecell>
# Let's create a new column 'trip_duration' with the trip duration in seconds, we'll need it later
df_clean['trip_duration'] = (df_clean.tpep_dropoff_datetime - df_clean.tpep_pickup_datetime).dt.total_seconds()
# Remove all the trips with duration null or negative
df_clean = df_clean[df_clean.trip_duration > 0]

# <codecell>
# According the analysis ran in RQ5, we remove from the dataset all the trips started from EWR
df_clean = df_clean[df_clean.Borough != 'EWR']

# <codecell>
# Let's check the mean values for all the columns by Borough
grouped_mean = df_clean.groupby(['Borough']).mean()
grouped_mean= grouped_mean.drop(columns=['PULocationID','DOLocationID']) # Remove not relevant columns
print(grouped_mean)
# Queens has the highest average on 'trip_distance'
# Staten Island has the highest 'fare_amount' average
# Queens has the highest mean 'trip_duration'

# <codecell>
# It's time to start exploring the data
# Here we check the distribution of the feature 'trip_distance'
df_clean['trip_distance'].plot.box()

# <codecell>
# According to RQ5, let's do a first cut at 150
df_clean = df_clean[df_clean.trip_distance < 150]
df_clean['trip_distance'].plot.hist(bins=100)

# <codecell>
# Let's investigate Queens trip_distance because it's the borough with the highest average
queens = df_clean[df_clean.Borough == "Queens"] # Select all trips from Queens
queens['trip_distance'].plot.hist(bins=80)

# <codecell>
# Analyzing the histogram we decide to cut out all the trips with distance > 35
# This seems a reasonable value to say that trips inside New York hardly can conver more than these miles
# We can also cut out trips with distance less or equal to zero
df_clean = df_clean.drop(df_clean[df_clean.trip_distance <= 0].index) # remove rows with trip distance <= 0
df_clean = df_clean.drop(df_clean[df_clean.trip_distance > 35].index) # remove rows with trip distance > 60
df_clean['trip_distance'].plot.hist(bins=100)

# <codecell>
# We can remove trips with 'total_amount' < 2.50 because is the minimum fee when you call a Taxi in New York
df_clean = df_clean.drop(df_clean[df_clean.total_amount < 2.5].index) # remove rows with total amount < 2.5, less than the minimum fee

# <codecell>
# Let's investigate the feature 'fare_amount'
df_clean['fare_amount'].plot.box()

# <codecell>
# We can clearly see two outliers staind at around 200000. We cut them out
# Together with the values below or equal to zero
df_clean = df_clean.drop(df_clean[df_clean.fare_amount <= 0].index) # remove rows with fare_amount <= 0
df_clean = df_clean.drop(df_clean[df_clean.fare_amount > 50000].index) # remove rows with fare_amount > 50000
df_clean['fare_amount'].plot.box()

# <codecell>
# We see other outliers above 2000, we can remove them
df_clean = df_clean.drop(df_clean[df_clean.fare_amount > 2000].index) # remove rows with fare_amount > 2000
df_clean['fare_amount'].plot.box()

# <codecell>
# We do another cut at 800
df_clean = df_clean.drop(df_clean[df_clean.fare_amount > 800].index) # remove rows with fare_amount > 800
df_clean['fare_amount'].plot.box()

# In[23]
# The plot is still unbalanced, we do another cut at 300
df_clean = df_clean.drop(df_clean[df_clean.fare_amount > 300].index) # remove rows with fare_amount > 300
df_clean['fare_amount'].plot.hist(bins=100)

# <codecell>
# Let's go down to 150
df_clean = df_clean.drop(df_clean[df_clean.fare_amount > 150].index) # remove rows with fare_amount > 175
df_clean['fare_amount'].plot.hist(bins=100)

# <codecell>
# Staten Island is the Borough with the highes fare amount, let's investgare the distribution
df_clean[df_clean.Borough == 'Staten Island'].fare_amount.plot.hist(bins = 100)

# <codecell>
# We can cut at 110
df_clean = df_clean.drop(df_clean[df_clean.fare_amount > 110].index) # remove rows with fare_amount > 110
df_clean['fare_amount'].plot.hist(bins=100)

# <codecell>
# Let's check the feature trip_duration
df_clean.trip_duration.plot.box()

# <codecell>
# There are three outliers, we remove them
# We remove also trips with duration lower or equal to 60, and > 5000, according to RQ5
df_clean = df_clean.drop(df_clean[df_clean.trip_duration <= 60].index)
df_clean = df_clean.drop(df_clean[df_clean.trip_duration > 7500].index)
df_clean.trip_duration.plot.hist(bins=100)

# <codecell>
# In the dataset we have many rows with 'Unknown' borough.
# We want to try to re-allocate the trips to the borough with the closest behaviour
# Let's recalculate the means and the stds for the boroughs
grouped_mean = df_clean.groupby(['Borough']).mean()
grouped_mean = grouped_mean.drop(columns=['PULocationID','DOLocationID']) # Remove not relevant columns
print(grouped_mean)

# <codecell>
# According to the means, Unknown seems to be close to Manhattan.
# Let's compare some distributions
unknown = df_clean[df_clean.Borough == "Unknown"] # Select all trips from Unknown
manhattan = df_clean[df_clean.Borough == "Manhattan"] # Select all trips from Manhattan

# <codecell>
# Plot trip_distance distribution comparison
bins = pd.np.linspace(0, 35, 100)

pyplot.hist(manhattan.trip_distance, bins, alpha=0.5, label='Manhattan', density=True)
pyplot.hist(unknown.trip_distance, bins, alpha=0.5, label='Unknown', density=True)
pyplot.legend(loc='upper right')
pyplot.show()

# <codecell>
# Plot trip_duration distribution comparison

bins = pd.np.linspace(0, 5000, 100)

pyplot.hist(manhattan.trip_duration, bins, alpha=0.5, label='Manhattan', density=True)
pyplot.hist(unknown.trip_duration, bins, alpha=0.5, label='Unknown', density=True)
pyplot.legend(loc='upper right')
pyplot.show()

# <codecell>
# Plot fare_amount distribution comparison

bins = pd.np.linspace(0, 60, 60)

pyplot.hist(manhattan.fare_amount, bins, alpha=0.5, label='Manhattan', density=True)
pyplot.hist(unknown.fare_amount, bins, alpha=0.5, label='Unknown', density=True)
pyplot.legend(loc='upper right')
pyplot.show()

# <codecell>
# All the three main features present the same behaviour between Unknown and Manhattan
# Thus we replace all the Unknown with Manhattan
df_clean.loc[df_clean.Borough == 'Unknown', 'Borough'] = 'Manhattan'

# <codecell>
# Let's calculate the fare_amount mean and std
fare_mean = df_clean.fare_amount.mean()
fare_std = df_clean.fare_amount.std()

# <codecell>
# We create a new column price_per_mile
df_clean['price_per_mile'] = df_clean.fare_amount / df_clean.trip_distance

# <codecell>
# Let's check the distribution of the price_per_mile
df_clean.price_per_mile.plot.box()

# <codecell>
# There are some outliers. We'll cut them out
df_clean = df_clean.drop(df_clean[df_clean.price_per_mile > 25].index) # remove rows with 'price_per_mile' > 40
df_clean = df_clean.drop(df_clean[df_clean.price_per_mile < 1].index) # remove rows with 'price_per_mile' < 1

df_clean.price_per_mile.plot.hist(bins=100)

# <codecell>
grouped_mean = df_clean.groupby(['Borough']).mean()
grouped_mean = grouped_mean.drop(columns=['PULocationID','DOLocationID'])
grouped_std = df_clean.groupby(['Borough']).std()
grouped_std = grouped_std.drop(columns=['PULocationID','DOLocationID'])

# <codecell>
# Plot the kde for each borough
sns.kdeplot(df_clean.price_per_mile[df_clean.Borough == "Queens"],label='Queens');
sns.kdeplot(df_clean.price_per_mile[df_clean.Borough == "Manhattan"],label='Manhattan');
sns.kdeplot(df_clean.price_per_mile[df_clean.Borough == "Brooklyn"],label='Brooklyn');
sns.kdeplot(df_clean.price_per_mile[df_clean.Borough == "Bronx"],label='Bronx');
sns.kdeplot(df_clean.price_per_mile[df_clean.Borough == "Staten Island"],label='Staten Island');

# <codecell>
plt.xlabel('$/miles')
plt.ylabel('KDE')
plt.title('Price per mile distribution over Boroughs')
plt.show()

# <codecell>
# Let's do a t-test on the price_per_mile series
# H0 = means are the same
# H1 = means are different

ttest_matrix = pd.DataFrame(index=df_clean.Borough.unique(), columns=df_clean.Borough.unique())

for col1 in df_clean.Borough.unique():
    for col2 in df_clean.Borough.unique():
        ttest_matrix.loc[col1,col2] = stats.ttest_ind(df_clean[df_clean.Borough == col1]['price_per_mile'], df_clean[df_clean.Borough == col2]['price_per_mile']).pvalue
        
# <codecell>
ttest_matrix = ttest_matrix.apply(pd.to_numeric)
print(ttest_matrix)

# We consider pvalue = 0.05 as a treshold to reject the H0.
# Pvalues higher than 0.05 mean that Boroughs have the same mean (we accept the H0)
# Pvalues lower than 0.05 mean that Boroughs have different mean (we reject the H0)
# H0 is rejected for all the pairs

# <codecell>
# We create a new column with 'ppm_adj'
df_clean['ppm_adj'] = df_clean.fare_amount/df_clean.trip_duration

# <codecell>
# Plot the kde for each borough
sns.distplot(df_clean.ppm_adj[df_clean.Borough == "Queens"],label='Queens', hist=True, kde=False);
sns.distplot(df_clean.ppm_adj[df_clean.Borough == "Manhattan"],label='Manhattan', hist=True, kde=False);
sns.distplot(df_clean.ppm_adj[df_clean.Borough == "Brooklyn"],label='Brooklyn', hist=True, kde=False);
sns.distplot(df_clean.ppm_adj[df_clean.Borough == "Bronx"],label='Bronx', hist=True, kde=False);
sns.distplot(df_clean.ppm_adj[df_clean.Borough == "Staten Island"],label='Staten Island', hist=True, kde=False);

# beautifying the labels
plt.xlabel('$/miles s')
plt.ylabel('Frequency (normed)')
plt.title('Price per mile adjusted distribution over Boroughs')
plt.show()

# <codecell>
# Let's update the tables with mean and std with the new columns
grouped_mean = df_clean.groupby(['Borough']).mean()
grouped_mean = grouped_mean.drop(columns=['PULocationID','DOLocationID'])
grouped_std = df_clean.groupby(['Borough']).std()
grouped_std = grouped_std.drop(columns=['PULocationID','DOLocationID'])

# <codecell>
# H0 = means are the same
# H1 = means are different

ttest_matrix_adj = pd.DataFrame(index=df_clean.Borough.unique(), columns=df_clean.Borough.unique())

for col1 in df_clean.Borough.unique():
    for col2 in df_clean.Borough.unique():
        ttest_matrix_adj.loc[col1,col2] = stats.ttest_ind(df_clean[df_clean.Borough == col1]['ppm_adj'], df_clean[df_clean.Borough == col2]['ppm_adj']).pvalue
        
# <codecell>
ttest_matrix_adj = ttest_matrix_adj.apply(pd.to_numeric)
print(ttest_matrix_adj)

# We consider pvalue = 0.05 as a treshold to reject the H0.
# Pvalues higher than 0.05 mean that Boroughs have the same mean (we accept the H0)
# Pvalues lower than 0.05 mean that Boroughs have different mean (we reject the H0)

# It happened that again all the boroughs have different means, so there are boroughs more expensive than others
