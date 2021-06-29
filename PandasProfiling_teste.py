#!/usr/bin/env python
# coding: utf-8

# # Simple Exploratory Data Analysis with Pandas-Profiling Package Python
#     ## Exemplo demonstrado no vídeo:
#         ## https://www.youtube.com/watch?v=773zrwAkmQ0
# In[3]:
# get_ipython().system('pip install pandas-profiling')

import pandas as pd
from pandas_profiling import ProfileReport

# In[11]:
#data = pd.read_excel('../flight_Data_Train.xlsx')
#data = pd.read_csv('../wine_quality_class_cat.csv')

data = pd.read_csv('D:/ProjetosGithub/kaggle_flight_delays/flights.csv', 
                   index_col=None, header=0, engine='python')
                 #lineterminator='\n')
data.head()

# In[14]:
profile = ProfileReport(data, title='Perfil Modelo de Preços de Vôos', html={'style': {'full_width':True}})
profile

