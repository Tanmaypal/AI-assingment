
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[6]:


d = {
    'Name':['Alisa','Bobby','Cathrine','Alisa','Bobby','Cathrine',
            'Alisa','Bobby','Cathrine','Alisa','Bobby','Cathrine'],
    'Exam':['Semester 1','Semester 1','Semester 1','Semester 1','Semester 1','Semester 1',
            'Semester 2','Semester 2','Semester 2','Semester 2','Semester 2','Semester 2'],
     
    'Subject':['Mathematics','Mathematics','Mathematics','Science','Science','Science',
               'Mathematics','Mathematics','Mathematics','Science','Science','Science'],
   'Result':['Pass','Pass','Fail','Pass','Fail','Pass','Pass','Fail','Fail','Pass','Pass','Fail']}
dataframe = pd.DataFrame(d,columns=['Name','Exam','Subject','Result'])
dataframe


# In[9]:


## 2 way Cross table
pd.crosstab(dataframe.Name,dataframe.Result,margins=True)


# In[12]:


##3 wat Cross table
pd.crosstab([dataframe.Name,dataframe.Subject],dataframe.Result,margins=True)

