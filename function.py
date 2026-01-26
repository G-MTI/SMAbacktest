
import pandas as pd
import yfinance as yf

#start_date=start_input-200
#end_date=end_input

def get_stock_data(ticker_input, start_sma, end_input):
    data = yf.download(tickers=ticker_input, start=start_sma, end=end_input)
    return data

def sma_calculate(data, slow_input, fast_input):
    data=data.copy()

