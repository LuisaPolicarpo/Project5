import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import geopandas as gpd

dash.register_page(__name__, path='/how_much')

df_22 = pd.read_csv('https://raw.githubusercontent.com/LuisaPolicarpo/Project5/main/ploty_earnings_FV.csv')
df_3 = df_22.groupby(['Year','Type']).agg({'Value':'sum'}).reset_index()

def earnings_value(df = df_3):
    return px.pie(df, values='Value', names='Type', color_discrete_sequence=["#008B45", "#00CD66", "#71C671"])

card_content = [
    dbc.CardHeader("2017"),
    dbc.CardBody(
        [
            html.H5("2.66 nights", className="card-title"),
        ]
    ),
]
card_content2 = [
    dbc.CardHeader("2022"),
    dbc.CardBody(
        [
            html.H5("2.58 nights", className="card-title"),
        ]
    ),
]

layout = html.Div(children=[
        dbc.Row([html.H1('How much are they spending?',
                        style={'textAlign':'center', "padding": "2rem 1rem"}
                        ),
                    ],),
        dbc.Row([[
                dbc.Col(dbc.Card(card_content, color="success",  outline=True, style={'textAlign':'center','width':'10rem', "height": "10rem"})),
                dbc.Col(dbc.Card(card_content2, color="success", outline=True, style={'textAlign':'center', 'width':'10rem', "height": "10em"})
                ),
                 ],
                 ]),
        dbc.Row([
            dbc.Col([html.Div(children = [dbc.Label("Choose a year:", style = {"margin-left": "25rem"}),
                          dbc.RadioItems(
                          options=[{"label": "2017", "value": 2017},
                                    {"label": "2018", "value": 2018},
                                    {"label": "2019", "value": 2019},
                                    {"label": "2020", "value": 2020},
                                    {"label": "2021", "value": 2021},
                                    {"label": "2022", "value": 2022},
                                  ],
                          value=2017,
                          id="radioitems-input",
                          style = {"margin-left": "25rem"}
                            ),
                        ],),
                     ]),
            dbc.Col([dcc.Graph(id='pie-graph',figure=earnings_value()
                                )
                        ]),]),
                            ])

# Callbacks
@callback(
    Output(component_id='pie-graph', component_property='figure'),
    Input(component_id='radioitems-input', component_property='value'), 
)
def update_graph(year):
  year_selected = df_3[df_3['Year']==year]
  return earnings_value(year_selected)