import pandas as pd
import ta.volatility
import ta.momentum
import binance.client
from binance.client import Client
import talib as taa


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

df['upper'] = ta.volatility.donchian_channel_hband(df["High"],df["Low"],df["Close"],window=50, offset=0, fillna=False)
df['middelt'] = ta.volatility.donchian_channel_mband(df["High"],df["Low"],df["Close"],window=50, offset=0, fillna=False)
df['lower'] = ta.volatility.donchian_channel_lband(df["High"],df["Low"],df["Close"],window=50, offset=0, fillna=False)


for index, row in df.iterrows():
    short = round(taa.EMA(df["Volume"], 5),2)
    long = round(taa.EMA(df["Volume"], 20),2)
    df['osc']= round(100*(short-long)/long,2)
color = []
for index, row in df.iterrows():
    if(df['Close'][index]<df['Open'][index]):
        color.append('r')
    if(df['Close'][index]>=df['Open'][index]):
        color.append('g')
    
df['color'] = color
print(df)
