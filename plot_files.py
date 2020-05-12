import dash
from dash.dependencies import  Input,Output,State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import data_gen
import plotly.graph_objs as go





colors = {
    'text' : '#F0F0F0',
    'paper_color': '#161a28',
    'plot_color': '#000000' ,
    'transperent': 'rgba(0,0,0,0.0)'
}




''' Head Metrics '''
######################################################################
#total page visits
card_visit_metric =dbc.Card( [
        dbc.CardHeader("Total Page Views"),
        dbc.CardBody(
            [
                html.H5(data_gen.total_page_views, className="card-title"),
                
            ]
        )
    ],
    color = 'success',
    inverse = True
)
#bounce rate
card_bounce_rate_metric =dbc.Card( [
        dbc.CardHeader("Bounce Rate"),
        dbc.CardBody(
            [
                html.H5(str(data_gen.bounce_rate)+' %', className="card-title"),
                
            ]
        )
    ],
    color = 'danger',
    inverse = True
)

#total users
card_total_user_metric =dbc.Card( [
        dbc.CardHeader("Total Users"),
        dbc.CardBody(
            [
                html.H5(data_gen.total_visitor_count, className="card-title"),
                
            ]
        )
    ],
    color = 'success',
    inverse = True
)

''' GRAPHS '''
##################################################################################################
state_graph = dcc.Graph(
                id = 'statewise-piechart',
                figure=go.Figure(
                        data = [ go.Bar(x = data_gen.state_names, y = data_gen.state_visitor_count)],
                        layout= go.Layout(
                            title =  'Statewise vistors',
                            plot_bgcolor = colors['plot_color'],
                            paper_bgcolor = colors['transperent'],
                            font =  {
                               'color' : colors['text']
                            }
                        )
                )
            )

daily_graph = dcc.Graph(
                id='datewise-graph'
                
            )

pages_pie = dcc.Graph(
            id = 'page-visits',
            figure=go.Figure(
                    data = [ go.Pie(labels = data_gen.page_names, values = data_gen.page_visitor_count,hole=.55)],
                    layout= go.Layout(
                        title =  'Page wise vistors',
                        plot_bgcolor = colors['plot_color'],
                        paper_bgcolor = colors['transperent'],
                        font =  {
                               'color' : colors['text']
                        }
                        
                    )
            )
        )


date_range = dcc.DatePickerRange(
                        id='dr-metrics',
                        clearable=True,
                        reopen_calendar_on_clear=True,
                        start_date_placeholder_text='Start Date',
                        end_date= data_gen.get_start_end_date()['end_date'],
                        start_date =  data_gen.get_start_end_date()['start_date'],
                        min_date_allowed=data_gen.get_start_end_date()['start_date'],
                        max_date_allowed=data_gen.get_start_end_date()['end_date']
                        
                        
                    )
state_dropdown = dcc.Dropdown(

                id = 'state_select',
                options = data_gen.state_dropdown_options,
                placeholder =  'Select state to view metric',
                value = 'Maharashtra',
                style={"color": '#0000CD' },
            )
state_cities_graph  =  dcc.Graph(
                id = 'state-detail-graph'
            )



''' Page Metrics'''
###########################################################################################
max_page_visit_metric = dbc.Card( [
        dbc.CardHeader("Maximum visitors"),
        dbc.CardBody(
            [
                html.H5(data_gen.max_visit_page, className="card-text"),
                
            ]
        )
    ],
    color = 'success',
    inverse = True
)

min_page_visit_metric = dbc.Card( [
        dbc.CardHeader("Minimum visitors"),
        dbc.CardBody(
            [
                html.H5(data_gen.min_visit_page, className="card-text"),
                
            ]
        )
    ],
    color = 'danger',
    inverse = True
)


''' State Metrics'''
###########################################################################################
max_state_visit_metric = dbc.Card( [
        dbc.CardHeader("Most visitors from"),
        dbc.CardBody(
            [
                html.H5(data_gen.max_visit_state, className="card-text"),
                
            ]
        )
    ],
    color = 'success',
    inverse = True
)

min_state_visit_metric = dbc.Card( [
        dbc.CardHeader("Least visitors from"),
        dbc.CardBody(
            [
                html.H5(data_gen.min_visit_state, className="card-text"),
                
            ]
        )
    ],
    color = 'danger',
    inverse = True
)






def date_with_visit_graph():
    return dbc.Card([
            dbc.CardBody([
                    dbc.Row([dbc.Alert("Daily Visitors Count", color="info")],
                        justify="start",
                    ),
                    html.Br(),
                    dbc.Row([
                            dbc.Col(dbc.Alert('Select Date Range',color = 'secondary',style = {'text-align': 'center'}),width = 4),
                            dbc.Col(date_range,width = 6)
                            ],
                        justify="start",
                    ),
                    html.Br(),
                    
                    dbc.Row([
                            dbc.Col(daily_graph,width = 12)
                            ],
                            justify = 'center'
                    )
            ])
        ],
        style={"width": "90%"},
        
    )


def get_state_graph():
    return dbc.Card([
                dbc.CardBody([
                        dbc.Row([dbc.Alert("Statewise Visitors Count", color="info")],
                            justify="start",
                        ),
                        html.Br(),
                        dbc.Row([
                                dbc.Col(state_graph,width = 10),
                                dbc.Col([max_state_visit_metric,html.Br(),min_state_visit_metric],width = 2)
                                ],
                                justify = 'center'
                        )
                ])
            ],
            style={"width": "90%"},
        
    )


def get_pages_pie():
    return dbc.Card([
                dbc.CardBody([
                        dbc.Row([dbc.Alert("Pagewise Visitors", color="info")],
                            justify="start",
                        ),
                        html.Br(),
                        dbc.Row([
                                dbc.Col(pages_pie,width = 10),
                                dbc.Col([max_page_visit_metric,html.Br(),min_page_visit_metric],width = 2)
                                ],
                                justify = 'center'
                        )
                ])
            ],
            style={"width": "90%"},
        
    )

def get_state_details():
    return dbc.Card([
            dbc.CardBody([
                    dbc.Row([dbc.Alert("Citywise visitors", color="info")],
                        justify="start",
                    ),
                    html.Br(),
                    dbc.Row([
                            dbc.Col(dbc.Alert('Select State to view cities',color = 'secondary',style = {'text-align': 'center'}),width = 4),
                            dbc.Col(state_dropdown,width = 6)
                            ],
                        justify="start",
                    ),
                    html.Br(),
                    
                    dbc.Row([
                            dbc.Col(state_cities_graph,width = 12)
                            ],
                            justify = 'center'
                    )
            ])
        ],
        style={"width": "90%"},
        inverse = True
    )    











