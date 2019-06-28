import requests as req
from bs4 import BeautifulSoup
import pandas as pd

#datainfo = https://bitcoincharts.com/charts/bitstampUSD#rg10zig5-minzczsg2019-06-17zeg2019-06-29ztgSzm1g10zm2g25zi1gRSIzv
#No tiene el exchange que busco, pero es lo unico que he encontrado que me facilite la info en min5.
data = pd.read_csv('BTCPrice.csv', engine = 'python', delimiter=";", decimal=",")
print(data.head())
print(data.shape)

data_clean = data[['Open', 'High', 'Low', 'Close', 'Volume (BTC)']]
print(data_clean.head())

