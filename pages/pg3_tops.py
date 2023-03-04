import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output
import altair as alt
import pandas as pd

dash.register_page(__name__,name="Top Games")

pg3_data = pd.read_csv("data/vgsales-cleaned.csv", parse_dates=['Year'])
pg3_data['Year'] = pg3_data['Year'].dt.year.astype('Int64')

layout = dbc.Container(
        children=[
            dbc.Row([
                dbc.Col(children=[
                    dbc.Card([
                        dbc.Form([
                            dbc.Label("Filters:",style={"background-color":"#7e8b8c","color":"#e4000f",'font-size':20}),
                            html.Br(),
                            html.Br(),
                            dbc.Label("Region:",style={'font-size':14}),
                            dcc.Dropdown(
                                id='region', value='Global_Sales',
                                options=[{'label' : "Global", 'value' : "Global_Sales"},
                                          {'label' : "North America", 'value' : "NA_Sales"},
                                          {'label' : "European Union", 'value' : "EU_Sales"},
                                          {'label' : "Japan", 'value' : "JP_Sales"},
                                          {'label' : "Other", 'value' : "Other_Sales"}]
                            ),
                            html.Br(),
                            html.Br(),
                            dbc.Label("Genre:",style={'font-size':14}),
                            dcc.Dropdown(
                                id='genre', value='All',
                                options=[{'label' : "All", 'value' : "All"},
                                          {'label' : "Action", 'value' : "Action"},
                                          {'label' : "Adventure", 'value' : "Adventure"},
                                          {'label' : "Fighting", 'value' : "Fighting"},
                                          {'label' : "Platform", 'value' : "Platform"},
                                          {'label' : "Puzzle", 'value' : "Puzzle"},
                                          {'label' : "Racing", 'value' : "Racing"},
                                          {'label' : "Role-Playing", 'value' : "Role-Playing"},
                                          {'label' : "Shooter", 'value' : "Shooter"},
                                          {'label' : "Simulation", 'value' : "Simulation"},
                                          {'label' : "Sports", 'value' : "Sports"},
                                          {'label' : "Strategy", 'value' : "Strategy"},
                                          {'label' : "Misc", 'value' : "Misc"}]
                            ),
                            html.Br(),
                            html.Br(),
                            dbc.Label("Publisher:",style={'font-size':14}),
                            dcc.Dropdown(
                                id='publisher', value='All',
                                options=[{'label' : "All", 'value' : "All"},
                                          {'label' : "Activision", 'value' : "Activision"},
                                          {'label' : "Electronic", 'value' : "Electronic"},
                                          {'label' : "Konami", 'value' : "Konami"},
                                          {'label' : "Namco", 'value' : "Namco"},
                                          {'label' : "Nintendo", 'value' : "Nintendo"},
                                          {'label' : "Sega", 'value' : "Sega"},
                                          {'label' : "Sony", 'value' : "Sony"},
                                          {'label' : "THQ", 'value' : "THQ"},
                                          {'label' : "Ubisoft", 'value' : "Ubisoft"},
                                          {'label' : "Other", 'value' : "Other"}]
                            ),
                            html.Br(),
                            html.Br(),
                            dbc.Label("Platform:",style={'font-size':14}),
                            dcc.Dropdown(
                                id='platform', value='All',
                                options=[{'label' : "All", 'value' : "All"},
                                          {'label' : "Atari", 'value' : "Atari"},
                                          {'label' : "Personal Computer", 'value' : "Computer"},
                                          {'label' : "Nintendo Console", 'value' : "Nintendo(console)"},
                                          {'label' : "Nintendo Handheld", 'value' : "Nintendo(handheld)"},
                                          {'label' : "PlayStation", 'value' : "PlayStation"},
                                          {'label' : "Sega", 'value' : "Sega"},
                                          {'label' : "Xbox", 'value' : "Xbox"},
                                          {'label' : "Other", 'value' : "Other"}]
                            ),
                            html.Br(),
                            html.Br(),
                            dbc.Label("Years:",style={'font-size':14}),
                           dcc.RangeSlider(id='years', min=1980, max=2017, value=[1980,2016], step=1, marks=None, tooltip={"placement": "bottom", "always_visible": True}),
                        ])
                    ], color="#95a5a6",style={"height": "55rem"},)
                  ],width=2),
                dbc.Col(children=[
                    html.Iframe(
                        id='topgames',
                        style={'border-width': '0', 'width': '100%', 'height': '75%'},
                    ),
                    dcc.Slider(id='ngames', min=1, max=20, value=5, step=1, marks={'1':'1','20':'20'}, tooltip={"placement": "bottom", "always_visible": True}),
                    dbc.Label("Number of Top Games",style={'font-size':14})
                ],width=9)
            ])
        ]
    )

    # Set up callbacks/backend
@dash.callback(
    Output('topgames', 'srcDoc'),
    [Input('region', 'value'),
     Input('years','value'),
     Input('genre','value'),
     Input('publisher','value'),
     Input('platform','value'),
     Input('ngames','value')
    ]
)
def topgames(region, years, genre, publisher, platform, ngames):
    #filter data
    df_temp = pg3_data[(pg3_data['Year'] > years[0]) & (pg3_data['Year'] < years[1])]
    if genre != 'All':
        df_temp = df_temp[df_temp['Genre'] == genre]
    if publisher != 'All':
        df_temp = df_temp[df_temp['Publisher_grouped'] == publisher]
    if platform != 'All':
        df_temp = df_temp[df_temp['Platform_grouped'] == platform]
    #generate plot
    plot = (alt.Chart(df_temp[:ngames]).mark_bar().encode(
                    alt.X(region, type='quantitative', title = 'Sales (millions)', axis=alt.Axis(format='$s')),
                    alt.Y('Name', title ='Game Name', sort='x'),
                    tooltip=['Rank','Year','Platform','Publisher']
                ).configure_mark(
                    color='red'
                )               
           )
    return plot.to_html()

#, style={'border': '5px solid #828282', 'margin-right':'1px','margin-bottom':'auto',}