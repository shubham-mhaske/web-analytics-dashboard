import dash
from dash.dependencies import  Input,Output,State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import data_gen

from cb import register_callback

import plot_files





app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])


app.layout = html.Div(children = [

    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="#")),
            
        ],
        brand="Web Analytics",
        brand_href="#",
        color="primary",
        dark=True,
    ),
    html.Br(),
    
    dbc.Row([
            
            dbc.Col(plot_files.card_visit_metric,width = 3),
            dbc.Col(plot_files.card_bounce_rate_metric,width = 3),
            dbc.Col(plot_files.card_total_user_metric,width = 3)

        ],
        justify="center"
    ),
    html.Br(),

    dbc.Row([
            plot_files.date_with_visit_graph()
        ],
        justify = 'center'
    ),
    html.Br(),

    dbc.Row([
            plot_files.get_state_graph()
        ],
        justify = 'center'
    ),
    html.Br(),

    dbc.Row([
            plot_files.get_pages_pie()
        ],
        justify = 'center'
    ),
    html.Br(),

    dbc.Row([
            plot_files.get_state_details()
        ],
        justify = 'center'
    )








])

register_callback(app)


if __name__ == "__main__":
    app.run_server(debug = True)

