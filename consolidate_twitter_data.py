# Imports
import argparse
from sm_text import *
import networkx as nx
import pandas as pd
import json
import ast
  
# reading the  users data from the file
with open('users_to_examine.txt') as f:
    data = f.read()
# reconstructing the users as a dictionary
userdict = json.loads(data)


file = open("users_to_examine.txt", "r")

contents = file.read()
userdict = ast.literal_eval(contents)

file.close()

# Loop over all users - for each, read in the data, apply transformations, append to main dataframe

data_tweets=[]
data_users=[]

#https://stackoverflow.com/questions/13784192/creating-an-empty-pandas-dataframe-then-filling-it

for key in userdict.keys():
    outfileuser='usernetwork'+key+'.csv'
    outfiletweets='tweets'+key +'.csv'
    usernetwork_df = pd.read_csv(outfileuser)
    tweet_df= pd.read_csv(outfiletweets)
    tweet_df["from"]=key
    data_tweets.append(tweet_df)
    data_users.append(usernetwork_df)


# Tidy up our tweets - we use the following list appending for performance reasons, so need to split it out

data_tweets_df= pd.concat([data_tweets[0]["id"],
data_tweets[0]["created_at"],
data_tweets[0]["favorite_count"],
data_tweets[0]["retweet_count"],
data_tweets[0]["text"],
data_tweets[0]["from"]],axis=1)



#data_users_df=  pd.DataFrame(data_users, columns["source","target"])
data_tweets_df["at_tags"] =data_tweets_df["text"].apply(lambda x:(sm_text.extract_at_tags(sm_text(x))))
data_tweets_df["hash_tags"] =data_tweets_df["text"].apply(lambda x:(sm_text.extract_hashtags(sm_text(x))))
# don't drop text for now - might need it. data_tweets_df = data_tweets_df.drop("text", 1)


# Tidy up our user/follower DataFrame

data_users_df= pd.concat([data_users[0]["Source"],
data_users[0]["Target"]],axis=1)


data_users_df.to_csv("all_users.csv")
data_tweets_df.to_csv("all_tweets.csv")




