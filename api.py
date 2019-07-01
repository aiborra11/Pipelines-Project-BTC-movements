import json
import requests
from datetime import datetime
#https://www.bitstamp.net/api/

res = requests.get('https://www.bitstamp.net/api/ticker_hour/')
dev=res.json()
print(dev)