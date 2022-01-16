import pandas as pd;
import numpy as np;
import plotly.express as px;

data = pd.read_csv('gravity_merged_data.csv');

# creating graphs for solar radius and solar mass;
fig1 = px.scatter(x = data['solar_mass'].tolist(), y = data['solar_radius'].tolist(), color=data['name'].tolist(), title='mass/radius');
fig2 = px.scatter(x = data['solar_mass'].tolist(), y = data['gravity'].tolist(), color=data['name'].tolist(), title='mass/gravity');

fig1.show();
fig2.show();