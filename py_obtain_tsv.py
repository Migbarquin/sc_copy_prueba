#!/usr/bin/env python
# coding: utf-8

# In[48]:


import pandas as pd
df = pd.read_csv('clusters_to_number_of_cells.txt', header=None, delimiter = ",")


# In[49]:


df.columns = ["SRA accession", "SRS accession", "Cluster index", "Number of cells"]


# In[50]:


df


# In[55]:


l = df.groupby('SRS accession')['Number of cells'].sum()
df2 = pd.DataFrame(data=l)
df2


# In[57]:


df3 = pd.read_csv('metadata.txt', header=None, delimiter = ",")
df3.columns = ["SRA accession", "SRS accession", "Tissue origin of the sample", "scRNA-seq protocol","Species","Sequencing instrument","Number of expressed genes","Median number of expressed genes per cell","Number of cell clusters in this sample","Is the sample from a tumor? (1 true otherwise false)","Is the sample from primary adult tissue?","Is the sample from a cell line?"]


# In[58]:


df3


# In[61]:


df4 = pd.merge(left=df3, right=df2, left_on='SRS accession', right_on='SRS accession')


# In[63]:


df4


# In[64]:


df4.to_csv("PanglaoDB", sep="\t", index=False)

