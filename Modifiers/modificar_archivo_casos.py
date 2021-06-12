#!/usr/bin/env python
# coding: utf-8

# ### Import libraries and Covid-19 data

# In[1]:


import pandas as pd
from datetime import datetime


# In[2]:


df = pd.read_csv("/home/andy/Documents/PythonExercises/Analytics_Report/data/Covid19Casos.csv")


# ### Removing unnecessary colums, only staying residencia_provincia_nombre, Count and fecha_diagnostico

# In[3]:


df = df.drop(columns=['id_evento_caso', 'sexo', 'edad', 'edad_años_meses',
         'residencia_pais_nombre','residencia_departamento_nombre', 'carga_provincia_nombre',
         'fecha_inicio_sintomas', 'fecha_apertura', 'sepi_apertura',
         'fecha_internacion', 'cuidado_intensivo', 'fecha_cui_intensivo',
         'fallecido', 'fecha_fallecimiento', 'asistencia_respiratoria_mecanica',
         'carga_provincia_id', 'origen_financiamiento', 'clasificacion',
         'clasificacion_resumen', 'residencia_provincia_id', 'residencia_departamento_id', 'ultima_actualizacion'])
#df.reset_index(drop=True, inplace=True)


# ### Create column "year"

# In[4]:


df["year"]=df["fecha_diagnostico"].str[0:4]
#df2["year"]=df2["year"].astype("int")


# ### Create new DF only with the rows beloging to the year 2021

# In[5]:


df = df.loc[(df['year'] == "2021")]
df = df.sort_values(['residencia_provincia_nombre', 'fecha_diagnostico'], ascending=[1,0])
df.reset_index(drop=True, inplace=True)


# ### Create new DF with the Count column

# In[6]:



#https://stackoverflow.com/questions/59631533/pandas-counting-rows-with-dates
#filter = df4["residencia_provincia_nombre"]=="CABA"
cnt = df.groupby(['fecha_diagnostico','residencia_provincia_nombre']).size().rename('Count')
result = df.drop_duplicates(subset=['fecha_diagnostico','residencia_provincia_nombre'])    .merge(cnt, left_on=['fecha_diagnostico','residencia_provincia_nombre'], right_index=True)
df = result.sort_values('fecha_diagnostico',ascending=False)


# In[7]:


#EXAMPLE TO COUNT ALL CASES
#filter2 = df4["residencia_provincia_nombre"]=="CABA"
#cntCABA2 = df4.groupby('fecha_diagnostico').size().rename('Count')
#cntBA = df.groupby('Date').size().rename('Count')
#result2 = df4.drop_duplicates(subset='fecha_diagnostico')\
    #.merge(cntCABA2, left_on='fecha_diagnostico', right_index=True)
#result2.sort_values('fecha_diagnostico',ascending=False).head(10)


# ### Moving "fecha_diagnostivo" to the first column

# In[8]:


cols = list(df.columns)
cols

def re_lista(x,y):
    l1 = x.copy()
    i1 = x.index(y)
    el1 = [l1[i1]]
    l1.remove(el1[0])
    return el1 + l1


# In[9]:


df = df[re_lista(cols,'fecha_diagnostico')]
#df.tail()


# In[11]:


#https://stackoverflow.com/questions/38067704/how-to-change-the-datetime-format-in-pandas

df['fecha_diagnostico'] = pd.to_datetime(df.fecha_diagnostico)
df['fecha_diagnostico'] = df['fecha_diagnostico'].dt.strftime('%m/%d/%y')
#df


# In[12]:


#https://stackoverflow.com/questions/17298313/python-pandas-convert-rows-as-column-headers
#https://towardsdatascience.com/a-step-by-step-guide-to-pandas-pivot-tables-e0641d0c6c70
#https://stackoverflow.com/questions/11346283/renaming-columns-in-pandas

df = df.pivot_table('Count', ['residencia_provincia_nombre'], 'fecha_diagnostico')
df.rename(columns=lambda x: x.replace("/0", "/").lstrip("0"), inplace=True)
#df


# In[13]:


df.to_csv('/home/andy/Documents/PythonExercises/Analytics_Report/data/Covid19Cases_FINAL.csv')


# In[ ]:




