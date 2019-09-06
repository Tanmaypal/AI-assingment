
# coding: utf-8

# In[58]:


import numpy as np
import matplotlib
import wordcloud
import pandas as pd
import os
import wordcloud


# In[59]:


from wordcloud import wordcloud,STOPWORDS


# In[60]:


os.chdir("C:\\Users\\TANMAY\\Downloads")


# In[76]:


dataset=pd.read_csv('wordcloud.csv')
dataset


# In[78]:


dataset.description


# In[80]:


country = dataset.groupby("country")
country


# In[81]:


country.describe().head()


# In[82]:


country.mean().sort_values(by="points",ascending=False).head()


# In[84]:


text=dataset.description[2]
text


# In[87]:


wordcloud=WordCloud(max_font_size=100, max_words=100, background_color="white").generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

