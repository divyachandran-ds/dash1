#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 15:19:42 2019

@author: divyachandran
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd 


app = dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'}) 

df = pd.read_csv('../python/dataset/mtcars.tsv',sep = '\t',header=None,skiprows=5)
print(df.head())

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )
    
app.layout = html.Div([
    html.Div([
      html.H1(children='MT CARS',
                    style={
                            'textAlign': 'center',"text-transform": 'uppercase'
                            },
                    className='twelve columns'),
          
            html.Div(children='''
                    Performance of types of cars.
                  ''',
                    style={
                            'textAlign': 'center',
                            },
                    className='eight columns offset-by-two'
            )
    ],className="row"),
    html.Div([
        html.Div([
            dcc.RadioItems(
                   id='transmission-button',
                   options=[{'label': i, 'value': i} for i in df[9].unique()],
                   value= (1),
                   labelStyle={'display': 'inline-block'}
                           ),
        
                  ],)  
    ],style={
                            'textAlign': 'center',
                            },className="row"),
    html.Div([
            dcc.Graph(
            id='graph'),
    
             ],className="row"),
    html.Div([],className="row")
    
      
])   
@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('transmission-button', 'value')])

def update_image(selector):
     
    dff = df[df[9] == selector]
    
    return  {
        'data': [go.Bar(
                x= dff[0],
                y= dff[1],      
            
                )],
        'layout': go.Layout(
            xaxis={'title': 'Type of cars'},
            yaxis={'title': "Miles/(US) gallon"},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }  
              
     
if __name__ == '__main__':
    app.run_server(debug=True)                 