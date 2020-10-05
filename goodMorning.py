import schedule
import tweepy
import logging
import schedule
import time
import json
import datetime

from main import create_api
from idolsConfig import randomIdols

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()

def main(): 

    formatTime = "%H:%M:%S"

    def goodMorning():
        api = create_api()
        idolToday = randomIdols()
        api.update_status('Good morning! Today is a good time to worship ' + idolToday + ' !')
        api.update_profile(name="Worshipping " + idolToday + " 🤖")
        log.info("Profile and tweet updated!")

    def timeUntilNextMorning():
        nextRun = schedule.next_run().time().strftime(formatTime)
        timeNow = datetime.datetime.now().strftime(formatTime)
        delta = datetime.datetime.strptime(nextRun, formatTime) - datetime.datetime.strptime(timeNow, formatTime)

        deltafix = str(delta).replace('-1 day,','')

        return deltafix + " Time Remaining Until Next Obliterate"

    schedule.every().day.at('06:00').do(goodMorning)

    while 1:
        schedule.run_pending()
        log.info(timeUntilNextMorning())
        time.sleep(1)
          
if __name__ == "__main__":
        main()
        
    