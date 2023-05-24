#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[4]:


df=pd.read_csv(r"C:\Users\panka\OneDrive\Documents\archive\dataset_Facebook.csv",sep=";")


# In[5]:


df


# In[6]:


df.describe()


# In[7]:


df.shape


# In[18]:


df1=df[['Post Month','Post Weekday','Post Hour','Paid']].loc[0:30]


# In[19]:


df1


# In[20]:


df2=df[['Post Month','Post Weekday','Post Hour','Paid']].loc[30:60]
df2


# In[21]:


p=pd.concat([df1,df2])
p


# In[24]:


s=df.sort_values('Category',ascending=False)


# In[25]:


s


# In[26]:


df.transpose()


# In[27]:


df.shape


# In[31]:


r=pd.pivot_table(df,index=['Type','Category'], values='comment')
print(r)


# In[ ]:




