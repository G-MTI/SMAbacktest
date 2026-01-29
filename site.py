import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from function import get_stock_data, sma_calculate, signal, cross_over

st.title("SMA Backtest Application")

ticker_input = st.text_input("Inserisci il ticker:", "AAPL")
start_input = st.date_input("Data di inizio:", pd.to_datetime("2020-01-01"))
start_sma = start_input - pd.Timedelta(300, unit='d') #il massimo per la media lunga è 200 giorni dato che 200 giorni reali non sono 200 di borsa quindi ne scarico 300 per avere margine 

end_input = st.date_input("Data di fine:", pd.to_datetime("2021-01-01"))

slow_input = st.number_input("Periodo SMA Lenta:", min_value=1, max_value=200, value=60)
fast_input = st.number_input("Periodo SMA Veloce:", min_value=1, max_value=200, value=20)

data = get_stock_data(ticker_input, start_sma, end_input)
print("Dati scaricati:", len(data))
print(data)

sma_data = sma_calculate(data, slow_input, fast_input)
pd.set_option('display.max_rows', None)
print(sma_data)

data_signal = signal(sma_data, start_input, fast_input)
print(data_signal)

data_fn = cross_over(data_signal)
print(data_fn)

