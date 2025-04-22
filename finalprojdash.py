import pandas as pd
import dash, plotly.express as px
from dash import dcc, html, Output, Input, Dash
import seaborn as sns
import matplotlib.pyplot as plt
import io
import base64

df = pd.read_csv('./DS2023/cars_hw2.csv')

app = dash.Dash()
app.layout = html.Div([
    html.H1('Body Type v. Mileage Dashboard'),
    dcc.Checklist(
        id="body_type_checklist",
        options=[{'label': body, 'value': body} for body in df['Body_Type'].unique()],
        value=[],
        inline=True
    ),
    dcc.Slider(
        id='year_slider',
        min=df['Make_Year'].min(),
        max=df['Make_Year'].max(),
        value=df['Make_Year'].min(),
        marks={str(year): str(year) for year in df['Make_Year'].unique()},
        step=None
    ),
    dcc.RadioItems(
        id='plot_type_radio',
        options=[
            {'label': 'KDE Plot', 'value': 'kde'},
            {'label': 'Histogram', 'value': 'hist'}
        ],
        value='kde',
        inline=True
    ),
    html.Img(id='plot_image', style={'width': '80%', 'height': 'auto'})
])

@app.callback(
    Output('plot_image', 'src'),
    [Input('body_type_checklist', 'value'),
     Input('year_slider', 'value'),
     Input('plot_type_radio', 'value')]
)
def update_plot(selected_body_types, selected_year, plot_type):
    filtered_data = df[df['Make_Year'] == selected_year]
    
    if selected_body_types:
        filtered_data = filtered_data[filtered_data['Body_Type'].isin(selected_body_types)]
    
    plt.figure(figsize=(10, 6))
    
    if plot_type == 'kde':
        sns.kdeplot(data=filtered_data, x='Mileage_Run', hue='Body_Type', common_norm=False)
        plt.title(f'KDE Plot of Mileage for Year {selected_year}')
        plt.xlabel('Mileage')
        plt.ylabel('Density')
    elif plot_type == 'hist':
        sns.histplot(data=filtered_data, x='Mileage_Run', hue='Body_Type', multiple='stack', bins=20)
        plt.title(f'Histogram of Mileage for Year {selected_year}')
        plt.xlabel('Mileage')
        plt.ylabel('Count')
    
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plot_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    
    return f"data:image/png;base64,{plot_base64}"

if __name__ == '__main__':
    app.run(debug=True)