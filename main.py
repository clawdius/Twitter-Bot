import tweepy
import logging
import os

log = logging.getLogger()

def create_api():
    consumer_key = os.environ['CONSUMER_KEY']
    consumer_key_secret = os.environ['CONSUMER_SECRET_KEY']
    access_token = os.environ['ACCESS_TOKEN']
    access_token_secret = os.environ['ACCESS_SECRET_TOKEN']

    auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as exc:
        log.error("Error creating API!", exc_info=True)
        raise exc

    log.info("API Created!")
    return api