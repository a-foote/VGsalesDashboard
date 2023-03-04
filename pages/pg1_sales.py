import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output
import altair as alt
import pandas as pd

from plot_functions import sales_time
import pg_head as ph

dash.register_page(__name__,path='/',name="Global Sales")

pg1_data = pd.read_csv("data/vgsales-cleaned.csv", parse_dates=['Year'])
pg1_data['Year'] = pg1_data['Year'].dt.year.astype('Int64')

layout = dbc.Container(
        children=[
            dbc.Row([
                dbc.Col(children=[html.H5("map plot will go here")], width=6),
                dbc.Col(children=[
                    html.Iframe(
                        id='scatter',
                        #srcDoc=sales_time(df,xmax=2016),
                        style={'border-width': '0', 'width': '100%', 'height': '400px'},
                    ),
                    dcc.RangeSlider(id='gs_slider', min=1980, max=2017, value=[1980,2016], step=1, marks=None, tooltip={"placement": "bottom", "always_visible": True})
            
                ], width=6)
            ])
        ]
    )

    # Set up callbacks/backend
@dash.callback(
    Output('scatter', 'srcDoc'),
    [Input('gs_slider', 'value')]
)
def sales_time(years):
    plot = (alt.Chart(pg1_data[(pg1_data['Year'] > years[0]) & (pg1_data['Year'] < years[1])], title='Total Regional Sales').mark_circle().encode(
                    alt.X('Year',scale=alt.Scale(zero=False), title=None, axis=alt.Axis(format='d')), 
                    alt.Y('sum(Global_Sales)', title='Sum of Sales (millions)', axis=alt.Axis(format='$s'))
                )
           )

#         band = (alt.Chart(df).mark_errorband(extent='ci').encode(
#                         x='Year',
#                         y='Global_Sales'
#                     )

#                )

    final_plot = (plot).configure_mark(color='red')
    return final_plot.to_html()

# def update_sales(xmax):
#     print(xmax)
#     return sales_time(df,xmax)
#sales_time.sales_time(vg_sales)