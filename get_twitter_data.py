
# Imports
import argparse
import time
from tweeter import *
val_name='##'
val='@###'





# Set up parser to take input variable as paremeter - turn of for now
#parser = argparse.ArgumentParser()
#parser.add_argument("--val")
#args = parser.parse_args()
#val = args.val

# run get extracts - with a break between each to aovoid 
followers=tweeter.get_followers(val, 250)
time.sleep(60*10)
friends=tweeter.get_friends(val,250)
time.sleep(60*10)

# create a dataframe of friends 
friend_df = pd.DataFrame(columns=['Source','Target']) #Empty DataFrame
friend_df['Target'] = friends #Set the list of followers as the target column
friend_df['Source'] = val_name
# followers dataframe
followers_df = pd.DataFrame(columns=['Source','Target']) #Empty DataFrame
followers_df['Source'] = followers
followers_df['Target'] = val_name#Set the list of followers as the target column

# stack to create a twitter user network dataframe

user_network=followers_df.append(friend_df, ignore_index=True)
outfileuser='usernetwork'+val_name +'.csv'
user_network.to_csv(outfileuser)

tweets_df=tweeter.get_latest_tweets(val, 50)
outfiletweets='tweets'+val_name +'.csv'
tweets_df.to_csv(outfiletweets)