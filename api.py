import json
import requests
from datetime import datetime

res = requests.get('https://www.bitstamp.net/api/ticker_hour/')
dev = res.json()

def timeconverter (dev):
    Timestamp = int(dev.get('timestamp'))
    time_conversion = str(datetime.fromtimestamp(Timestamp))
    date_split = time_conversion.split()
    date=[date_split[0]]
    time=[date_split[1]]
    return date, time

def getbtc(df):
    lst = [*dev.values()]
    date, time = timeconverter(dev)
    Open = [lst[8]]
    High = [lst[0]]
    Low = [lst[6]]
    Close = [lst[1]]
    VolumeBTC = [lst[5]]
    Weighted_Price = [lst[4]]
    return 'Date: {}, Time: {}, Open {}, High {}, Low {}, Close {}, VolumeBTC {}, Weighted_Price {}' .format(date, time, Open, High, Low, Close, VolumeBTC, Weighted_Price)

