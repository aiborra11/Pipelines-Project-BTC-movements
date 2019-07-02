import json
import requests
from datetime import datetime

res = requests.get('https://www.bitstamp.net/api/ticker_hour/')
dev=res.json()

def TimeConverter (dev):
    Timestamp = int(dev.get('timestamp'))
    time_conversion = str(datetime.fromtimestamp(Timestamp))
    date_split = time_conversion.split()
    date=[date_split[0]]
    time=[date_split[1]]
    return date, time

def GetBtc(df):

    lst = [*dev.values()]
    date, time = TimeConverter(dev)
    Open = [lst[8]]
    High = [lst[0]]
    Low = [lst[6]]
    Close = [lst[1]]
    VolumeBTC = [lst[5]]
    Weighted_Price = [lst[4]]
    print('Date: {}, ' .format(date))
    print('Time: {}, ' .format(time))
    print('Open: {}, ' .format(Open))
    print('High: {}, ' .format(High))
    print('Low: {}, ' .format(Low))
    print('Close: {}, ' .format(Close))
    print('Volume BTC: {}, ' .format(VolumeBTC))
    print('Weighted Price: {}, ' .format(Weighted_Price))
    return date, time, Open, High, Low, Close, VolumeBTC, Weighted_Price



#print(dev)
#print(TimeConverter(dev))
#print(GetBtc(dev))