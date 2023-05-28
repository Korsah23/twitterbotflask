
# Authenticate with Twitter
from flask import Flask
import tweepy
import time
import requests

# Create Flask application
app = Flask(__name__)


bearer_token=''
access_token = ''
access_token_secret = ""
consumer_key = ""
consumer_secret = ""



# Create API object
api = tweepy.Client(bearer_token=
                    bearer_token,
                    access_token = access_token,
                    access_token_secret = access_token_secret,
                    consumer_key = consumer_key,
                    consumer_secret = consumer_secret)

# Function to post a tweet
#@app.route('/')
def post_tweet(message):
    tweet = f"{message['character']} [{message['anime']}] \n \n {message['quote']}  "
    api.create_tweet(text=tweet)
    

@app.route('/')
def anime_quotes():
  response = requests.get("https://animechan.vercel.app/api/random")
  message = response.json()
  post_tweet(message)
  #print(quote)

  return "Tweet posted Successfully"





if __name__ == '__main__':
    # Main program loop
    while True:
        # Get current hour
        current_hour = time.localtime().tm_hour

        # Check if the current hour is a multiple of 1 (every hour)
        if current_hour % 1 == 0:
            anime_quotes()

        # Wait for an hour
        time.sleep(3600)  # 1 hour = 3600 seconds
