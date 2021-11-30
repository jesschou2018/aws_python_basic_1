
# Imports
import argparse
import time
from tweeter import *

# Set up parser to take input variable as paremeter
parser = argparse.ArgumentParser()
parser.add_argument("--val")
args = parser.parse_args()
val = args.val

# run get extracts - with a break between each
followers=tweeter.get_followers(val, 250)
time.sleep(60*15)
friends=tweeter.get_friends(val, 250)
time.sleep(60*15)

# create a dataframe of friends 
friend_df = pd.DataFrame(columns=['Source','Target']) #Empty DataFrame
friend_df['Target'] = friends #Set the list of followers as the target column
friend_df['Source'] = val
# followers dataframe
followers_df = pd.DataFrame(columns=['Source','Target']) #Empty DataFrame
followers_df['Source'] = followers
followers_df['Target'] = val#Set the list of followers as the target column

# stack to create a twitter user network dataframe

user_network=followers_df.append(friend_df, ignore_index=True)

user_network.to_csv('user_network.csv')

tweets_df=tweeter.get_latest_tweets(val, 200)
tweets_df.to_csv('tweets.csv')