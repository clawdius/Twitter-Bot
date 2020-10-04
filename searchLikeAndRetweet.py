import tweepy
import logging
from main import create_api
from idolsHashtags import hashtags
import schedule
import time
import json

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


def main():
    api = create_api()
    
    def obliterate():
        counter = 0
        for idols in hashtags:
            for i in api.search(hashtags[counter], count=1, result_type='photos', lang='en'):

                if not i.favorited:
                    try:
                        i.favorite()
                    except Exception:
                        log.error("Cant like", exc_info=True)

                if not i.retweeted:
                    try:
                        i.retweet()
                    except Exception:
                        log.error("Cant like and retweet", exc_info=True)

            counter += 1
            time.sleep(5)

    schedule.every(12).hours.do(obliterate)

    while 1:
        schedule.run_pending()
        time.sleep(1)
          
if __name__ == "__main__":
        main()
        


