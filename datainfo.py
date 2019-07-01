#datainfo = https://bitcoincharts.com/charts/bitstampUSD#rg10zig5-minzczsg2019-06-17zeg2019-06-29ztgSzm1g10zm2g25zi1gRSIzv
#No tiene el exchange que busco, pero es lo unico que he encontrado que me facilite la info en min5.
import requests as req
import pandas as pd
import json
import requests
from datetime import datetime

data = pd.read_csv ('BTCPrice.csv', engine = 'python', delimiter=";", decimal=",")
print(data.shape)