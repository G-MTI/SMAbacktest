
import pandas as pd
import yfinance as yf


def get_stock_data(ticker_input, start_sma, end_input):
    data = yf.download(tickers=ticker_input, start=start_sma, end=end_input)
    print("Dati scaricati:", len(data))
    return data


