import dash
from dash import html, dcc
import pandas as pd
import geopandas as gpd
import plotly.express as px

dash.register_page(__name__,path='/')

map_world = gpd.read_file('https://raw.githubusercontent.com/LuisaPolicarpo/Project5/main/Dataset/countries.geojson')
nacionalities = pd.read_csv('https://raw.githubusercontent.com/LuisaPolicarpo/Project5/main/Dataset/nacionality_22.csv')
nacionalities = nacionalities.rename(columns = {'Value':'Nb_tourists'})

# Additional Functions
def world_nacion(df = nacionalities):
  return px.choropleth_mapbox(nacionalities, geojson = map_world, locations='Countries', color='Nb_tourists',
                           color_continuous_scale="ylorrd",
                           range_color=(80000, 2200000),
                           mapbox_style="carto-positron",
                           featureidkey = 'properties.ADMIN',
                           zoom=2, center = {"lat": 38.7436057, "lon": -9.2302432},
                           opacity=0.8, height=800)

layout = [html.H1(children='Where are tourists coming from?',
                        style={'textAlign':'center', "padding": "2rem 1rem"}
                        ),
                dcc.Graph(id='world-graph',figure=world_nacion()
                        ),
                ]
    #html.H1(children='This is our Home page'),

    #html.Div(children='''
     #   This is our Home page content.
    #'''),