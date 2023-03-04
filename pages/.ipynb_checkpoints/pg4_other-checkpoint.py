import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output
import altair as alt
import pandas as pd

dash.register_page(__name__,name="Other Analysis")

pg4_data = pd.read_csv("data/vgsales-cleaned.csv", parse_dates=['Year'])
pg4_data['Year'] = pg4_data['Year'].dt.year.astype('Int64')

layout = dbc.Container(
        children=[
            dbc.Row([
                dbc.Col(children=[
                    dbc.Row([dbc.Label("Region:",style={'font-size':14}),
                            dcc.Dropdown(
                                id='region', value='Global_Sales',
                                options=[{'label' : "Global", 'value' : "Global_Sales"},
                                          {'label' : "North America", 'value' : "NA_Sales"},
                                          {'label' : "European Union", 'value' : "EU_Sales"},
                                          {'label' : "Japan", 'value' : "JP_Sales"},
                                          {'label' : "Other", 'value' : "Other_Sales"}]
                                )
                            ]),
                    html.Iframe(
                        id='hist_sales',
                        style={'border-width': '0', 'width': '100%', 'height': '200%'},
                    ),
                   dcc.Checklist(
                       id='logcheck', value=["Logarithmic"], persistence=True,
                       options=[{"label":"Logarithmic Scale", "value":"Logarithmic"}]
                   )
                  ],width=6),
                dbc.Col(children=[
                     dbc.Row([dbc.Label("Category:",style={'font-size':14}),
                            dcc.Dropdown(
                                id='category', value='Genre',
                                options=[{'label' : "Genre", 'value' : "Genre"},
                                          {'label' : "Platform", 'value' : "Platform_grouped"},
                                          {'label' : "Publisher", 'value' : "Publisher_grouped"}]
                                )
                    ]),
                    html.Iframe(
                        id='piechart',
                        style={'border-width': '0', 'width': '100%', 'height': '200%'},
                    )
                ],width=6)
            ])
        ]
    )

    # Set up callbacks/backend
@dash.callback(
    Output('hist_sales', 'srcDoc'),
    [Input('region', 'value'),
     Input('logcheck','value')
    ]
)
def sales_hist(region, logcheck):
    plot = (alt.Chart(pg4_data).mark_bar().encode(
                    alt.X(region, bin=alt.Bin(extent=[0, 3], step=0.2), title = 'Sales (millions)', axis=alt.Axis(format='$s')),
                    alt.Y('count()', scale=alt.Scale(type="log" if len(logcheck) != 0 else "linear"), title = 'Number of Games'),
                    tooltip=['count()']
                )
            .configure_mark(color='red')
           )
    return plot.to_html()
@dash.callback(
    Output('piechart', 'srcDoc'),
    [Input('category', 'value')]
)
def piechart(category):
    plot = (alt.Chart(pg4_data).mark_arc().encode(
                    theta=alt.Theta(
                        field=category,
                        aggregate='count'
                    ),
                    color=alt.Color(
                        field=category
                    ),
                    tooltip = [category,'count(category):Q']
                )             
           )
    return plot.to_html()



#, style={'border': '5px solid #828282', 'margin-right':'1px','margin-bottom':'auto',}