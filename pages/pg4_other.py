import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
#from dash import html, dcc
from dash.dependencies import Input, Output
import altair as alt
import pandas as pd
import numpy as np

dash.register_page(__name__,name="Other Analysis")

pg4_data = pd.read_csv("data/vgsales-cleaned.csv", parse_dates=['Year'])
pg4_data['Year'] = pg4_data['Year'].dt.year.astype('Int64')

alt.data_transformers.disable_max_rows()

layout = dbc.Container(
        children=[
            dbc.Row([
                dbc.Col(children=[
                    dbc.Row([dbc.Label("Region:",style={'font-size':16}),
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
                     dbc.Row([dbc.Label("Category:",style={'font-size':16}),
                            dcc.Dropdown(
                                id='category', value='Genre',
                                options=[{'label' : "Genre", 'value' : "Genre"},
                                          {'label' : "Platform", 'value' : "Platform_grouped"},
                                          {'label' : "Publisher", 'value' : "Publisher_grouped"}]
                                )
                    ]),
                    html.Iframe(
                        id='piechart',
                        style={'border-width': '0', 'width': '300%', 'height': '350%'},
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
            .configure_mark(color='red').properties(
        		width=500,
        		height=400
        	)
            .properties(background='#ffffff00')
           )
    return plot.to_html()
@dash.callback(
    Output('piechart', 'srcDoc'),
    [Input('category', 'value')]
)
def piechart(category):
    # plot = (alt.Chart(pg4_data).mark_arc().encode(
    #                 theta=alt.Theta(
    #                     field=category,
    #                     aggregate='count'
    #                 ),
    #                 color=alt.Color(
    #                     field=category
    #                 ),
    #                 tooltip = [category,'count(category):Q']
    #             ).configure_view(
    #         		strokeWidth=0,
    #         		strokeOpacity=0
    #         	).properties(
    #         		width=450,
    #         		height=450
    #         	)
    #        )
    breakdown = pg4_data.groupby(category)['Name'].count().reset_index()
    breakdown.rename(columns = {'Name': 'count'}, inplace=True)
    breakdown['percentage'] = [str(np.round(i*100/np.sum(breakdown['count']))) + '%' for i in breakdown['count']]

    plot = (alt.Chart(breakdown).mark_arc().encode(
        theta=alt.Theta(field=category),
        color=alt.Color(field=category),
        tooltip=[category, 'count', 'percentage']
    ).configure_view(
             		strokeWidth=0,
             		strokeOpacity=0
             	).properties(
             		width=450,
             		height=450,
                    background='#ffffff00'
             	))

    return plot.to_html()



#, style={'border': '5px solid #828282', 'margin-right':'1px','margin-bottom':'auto',}
