# Imports
import argparse
from sm_text import *
import networkx as nx
import pandas as pd
import json
import ast
from tweet_consol_fns import *
from pandas._testing import assert_frame_equal
  
# reading the  users data from the file
with open('test_users_to_examine.txt') as f:
    data = f.read()
# reconstructing the users as a dictionary
our_userdict = json.loads(data)

our_data_users_df=consolidate_users_network(our_userdict)
our_data_tweets_df=consolidate_tweets(our_userdict)

print(our_data_users_df.reset_index(drop=True).equals(pd.read_csv("test_all_users.csv")))

print(our_data_users_df.reset_index(drop=True).head(10))
print(pd.read_csv("test_all_users.csv").head(10))
#print(our_data_tweets_df.equals(pd.read_csv("test_all_tweets.csv")))





