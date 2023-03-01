import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

def header(app):
    header = dbc.Container([
                dbc.Row([
                    dbc.Col(
                        html.H1("Video Game Sales: A Historial Analysis", style={"background-color":"#95a5a6","color":"#e4000f","border-style": "solid","border": "25px #495152"})
                    )
                ]),
                dbc.Row([
                    dbc.Col(
                        dbc.Nav(
                            [
                                dbc.NavItem(dbc.NavLink("Global Sales", active=True, href="/vg-sales/global-sales")),
                                dbc.NavItem(dbc.NavLink("Distributions", href="/vg-sales/distributions")),
                                dbc.NavItem(dbc.NavLink("Top Games", href="/vg-sales/top-games")),
                                dbc.NavItem(dbc.NavLink("Additional Analysis", href="/vg-sales/other")),
                            ],
                            pills=True,
                        )
                    )
                ])
            ])
    return header