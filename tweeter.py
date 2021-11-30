from dotenv import load_dotenv
import os 
import tweepy
from tweepy.auth import OAuthHandler
import pandas as pd
import json
import time
from pandas import DataFrame
import numpy as np

load_dotenv()
consumer_key=os.environ.get('APIKey')
consumer_secret=os.environ.get('APIKeySecret')

access_token=os.environ.get('AccessKey')
access_token_secret = os.environ.get('AccessSecret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class tweeter:
  def __init__(self,userhandle):
    self.text = userhandle

  def get_friends(self,retrieve_no):
    print('Getting friends (those the users follows)',self)
    friends = tweepy.Cursor(api.get_friends, screen_name=self).items(retrieve_no)
    friends_list=[i.name for i in friends]
    return(friends_list)

  def get_followers(self, retrieve_no):
    print('Getting followers',self)
    followers = tweepy.Cursor(api.get_followers, screen_name=self).items(retrieve_no)
    followers_screen_list=[j.name for j in  followers]
    #followers_list_id=[i.id for i in followers]
    return(followers_screen_list)
    
  def get_latest_tweets(self,retrieve_no):     
    tweets = api.user_timeline(screen_name=self,# 200 is the maximum allowed count 
                            count=retrieve_no,# 200 is the maximum allowed count 
                           include_rts = False,
                           tweet_mode = 'extended' # get full text 
                           )
    all_tweets = []
    all_tweets.extend(tweets)
    oldest_id = tweets[-1].id
    while True:
        tweets = api.user_timeline(screen_name=self, 
                               # 200 is the maximum allowed count
                               count=retrieve_no,
                               include_rts = False,
                               max_id = oldest_id - 1,
                               # Necessary to keep full_text 
                               # otherwise only the first 140 words are extracted
                               tweet_mode = 'extended'
                               )
        if len(tweets) == 0:
            break
        oldest_id = tweets[-1].id
        all_tweets.extend(tweets)
    #transform the tweepy tweets into a 2D array that will populate the csv	
    outtweets = [[tweet.id_str, 
                  tweet.created_at, 
                  tweet.favorite_count, 
                  tweet.retweet_count, 
                  tweet.full_text.encode("utf-8").decode("utf-8")] 
                 for idx,tweet in enumerate(all_tweets)]
    tweet_df = DataFrame(outtweets,columns=["id","created_at","favorite_count","retweet_count", "text"])
    return(tweet_df)