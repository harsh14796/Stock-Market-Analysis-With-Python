
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[2]:


PG = wb.DataReader('PG', 'quandl', '1995-01-01', '2018-01-01')


# In[4]:


PG = PG.iloc[::-1]
PG


# In[5]:


PG['simple_return']=(PG['AdjClose']/PG['AdjClose'].shift(1))-1
print(PG['simple_return'])


# In[6]:


PG['simple_return'].plot(figsize=(8, 5))
plt.show()


# In[7]:


avg_d = PG['simple_return'].mean()
avg_d


# In[12]:


avg_a = (((avg_d+1)**250)-1)*100
print(str(round(avg_a,5)) + ' %')


# In[13]:


PG['log_returns'] = np.log(PG['AdjClose']/PG['AdjClose'].shift(1))
print(PG['log_returns'])


# In[21]:


daily_l = PG['log_returns'].mean()
print(str(round(daily_l,5) *100) + ' %')


# In[22]:


annual_l = (((daily_l+1)**250)-1)*100
print(str(round(annual_l,5)) + ' %')

