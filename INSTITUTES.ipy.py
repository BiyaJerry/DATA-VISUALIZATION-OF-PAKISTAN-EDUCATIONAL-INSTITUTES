#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns
sns.set(color_codes=True)
df = pd.read_csv("C:\\Users\\Nouman\\Documents\Institutes.csv")
df.head()


# In[3]:


df=df.fillna(df.mean())
df


# In[4]:


df.info


# In[5]:


df.info()


# In[6]:


sns.distplot(df['INSTITUTES'])


# In[7]:


sns.barplot(df['GIRL'],df['INSTITUTES'])


# In[8]:


sns.barplot(df['BOYS '],df['INSTITUTES'])


# In[9]:


sns.barplot(df['MIXED'],df['INSTITUTES'])


# In[10]:


sns.distplot(df['BOYS '])


# In[11]:


sns.distplot(df['GIRL'])


# In[12]:


sns.distplot(df['MIXED'])


# In[13]:


sns.distplot(df['INSTITUTES'])


# In[14]:


sns.jointplot(df['BOYS '],df['INSTITUTES'])


# In[15]:


sns.jointplot(df['GIRL'],df['INSTITUTES'])


# In[17]:


sns.jointplot(df['BOYS '],df['GIRL'])


# In[18]:


sns.jointplot(df['BOYS '],df['INSTITUTES'],kind="hex")


# In[19]:


sns.jointplot(df['GIRL'],df['INSTITUTES'],kind="hex")


# In[20]:


sns.jointplot(df['MIXED'],df['INSTITUTES'],kind="hex")


# In[21]:


sns.jointplot(df['BOYS '],df['GIRL'])


# In[22]:


sns.jointplot(df['BOYS '],df['INSTITUTES'])


# In[23]:


sns.jointplot(df['GIRL'],df['INSTITUTES'])


# In[24]:


sns.jointplot(df['BOYS '], df['INSTITUTES'], kind="kde")


# In[25]:


sns.jointplot(df['GIRL'], df['INSTITUTES'], kind="kde")


# In[26]:


sns.jointplot(df['MIXED'], df['INSTITUTES'], kind="kde")


# In[27]:


sns.pairplot(df[['BOYS ', 'GIRL', 'MIXED', 'INSTITUTES']])


# In[28]:


sns.stripplot(df['MIXED'], df['INSTITUTES'])


# In[29]:


sns.stripplot(df['BOYS '], df['INSTITUTES'])


# In[30]:


sns.stripplot(df['GIRL'], df['INSTITUTES'])


# In[31]:


sns.stripplot(df['MIXED'], df['INSTITUTES'], jitter = True)


# In[32]:


sns.swarmplot(df['BOYS '], df['INSTITUTES'])


# In[33]:


sns.swarmplot(df['GIRL'], df['INSTITUTES'])


# In[34]:


sns.swarmplot(df['BOYS '], df['GIRL'])


# In[35]:


sns.boxplot(df['BOYS '], df['INSTITUTES'], hue=df['BOYS '])


# In[37]:


sns.countplot(df['BOYS '])


# In[39]:


sns.countplot(df['GIRL'])


# In[40]:


sns.countplot(df['INSTITUTES'])


# In[ ]:


sns.pointplot(df['BOYS '], df['INSTITUTES'], hue=df['GIRL'])


# In[ ]:





# In[ ]:





# In[ ]:




