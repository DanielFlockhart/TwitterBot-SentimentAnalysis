'''
Daniel Flockhart
Twitter Sentiment Analysis Test
Based off Siraj Raval Video (Youtube)
'''

import tweepy,random,time,sys
from textblob import TextBlob
consumer_key = 'xZOztdk8i9T5Xom0sLoEFv01J'
consumer_secret = '90MvUy3j09CHzGAy3GLkXKgM33FUIUXsCcEBiICYy5yxQdni1y'
access_token = '1157382902793015297-LpcUdyke1tnBESZZsBQNcKEnEVNcPa'
access_token_secret = '6zwt8fTAr0EdxDIKJAkKyaQ5fwv8XVknPrVJTAv7rzWzx'
def OAuth():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e:
        return None
oauth = OAuth()
api=tweepy.API(oauth)
words = ["twitter","2020","UK","US"]
public_tweets = api.search(random.choice(words))
most_negative = 10000000
tweetId = ""
for tweet in public_tweets:
    try:
        analysis = TextBlob(tweet.text)
        negativity = analysis.sentiment
        
        if negativity > most_negative:
            tweetId = tweet['results'][0]['id']
            most_negative = negativity
    except:
        pass
api.update_status('This tweet has been identified as one needing some positivity :), so whatever you are going through just know that there are people to support you and you are a beautiful, smart intelligent human', tweetId)

