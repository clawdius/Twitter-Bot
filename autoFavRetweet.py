import tweepy
import logging
from main import create_api
from idolsHashtags import hashtags
import time
import json

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()

class likeRetweet(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        log.info(f"Processing {tweet.id}")
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # Ignoring bruv
            return
        if not tweet.favorited:
            try:
                tweet.favorite()
            except Exception:
                log.error("Cant like", exc_info=True)
                
        if not tweet.retweeted:
            try:
                tweet.retweet()
            except Exception:
                log.error("Cant like and retweet", exc_info=True)
                
    def on_error(self, status):
        log.error(status)

def main():
    api = create_api()
    tweets_listener = likeRetweet(api)
    streaming = tweepy.Stream(api.auth, tweets_listener)
    streaming.filter(track=hashtags, languages=["en"])
        
if __name__ == "__main__":
        main()
        


