import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd

from pages import (
    distributions, 
    global_sales, 
    otherAnalysis, 
    topGames
)

#read data file
vg_sales = pd.read_csv("data/vgsales-cleaned.csv", parse_dates=['Year'])
vg_sales['Year'] = vg_sales['Year'].dt.year.astype('Int64')

# Setup app and layout/frontend
app = dash.Dash(__name__,  external_stylesheets= [dbc.themes.UNITED])
app.title = "Video Game Sales"
server = app.server
app.layout = dbc.Container(
    [dcc.Location(id="url", refresh=False), dbc.Container(id="page-content")]
)
                       
# Update page
@app.callback(
    Output("page-content", "children"), 
    [Input("url", "pathname")]
)
def display_page(pathname):
    #if pathname == "/vg-sales/distributions":
    #    return distributions.create_layout(app,vg_sales)
    #elif pathname == "/vg-sales/top-games":
    #    return topGames.create_layout(app,vg_sales)
    #elif pathname == "/vg-sales/other":
    #    return otherAnalysis.create_layout(app,vg_sales)
    #else:
    return global_sales.create_layout(app,vg_sales)

if __name__ == '__main__':
    app.run_server(debug=True)