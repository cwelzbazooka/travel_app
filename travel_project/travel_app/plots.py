from geopy.geocoders import Nominatim
from plotly.offline import plot
from plotly.graph_objs import Scattergeo, Layout
import pandas as pd 
from datetime import datetime




def get_map_travel():
    
    lons = [-73.968285]
    lats = [40.785091]
    czasy =[3]
    title = 'próba'
    data=[{
        'type': 'scattergeo',
        'lon' : lons,
        'lat' : lats,
        'text': "text",
        'marker' : {
            'size' : [20+czas for czas in czasy],
            'color' : "gold",
            
        },
    
    }]
    
    my_layout = Layout(
        margin=dict(l=10, r=10, t=10, b=10),
    )
    
    fig = {'data':data,'layout':my_layout}
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div

