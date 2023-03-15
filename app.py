import gunicorn
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

#initialize a dash app
app = dash.Dash(__name__,  external_stylesheets= [dbc.themes.UNITED], suppress_callback_exceptions=True,use_pages = True, title='Video Game Analysis')
server = app.server

#setup general layout
app.layout = dbc.Container(children=[
                dbc.Row(children=[
                    dbc.Col(children=[
                        #app title
                        html.H1("Video Game Sales: A Historical Analysis", style={"background-color":"#95a5a6","color":"#c9020f",'border': '5px solid #828282','padding':0})
                    ])
                ]),
                dbc.Row(children=[
                    dbc.Col(children=[
                        dbc.Nav(
                            [
                                #create tabs
                                dbc.NavItem(dbc.NavLink(page['name'], href=page['path'],active="exact"))
                                for page in dash.page_registry.values()
                            ],
                            pills=True
                        )
                    ])
                ]),
                #call current page
                dbc.Row(children=[dash.page_container])
            ],fluid=True,
            style={'height': '100vh', 'background-image': 'url(/assets/background.jpg)','background-size': '100%', 'position': 'fixed',}
)
#run app
if __name__ == '__main__':
    app.run_server()
