import tweepy
from textblob import TextBlob

consumer_key = 'YOUR CONSUMER KEY HERE'
consumer_secret = 'YOUR CONSUMER SECRET HERE'

access_token = 'YOUR ACCESS TOKEN HERE'
access_token_secret = 'YOUR ACCESS TOKEN SECRET HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
tweet_tags = input("Enter a tag or a keyword ")
public_tweets = api.search(tweet_tags)

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
