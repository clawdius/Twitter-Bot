import tweepy
import logging
import schedule
import time
import json
import datetime
import sys

from main import create_api
from idolsConfig import randomIdols, idols, hashtags

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


def main():    

    def obliterate():
        api = create_api() 
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
        api.update_profile(description="Last successful obliterating idols at "+ nextObliterateString() + " (GMT+7)")

    schedule.every(2).hours.do(obliterate)
    formatTime = "%H:%M:%S"

    def timeUntilNextObliterate():
        nextRun = schedule.next_run().time().strftime(formatTime)
        timeNow = datetime.datetime.now().strftime(formatTime)
        delta = datetime.datetime.strptime(nextRun, formatTime) - datetime.datetime.strptime(timeNow, formatTime)

        deltafix = str(delta).replace('-1 day,','')

        return deltafix + " Time Remaining Until Next Obliterate"

    def nextObliterateString():
        return str(schedule.next_run().time().strftime(formatTime))

    while 1:
        schedule.run_pending()
        log.info(timeUntilNextObliterate())
        time.sleep(1)
          
if __name__ == "__main__":
        main()
        


