
import pandas as pd
import yfinance as yf

def get_stock_data(tickers_input, start_input, end_input):
    data = yf.download(tickers=tickers_input, start=start_input, end=end_input)
    return data

