from datetime import datetime
from pytz import timezone
import pytz


class timeLog:

    def __init__(self, timesTamp=None) -> None:
        self.timestamp = timesTamp

    def datenow(self):
        now = datetime.now()
        return now

    def get_TimesTamp(self):
        timestamp = self.timestamp
        date_time = datetime.utcfromtimestamp(timestamp)
        str_date_time = date_time.strftime("%H:%M")
        return str_date_time

    def set_Timestamp(self):
        now = datetime.now(pytz.timezone('UTC'))
        new_now = now.replace(microsecond=0) 
        set_utc_time = new_now.replace(tzinfo=pytz.utc).timestamp()
        return set_utc_time

if __name__ == '__main__':
    a = timeLog().set_Timestamp()
    print(a)
