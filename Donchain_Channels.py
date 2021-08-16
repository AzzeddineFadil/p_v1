import pandas as pd
import ta.volatility
import binance.client
from binance.client import Client


"""1 : you must to install library ta ==> pip install ta"""
"""2 : you must to install library pandas ==> pip install pandas"""
"""3 : ajouter pkey and skey"""

Pkey = ''
Skey = ''

client = Client(api_key=Pkey, api_secret=Skey)
columns = ['Date','Open','High','Low','Close' ,'Volume','IGNORE','Quote_Volume','Trades_Count','BUY_VOL','BUY_VOL_VAL','x']
#interval = "15m"
depth = "30 day ago UTC+1"
ema_used = [50, 100]
data = client.get_historical_klines("CTXCUSDT", "15m", depth)
df = pd.DataFrame(data)
df.columns = columns
df['Date'] =  pd.to_datetime(df['Date'],unit='ms')
df = df.set_index('Date')
df["Close"] = pd.to_numeric(df["Close"])
df["Open"] = pd.to_numeric(df["Open"])
df["High"] = pd.to_numeric(df["High"])
df["Low"] = pd.to_numeric(df["Low"])
df["Volume"] = pd.to_numeric(df["Volume"])

df['upper'] = ta.volatility.donchian_channel_hband(df["High"],df["Low"],df["Close"],window=20, offset=0, fillna=False)
df['lower'] = ta.volatility.donchian_channel_mband(df["High"],df["Low"],df["Close"],window=20, offset=0, fillna=False)
df['middelt'] = ta.volatility.donchian_channel_lband(df["High"],df["Low"],df["Close"],window=20, offset=0, fillna=False)


print(round(df['upper'],4))
print(round(df['lower'],4))
print(round(df['middelt'],4))