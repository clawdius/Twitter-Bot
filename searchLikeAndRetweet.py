import tweepy
import logging
from mainDummy import create_api
from idolsHashtags import hashtags
import schedule
import time
import json
import datetime

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
                        log.info(f"Liked tweet from {i.user.name}")
                    except Exception:
                        log.error("Cant like", exc_info=True)

                if not i.retweeted:
                    try:
                        i.retweet()
                        log.info(f"Retweeted tweet from {i.user.name}")
                    except Exception:
                        log.error("Cant like and retweet", exc_info=True)


            counter += 1
        log.info("Process Completed")

    schedule.every().hours.do(obliterate)

    while 1:
        schedule.run_pending()
        log.info("Waiting next run")
        time.sleep(1)
          
if __name__ == "__main__":
        main()
        


