'''
Daniel Flockhart - 2019
Twitter Response Bot (Youtube)
Version 4.0
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
FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if 'homie' in mention.full_text.lower():
            print('found homie', flush=True)
            print('responding back...', flush=True)
            api.update_status('@' + mention.user.screen_name +
                    ' Your an absolute homie', mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)

