import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import pandas as pd
from plot_functions import *


#read data file
vg_sales = pd.read_csv("data/vgsales-cleaned.csv", parse_dates=['Year'])

# Setup app and layout/frontend
app = dash.Dash(__name__,  external_stylesheets= ['https://codepen.io/chriddyp/pen/bWLwgP.css'])
app.layout = html.Div([
    html.Iframe(
        id='scatter',
        srcDoc=sales_time.sales_time(vg_sales),
        style={'border-width': '0', 'width': '100%', 'height': '400px'})])

# Set up callbacks/backend
#@app.callback(
#    Output('scatter', 'srcDoc'),
#    Input('xcol-widget', 'value'))
#sales_time.sales_time(vg_sales)

if __name__ == '__main__':
    app.run_server(debug=True)