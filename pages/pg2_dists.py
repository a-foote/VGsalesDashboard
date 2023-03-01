import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output
import altair as alt
import pandas as pd

from plot_functions import sales_time
import pg_head as ph

dash.register_page(__name__,name="Distributions")

pg2_data = pd.read_csv("data/vgsales-cleaned.csv", parse_dates=['Year'])
pg2_data['Year'] = pg2_data['Year'].dt.year.astype('Int64')

layout = dbc.Container(
        children=[
            dbc.Row([
                dbc.Col(children=[
                    dbc.Card([
                        dbc.Form([
                            dbc.Label("Select X Axis:"),
                            dcc.Dropdown(
                                id='xcol', value='Platform',
            options=[{'label': i, 'value': i} for i in ['Genre','Platform','Publisher']]),
                            dbc.Label("Select Y Axis:"),
                            dcc.Dropdown(
                                id='ycol', value='Genre',
            options=[{'label': i, 'value': i} for i in ['Genre','Platform','Publisher']]),
                            dbc.Label("Select Time Rage:"),
                            dcc.RangeSlider(id='dist_slider', min=1980, max=2017, value=[1980,2016], step=1, tooltip={"placement": "bottom", "always_visible": True})
                        ])
                    ])
                ]),
                dbc.Col(children=[
                    html.Iframe(
                        id='heatmap',
                        style={'border-width': '0', 'width': '100%', 'height': '400px'},
                    )            
                ])
            ])
        ], style={'border': '5px solid #828282', 'border-radius': '10px'}
    )

    # Set up callbacks/backend
@dash.callback(
    Output('heatmap', 'srcDoc'),
    [Input('dist_slider', 'value'),
     Input('xcol','value'),
     Input('ycol','value')
    ]
)
def heatmap(years,xcol,ycol):
    plot = (alt.Chart(pg2_data[(pg2_data['Year'] > years[0]) & (pg2_data['Year'] < years[1])]).mark_rect().encode(
                    alt.X(xcol, title = xcol, axis=alt.Axis(labelAngle=-45)),
                    alt.Y(ycol, title = ycol),
                    color = alt.Color('count()',title ='Games Count', scale=alt.Scale(scheme='lightgreyred')),
                    tooltip=['count()']
                )
            .properties(width=500, height=500)
           )
    return plot.to_html()