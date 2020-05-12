import dash
from dash.dependencies import  Input,Output,State
import data_gen



colors = {
    'text' : '#F0F0F0',
    'paper_color': '#161a28',
    'plot_color': '#000000' ,
    'transperent': 'rgba(0,0,0,0.0)'
}


def register_callback(app):

    @app.callback(dash.dependencies.Output('datewise-graph','figure'),
                    [dash.dependencies.Input('dr-metrics','start_date'),
                    dash.dependencies.Input('dr-metrics','end_date')])
    def update_datewise_graph(start_date,end_date):

        
        data = []
        dt = data_gen.get_datewise_visitor_count(start_date,end_date)
        dates = dt['dates']
        date_cnt = dt['date_cnt']
        trace = dict(x = dates,y = date_cnt,type = 'line')
        data.append(trace)
        layout = {      'title': 'Daily Visitors Count',
                        'plot_bgcolor' : colors['plot_color'],
                        'paper_bgcolor' : colors['transperent'],
                        'font': {
                        'color': colors['text']
                    }
                    }
        return {'data': data,'layout' : layout}

    @app.callback(dash.dependencies.Output('state-detail-graph','figure'),
                    [dash.dependencies.Input('state_select','value')])

    def update_state_detail_graph(state):
        
        data = []

        dt = data_gen.get_cities_count(state)
        #import sys

        
        trace = dict(x= dt['cities'], y= dt['cities_cnt'], type=  'bar')
        

        data.append(trace)
        layout = {'title':'Detailed State Wise Metrics',
                    'plot_bgcolor' : colors['plot_color'],
                        'paper_bgcolor' : colors['transperent'],
                        'font': {
                        'color': colors['text']
                    }}
        #print({'data': data,'layout' : layout}, file=sys.stderr)      
        return {'data': data,'layout' : layout}