# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 11:20:12 2018

@author: ValerioV
"""
# In[]
import pandas as pd

# In[2]:
from pandas import DataFrame, read_csv

# In[]
import scipy.stats as stats

# In[]
import scipy.stats

# In[]
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

# In[]
nytaxi = pd.read_csv(Location_Jan, usecols=[7,9]) 
nytaxi = pd.concat([nytaxi, pd.read_csv(Location_Feb, usecols=[7,9])])
nytaxi = pd.concat([nytaxi, pd.read_csv(Location_Mar, usecols=[7,9])])
nytaxi = pd.concat([nytaxi, pd.read_csv(Location_Apr, usecols=[7,9])])
nytaxi = pd.concat([nytaxi, pd.read_csv(Location_May, usecols=[7,9])])
nytaxi = pd.concat([nytaxi, pd.read_csv(Location_Jun, usecols=[7,9])])
nytaxi.head()

# In[]
nyBorough =pd.read_csv(Location_taxi_zone, usecols=[0,1])

# In[]
taxi_and_Borough=nytaxi.join(nyBorough.set_index('LocationID'), on='PULocationID')

# In[]
# Group by payment type and borough
df_grouped_p_b = taxi_and_Borough.groupby(['payment_type','Borough']).count() 

# In[]
# Let's visualize data into df_grouped_p_b
df_grouped_p_b

# In[]
# Let's to system out dataframe
df_grouped_p_b = df_grouped_p_b.unstack()

# In[]
df_grouped_p_b

# In[]
df_grouped_p_b.columns = ['Bronx','Brooklyn','EWR','Manhattan','Queens','Staten Island','Unknown']

# In[]
# Let's repeat the usual cleaning operation of the data frame
df_grouped_p_b = df_grouped_p_b.drop('Unknown', axis=1)

# In[]
df_grouped_p_b[:3]

# In[]
# Here is possible visualize the chart for all boroughs
df_grouped_p_b.plot.bar(stacked=True)
# The chart shows that credit or debit card is the most widespread type of payment. In second place we find cash

# In[]
# For a better visulization, let's to plot the outcomes for each borough
df_grouped_p_b.plot(subplots=True,figsize=(8,18),kind='bar',title='Payment type for each borough')

# In[]
# Let's to run chi squared test
df_grouped_p_b

# In[]
# Convert datafram index in a column
df_grouped_p_b['payment_type'] = df_grouped_p_b.index

# In[]
sum_by_payment = df_grouped_p_b.sum(axis=1)

# In[]
# Convert datafram index in a column
sum_by_payment=pd.DataFrame(sum_by_payment)

# In[]
sum_by_payment

# In[]
sum_by_payment.columns=['Sum by payment']

# In[]
sum_by_payment

# In[]
# Let's to run chi squared test
#The H0 (Null Hypothesis): There is relationship between method of payment and borough
#The H1 (Alternative Hypothesis): There is no relationship between method of payment and borough

# In[]
crosstab2 = pd.crosstab(df_grouped_p_b['payment_type'],sum_by_payment['Sum by payment'])

# In[]
stats.chi2_contingency(crosstab2)

#The firt value is chi squared value (12.0), followed by the p-value (0.21330930508341653), then comes the degrees of freedom (9).
#We can reject the null hypothesis as the p-value is less than 0.05
#Moreover, from chi squared table it's possible to see that with 9 degrees of freedom we must reject null hypothesis with chi squared value upper than 16,92
#For this reasons we accept null hypothesis: there's correlation between borough and type of payment 



# Whit other ways, i obtain always the same outcome
# In[]
scipy.stats.chisquare(df_grouped_p_b['payment_type'].value_counts())
# In[]
scipy.stats.chisquare(df_grouped_p_b['Bronx'].value_counts())
# In[]
cont = pd.crosstab(df_grouped_p_b['Bronx'],df_grouped_p_b['payment_type'])
# In[]
scipy.stats.chi2_contingency(cont)

# In[]
crosstab4 = pd.crosstab(df_grouped_p_b['Bronx'],df_grouped_p_b['Brooklyn']) 

# In[]
stats.chi2_contingency(crosstab4)


