import dash
import dash_bootstrap_components as dbc
#from dash import html, dcc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import altair as alt
import pandas as pd

dash.register_page(__name__,name="Distributions")

pg2_data = pd.read_csv("data/vgsales-cleaned.csv", parse_dates=['Year']) #reading in data
pg2_data['Year'] = pg2_data['Year'].dt.year.astype('Int64') #parse dates/years properly

alt.data_transformers.disable_max_rows()

#define layout
layout = dbc.Container(
        children=[
            dbc.Row([
                dbc.Col(children=[
                    dbc.Card([
                        dbc.CardHeader("Menu",style={"background-color":"#7e8b8c","color":"black",'font-size':30, 'text-align':'center'}),
                        dbc.CardBody([
                            dbc.Form([
                                html.Br(),
                                html.Br(),
                                dbc.Label("Select X Axis:",style={'font-size':16}),
                                dcc.Dropdown(
                                    id='xcol', placeholder = 'Platform', value='Platform_grouped',
                                    options=[{'label' : "Genre", 'value' : "Genre"},
                                              {'label' : "Platform", 'value' : "Platform_grouped"},
                                              {'label' : "Publisher", 'value' : "Publisher_grouped"}]
                                ),
                                html.Br(),
                                html.Br(),
                                html.Br(),
                                html.Br(),
                                dbc.Label("Select Y Axis:",style={'font-size':16}),
                                dcc.Dropdown(
                                    id='ycol', value='Genre',
                                    options=[{'label' : "Genre", 'value' : "Genre"},
                                              {'label' : "Platform", 'value' : "Platform_grouped"},
                                              {'label' : "Publisher", 'value' : "Publisher_grouped"}]),
                                html.Br(),
                                html.Br(),
                                html.Br(),
                                html.Br(),
                                dbc.Label("Select Time Rage:",style={'font-size':16}),
                                dcc.RangeSlider(id='dist_slider', min=1980, max=2016, value=[1980,2016], step=1, marks=None, tooltip={"placement": "bottom", "always_visible": True})
                            ])
                        ])
                    ], color="#95a5a6",style={"height": "55rem"},)
                  ],width=2),
                dbc.Col(children=[
                    html.Iframe( #heatmap plot goes here
                        id='heatmap',
                        style={'border-width': '0', 'width': '200%', 'height': '200%'},
                    )
                ],width=10)
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
    # """
    # Creates the categorical heatmap plot.
    #
    #         Parameters:
    #                 years (array of int): an array of two integers, used to filter data
    #                 xcol (string): the categorical variable, as a string, used to create the heatmap
    #                 ycol (string): the categorical variable, as a string, used to create the heatmap
    #
    #         Returns:
    #                 plot (altair plot): An HTML formatted Altair heatmap plot
    # """

    #switch titles based on category selected (to get rid of '_grouped')
    if xcol == 'Platform_grouped':
        xtitle = 'Platform'
    elif xcol == 'Publisher_grouped':
        xtitle = 'Publisher'
    else:
        xtitle = xcol
    if ycol == 'Platform_grouped':
        ytitle = 'Platform'
    elif ycol == 'Publisher_grouped':
        ytitle = 'Publisher'
    else:
        ytitle = ycol
    #define plot
    plot = (alt.Chart(pg2_data[(pg2_data['Year'] > years[0]) & (pg2_data['Year'] < years[1]) & (pg2_data['Publisher_grouped'] != 'other')],title="").mark_rect().encode( #filter data
                    alt.X(xcol, title = xtitle, axis=alt.Axis(labelAngle=-45)),
                    alt.Y(ycol, title = ytitle),
                    color = alt.Color('count()',title ='Games Count', scale=alt.Scale(scheme='lightgreyred')),
                    tooltip=['count()']
                ).properties(
                    width=650,
                    height=650,
                    background='#ffffff00' #clear background
                ).configure_axis(
                    labelFontSize=15,
                    titleFontSize=15
                )
           )
    return plot.to_html()

#, style={'border': '5px solid #828282', 'margin-right':'1px','margin-bottom':'auto',}
