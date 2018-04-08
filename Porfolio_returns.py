
# coding: utf-8

# In[20]:


import pandas as pd
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[10]:


tickers=['PG','F','MSFT','GE']
new_data = pd.DataFrame()
for t in tickers :
    new_data[t] = wb.DataReader(t,'quandl','1995-1-1','2018-1-1')['AdjClose']


# In[11]:


new_data.info()


# In[12]:


new_data = new_data.iloc[::-1]


# In[13]:


(new_data / new_data.iloc[0]*100).plot(figsize = (15,6));
plt.show()


# In[15]:


new_data.plot(figsize = (15,6))
plt.show()


# In[17]:


returns = (new_data / new_data.shift(1)) - 1
returns.head()


# In[22]:


annual_returns = (((returns.mean() + 1)**250) -1)
weights = np.array([0.25,0.25,0.25,0.25])


# In[23]:


pfolio = str(round(np.dot(annual_returns,weights),5)*100) + '%'
print(pfolio)


# In[25]:


weights_1 = np.array([0.40,0.05,0.40,0.15])
pfolio_1 = str(round(np.dot(annual_returns,weights_1),5)*100) + '%'
print(pfolio_1)

