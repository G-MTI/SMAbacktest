
import pandas as pd
import yfinance as yf

#start_date=start_input-200
#end_date=end_input

def get_stock_data(tickers_input, start_date, end_date):
    data = yf.download(tickers=tickers_input, start=start_date, end=end_date)
    return data

def sma_calculate(data, slow_input, fast_input):
    data=data.copy()

