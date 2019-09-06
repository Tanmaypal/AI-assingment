
import numpy as np
import matplotlib
import wordcloud
import pandas as pd
import os
import wordcloud

from wordcloud import wordcloud,STOPWORDS

os.chdir("C:\\Users\\TANMAY\\Downloads")

dataset=pd.read_csv('wordcloud.csv')
dataset

dataset.description

country = dataset.groupby("country")
country

country.describe().head()

country.mean().sort_values(by="points",ascending=False).head()

text=dataset.description[2]
text

wordcloud=WordCloud(max_font_size=100, max_words=100, background_color="white").generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

