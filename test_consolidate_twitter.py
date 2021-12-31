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

# test 1 - users are conslidated correctly 

our_data_users_df=consolidate_users_network(our_userdict)
print(our_data_users_df.reset_index(drop=True).equals(pd.read_csv("test_all_users.csv")))

# test 2 - tweets are conslidated correctly 
our_data_tweets_df=consolidate_tweets(our_userdict).reset_index(drop=True)
test_data_tweets_df=pd.read_csv("test_all_tweets.csv").reset_index(drop=True)
print(our_data_tweets_df.head(20))
print(test_data_tweets_df.head(10))
print(our_data_tweets_df.equals(test_data_tweets_df))
print(our_data_tweets_df["hash_tags"].equals(test_data_tweets_df["hash_tags"]))
print(our_data_tweets_df.dtypes)
print(test_data_tweets_df.dtypes)

