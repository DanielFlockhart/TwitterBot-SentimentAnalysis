'''
Daniel Flockhart
Twitter Sentiment Analysis Test
Based off Siraj Raval Video (Youtube)
Version 2.0
'''

import tweepy,random,time,sys
from textblob import TextBlob
from colorama import *
init()
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
max_tweets = 1000
word = str(input("Search Term : "))
public_tweets = api.search(word, count=max_tweets)
polarityscore = 0
subjectivityscore = 0
tweetcount = 0
for tweet in public_tweets:
    try:
        ##print(tweet.text)
        analysis = TextBlob(tweet.text)
        ##print(analysis.sentiment)
        if analysis.polarity>=0:
            print(Fore.GREEN + "Good")
        elif analysis.polarity<0:
            print(Fore.RED +"Bad")
        subjectivityscore += analysis.subjectivity
        polarityscore += analysis.polarity
        tweetcount += 1
    except:
        pass
print(Fore.WHITE)
print("Average Polarity : " + str(polarityscore/tweetcount))
print("Average Subjectivity : " + str(subjectivityscore/tweetcount))
print("Tweet Count : " + str(tweetcount))
time.sleep(100)
