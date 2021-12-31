 #Imports
import argparse
from sm_text import *
import networkx as nx
import pandas as pd
import json
import seaborn as sns
import matplotlib.pyplot as plt

# Define a function to plot word cloud
def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(figsize=(40, 30))
    # Display image
    plt.imshow(wordcloud) 
    # No axis details
    plt.axis("off");


user_tweets= pd.read_csv("all_tweets.csv")


user_tweets["infl"]= user_tweets["favorite_count"]+user_tweets["retweet_count"]
user_tweets["att_infl"]=user_tweets["at_tags"].apply(lambda x:x.count("@"))+user_tweets["hash_tags"].apply(lambda y:y.count("#"))

user_tweets_summary=user_tweets.drop(columns=["Unnamed: 0","Unnamed: 0.1", "id","created_at","text","retweet_count","favorite_count"])
new_user_df=user_tweets[["text"]]
new_user_df["all"]='All'
print(new_user_df.head())





sns.set_theme()


g = sns.lmplot(
    data=user_tweets_summary,
    x="att_infl", y= "infl", hue="from",col="from",
    height=5
)

# Use more informative axis labels than are provided by default
#g.set_axis_labels("attempted influence", "actual influence")

#g.savefig('figure1.pdf')
plt.figure(figsize=(10, 8))

# Now a basic box plots of retweets/favourites 
sns.boxplot(x="from", y="infl",palette=["m"],
            data=user_tweets_summary)
            
sns.despine(offset=10, trim=True)
plt.savefig("Figure2.pdf")

text_cloud=(', '.join(new_user_df["text"])).replace("https://t.co/", " ")


# Import package
from wordcloud import WordCloud, STOPWORDS
# Generate word cloud
wordcloud = WordCloud(width= 3000, height = 2000, random_state=1, background_color='salmon', colormap='Pastel1', collocations=False, stopwords = STOPWORDS).generate(text_cloud)
# Plot
plot_cloud(wordcloud)

wordcloud.to_file("wordcloud.pdf")

## next steps 
## tidy up
## label graphs
## loop of followers
## get rid of tiny URL in Tweets input andbettert
