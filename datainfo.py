import requests as req
import pandas as pd

#datainfo = https://bitcoincharts.com/charts/bitstampUSD#rg10zig5-minzczsg2019-06-17zeg2019-06-29ztgSzm1g10zm2g25zi1gRSIzv
data = pd.read_csv('BTCPrice.csv', engine = 'python', delimiter=";", decimal=",")
#print(data)
#print(data.shape)

#Separo la fecha de los min5 y elimino la columna de 'Timestamp' y 'Volume Currency'
times = [i.split() for i in data['Timestamp']]

date = []
time = []
for i in times:
    date.append(i[0])
    time.append(i[1])

data_clean = data.drop(['Timestamp'], axis=1)
#data_clean.insert(0, "Date", date, False) 
#data_clean.insert(1, '5min', time, False)


#print(data_clean)
"""
El siguiente paso seria actualizar la info importando nuevos datos
cada 5 minutos desde la API. Consigo vincular la API pero no se como 
montarlo.

La idea seria crear una clase o una funcion que reciba la info de la api
seleccione las columnas que me interesa y anyada las nuevas filas.

"""
#Codigo que he conseguido:
"""
import json
import requests

res = requests.get('https://www.bitstamp.net/api/ticker_hour/')
dev=res.json()
from datetime import datetime, timedelta
a = [*dev.values()]

Lo mismo pero en una funcion:
def getBtc(value):
    res = requests.get('https://www.bitstamp.net/api/ticker_hour/')
    dev = res.json()
    return [*dev.values()]

"""
