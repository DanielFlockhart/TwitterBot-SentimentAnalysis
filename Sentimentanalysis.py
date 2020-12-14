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
consumer_key = '2sHw7Vi6MeMCiE4cIChSkzJiU'
consumer_secret = 'zwmHQfIkyrDDV2f50RMZey8DnhxLxXDQuCrFQDi4WWdECIUEUI'
access_token = '1157382902793015297-U9tcLHaO2PWqVO7YVUqk6muX8gpsIB'
access_token_secret = 'F3kUBOLBLJ2oYsPtS2ON931XQBfZSi3lWb1YiUIKhPBc9'
def OAuth():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e:
        return None
oauth = OAuth()
api=tweepy.API(oauth)
alpha = '1157382902793015297-LpcUdyke1tnBESZZsBQNcKEnEVNcPa'
while True:
    print("tweeted")
    api.update_status("@rathburnroad hi " + str(random.choice(alpha))+ str(random.choice(alpha))+ str(random.choice(alpha))+ str(random.choice(alpha))+ str(random.choice(alpha))+ str(random.choice(alpha))+ str(random.choice(alpha))+ str(random.choice(alpha)))
    time.sleep(5 + random.randrange(0,10))

