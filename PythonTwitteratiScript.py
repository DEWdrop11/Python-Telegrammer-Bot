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



BG_API_KEY="Your API Key"

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        username = status.user.screen_name
        status_id = status.id

        if ‘media’ in status.entities:
            for image in status.entities['media']:
                tweet_image(image['media_url'], username, status_id)
                
                
my_stream_listener = MyStreamListener()
stream = tweepy.Stream(auth, my_stream_listener)
stream.filter(track=['@saral_gyaan'])

import requests
from io import BytesIO
from PIL import Image

def tweet_image(url, username, status_id):
    filename = 'temp.png'
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        i = Image.open(BytesIO(request.content))
        i.save(filename)
        remove_bg(filename)
        api.update_with_media('no-bg.png', status=f'@{username}, Here is the picture without the background', in_reply_to_status_id=status_id)
    else:
        print("unable to download image")
def remove_bg(filename):
    response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open(filename, 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': config('BG_API_KEY')},)
    if response.status_code == requests.codes.ok:
        with open('no-bg.png', 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)

   
