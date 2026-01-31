
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from function import get_stock_data, sma_calculate, signal, cross_over, returns_calculate, cumulative_returns, average_return

st.title("SMA Backtest Application")

ticker_input = st.text_input("Enter a title:", "AAPL")
start_input = st.date_input("Start Date:", pd.to_datetime("2019-01-01"))
start_sma = start_input - pd.Timedelta(300, unit='d') #il massimo per la media lunga è 200 giorni dato che 200 giorni reali non sono 200 di borsa quindi ne scarico 300 per avere margine 

end_input = st.date_input("End date:", pd.to_datetime("2024-01-01"))

slow_input = st.number_input("Slow SMA(max 200:", min_value=1, max_value=200, value=60)
fast_input = st.number_input("Fast SMA(max 200):", min_value=1, max_value=200, value=20)

data = get_stock_data(ticker_input, start_sma, end_input)
print("dawnloaded data ", len(data))
print(data)

if st.button("Run backtest"):
    sma_data = sma_calculate(data, slow_input, fast_input)
    pd.set_option('display.max_rows', None)
    print(sma_data)

    data_signal = signal(sma_data, start_input)
    print(data_signal)


    data_fn, prices = cross_over(data_signal)
    print(data_fn)
    print("Prices:", prices)

    returns = returns_calculate(prices)
    print("returns:", returns)

    average = average_return(returns)


    cum_fn = cumulative_returns(returns)
    print(cum_fn)


    #Grafico con Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=sma_data.index, y=sma_data['Close'], name='Close price'))
    fig.add_trace(go.Scatter(x=sma_data.index, y=sma_data['smaFast'], name=f'SMA {fast_input}'))
    fig.add_trace(go.Scatter(x=sma_data.index, y=sma_data['smaSlow'], name=f'SMA {slow_input}'))

    buy_signals = data_fn[data_fn['signal'] == 1]
    sell_signals = data_fn[data_fn['signal'] == -1]
    fig.add_trace(go.Scatter(x=buy_signals.index, y=buy_signals['Close'],
                             mode='markers', marker=dict(color='green', size=10),
                             name='Buy'))
    fig.add_trace(go.Scatter(x=sell_signals.index, y=sell_signals['Close'],
                             mode='markers', marker=dict(color='red', size=10),
                             name='Sell'))

    st.plotly_chart(fig)

    st.subheader(f"SMA Backtest Results for {ticker_input}")
    st.write('Total trade:', len(returns))
    st.write('Cumulative returns:', cum_fn,"%")
    st.write('Average return per trade:', average,"%")
    