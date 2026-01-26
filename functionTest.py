
import pandas as pd
import yfinance as yf

tickers_input = "AAPL"


start_input = "2020-01-01"
start_dt = pd.to_datetime(start_input)
start_sma = start_dt - pd.Timedelta(300, unit='d')

end_input = "2021-01-01"


def get_stock_data(tickers_input, start_sma, end_input):
    data = yf.download(tickers=tickers_input, start=start_sma, end=end_input)
    print("Dati scaricati:", len(data))
    return data


r = get_stock_data(tickers_input, start_sma, end_input)
print(r)