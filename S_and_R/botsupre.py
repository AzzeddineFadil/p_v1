# Step 1: Start with loading the needed modules
import fix_yahoo_finance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
from binance_client import client
import mplfinance as mpf


class getinfo : 



    def get_SR(ticker,interval):
        columns = ['Date','Open','High','Low','Close' ,'Volume','IGNORE','Quote_Volume','Trades_Count','BUY_VOL','BUY_VOL_VAL','x']
        #interval = "15m"
        depth = "30 day ago UTC+1"
        ema_used = [50, 100]
        data = client.get_historical_klines(ticker, interval, depth)
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
        # Step 4: Adding trend resistance & support lines
        pivot_high_1=df['High'][-21:-1].max()
        pivot_high_2=df['High'][-55:-22].max()
        pivot_low_1=df['Low'][-21:-1].min()
        pivot_low_2=df['Low'][-55:-22].min()

        A=[df['High'][-21:-1].idxmax(), pivot_high_1]
        B=[df['High'][-55:-22].idxmax(), pivot_high_2]

        A1=[df['Low'][-21:-1].idxmin(), pivot_low_1]
        B1=[df['Low'][-55:-22].idxmin(), pivot_low_2]

        x1_high_values = [A[0], B[0]]
        y1_high_values = [A[1], B[1]]

        x1_low_values = [A1[0], B1[0]]
        y1_low_values = [A1[1], B1[1]]



        # Step 3: Visualisation with Matplotlib
        plt.rcParams.update({'font.size': 10})
        fig, ax1 = plt.subplots(figsize=(14,7))

        ax1.set_ylabel('Price in €')
        ax1.set_xlabel('Date')
        ax1.set_title(ticker)
        ax1.plot('Close',data=df, label='Close Price', linewidth=0.5, color='blue')

        ax1.plot(x1_high_values, y1_high_values, color='r', linestyle='--', linewidth=0.5, label='Trend resistance')
        ax1.plot(x1_low_values, y1_low_values, color='g', linestyle='--', linewidth=0.5, label='Trend support')

        ax1.axhline(y=pivot_high_1, color='r', linewidth=6, label='First resistance line', alpha=0.2)
        ax1.axhline(y=pivot_low_1, color='g', linewidth=6, label='First support line', alpha=0.2)
        point1 ="res : "+ str(pivot_high_1)
        point2 ="sup : "+ str(pivot_low_1)
        trans = transforms.blended_transform_factory(ax1.get_yticklabels()[0].get_transform(), ax1.transData)
        ax1.text(0,pivot_high_1, "{:.2f}".format(pivot_high_1), color="r", transform=trans,ha="right", va="center")
        ax1.text(0,pivot_low_1, "{:.2f}".format(pivot_low_1), color="g", transform=trans,ha="right", va="center")
        
        
        return point1,point2
        """ax1.legend()
        ax1.grid()
        plt.show()
        mpf.plot(df, figratio=(10, 6), type="candle", 
                mav=(21), volume=True,
                title = f"Price of {ticker}",
                tight_layout=True, style="binance")
"""


 