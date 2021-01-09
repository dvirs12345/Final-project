#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[3]:





# In[ ]:





# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data2=pd.read_excel("C:/Users/97254/Downloads/Demo_metabolic.xlsx", engine='openpyxl')

data2 = pd.DataFrame(data2.iloc[:30, :3])
#data2['Weight_adm']=data2['Weight_adm']/data2['Height']
#data2= pd.DataFrame(data2.iloc[:10, :2])
data2.head()


# In[4]:


data = pd.read_csv("C:/Users/97254/Downloads/Demo_Patient_level_feeding_Daily_19.11.csv",encoding='latin-1')

#importer le jeu de données Iris dataset à l'aide du module pandas
data = pd.DataFrame(data.iloc[:30, :])
data.head()


# In[99]:


#merg by id
mer=pd.merge(data2,data,left_on='patient_id',right_on='patient_id',how='left')
mer.head()


# In[94]:


#onley kcal_day and protein_day
mer2 = pd.DataFrame(mer.iloc[:,3 :])

# normelize and concat

for col in mer2.columns:
    mer2[col] = mer2[col]/mer['Weight_adm']
    
mer = mer.iloc[:, :1]
lest=pd.concat([mer,mer2],axis=1)
lest.head()


# In[57]:


#run on the simple kmean algorithm
data_scaled=mer2
data_scaled=data_scaled.dropna(how='all')
# defining the kmeans function with initialization as k-means++
kmeans = KMeans(n_clusters=2, init='k-means++')

# fitting the k means algorithm on scaled data
kmeans.fit(data_scaled)

# inertia on the fitted data
kmeans.inertia_

# fitting multiple k-means algorithms and storing the values in an empty list
SSE = []
for cluster in range(1,7):
    kmeans = KMeans(n_jobs = -1, n_clusters = cluster, init='k-means++')
    kmeans.fit(data_scaled)
    SSE.append(kmeans.inertia_)

# converting the results into a dataframe and plotting them
frame = pd.DataFrame({'Cluster':range(1,7), 'SSE':SSE})
plt.figure(figsize=(12,6))
plt.plot(frame['Cluster'], frame['SSE'], marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')


# In[ ]:


#take 5 as the best num of clusters


# In[64]:


# k means using 5 clusters and k-means++ initialization
kmeans = KMeans(n_jobs = -1, n_clusters = 5, init='k-means++')
kmeans.fit(data_scaled)
pred = kmeans.predict(data_scaled)
#show how many sampels in each cluster
frame = pd.DataFrame(data_scaled)
frame['cluster'] = pred
frame['cluster'].value_counts()


# In[65]:


cls=pd.DataFrame()
cls['data_index']=data_scaled.index.values
cls['cluster']=kmeans.labels_


# In[109]:


#show which sampels in each cluster

d=cls[cls.cluster==2]
d


# In[115]:


#this line for compere
mer2.head(6)


# In[ ]:





# In[ ]:





# In[118]:


#x axis for the day

mer2.loc[12, ::2].plot.line()


# In[ ]:




