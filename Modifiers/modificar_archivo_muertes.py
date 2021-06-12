#!/usr/bin/env python
# coding: utf-8

# ### Import libraries and Covid-19 data

# In[1]:


import pandas as pd
from datetime import datetime


# In[2]:


df = pd.read_csv("/home/andy/Documents/PythonExercises/Analytics_Report/data/Covid19Casos.csv")


# ### Removing unnecessary colums, only staying residencia_provincia_nombre, Count and fecha_diagnostico

# In[4]:


list(df.columns)


# In[12]:


columns_del = ['id_evento_caso',
 'sexo',
 'edad',
 'edad_años_meses',
 'residencia_pais_nombre',
 'residencia_departamento_nombre',
 'carga_provincia_nombre',
 'fecha_inicio_sintomas',
 'fecha_apertura',
 'sepi_apertura',
 'fecha_internacion',
 'cuidado_intensivo',
 'fecha_cui_intensivo',
 'fallecido',
 'asistencia_respiratoria_mecanica',
 'carga_provincia_id',
 'origen_financiamiento',
 'clasificacion',
 'clasificacion_resumen',
 'residencia_provincia_id',
 'fecha_diagnostico',
 'residencia_departamento_id',
 'ultima_actualizacion']

df = df.drop(columns=columns_del)
df = df.dropna()
df.reset_index(drop=True, inplace=True)


# ### Create column "year"

# In[13]:


df["year"]=df["fecha_fallecimiento"].str[0:4]
#df2["year"]=df2["year"].astype("int")


# ### Create new DF only with the rows beloging to the year 2021

# In[14]:


df = df.loc[(df['year'] == "2021")]
df = df.sort_values(['residencia_provincia_nombre', 'fecha_fallecimiento'], ascending=[1,0])
df.reset_index(drop=True, inplace=True)


# ### Create new DF with the Count column

# In[15]:



#https://stackoverflow.com/questions/59631533/pandas-counting-rows-with-dates
#filter = df4["residencia_provincia_nombre"]=="CABA"
cnt = df.groupby(['fecha_fallecimiento','residencia_provincia_nombre']).size().rename('Count')
result = df.drop_duplicates(subset=['fecha_fallecimiento','residencia_provincia_nombre'])    .merge(cnt, left_on=['fecha_fallecimiento','residencia_provincia_nombre'], right_index=True)
df = result.sort_values('fecha_fallecimiento',ascending=False)


# In[18]:


#EXAMPLE TO COUNT ALL CASES
#filter2 = df["residencia_provincia_nombre"]=="CABA"
#cntCABA2 = df.groupby('fecha_diagnostico').size().rename('Count')
#cntBA = df.groupby('fecha_fallecimiento').size().rename('Count')
#result2 = df.drop_duplicates(subset='fecha_fallecimiento')\
    #.merge(cntBA, left_on='fecha_fallecimiento', right_index=True)
#result2.sort_values('fecha_fallecimiento',ascending=False).head(10)


# ### Moving "fecha_diagnostivo" to the first column

# In[19]:


cols = list(df.columns)
cols

def re_lista(x,y):
    l1 = x.copy()
    i1 = x.index(y)
    el1 = [l1[i1]]
    l1.remove(el1[0])
    return el1 + l1


# In[23]:


df = df[re_lista(cols,'fecha_fallecimiento')]
df.tail()


# In[26]:


#https://stackoverflow.com/questions/38067704/how-to-change-the-datetime-format-in-pandas

df['fecha_fallecimiento'] = pd.to_datetime(df.fecha_fallecimiento)
df['fecha_fallecimiento'] = df['fecha_fallecimiento'].dt.strftime('%m/%d/%y')


# In[28]:


#https://stackoverflow.com/questions/17298313/python-pandas-convert-rows-as-column-headers
#https://towardsdatascience.com/a-step-by-step-guide-to-pandas-pivot-tables-e0641d0c6c70
#https://stackoverflow.com/questions/11346283/renaming-columns-in-pandas

df = df.pivot_table('Count', ['residencia_provincia_nombre'], 'fecha_fallecimiento')
df.rename(columns=lambda x: x.replace("/0", "/").lstrip("0"), inplace=True)
#df


# In[29]:


df.to_csv('/home/andy/Documents/PythonExercises/Analytics_Report/data/Covid19Deaths_FINAL.csv')


# In[ ]:




