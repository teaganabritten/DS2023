import dash
from dash import Dash, html, dcc, Input, Output
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import numpy as np
import pandas as pd
import plotly.express as px

data = pd.read_csv('Guns.csv')

app2 = Dash()

app2.layout = html.Div([
    html.H1("Gapminder Dashboard"), 
    dcc.RadioItems(id = 'vars', 
                   options = [{'label': 'Life Expectancy', 'value': 'LifeExp'},
                              {'label': 'Population', 'value': 'pop'},
                              {'label': 'GDP per capita', 'value': 'gdpPercap'}],
                    value = 'gdpPercap'),
    dcc.Slider(id='year_slider',
               min = gap['year'].min(),
               max = gap['year'].max(),
               value = gap['year'].min(),
               marks = {str(year):str(year) for year in gap['year'].unique()},
               step = 5),
    dcc.Graph(id = 'map')
])

@app2.callback(
    Output('map', 'figure'),
    [Input('vars', 'value'), Input('year_slider', 'value')]
)
def update_map(variables, year_selected):
    gap_filtered = gap[gap['year']==year_selected]
    fig = px.choropleth(gap_filtered, locations = 'iso_alpha', color = variables, hover_name = 'country', color_continuous_scale = 'viridis')
    return fig

if __name__ == '__main__':
    app2.run()