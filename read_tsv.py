#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
panglao = pd.read_csv('PanglaoDB', sep='\t')


# In[10]:


panglao


# In[14]:


panglao.loc[panglao['Species'] == "Homo sapiens"]

