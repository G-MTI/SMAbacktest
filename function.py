
import pandas as pd
import yfinance as yf

#start_date=start_input-200
#end_date=end_input

def get_stock_data(ticker_input, start_sma, end_input):
    data = yf.download(tickers=ticker_input, start=start_sma, end=end_input)
    return data

def sma_calculate(data, slow_input, fast_input):
    sma_data = data.copy()
    sma_data['smaSlow'] = sma_data['Close'].rolling(window=slow_input).mean()
    sma_data['smaFast'] = sma_data['Close'].rolling(window=fast_input).mean()
    return sma_data 

def cross_over(sma_data, start_input, fast_input):

    data_signal = sma_data.copy().loc[start_input:]
    data_signal['signal'] = (data_signal['smaFast'] > data_signal['smaSlow']).astype(int).diff()

    return data_signal