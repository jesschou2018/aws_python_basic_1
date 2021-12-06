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


# At present most effective way to consolidate DataFrames  - toreview.
user_list=[]
tweet_list=[]
list_iter = [j for j in range(5)]


for i in list_iter:
    user_list.append(data_users[i])
    
for k in list_iter:
    tweet_list.append(data_tweets[k])  
    

data_tweets_df=pd.concat(tweet_list, axis=0)
data_tweets_df["at_tags"] =data_tweets_df["text"].apply(lambda x:(sm_text.extract_at_tags(sm_text(x))))
data_tweets_df["hash_tags"] =data_tweets_df["text"].apply(lambda x:(sm_text.extract_hashtags(sm_text(x))))

# tidy up our users_df

data_users_df=  pd.concat(user_list, axis=0)
print(data_users_df.head(10))

data_users_df.to_csv("all_users.csv")
data_tweets_df.to_csv("all_tweets.csv")




