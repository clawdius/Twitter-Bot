import pytz
from datetime import datetime

def morningHoursWIB():

    formatTime = "%H:%M:%S"

    UTC = pytz.utc.localize(datetime.utcnow())
    WIB = UTC.astimezone(pytz.timezone('Asia/Jakarta'))

    return WIB.strftime(formatTime)

