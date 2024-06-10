#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


dataframe = pd.read_csv(r"C:\Users\NIKHIL\OneDrive\Documents\ONE\OneDrive\Desktop\intern\01.Data Cleaning and Preprocessing.csv")


# In[3]:


print(dataframe)


# In[5]:


type(dataframe)


# In[11]:


##data filtering based on condition
dataframe.loc[dataframe['Y-Kappa']<24]


# In[17]:


dataframe['ChipRate']


# In[13]:


dataframe.loc[dataframe['ChipRate']==16.520]


# In[15]:


dataframe.loc[dataframe['BlowFlow'] == 11]


# In[16]:


##handling missing values using dropna and fillna
dataframe.dropna()


# In[18]:


##filling missing values with null
dataframe.fillna('NULL')


# In[20]:


##summary statistics of the dataframe
print(dataframe['Y-Kappa'].mean())


# In[21]:


print(dataframe['Y-Kappa'].median())


# In[22]:


print(dataframe['Y-Kappa'].mode())

