#insert classes

#1. Insertar una clase que limpie la tabla eliminando las columnas que no necesitamos 
# + comprobar que la info de ese tiempo no esta y añada solo los nuevos.

import json
import requests
import datainfo
import numpy as np

def resta(df, open,close, diff):
    df[diff] = df[open]-df[close]
    return df

print(resta(data_clean, 'open','close', 'diff'))