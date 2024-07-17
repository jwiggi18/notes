#for functionality
# python3 -m pip install packaging
# python3 -m pip install pandas dash
# pip3 install httpx==0.20 dash plotly

# to run: python3 dash_interactivity_barplot.py

#import libraries
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

#read in the dataset
airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str}) # define these columns as strings instead of numbers

# Create a dash application layout
app = dash.Dash(__name__)

app.layout = html.Div(children=[html.H1('Total number of flights to the destination state split by reporting air', style={'textAlign':'center', 'color': '#503D36', 'font-size':50}),
                                html.Div(["Input Year:", dcc.Input(id='input-year', value='2010', type='number', style={'height':'30px', 'font-size':25}),], 
                                style={'font-size': 40}),
                                html.Br(),
                                html.Br(),
                                html.Div(dcc.Graph(id='bar-plot')),
                                ])

# add callback decorator
@app.callback(Output(component_id='bar-plot', component_property='figure'),
               Input(component_id='input-year', component_property='value'),
               style={'font-size': 35})

# define callback graph function
def get_graph(entered_year):
    df =  airline_data[airline_data['Year']==int(entered_year)]
    bar_data = df.groupby('DestState')['Flights'].sum().reset_index()
    fig = px.bar(bar_data, x= "DestState", y= "Flights", title='Total number of flights to the destination state split by reporting airline') 
    fig.update_layout(title='Flights to Destination State', xaxis_title='DestState', yaxis_title='Flights')
    return fig 

#need to add go.Figure?       

# Run the app
if __name__ == '__main__':
    app.run_server()

