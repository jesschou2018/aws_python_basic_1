# Imports
import argparse
from sm_text import *
import networkx as nx
import pandas as pd
import json
import ast

usernetwork_df = pd.read_csv("all_users.csv")

G = nx.from_pandas_edgelist(usernetwork_df, 'Source', 'Target',edge_attr=None, create_using=nx.DiGraph()) #Turn df into graph
pos = nx.spring_layout(G)

import matplotlib.pyplot as plt
f, ax = plt.subplots(figsize=(30, 30))
plt.style.use('ggplot')
nodes = nx.draw_networkx_nodes(G, pos,  alpha=0.8)
nodes.set_edgecolor('k')
nx.draw_networkx_labels(G, pos, font_size=8)
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.2)

plt.savefig("Graph1.png", format="PNG")


#G = nx.from_pandas_edgelist(complete_df, 'Source', 'Target') #Turn df into graph
#pos = nx.spring_layout(G)
# Set up parser to take input variab
# run sm_text
#text1 = sm_text(val)
#print(sm_text.extract_at_tags(text1))
#print(sm_text.extract_hashtags(text1))
