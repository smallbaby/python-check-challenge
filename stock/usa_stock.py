# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2021/07/04

import yfinance as yf
import plotly.graph_objects as go

symbol = 'TSLA'
interal = '1d'
period = '180d'
prices = yf.Ticker(symbol).history(period=period, interval=interal)

prices['Close'].plot(figsize=(16,10))

# go.Figure(data=[go.Candlestick(x=prices.index,
#                                open=prices['Open'], high=prices['High'],
#                                low=prices['Low'], close=prices['Close'])]).show()

from pandas_datareader import DataReader
import datetime as dt
import pandas as pd
symbol = 'APPL'
start = dt.datetime(2021, 3, 1)
end = pd.Timestamp.today()

#df = DataReader(symbol, 'yahoo', start, end)
#print(df)


