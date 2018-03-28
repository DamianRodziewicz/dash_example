# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Input(
        id = 'text-input',
        placeholder='Enter a value...',
        type='text',
        value=''
    ),

    html.Div(id = 'text-output'),

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
    Output('text-output', 'children'),
    [Input('text-input', 'value')])
def update_text_output(input_value):
    return 'You have entered: ' + input_value


if __name__ == '__main__':
    app.run_server(debug=True)
