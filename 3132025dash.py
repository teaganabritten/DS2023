import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import dash
from dash import dcc, html, Dash, Input, Output

cd = pd.read_csv('CleanClassData.csv')

cat_vars = cd.select_dtypes(include = ['object']).columns.tolist()

words = WordCloud(scale = 3, background_color = 'white', colormap = 'viridis').generate(winter)
plt.figure(figsize = (15, 10))
plt.imshow(words, interpolation = 'bilinear')
plt.axis('off')
plt.show()



