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
with open('in_data_test_users_to_examine.txt') as f:
    data = f.read()
# reconstructing the users as a dictionary
our_userdict = json.loads(data)

# test 1 - users are conslidated correctly 

def test_consolidate_users_network():
    our_data_users_df=consolidate_users_network(our_userdict)
    assert our_data_users_df.reset_index(drop=True).equals(pd.read_csv("test_all_users.csv"))

# test 2 - tweets are conslidated correctly - note conversion of object type to string.
def test_consolidate_tweets():
    our_data_tweets_df=consolidate_tweets(our_userdict).reset_index(drop=True)
    test_data_tweets_df=pd.read_csv("test_all_tweets.csv").reset_index(drop=True)
    assert our_data_tweets_df.astype("string").equals(test_data_tweets_df.astype("string"))
    
