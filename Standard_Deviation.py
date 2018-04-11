
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[25]:


tickers = ['PG','AAPL']

sec_data = pd.DataFrame()

for t in tickers :
    sec_data[t] = wb.DataReader(t,'quandl','2007-1-1','2018-3-1')['AdjClose']


# In[26]:


sec_data = sec_data.iloc[::-1]
sec_returns = np.log(sec_data / sec_data.shift(1))
sec_returns


# In[27]:


sec_returns['PG'].mean()


# In[33]:


daily = sec_returns[['PG','AAPL']].mean()


# In[34]:


annual = (((daily+1)**250)-1)*100
print(str(annual) + '%')


# In[35]:


daily_std = sec_returns[['PG','AAPL']].std()
daily_std


# In[38]:


annual_std = sec_returns[['PG','AAPL']].std()*250**0.5
annual_std

