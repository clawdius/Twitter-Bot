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

    def goodMorning():
        api = create_api()
        idolToday = randomIdols()
        api.update_status('Good morning! Today is a good time to worship ' + idolToday + ' !')
        api.update_profile(name="Worshipping " + idolToday + " 🤖")
        log.info("Profile and tweet updated!")

    schedule.every().day.at('06:00').do(goodMorning)

    while 1:
        schedule.run_pending()
        time.sleep(1)
          
if __name__ == "__main__":
        main()
        
    