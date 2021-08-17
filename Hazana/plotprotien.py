#!/usr/bin/env python
# coding: utf-8

# just enter the num_of_lines and the path to the datasets and run all

# In[55]:


num_of_lines=200


# In[61]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

Demo_metabolic=pd.read_excel("C:/Users/97254/Downloads/Demo_metabolic.xlsx", engine='openpyxl')
Demo_patient_week1_23=pd.read_excel("C:/Users/97254/Downloads/Demo_patient_week1_23.12.xlsx", engine='openpyxl')
Demo_Patient_level_feeding_Daily_19 = pd.read_csv("C:/Users/97254/Downloads/Demo_Patient_level_feeding_Daily_19.11.csv",encoding='latin-1')

Demo_metabolic = pd.DataFrame(Demo_metabolic.iloc[:num_of_lines, :3])
dataap1 = pd.DataFrame(Demo_patient_week1_23.iloc[:num_of_lines, :1])
dataap2 = pd.DataFrame(Demo_patient_week1_23.iloc[:num_of_lines, 43:45])

#data2['Weight_adm']=data2['Weight_adm']/data2['Height']
#data2= pd.DataFrame(data2.iloc[:10, :2])

Demo_patient_week1_23=pd.concat([dataap1,dataap2],axis=1)

Demo_patient_week1_23.head()


# In[70]:


Demo_Patient_level_feeding_Daily_19 = pd.DataFrame(Demo_Patient_level_feeding_Daily_19.iloc[:num_of_lines, :])
#data.head()

#merg by id
mer=pd.merge(Demo_metabolic,Demo_Patient_level_feeding_Daily_19,left_on='patient_id',right_on='patient_id',how='left')
mer.head()


# In[71]:


#onley kcal_day and protein_day
mer2 = pd.DataFrame(mer.iloc[:,3 :])

# normelize and concat

for col in mer2.columns:
    mer2[col] = mer2[col]/mer['Weight_adm']
    
mer = mer.iloc[:, :1]
lest=pd.concat([mer,mer2],axis=1)
lest.head()


# In[72]:


Demo_patient_week1_23=Demo_patient_week1_23.rename(columns={'patient_id':'patient_id2'},inplace = False)
#dataap.head()

lest=pd.concat([lest,Demo_patient_week1_23],axis=1)
lest.drop('patient_id2',
  axis='columns', inplace=True)
lest.head()


# In[73]:


lest=lest.dropna(how='all')
lest2=lest.loc[:, ::2]
lest2['LOS'] = Demo_patient_week1_23['LOS'] 
lest.shape


# # plb=lest.iloc[:, :9]
# plb.head()

# In[44]:


plb.mean().plot(kind='bar')


# In[45]:


plb['protein_day0'].plot(kind='bar')


# In[46]:


plb['protein_day4'].plot(kind='bar')


# In[ ]:




