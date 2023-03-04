import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output
import altair as alt

from plot_functions import sales_time
import pg_head as ph

alt.data_transformers.disable_max_rows()

def create_layout(app, df):
    #create plot
    # def sales_time(df,xmax):
    #     print('xmax:',xmax)
    #     print('year:',df['Year'])
    #     plot = (alt.Chart(df[df['Year'] < xmax], title='Total Regional Sales').mark_circle().encode(
    #                     alt.X('Year:T',scale=alt.Scale(zero=False), title=None,  axis=alt.Axis(labels=False)), 
    #                     alt.Y('sum(Global_Sales)', title='Sum of Sales (millions)', axis=alt.Axis(format='$s'))
    #                 ).configure_mark(color='red')
    #            )

#         band = (alt.Chart(df).mark_errorband(extent='ci').encode(
#                         x='Year',
#                         y='Global_Sales'
#                     )

#                )

#         final_plot = (plot + band).configure_mark(color='red')
        #return plot.to_html()

    # Page layouts
    print(df.info())
    return dbc.Container(
        [
            dbc.Row([ph.header(app)]),
            dbc.Row([
                dbc.Col(html.H5("map plot will go here")),
                dbc.Col([
                    html.Iframe(
                        id='scatter',
                        sandbox='allow-scripts',
                        #srcDoc=sales_time(df,xmax=2016),
                        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
                    dcc.RangeSlider(1980, 2016, value=[1980,2016], marks={1980: '1980', 2016: '2016'}, step=1,id='gs-slider',tooltip={"placement": "bottom", "always_visible": True})
                ])
            ])
        ], style={'border': '5px solid #828282', 'border-radius': '10px'}
    )

    # Set up callbacks/backend
    @app.callback(
        Output('scatter', 'srcDoc'),
        [Input('gs-slider', 'value')]
        )
    def sales_time(years):
        print(years)
        plot = (alt.Chart(df[(df['Year'] > years[0]) & (df['Year'] < years[1])], title='Total Regional Sales').mark_circle().encode(
                        alt.X('Year',scale=alt.Scale(zero=False), title=None), 
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