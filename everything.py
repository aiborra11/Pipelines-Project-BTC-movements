from acquisition import *
from dataclean import *
from analysis import *
from api import *

def read_file(df):
    print('Reading file...')
    data_csv = read_data(df)
    return data_csv

def cleaning(df):
    print('Cleaning data...')
    read_file = replace (df, "Open")
    read_file = replace (df, "Low")
    read_file = replace (df, "High")
    read_file = replace (df, "Volume (BTC)")
    read_file = replace (df, "Volume (Currency)")
    read_file = replace (df, "Weighted Price")
    read_file = replace (df, "Close")
    read_file = fixstuff (df, "Open")
    read_file = fixstuff (df, "Low")
    read_file = fixstuff (df, "High")
    read_file = fixstuff (df, "Volume (BTC)")
    read_file = fixstuff (df, "Volume (Currency)")
    read_file = fixstuff (df, "Weighted Price")
    read_file = fixstuff (df, "Close")
    read_file = splittime (df)
    read_file = timedate (df, 'Date', '5min')
    return read_file

def analysis(df):
    print('Analyzing data...')
    value = resta(df, 'Open', 'Close', 'Diff')
    value = position(df, 'Diff', 'Position')
    value = absolute(df, 'Diff', 'Open', 'Close')
    value = movesize(df, 'Close', 'Open')
    value = ordering(df)
    return value

def api(df):
    btc_status = timeconverter (dev)
    btc_status = getbtc (df)
    return btc_status

#a = read_file('BTCPrice.csv')
#b = cleaning(a)
#c = analysis(b)
#d= api(c)
#print(c.head())