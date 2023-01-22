import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import geopandas as gpd

dash.register_page(__name__, path='/where')

map_pt = gpd.read_file('https://raw.githubusercontent.com/ufoe/d3js-geojson/master/Portugal.json')
passengers = pd.read_csv('https://raw.githubusercontent.com/LuisaPolicarpo/Project5/main/passengers_year_city%20(1).csv')

# Additional Functions
def map_year(df = passengers):
    return px.choropleth_mapbox(df, geojson=map_pt, locations='Region1', color='Nb_passengers',
                                animation_frame="Date",
                                color_continuous_scale="ylorrd",
                                range_color=(500000, 11000000),
                                mapbox_style="carto-positron",
                                featureidkey="properties.name",
                                zoom=4, center = {"lat": 38.7436057, "lon": -9.2302432},
                                opacity=0.8, width=800, height=800)

                            
layout = [html.H1(children='Where are tourists landing?',
                        style={'textAlign':'center', "padding": "2rem 1rem"}
                        ),
                dcc.Graph(id='world-graph',figure=map_year(), 
                style= {"margin-left": "20rem",
                        "margin-right": "20rem",
                        "padding": "1rem 1rem",}
                        ),
                ]
