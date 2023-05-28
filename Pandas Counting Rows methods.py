#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

# count rows  using len


data = {
    "name":["John","Rahul","Roshan"],
    "age":[12,66,33]
}

df= pd.DataFrame(data)

df


# In[5]:


num_of_rows =len(df)

num_of_rows


# In[9]:


# count rows by shape 

num_of_rows = df.shape 

num_of_rows # returns rows and columns 


# In[11]:


num_of_rows= df.shape[0]

num_of_rows # only return the rows 


# In[12]:


# using index 

num_of_rows = df.index 

num_of_rows # returns in the form of tuple (start is starting value , stop is the ending value and 
# step is the step value by defalt 1)


# In[14]:


num_of_rows = df.index.size  # it returns only the number of rows 

num_of_rows


# In[15]:


num_of_rows = len(df.index) # returns the number of rows 

num_of_rows


# In[16]:


# using axes 

num_of_rows = df.axes

num_of_rows


# In[18]:


num_of_rows = df.axes[0].shape 

num_of_rows


# In[19]:


num_of_rows = df.axes[0] # returns in the form of tuple(start,stop,step)
num_of_rows


# In[21]:


num_of_rows = len(df.axes[0]) # returns the number of rows 
num_of_rows 


# In[ ]:




