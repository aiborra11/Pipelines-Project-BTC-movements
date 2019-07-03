from dataclean import *

def resta(df, Open, Close, Diff):
    df['Diff'] = df[Open] - df[Close]
    return df

"""
*idea: El mercado es mas manipulable cuando el BTC vale menos vs. es menos manipulable porque el inversor tiene mas BTC acumulados por tema wykoff. 
Medir mechas tras movimientos fuertes. Detectar long/short close - high/low.
"""

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
    df['MoveSize (%)']= abs(round(((df[Open]-df[Close])/df[Open])*100, 2))
    return df

def ordering(df):
    big_sizes = df.sort_values(['MoveSize (%)', 'Date', '5min'], ascending = False)
    return big_sizes
