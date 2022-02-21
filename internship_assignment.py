#!/usr/bin/env python
# coding: utf-8

# In[339]:


import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime
import plotly.express as px
from sklearn.ensemble import IsolationForest
df = pd.read_excel("C:\\Users\\akky4415\\Desktop\\Assignment\\internship-data-1.xlsx", sheet_name="internship-data-1")


# In[340]:


a = ['Comm Fail' , 'Configure','I/O Timeout','Not Connect','Scan Timeout','Unit Down']
df = df[~df['Cyclone_Inlet_Gas_Temp'].isin(a)]
df = df[~df['Cyclone_Material_Temp'].isin(a)]
df = df[~df['Cyclone_Outlet_Gas_draft'].isin(a)]
df = df[~df['Cyclone_cone_draft'].isin(a)]
df = df[~df['Cyclone_Gas_Outlet_Temp'].isin(a)]
df = df[~df['Cyclone_Inlet_Draft'].isin(a)]


# In[325]:


df.to_excel("C:\\Users\\akky4415\\Desktop\\Assignment\\cleaned_data.xlsx")


# In[341]:


#df.shape
df['Cyclone_Inlet_Gas_Temp']=pd.to_numeric(df['Cyclone_Inlet_Gas_Temp'])
df['Cyclone_Material_Temp']=pd.to_numeric(df['Cyclone_Material_Temp'])
df['Cyclone_Outlet_Gas_draft']=pd.to_numeric(df['Cyclone_Outlet_Gas_draft'])
df['Cyclone_cone_draft']=pd.to_numeric(df['Cyclone_cone_draft'])
df['Cyclone_Gas_Outlet_Temp']=pd.to_numeric(df['Cyclone_Gas_Outlet_Temp'])
df['Cyclone_Inlet_Draft']=pd.to_numeric(df['Cyclone_Inlet_Draft'])


# In[310]:


#df.info()


# In[342]:


df = df.set_index('time')


# In[343]:


df.info()


# In[344]:


print(pd.date_range(start="01/01/2017 ", end="07/08/2020").difference(df.index))


# In[185]:


#fig = px.line(df.reset_index(), x='time',y = 'Cyclone_Inlet_Draft', title = 'col1vstime')

#fig.update_xaxes(
#		rangeslider_visible = True,
#)
#fig.show()


# In[345]:


Anomaly_model = IsolationForest(bootstrap = 'False',contamination = 'auto', max_features = 6, max_samples = 'auto',n_estimators = 500, n_jobs = None, random_state = None, verbose = 0, warm_start=False)
Anomaly_model.fit(df[['Cyclone_Inlet_Gas_Temp','Cyclone_Material_Temp','Cyclone_Outlet_Gas_draft','Cyclone_cone_draft','Cyclone_Gas_Outlet_Temp','Cyclone_Inlet_Draft']])


# In[346]:


score = Anomaly_model.decision_function(df[['Cyclone_Inlet_Gas_Temp','Cyclone_Material_Temp','Cyclone_Outlet_Gas_draft','Cyclone_cone_draft','Cyclone_Gas_Outlet_Temp','Cyclone_Inlet_Draft']])


# In[347]:


score


# In[348]:


plt.hist(score, bins=70)


# In[349]:


df['scores'] = score


# In[350]:


df


# In[351]:


df = df.query('scores<-0.2')


# In[352]:


df


# In[353]:


df.info()


# In[338]:


df.to_excel("C:\\Users\\akky4415\\Desktop\\Assignment\\outliers3.xlsx")


# In[ ]:




