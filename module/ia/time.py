from datetime import datetime

def timestamp_atc(value):
    timestamp = value
    date_time = datetime.fromtimestamp(timestamp)
    str_date_time = date_time.strftime("%H:%M:%S")
    print(str_date_time)

