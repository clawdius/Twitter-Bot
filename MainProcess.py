import datetime
import json
import logging
import random
import sys
import time

import schedule
import tweepy

from idolsConfig import hashtags, idols
from mainDummy import create_api

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()

# Create blank availableIdols on first program run
availableIdols = []

def main():   
   
    def nextOperationString():
        return str(schedule.next_run().time().strftime(formatTime)) 

    def goodMorning():

        global availableIdols

        if not availableIdols:
            availableIdols = idols[:]
        
        idolToday = randomIdolsGenerator()
        availableIdols.remove(idolToday)

        api = create_api()
        api.update_status('Good morning! Today is a good time to worship ' + idolToday + '!')
        api.update_profile(name="Worshipping " + idolToday + " 🤖")

        picsIndex = str(random.randint(1, 3))
        picsLoc = 'pic/' + idolToday + picsIndex + '.png'
        api.update_profile_image(picsLoc)

        log.info("Profile and tweet updated!")
        log.info("Current idols on pool: "+ str(len(availableIdols)) +" idols")

    def obliterate():
        api = create_api() 
        successfulProcess = 0
        counter = 0

        # create available hashtags every 2 hours
        availableHashtags = hashtags[:]
        random.shuffle(availableHashtags)

        for j in availableHashtags:

            for i in api.search(availableHashtags[counter] + ' filter:media', count=1, result_type='recent', lang='en'):

                log.info("Searching " + availableHashtags[counter]) 

                if not i.favorited:
                    try:
                        i.favorite()
                        log.info(f"Liked tweet from {i.user.name}")
                    except Exception:
                        log.error("Already Liked")

                if not i.retweeted:
                    try:
                        i.retweet()
                        log.info(f"Retweeted tweet from {i.user.name}")
                        successfulProcess += 1
                    except Exception:
                        log.error("Already Retweeted")
                time.sleep(1)
            
            counter += 1  

        availableHashtags.clear()
        log.info("Successfully processing " + str(successfulProcess) + " tweet(s)")
        api.update_profile(description="Successfully obliterated " + str(successfulProcess) + " tweet(s) at " + nextOperationString() + " timestamp (GMT+7)")

    def timeUntilNextOperation():
        nextRun = schedule.next_run().time().strftime(formatTime)
        timeNow = datetime.datetime.now().strftime(formatTime)
        delta = datetime.datetime.strptime(nextRun, formatTime) - datetime.datetime.strptime(timeNow, formatTime)

        deltafix = str(delta).replace('-1 day,','')

        return deltafix + " next until operation"

    def randomIdolsGenerator():
        maxLength = len(availableIdols) - 1
        index = random.randint(0, maxLength)
        return availableIdols[index]

    # Scheduling tasks
    schedule.every(2).hours.do(obliterate)
    schedule.every().day.at('06:00').do(goodMorning)

    # Format used in time
    formatTime = "%H:%M:%S"

    while 1:
        schedule.run_pending()
        log.info(timeUntilNextOperation())
        time.sleep(1)
          
if __name__ == "__main__":
        main()
        


