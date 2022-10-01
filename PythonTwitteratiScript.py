Update the below details in the .env file and add personal credentials...
# CONSUMER_KEY=YOURKEYGOESHERE
# CONSUMER_SECRET=YOURSECRETGOESHERE
# ACCESS_TOKEN=YOURACCESSTOKENGOESHERE
# ACCESS_SECRET=ACCESSSECRETGOESHERE

import tweepy
from decouple import config

auth = tweepy.OAuthHandler(config("CONSUMER_KEY"), config("CONSUMER_SECRET"))
auth.set_access_token(config("ACCESS_TOKEN"), config("ACCESS_SECRET"))

# API instance

api = tweepy.API(auth)

api.update_status("This is a test tweet using tweepy.")
