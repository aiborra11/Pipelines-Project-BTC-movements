import pandas as pd  

def read_data(df):
    data = pd.read_csv(df, engine = 'python', delimiter=";", decimal=",")
    return data
