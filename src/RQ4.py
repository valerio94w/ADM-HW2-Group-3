# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 11:10:25 2018

@author: mikyl
"""

#!/usr/bin/env python
# coding: utf-8

# In[1]:
import pandas as pd
import scipy.stats as stats

# In[2]:
Location = r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\yellow_tripdata_2018-01.csv"   #here is where i save january data

# In[3]:
nytaxi =pd.read_csv(Location, usecols=[7,9])           #with command usecols i use only columns that i need to solve RQ2

# In[4]:
nytaxi[:3]       

# In[5]:
Location_2 =r"C:\Users\mikyl\Documents\GitHub\ADM-HW2-Group-3\data\taxi_zone_lookup.csv"     #here is where i save new vork borough data

# In[6]:
nyBorough =pd.read_csv(Location_2, usecols=[0,1])          

# In[7]:
nyBorough[:3]

# In[8]:
taxi_and_Borough=nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')

# In[9]
df_grouped = taxi_and_Borough.groupby(['payment_type','Borough']).count() # group by payment type and borough
df_grouped = df_grouped.unstack()

# In[10]
df_grouped.columns = ['Bronx','Brooklyn','EWR','Manhattan','Queens','Staten Island','Unknown']
df_grouped = df_grouped.drop('Unknown', axis=1)

# In[11]
df_grouped[:3]

# In[12]
df_grouped.plot.bar(stacked=True);

# In[13]
df_grouped.plot(subplots=True,figsize=(8,18),kind='bar') # Plot everything

# In[14]
sum_by_borough = df_grouped.sum()
sum_by_payment = df_grouped.sum(axis=1)
grandtotal = sum_by_borough.sum()

# In[15]
chi2, p, dof, expected = stats.chi2_contingency(df_grouped)