#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


from pandas import DataFrame, read_csv


# In[3]:


Location = r"F:\Valerio\yellow_tripdata_2018-01.csv"   #here is where i save january data


# In[5]:


nytaxi_january =pd.read_csv(Location, usecols=[1,7])

# In[6]:


nytaxi_january[:3]  


# In[7]:


Location_taxi_zone =r"C:\Users\ValerioV\Downloads\taxi _zone_lookup.csv" 


# In[8]:


nyBorough =pd.read_csv(Location_taxi_zone, usecols=[0,1])


# In[9]:


taxi_and_Borough_january=nytaxi_january.join(nyBorough.set_index('LocationID'), on='PULocationID')


# In[10]:


taxi_and_Borough_january[:3]


# In[12]:


Borough_grouped_january = taxi_and_Borough_january.groupby('Borough')   #groups data by borough


# In[13]:


# In[13]:


taxi_and_Borough_january['Borough'].value_counts()


# In[15]:


taxi_and_Borough_january=taxi_and_Borough_january[taxi_and_Borough_january.Borough != 'Unknown']


# In[17]:


january_average =taxi_and_Borough_january['Borough'].value_counts()/31


# In[18]:


january_average


# In[19]:


round(january_average,2)  


# In[ ]:





# In[20]:


january_average=round(january_average,2) 


# In[21]:


january_average=pd.DataFrame(january_average)


# In[77]:


january_average[:3]


# In[22]:


january_average.columns=['January']


# In[31]:


Location_february =r"F:\Valerio\yellow_tripdata_2018-02.csv"


# In[32]:


ny_taxi_february =pd.read_csv(Location_february, usecols=[1,7])


# In[79]:


taxi_and_Borough_february=ny_taxi_february.join(nyBorough.set_index('LocationID'), on='PULocationID')


# In[80]:


Borough_grouped_february = taxi_and_Borough_february.groupby('Borough')


# In[81]:


taxi_and_Borough_february['Borough'].value_counts()


# In[82]:


taxi_and_Borough_february=taxi_and_Borough_february[taxi_and_Borough_february.Borough != 'Unknown']


# In[83]:


february_average = taxi_and_Borough_february['Borough'].value_counts()/31


# In[84]:


february_average = round(february_average,2)  


# In[85]:



february_average


# In[33]:


Location_3="F:\Valerio\yellow_tripdata_2018-03.csv"


# In[34]:


nytaxi_march =pd.read_csv(Location_3, usecols=[1,7])


# In[35]:


taxi_and_Borough_march=nytaxi_march.join(nyBorough.set_index('LocationID'), on='PULocationID')


# In[36]:


Borough_grouped_march = taxi_and_Borough_march.groupby('Borough').count()


# In[37]:


taxi_and_Borough_march=taxi_and_Borough_march[taxi_and_Borough_march.Borough != 'Unknown']


# In[38]:


march_average = taxi_and_Borough_march['Borough'].value_counts()/31


# In[84]:


march_average=round(march_average,2) 


# In[83]:


march_average


# In[82]:


march_average 


# In[81]:


february_average=pd.DataFrame(february_average)
february_average.columns=['February']

# In[42]:

march_average=pd.DataFrame(march_average)
march_average.columns=['March']


# In[168]:


first_2=january_average.join(february_average) 


# In[ ]:
first_3 = first_2.join(march_average)
first_3





# In[44]:
Location_4="F:\Valerio\yellow_tripdata_2018-04.csv"

nytaxi_april=pd.read_csv(Location_4, usecols=[1,7])


# In[ ]:



ny_taxi_april =pd.read_csv(Location_4, usecols=[1,7])



# In[ ]:


taxi_and_Borough_april=nytaxi_april.join(nyBorough.set_index('LocationID'), on='PULocationID')


Borough_grouped_april = taxi_and_Borough_april.groupby('Borough').count()
taxi_and_Borough_april=taxi_and_Borough_april[taxi_and_Borough_april.Borough != 'Unknown']


# In[38]:


april_average = taxi_and_Borough_april['Borough'].value_counts()/31


# In[84]:


april_average=round(april_average,2) 


# In[83]:


april_average
april=pd.DataFrame(april_average)


# In[70]:


april_average.columns=['April']

first_4=first_3.join(april_average)
first_4
# In[45]:


Location_5="F:\Valerio\yellow_tripdata_2018-05.csv"


# In[46]:


nytaxi_may =pd.read_csv(Location_5, usecols=[1,7])


# In[47]:


taxi_and_Borough_may=nytaxi_may.join(nyBorough.set_index('LocationID'), on='PULocationID')


# In[48]:


Borough_grouped_may = taxi_and_Borough_may.groupby('Borough')


# In[49]:


taxi_and_Borough_may=taxi_and_Borough_may[taxi_and_Borough_may.Borough != 'Unknown']


# In[50]:


may_average = taxi_and_Borough_may['Borough'].value_counts()/31


# In[51]:


may_average=round(may_average,2) 


# In[53]:


may_average


# In[ ]:





# In[69]:


may_average=pd.DataFrame(may_average)


# In[70]:


may_average.columns=['May']

first_5 = first_4.join(may_average)
# In[52]:


Location_6="F:\Valerio\yellow_tripdata_2018-06.csv"
Location_4="F:\Valerio\yellow_tripdata_2018-04.csv"

# In[54]:


nytaxi_july=pd.read_csv(Location_6, usecols=[1,7])


# In[55]:


taxi_and_Borough_july=nytaxi_july.join(nyBorough.set_index('LocationID'), on='PULocationID')


# In[145]:


taxi_and_Borough_july[:3]


# In[56]:


Borough_grouped_july = taxi_and_Borough_july.groupby('Borough')


# In[57]:


taxi_and_Borough_july=taxi_and_Borough_july[taxi_and_Borough_july.Borough != 'Unknown']


# In[58]:


july_average = taxi_and_Borough_july['Borough'].value_counts()/31


# In[59]:


july_average=round(july_average,2) 


# In[60]:


july_average


# In[147]:





# In[61]:


july_average=pd.DataFrame(july_average)


# In[149]:


print(type(july_average))


# In[62]:


july_average[:3]


# In[63]:


july_average.columns=['July']


# In[6july_average.hist()
monthly_average=pd.concat([january_average,february_average,march_average,april_average,may_average,july_average], axis=1,sort=True)

# In[140



# In[71]:




# In[72]:


monthly_average


# Inuly_average)


# In[75]:


monthly_average.plot.bar(stacked=True)


# In[87]:

monthly_average= monthly_average.T   #i use this command to traspose dataframe 

monthly_average


monthly_average_trasposed.plot.bar()
# In[]

monthly_average_trasposed.plot.bar(subplots=True, figsize=(8,15), sharex=False, title='use of taxis')
# In[]

# In[]
