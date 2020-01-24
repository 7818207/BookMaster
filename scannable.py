import pandas as pd

def getSymbols():
    df = pd.read_csv('Data/nasdaq100vol.csv')
    l = df['Symbol'].tolist()[:-1]
    return l