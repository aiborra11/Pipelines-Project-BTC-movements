import pandas as pd
import numpy as np
from datainfo import *
from api import *

def SplitTime (df):  
    return [i.split() for i in df['Timestamp']] 
    
def TimeDate (df, col1, col2):
    date=[]
    time=[]
    for t in SplitTime(df):
        date.append(t[0])
        time.append(t[1])
    df[col1]=date
    df[col2]=time
    return df

def colsDropper(df, col):
    return df.drop([col], axis = 1, inplace = True)

def Replace(df):
    a = df.replace('—', 0, inplace=True)
    return a

def FixShit(col):
    data[col] = data[col].astype(float)
    return  data[col]

def resta(df, Open, Close, Diff):
    df[Diff] = df[Open]-df[Close]
    return df

def position(df, Diff, Position):
    
    lst=[]  
    for pos in df[Diff]:
        if pos > 0:
            lst.append('long')
        elif pos == 0:
            lst.append('no mov')
        else:
            lst.append('short')
    df[Position]=lst
    return df

def absolute(df, Diff, Open, Close):
    df[Diff] = abs(df[Open]-df[Close])
    return df

def movesize(df, Close, Open):
    df['MoveSize (%)']= round(((df[Open]-df[Close])/df[Open])*100, 2)
    return df

#API stuff
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
    
    return date, time, Open, High, Low, Close, VolumeBTC, Weighted_Price

