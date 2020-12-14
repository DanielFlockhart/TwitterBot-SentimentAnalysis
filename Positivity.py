

import tweepy,random,time,sys
from textblob import TextBlob
consumer_key = 'zcczgt1C8b9NO2bPWU5hOjcPv'
consumer_secret = 't0EKMV1mFnkzsNsEMN7bUDvR1ZW0CxRNQfaJiKTzWCoxhqg4PA'
access_token = '1157382902793015297-r8ovrS4FFPaAGBQOo5YSuggQDxIJKk'
access_token_secret = 'tYhPE6tuNOYLpxGmVTK65iEulwouYvrXbzcH5GkfABsAG'
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
message = "This tweet has been identified as one needing some positivity :),so whatever you are going throughjust know that there are people to support you and you are a beautiful, smart intelligent human"
public_tweets = api.search(random.choice(words))
most_negative = 10000000
tweetId = ""
for tweet in public_tweets:
    try:
        analysis = TextBlob(tweet.text)
        negativity = analysis.sentiment
        
        if negativity > most_negative:
            tweetId = tweet.id
            most_negative = negativity
    except:
        pass


api.update_status(status=message,in_reply_to_status_id=tweetId)


