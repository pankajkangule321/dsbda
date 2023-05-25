#!/usr/bin/env python
# coding: utf-8

# In[3]:


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# In[31]:


df=pd.read_csv(r"C:\Users\panka\OneDrive\Documents\heart.csv", sep=',')


# In[32]:


df


# In[33]:


df.sample(5)


# In[34]:


plt.figure(figsize=(15,11))


# In[35]:


sns.heatmap(df.corr(),annot=True)


# In[38]:


plt.hist(df['age'], bins=10, edgecolor='k')
plt.show()


# In[44]:


a=df['sex'].value_counts()


# In[45]:


plt.bar(a.index,a.values)


# In[46]:


plt.scatter(df['age'],df['sex'],alpha=0.5)


# In[47]:


plt.boxplot([df[df['target'] == 0]['trestbps'],
             df[df['target'] == 1]['trestbps']],
            labels=['No Disease', 'Disease'])
plt.xlabel('Target')
plt.ylabel('Resting Blood Pressure')
plt.title('Resting Blood Pressure by Target')


# In[48]:


plt.scatter(df3['NOx(GT)'], df3['NO2(GT)'], alpha=0.5)


# In[49]:


plt.scatter(df3['PT08.S1(CO)'], df3['PT08.S2(NMHC)'], alpha=0.5)


# In[50]:


sns.distplot(df['age'])


# In[51]:


df3


# In[ ]:




