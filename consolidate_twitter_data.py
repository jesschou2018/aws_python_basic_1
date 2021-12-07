# Imports
import argparse
from sm_text import *
import networkx as nx
import pandas as pd
import json
import ast
from tweet_consol_fns import *
  
# reading the  users data from the file
with open('users_to_examine.txt') as f:
    data = f.read()
# reconstructing the users as a dictionary
our_userdict = json.loads(data)




our_data_users_df=consolidate_tweets(our_userdict)
data_tweets_df=consolidate_users_network(our_userdict)

our_data_users_df.to_csv("all_users.csv")
data_tweets_df.to_csv("all_tweets.csv")




