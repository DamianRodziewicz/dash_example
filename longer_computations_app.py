# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import time

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Input(
        id = 'first-text-input',
        placeholder='Enter a value...',
        type='text',
        value=''
    ),

    html.Div(id = 'first-text-output'),

    dcc.Input(
        id = 'second-text-input',
        placeholder='Enter a value...',
        type='text',
        value=''
    ),

    html.Div(id = 'second-text-output'),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

@app.callback(
    Output('first-text-output', 'children'),
    [Input('first-text-input', 'value')])
def update_text_output(input_value):
    time.sleep(5)
    return 'You have entered: ' + input_value


@app.callback(
    Output('second-text-output', 'children'),
    [Input('second-text-input', 'value')])
def update_text_output(input_value):
    time.sleep(5)
    return 'You have entered: ' + input_value

server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)
