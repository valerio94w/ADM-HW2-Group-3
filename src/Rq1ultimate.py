# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 22:56:59 2018

@author: ValerioV
"""

import pandas as pd

# In[2]:
from pandas import DataFrame, read_csv

# In[3]:
# Location indicates the place where we save my monthly data
Location_Jan = r"C:\Users\ValerioV\Downloads\yellow_tripdata_2018-01.csv"
Location_Feb = r"C:\Users\ValerioV\Downloads\yellow_tripdata_2018-02.csv"
Location_Mar = r"C:\Users\ValerioV\Downloads\yellow_tripdata_2018-03.csv"
Location_Apr = r"C:\Users\ValerioV\Downloads\yellow_tripdata_2018-04.csv"
Location_May = r"C:\Users\ValerioV\Downloads\yellow_tripdata_2018-05.csv"
Location_Jun = r"C:\Users\ValerioV\Downloads\yellow_tripdata_2018-06.csv"

# In[]
# Location_taxi_zone indicates the place where we save dataframe about New York's Boroughs and their Location ID
Location_taxi_zone = r"C:\Users\ValerioV\Downloads\taxi _zone_lookup.csv"

# In[9]:
# We've uploaded all available monthly dataframes of year 2018
nytaxi_january = pd.read_csv(Location_Jan, usecols=[1,7])
nytaxi_february = pd.read_csv(Location_Feb, usecols=[1,7])
nytaxi_march = pd.read_csv(Location_Mar, usecols=[1,7])
nytaxi_april = pd.read_csv(Location_Apr, usecols=[1,7])
nytaxi_may = pd.read_csv(Location_May, usecols=[1,7])
nytaxi_june = pd.read_csv(Location_Jun, usecols=[1,7])

# In[7]:
Location_taxi_zone =r"C:\Users\ValerioV\Downloads\taxi _zone_lookup.csv" 

# In[8]:
nyBorough =pd.read_csv(Location_taxi_zone, usecols=[0,1])

# In[9]:
# Now we need to add a new column with the indication of the Borough. We decide to use the pick up location as reference
taxi_and_Borough_january=nytaxi_january.join(nyBorough.set_index('LocationID'), on='PULocationID')

# In[13]:
# Here we group january data by borough and we compute montlhy average of trips 
january_average =taxi_and_Borough_january['Borough'].value_counts()/31

# In[]
# we create a dataframe with january average for each borough
january_average=pd.DataFrame(january_average)

# In[]
january_average

# In[]
# We decide to cut down from our analysis values that have unkown borough]
january_average = january_average.drop('Unknown', axis=0)

# In[]
january_average

# In[]
# We denomite column with the name 'January'
january_average.columns=['January']

# In[18]:
# Let's to visualize january average for each borough
january_average

# In[19]:
# For a better visualization, we decide to round values with two decimal places
january_average = round(january_average,2)  

# In[ ]:
january_average

# In[31]:
# Now, we are going to compute others monthly averages replacing the same steps
taxi_and_Borough_february=nytaxi_february.join(nyBorough.set_index('LocationID'), on='PULocationID')

# In[]
february_average = taxi_and_Borough_february['Borough'].value_counts()/28

# In[]
february_average=pd.DataFrame(february_average)

# In[]
february_average = february_average.drop('Unknown', axis=0)

# In[]
february_average.columns=['February']

# In[19]:
february_average = round(february_average,2)  

# In[ ]:
february_average

# In[85]:
taxi_and_Borough_march=nytaxi_march.join(nyBorough.set_index('LocationID'), on='PULocationID')

# In[]
march_average = taxi_and_Borough_march['Borough'].value_counts()/31

# In[]
march_average=pd.DataFrame(march_average)

# In[]
march_average = march_average.drop('Unknown', axis=0)

# In[]
march_average.columns=['March']

# In[19]:
march_average = round(march_average,2)  

# In[ ]:
march_average

# In[85]:
taxi_and_Borough_april=nytaxi_april.join(nyBorough.set_index('LocationID'), on='PULocationID')

# In[]
april_average = taxi_and_Borough_april['Borough'].value_counts()/30

# In[]
april_average=pd.DataFrame(april_average)

# In[]
april_average = april_average.drop('Unknown', axis=0)

# In[]
april_average.columns=['April']

# In[19]:
april_average = round(april_average,2) 

# In[]
april_average 

# In[85]:
taxi_and_Borough_may=nytaxi_may.join(nyBorough.set_index('LocationID'), on='PULocationID')

# In[ ]:
may_average= taxi_and_Borough_may['Borough'].value_counts()/31

# In[]
may_average=pd.DataFrame(may_average)

# In[]
may_average = may_average.drop('Unknown', axis=0)

# In[]
may_average.columns=['May']

# In[19]:
may_average = round(may_average,2)  

# In[ ]:
may_average

# In[45]:
taxi_and_Borough_june=nytaxi_june.join(nyBorough.set_index('LocationID'), on='PULocationID')

# In[ ]:
june_average= taxi_and_Borough_june['Borough'].value_counts()/30

# In[]
june_average=pd.DataFrame(june_average)

# In[]
june_average = june_average.drop('Unknown', axis=0)

# In[]
june_average.columns=['June']

# In[19]:
june_average = round(june_average,2)  

# In[ ]:
june_average

# In[6july_average.hist()
# now, we create a dataframe which contains monthly averages of taxis trips for each borough
monthly_average=pd.concat([january_average,february_average,march_average,april_average,may_average,june_average], axis=1,sort=True)

# In[72]:
monthly_average

# In[87]:
monthly_average_trasposed= monthly_average.T   #i use this command to traspose dataframe 

# In[]
monthly_average_trasposed

# In[]
monthly_average_trasposed.plot.bar()
# In[]
monthly_average_trasposed.plot.bar(subplots=True, figsize=(8,15), sharex=False, title='Monthly average taxis trips')

