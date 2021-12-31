# Imports
import argparse
from sm_text import *
import networkx as nx
import pandas as pd
import json
import ast

#https://stackoverflow.com/questions/13784192/creating-an-empty-pandas-dataframe-then-filling-it
def consolidate_tweets(userdict):
    data_tweets=[]
    user_size=len(userdict)
    for key in userdict.keys():
        outfiletweets='tweets'+key +'.csv'
        tweet_df= pd.read_csv(outfiletweets)
        tweet_df["from"]=key
        data_tweets.append(tweet_df)
    tweet_list=[]
    list_iter = [j for j in range(user_size)]
    for i in list_iter:
        tweet_list.append(data_tweets[i])
    data_tweets_df=pd.concat(tweet_list, axis=0)
    data_tweets_df["at_tags"] =data_tweets_df["text"].apply(lambda x:(sm_text.extract_at_tags(sm_text(x))))
    data_tweets_df["hash_tags"] =data_tweets_df["text"].apply(lambda x:(sm_text.extract_hashtags(sm_text(x))))
    return(data_tweets_df)

def consolidate_users_network(userdict):
    data_users=[]
    user_size=len(userdict)
    for key in userdict.keys():
        outfileuser='usernetwork'+key+'.csv'
        usernetwork_df = pd.read_csv(outfileuser)
        data_users.append(usernetwork_df)
    user_list=[]
    list_iter = [j for j in range(user_size)]
    for i in list_iter:
        user_list.append(data_users[i])
    data_users_df=  pd.concat(user_list, axis=0)
    return(data_users_df)
