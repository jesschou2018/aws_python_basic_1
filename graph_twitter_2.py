 #Imports
import argparse
from sm_text import *
import networkx as nx
import pandas as pd
import json
import ast
import random
import plotly.graph_objects as go



usernetwork_df = pd.read_csv("all_users.csv")
pos = {i: (random.gauss(0, 2), random.gauss(0, 2)) for i in range(20)}
G = nx.from_pandas_edgelist(usernetwork_df, 'Source', 'Target',edge_attr=None )#Turn df into graph

# this is the layout side- need to figure out the adding in our own data for this 


    




# adding in some things.

node_adjacencies = []
node_text = []
for node, adjacencies in enumerate(G.adjacency()):
    node_adjacencies.append(len(adjacencies[1]))
    node_text.append('# of connections: '+str(len(adjacencies[1])))

#node_trace.marker.color = node_adjacencies


fig = go.Figure(data=G,
             layout=go.Layout(
                title='<br>Network graph made with Python',
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    text="Python code: <a href='https://plotly.com/ipython-notebooks/network-graphs/'> https://plotly.com/ipython-notebooks/network-graphs/</a>",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002 ) ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )
fig.show()