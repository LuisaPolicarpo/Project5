import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

dash.register_page(__name__, path='/how_long')

df_real_pred = pd.read_csv("https://raw.githubusercontent.com/LuisaPolicarpo/Project5/main/Pred_2023.csv")
df_date = pd.read_csv("https://raw.githubusercontent.com/LuisaPolicarpo/Project5/main/RealvsPred_Covid.csv")

def prevision_value(df = df_real_pred):
  return px.line(df, x='Date', y=['Overnight_real', 'Overnight_Pred'], color_discrete_sequence=["#008B45", "#71C671"])

def overnight(df2 = df_date):
  return px.line(df2, x='Date', y=['Overnight_Real', 'Overnight_Pred'], color_discrete_sequence=["#008B45", "#71C671"])

def make_graph():
    fig = go.Figure()
    # app.layout = html.Div([
  # Create scatter trace of text labels
    fig.add_trace(go.Scatter(
        x=[0.50, 3.5, 2, 0.50, 3.5],
        y=[3.5, 3.5, 3.9, 2.75, 2.75],
        text=["25 798 299",
            "65 840 437",
            "+ 155%","2020","2022"],
        mode="text",
    )),
    fig.update_xaxes(
        showticklabels=False,
        showgrid=False,
        zeroline=False,
    ),
    fig.update_yaxes(
        showticklabels=False,
        showgrid=False,
        zeroline=False,
    ),
    fig.add_shape(type="circle",
        xref="x", yref="y",
        x0=0, y0=3, x1=1, y1=4,
        line_color="#008B45",
    ),
    fig.add_annotation(
      x=2.75,
      y=3.5,
      ax=1.25,
      ay=3.5,
      xref='x',
      yref='y',
      axref='x',
      ayref='y',
      text='',
      showarrow=True,
      arrowhead=3,
      arrowsize=1,
      arrowwidth=3,
      arrowcolor='#008B45'
    ),
    fig.add_shape(type="circle",
        xref="x", yref="y",
        x0=3, y0=3, x1=4, y1=4,
        line_color="#008B45",
    ),
    fig.update_layout(
      margin=dict(l=20, r=20, b=100),
      height=300, width=500,
      plot_bgcolor="white"
)
    return fig
def make_graph_2():
    fig2 = go.Figure()
    # app.layout = html.Div([
  # Create scatter trace of text labels
    fig2.add_trace(go.Scatter(
        x=[0.50, 3.5, 2, 0.50, 3.5],
        y=[3.5, 3.5, 3.9,2.5, 2.5],
        text=["64 965 741",
          "70 158 964",
          "+ 7.9%","2017","2019"],
        mode="text",
    )),
    fig2.update_xaxes(
        showticklabels=False,
        showgrid=False,
        zeroline=False,
    ),
    fig2.update_yaxes(
        showticklabels=False,
        showgrid=False,
        zeroline=False,
    ),
    fig2.add_shape(type="circle",
        xref="x", yref="y",
        x0=0, y0=3, x1=1, y1=4,
        line_color="#008B45",
    ),
    fig2.add_annotation(
      x=2.75,
      y=3.5,
      ax=1.25,
      ay=3.5,
      xref='x',
      yref='y',
      axref='x',
      ayref='y',
      text='',
      showarrow=True,
      arrowhead=3,
      arrowsize=1,
      arrowwidth=3,
      arrowcolor='#008B45'
    ),
    fig2.add_shape(type="circle",
        xref="x", yref="y",
        x0=3, y0=3, x1=4, y1=4,
        line_color="#008B45",
    ),
    fig2.update_layout(
    margin=dict(l=20, r=20, b=100),
    height=300, width=500,
    plot_bgcolor="white"
)
    return fig2

layout = html.Div(children=[
      dbc.Row([
            html.H1('Overnights', style={'textAlign':'center', "padding": "2rem 1rem"}
                        ),
          dbc.Col([
            dcc.Graph(figure=make_graph_2())]),
            # dcc.Graph(figure=prevision_value()),
          dbc.Col([
            dcc.Graph(figure=make_graph())]),
          html.Hr(),
          dbc.Row([html.H1('Forescast for 2023',
                        style={'textAlign':'center', "padding": "2rem 1rem"}
                        ),
                    ],),
    dbc.Row([dcc.Graph(figure=prevision_value()),]),
    dbc.Row([html.H1('What if Covid-19 never happened?',
                        style={'textAlign':'center', "padding": "2rem 1rem"}
                        ),
                    ],),
    dbc.Row([dcc.Graph(figure=overnight()),]),
])])