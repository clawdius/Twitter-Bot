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

    def goodMorning():
        api = create_api()
        idolToday = randomIdols()
        api.update_status('Good morning! Today is a good time to worship ' + idolToday + '!')
        api.update_profile(name="Worshipping " + idolToday + " 🤖")
        log.info("Profile and tweet updated!")

    def obliterate():
        api = create_api() 
        counter = 0
        successfulProcess = 0

        for idols in hashtags:
            for i in api.search(hashtags[counter], count=2, result_type='mixed', lang='en'):

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
                        successfulProcess += 1
                    except Exception:
                        log.error("Cant like and retweet", exc_info=True)

                counter += 1
                time.sleep(1)
                log.info("Searching next hashtag")
        
        log.info("Successfully processing " + str(successfulProcess) + " tweet(s)")
        api.update_profile(description="Successfully obliterated " + str(successfulProcess) + " tweet(s) on the last operation")

    schedule.every(2).hours.do(obliterate)
    schedule.every().day.at('06:00').do(goodMorning)
    # formatTime = "%H:%M:%S"

    # def timeUntilNextObliterate():
    #     nextRun = schedule.next_run().time().strftime(formatTime)
    #     timeNow = datetime.datetime.now().strftime(formatTime)
    #     delta = datetime.datetime.strptime(nextRun, formatTime) - datetime.datetime.strptime(timeNow, formatTime)

    #     deltafix = str(delta).replace('-1 day,','')

    #     return deltafix + " next until operation"

    # def nextObliterateString():
    #     return str(schedule.next_run().time().strftime(formatTime))

    while 1:
        schedule.run_pending()
        time.sleep(1)
          
if __name__ == "__main__":
        main()
        


