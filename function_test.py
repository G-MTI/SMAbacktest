
import pandas as pd
import yfinance as yf

tickers_input = "AAPL"
period_input = "1mo"



def get_stock_data(tickers_input, period_input):
    data = yf.download(tickers=tickers_input, period=period_input)
    pd.set_option('display.max_rows', None)
    print("Dati scaricati:", len(data))
    return data


r = get_stock_data(tickers_input, period_input)
print(r)