import pandas as pd
import ta.volatility
import binance.client
from binance.client import Client
import Donchain_Channels as d

"""1 : you must to install library ta ==> pip install ta"""
"""2 : you must to install library pandas ==> pip install pandas"""
"""3 : ajouter pkey and skey"""

Pkey = 'VWC1L5rekzdGOHdlonOwoRUQQHzrvZ6cG1BP2Tg679B5mYae4kcSsG2iUEL6gkHO'
Skey = 'pZ6v3r4IsyliUXu2qrW2gAOh6Ko8VUpowy6cA9IW42gwRsyUcqkqpDcbg33CiSl3'

client = Client(api_key=Pkey, api_secret=Skey)
columns = ['Date','Open','High','Low','Close' ,'Volume','IGNORE','Quote_Volume','Trades_Count','BUY_VOL','BUY_VOL_VAL','x']
#interval = "15m"
depth = "30 day ago UTC+1"
ema_used = [50, 100]
data = client.get_historical_klines("MATICUSDT", "1h", depth)
df = pd.DataFrame(data)
df.columns = columns
df['Date'] =  pd.to_datetime(df['Date'],unit='ms')
df = df.set_index('Date')
df["Close"] = pd.to_numeric(df["Close"])
df["Open"] = pd.to_numeric(df["Open"])
df["High"] = pd.to_numeric(df["High"])
df["Low"] = pd.to_numeric(df["Low"])
df["Volume"] = pd.to_numeric(df["Volume"])

print(df)
exit()
DIMinus = df['adx1'] = ta.trend.ADXIndicator(df["High"], df["Low"], df["Close"], window = 14, fillna= False).adx_neg()
DIPlus = df['adx2'] = ta.trend.ADXIndicator(df["High"], df["Low"], df["Close"], window = 14, fillna= False).adx_pos()

"""DXdc = abs(DIPlus-DIMinus) / (DIPlus+DIMinus)*100
smad = ta.trend.sma_indicator(DXdc, window=14, fillna=True)"""

for index, row in df.iterrows():
    DXdc = abs(df['adx1']-df['adx2']) / (df['adx1']+df['adx2'])*100
    df['adx'] = ta.trend.sma_indicator(DXdc, window=14, fillna=True)




for index, row in df.iterrows():
    adxM = df['adx1'][index]
    adxP = df['adx2'][index]
    adxMI = df['adx'][index]
    upper = d.df['upper'][index]
    lower = d.df['lower'][index]
    middelt = d.df['middelt'][index]
    print(f" {adxP} {adxM} {adxMI} {upper} {lower} {middelt}")

    
        



