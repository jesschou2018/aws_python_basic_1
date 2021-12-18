 #Imports
import argparse
from sm_text import *
import networkx as nx
import pandas as pd
import json
import seaborn as sns




user_tweets= pd.read_csv("all_tweets.csv")


user_tweets["infl"]= user_tweets["favorite_count"]+user_tweets["retweet_count"]
user_tweets["att_infl"]=user_tweets["at_tags"].apply(lambda x:x.count("@"))+user_tweets["hash_tags"].apply(lambda y:y.count("#"))

user_tweets_summary=user_tweets.drop(columns=["Unnamed: 0","Unnamed: 0.1", "id","created_at","text","retweet_count","favorite_count"])

print(user_tweets_summary.head())

#ax=user_tweets_summary.plot.scatter(x="att_infl", y= "infl")
ax=sns.scatterplot(x="att_infl", y= "infl", data=user_tweets_summary, hue="from")


# try one of the following
#fig = ax.get_figure()

#fig.savefig('figure.pdf')

sns.set_theme()

# Load the penguins dataset

# Plot sepal width as a function of sepal_length across days
g = sns.lmplot(
    data=user_tweets_summary,
    x="att_infl", y= "infl", hue="from",col="from",
    height=5
)

# Use more informative axis labels than are provided by default
g.set_axis_labels("attempted influence", "actual influence")

g.savefig('figure.pdf')