#import gunicorn
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
#from dash import html, dcc
import dash_html_components as html
import dash_core_components as dcc
import os


app = dash.Dash(__name__,  external_stylesheets= [dbc.themes.UNITED], suppress_callback_exceptions=True,use_pages = True)
server = app.server

app.layout = dbc.Container(children=[
                dbc.Row(children=[
                    dbc.Col(children=[
                        html.H1("Video Game Sales: A Historial Analysis", style={"background-color":"#95a5a6","color":"#e4000f",'border': '5px solid #828282','padding':0})
                    ])
                ]),
                dbc.Row(children=[
                    dbc.Col(children=[
                        dbc.Nav(
                            [
                                dbc.NavItem(dbc.NavLink(page['name'], href=page['path']))
                                for page in dash.page_registry.values()
                            ],
                            pills=True
                        )
                    ])
                ]),
                dbc.Row(children=[dash.page_container])
            ],fluid=True,
)

if __name__ == '__main__':
    app.run_server(debug=True)
