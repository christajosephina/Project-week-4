#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# # How many kids do women have?

# This csv goes up until 1980, because we don't know it yet for younger women.

# In[2]:


df_amount=pd.read_csv("Aantal kinderen per vrouw (%).csv", sep=';', decimal=',')


# In[3]:


#df_amount.tail(5)


# In[4]:


#it needs some changes to make it readable.
df_amount['year']=df_amount.Jaar


# In[5]:


df_amount['zero'] = df_amount['Geen kinderen']


# In[6]:


df_amount['one'] = df_amount['1 kind']


# In[7]:


df_amount['two'] = df_amount['2 kinderen']


# In[8]:


df_amount['more'] = df_amount['3 of meer kinderen']


# In[9]:


df_amount = df_amount.drop(columns=['Jaar', 'Geen kinderen', '1 kind', '2 kinderen', '3 of meer kinderen'])


# In[10]:


df_amount.head(5)


# In[11]:


#df_amount.shape


# In[12]:


#df_amount.dtypes


# In[13]:


#graph it and add some annotations (search for matplotlib annotations on google)
import matplotlib.pyplot as plt
ax = plt.gca()

df_amount.plot(kind='line',x='year',y=["zero", "one", "two", "more"],ax=ax)
plt.annotate(text='End of WW2', xy=(1945,23), xytext=(1950, 30),arrowprops=dict(arrowstyle='->', linewidth=2))
plt.annotate(text='End of WW2', xy=(1945,50), xytext=(1950, 30),arrowprops=dict(arrowstyle='->', linewidth=2))
plt.annotate(text='Introduction of the pill', xy=(1964,23), xytext=(1960, 10),arrowprops=dict(arrowstyle='->', linewidth=2))
plt.show()


# # What is the average age of a mother at childbirth?

# In[14]:


df_age=pd.read_csv("Gemiddelde leeftijd van de moeder (jaar).csv", sep=';', decimal=',')


# In[15]:


df_age['year']=df_age.Jaar


# In[16]:


df_age['all']=df_age['Bij alle kinderen']


# In[17]:


df_age['first']=df_age['Bij eerste kind']


# In[18]:


df_age['second']=df_age['Bij tweede kind']


# In[19]:


df_age=df_age.drop(columns=['Jaar', 'Bij alle kinderen', 'Bij eerste kind', 'Bij tweede kind'])


# In[20]:


df_age.tail(5)


# In[21]:


#df_amount.shape


# In[22]:


#df_age.dtypes


# In[23]:


#graph the amount of kids over time and average age and add annotations 


# In[24]:


ax = plt.gca()

df_age.plot(kind='line',x='year',y=["all", "first", "second"],ax=ax)
plt.annotate(text='Introduction of the pill', xy=(1964,24), xytext=(1951.8, 32),arrowprops=dict(arrowstyle='-', linewidth=2))

plt.show()


# # What is the average number of children per Dutch woman?

# In[25]:


#loading and cleaning the csv
df_children=pd.read_csv("Geboorte__kerncijfers_07072021_150038.csv", sep=';', decimal=',')


# In[26]:


df_children=df_children.transpose()


# In[27]:


df_children=df_children.drop(['Year'])


# In[28]:


df_children=df_children.reset_index()


# In[29]:


df_children['childavg']=df_children[0]


# In[30]:


df_children=df_children.drop(columns=[0])


# In[31]:


df_children.head()


# Time to graph it.

# In[43]:


ax = plt.gca()

df_children.plot(kind='line',x='index',y=["childavg"],ax=ax)
plt.annotate(text='Introduction of the pill', xy=(1964,3), xytext=(1964, 3),arrowprops=dict(arrowstyle='->', linewidth=2))
plt.show()


# According to CBS, "The sharp decline around 1970 was partly due to a real decline in the average number of children that women had, but also because women started delaying the birth of their first child."

# # Do women who get more babies, start earlier?

# For this, we need to make a scaterplot. First, we need to merge average age of a mother at childbirth and the amount of kids women get.

# In[46]:


merged = df_amount.merge(df_age, left_on='year', right_on='year')


# In[47]:


merged.head()


# In[48]:


df_children['index'].astype(int)


# In[49]:


df_children['index'] =df_children['index'].astype(int)


# In[50]:


df_children.dtypes


# In[51]:


merged = merged.merge(df_children, left_on='year', right_on='index')


# In[52]:


merged.head()


# In[347]:


ax = plt.gca()

merged.plot(kind='scatter',x='first',y='childavg',ax=ax)


# In[318]:


#this doesn't really make sense becuase 'all' is an age, and the others are percentages
import numpy as np

ax1 = merged.plot(kind='scatter', x='first', y='one', color='r')    
ax2 = merged.plot(kind='scatter', x='first', y='two', color='g', ax=ax1)    
ax3 = merged.plot(kind='scatter', x='first', y='more', color='b', ax=ax1)

