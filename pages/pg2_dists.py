import dash
import dash_bootstrap_components as dbc
#from dash import html, dcc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import altair as alt
import pandas as pd

dash.register_page(__name__,name="Distributions")

pg2_data = pd.read_csv("data/vgsales-cleaned.csv", parse_dates=['Year'])
pg2_data['Year'] = pg2_data['Year'].dt.year.astype('Int64')

alt.data_transformers.disable_max_rows()

layout = dbc.Container(
        children=[
            dbc.Row([
                dbc.Col(children=[
                    dbc.Card([
                        dbc.Form([
                            dbc.Label("Menu",style={"background-color":"#7e8b8c","color":"#e4000f",'font-size':20}),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            dbc.Label("Select X Axis:",style={'font-size':14}),
                            dcc.Dropdown(
                                id='xcol', value='Platform',
            options=[{'label': i, 'value': i} for i in ['Genre','Platform','Publisher']]), #{'label': i, 'value': i} for i in ['Genre','Platform','Publisher']]
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            dbc.Label("Select Y Axis:",style={'font-size':14}),
                            dcc.Dropdown(
                                id='ycol', value='Genre',
            options=[{'label': i, 'value': i} for i in ['Genre','Platform','Publisher']]),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            dbc.Label("Select Time Rage:",style={'font-size':14}),
                            dcc.RangeSlider(id='dist_slider', min=1980, max=2016, value=[1980,2016], step=1, marks=None, tooltip={"placement": "bottom", "always_visible": True})
                        ])
                    ], color="#95a5a6",style={"height": "55rem"},)
                  ],width=2),
                dbc.Col(children=[
                    html.Iframe(
                        id='heatmap',
                        style={'border-width': '0', 'width': '100%', 'height': '100%'},
                    )
                ],width=9)
            ])
        ]
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
    plot = (alt.Chart(pg2_data[(pg2_data['Year'] > years[0]) & (pg2_data['Year'] < years[1])],title="").mark_rect().encode(
                    alt.X(xcol, title = xcol, axis=alt.Axis(labelAngle=-45)),
                    alt.Y(ycol, title = ycol),
                    color = alt.Color('count()',title ='Games Count', scale=alt.Scale(scheme='lightgreyred')),
                    tooltip=['count()']
                ).properties(
                    width=650,
                    height=650
                ).configure_axis(
                    labelFontSize=15,
                    titleFontSize=15
                )
           )
    return plot.to_html()

#, style={'border': '5px solid #828282', 'margin-right':'1px','margin-bottom':'auto',}
