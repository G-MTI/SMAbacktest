
import pandas as pd
import yfinance as yf
import numpy as np

def get_stock_data(ticker_input, start_sma, end_input):
    data = yf.download(tickers=ticker_input, start=start_sma, end=end_input)
    data.columns = data.columns.get_level_values(0)
    return data

def sma_calculate(data, slow_input, fast_input):
    sma_data = data.copy() #evito di modificare direttamente i dati originali
    sma_data['smaSlow'] = sma_data['Close'].rolling(window=slow_input).mean() #creo una nuova colonna
    sma_data['smaFast'] = sma_data['Close'].rolling(window=fast_input).mean()
    return sma_data 

def signal(sma_data, start_input):

    data_signal = sma_data.copy().loc[start_input:] #loc "filtra" i dati, in questo caso parte dalla data start_input
    data_signal['signal'] = (data_signal['smaFast'] > data_signal['smaSlow']).astype(int).diff() #calocolo la differenza con .diff() tra il signal di un giorno e quelo del giorno precedente così capisco quando ci sono i crossover
                # se facessi senza .diff() avrei solo un valore = e ! perche .astype(int) mi converte i valori booleani in interi
                # moltiplico per il signal shiftato di 1 giorno perche l'operazione avviene il giorno dopo il segnale 1 o -1, (i segnali avvengono alla chiusura del mercato)
                # 0 = no position, 1 = long position, -1 = short position
    data_signal['entry'] = 0.0
    data_signal['exit'] = 0.0
    return data_signal

def cross_over(data_signal):
    prices=[]
    data_fn = data_signal.copy()

    for i in range(1, len(data_fn)):
        if data_fn['signal'].iloc[i] == 1:
            price = data_fn['Close'].iloc[i+1] * data_fn['signal'].iloc[i]
            data_fn.at[data_fn.index[i], 'entry'] = price
            prices.append(price)
        elif data_fn['signal'].iloc[i] == -1:
            price = data_fn['Close'].iloc[i+1] * data_fn['signal'].iloc[i]
            data_fn.at[data_fn.index[i], 'exit'] = price
            prices.append(price)
    if prices[-1] > 0:
        prices.pop()
    if prices[0] < 0:
        prices.pop(0)
    return data_fn, prices

def returns_calculate(prices):
    returns = []
    for i in range (0, len(prices)-1):
        if prices[i] > 0:
            returns.append(((prices[i] + prices[i+1]) / -prices[i]))
    return returns 

def average_return(returns):
    average = sum(returns)/len(returns)*100
    return round(average,3)

def cumulative_returns(returns):
    for i in returns:
        cum = np.cumprod(1+i)
        print(cum)
    cum_fn = ((cum[0]-1) * 100)
    return round (cum_fn, 3)
