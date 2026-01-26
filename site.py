import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from function import get_stock_data

st.title("SMA Backtest Application")

ticker_input = st.text_input("Inserisci il ticker:", "AAPL")
start_input = st.date_input("Data di inizio:", pd.to_datetime("2020-01-01"))
start_sma = start_input - pd.Timedelta(300, unit='d') #il massimo per la media lunga è 200 giorni dato che 200 giorni reali non sono 200 di borsa quindi ne scarico 300 per avere margine 

end_input = st.date_input("Data di fine:", pd.to_datetime("2021-01-01"))

data = get_stock_data(ticker_input, start_sma, end_input)
print("Dati scaricati:", len(data))
print(data)