import kagglehub
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path = kagglehub.dataset_download("vivovinco/2023-2024-nba-player-stats")

print("Path to dataset files:", path)

nba = pd.read_csv("/home/teaganabritten/.cache/kagglehub/datasets/vivovinco/2023-2024-nba-player-stats/versions/13/2023-2024NBAPlayerStats-Regular.csv", encoding='latin1', delimiter=';')

nba.head(10)
nba.describe()

sns.scatterplot(nba, x = 'FT%', y = 'ORB')

print(nba.columns)

df = nba[nba['FTA']>2]

df['Pos'] = df['Pos'].replace({
    'SF-PF': 'SF',
    'PG-SG': 'PG',
    'C-PF': 'C'})

sns.scatterplot(df, x = 'FT%', y = 'FG%')

import plotly.express as px
px.scatter(df, x = 'FG%', y = 'eFG%', title = 'Field Goal Percentage vs. Effective Field Goal Percentage', color = 'Tm', size = 'FGA', hover_name = 'Player')

px.scatter(df, x = 'FG%', y = '3P%', title = 'Field Goal Percentage vs. Three Point Percentage', color = 'Pos', size = '3PA', hover_name = 'Player')

plt.figure(figsize = (20,5))
sns.kdeplot(df, x = '3P%', hue = 'Pos', fill = True)
plt.title('3 Point Percentage by Position')
plt.show()

px.scatter_3d(df, x = 'FG%', y = '3P%', z = 'eFG%', color = 'Pos')

px.treemap(df, path=[px.Constant("NBA"), 'Pos', 'Tm'], values = '3P', color = '3P%')

px.scatter_ternary(df, a = '3PA', b = '2PA', c = 'FTA')

px.density_heatmap(df, x = '3P', y = '2P')

px.scatter(df, x = '3P%', y = 'eFG%', color = 'Pos', size = 'FGA', hover_data = 'Player')

plt.figure(figsize = (20,5))
sns.kdeplot(df, x = 'eFG%', hue = 'Pos', fill = True)
plt.title('eFG by Position')
plt.show()

sns.boxplot(data=df, x='Pos', y='3P%', hue = 'Pos', palette = 'colorblind')
plt.title('3PT Percentage by Position')
plt.xlabel('Position')
plt.show()

px.scatter(
    df,
    x='AST',
    y='TOV',
    hover_name='Player',
    size='MP',
    title='Assists vs. Turnovers (Right and Down is better)',
    labels={
        'AST': 'Assists Per Game',
        'TOV': 'Turnovers Per Game'
    },
    color = 'Pos'
)

px.scatter(df, x = 'ORB', y = 'DRB', hover_name = 'Player', color = 'Pos', size_max = 15, size = 'MP', 
           labels = {
               'ORB': 'Offensive Rebounds per Game',
               'DRB': 'Defensive Rebounds per Game'
           },
           title = 'Offensive Rebounds v. Defensive Rebounds (Right and Up is better)')

