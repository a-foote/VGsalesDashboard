import dash
import dash_bootstrap_components as dbc
#from dash import html, dcc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import altair as alt
import pandas as pd

from plot_functions import map
#connect page to app.py
dash.register_page(__name__,path='/',name="Global Sales")
#read data
pg1_data = pd.read_csv("data/vgsales-cleaned.csv", parse_dates=['Year'])
pg1_data['Year'] = pg1_data['Year'].dt.year.astype('Int64')

alt.data_transformers.disable_max_rows()
#design layout
layout = dbc.Container(
        children=[
            #row 1
            dbc.Row([
                dbc.Col(children=[
                dcc.Graph(
                        id='map',
                        style={'float': 'left', 'border-width': '0'},
                    )], style={'float':'left'})
            ]), #end of row1
            #row2
            dbc.Row([
                dbc.Col(children=[
                    html.Iframe(
                        id='scatter',
                        style={'border-width': '0', 'width': '100%', 'height': '165%'},
                    ),
                    html.Div([
                        dcc.RangeSlider(id='gs_slider', min=1980, max=2017, value=[1980,2016], step=1, marks=None, tooltip={"placement": "bottom", "always_visible": True})
                    ], style={'width':'50vw'})
                ])
            ]) #end of row2
        ]
    )

# Set up callbacks/backend
@dash.callback(
    [Output('scatter', 'srcDoc'),
    Output('map','figure')],
    [Input('gs_slider', 'value')]
)
def sales_time(years):
#"""
#A function that creates a line plot in Altair.

#    Parameters:
#    years (array of int): an array of two integers, used to filter data

#    Returns:
#    plot (altair plot): An HTML formatted Altair line plot
#"""
    plot = (alt.Chart(pg1_data[(pg1_data['Year'] > years[0]) & (pg1_data['Year'] < years[1])], title='Total Regional Sales').mark_line().encode(
                    alt.X('Year',scale=alt.Scale(zero=False), title=None, axis=alt.Axis(format='d')),
                    alt.Y('sum(Global_Sales)', title='Sum of Sales (millions)', axis=alt.Axis(format='$s'))
                ).properties(
                    width=800,
                    height=250
                )#.mark_errorband(extent='ci')
           )

# To Do - Add confidence band to line plot
#         band = (alt.Chart(df).mark_errorband(extent='ci').encode(
#                         x='Year',
#                         y='Global_Sales'
#                     )

#                )

    final_plot = (plot).configure_mark(color='red')
    return final_plot.to_html(), map.map_figure()
