import numpy as np 

from acquisition import *

def splittime(df):
    return [i.split() for i in df['Timestamp']] 

def timedate (df, col1, col2):
    date=[]
    time=[]
    for t in splittime(df):
        date.append(t[0])
        time.append(t[1])
    df[col1]=date
    df[col2]=time
    df.drop(['Timestamp'], axis=1, inplace = True)
    return df

def replace(df, col):
    a = df.replace('—', '0', inplace=True)
    return a

def fixstuff(df, col):
    df[col] = df[col].astype(float)
    return df[col]

