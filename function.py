
import pandas as pd
import yfinance as yf

#start_date=start_input-200
#end_date=end_input

def get_stock_data(ticker_input, start_sma, end_input):
    data = yf.download(tickers=ticker_input, start=start_sma, end=end_input)
    data.columns = data.columns.get_level_values(0)
    return data

def sma_calculate(data, slow_input, fast_input):
    sma_data = data.copy() #evito di modificare direttamente i dati originali
    sma_data['smaSlow'] = sma_data['Close'].rolling(window=slow_input).mean() #creo una nuova colonna
    sma_data['smaFast'] = sma_data['Close'].rolling(window=fast_input).mean()
    return sma_data 

def signal(sma_data, start_input, fast_input):

    data_signal = sma_data.copy().loc[start_input:] #loc "filtra" i dati, in questo caso parte dalla data start_input
    data_signal['signal'] = (data_signal['smaFast'] > data_signal['smaSlow']).astype(int).diff() #calocolo la differenza con .diff() tra il signal di un giorno e quelo del giorno precedente così capisco quando ci sono i crossover
                # se facessi senza .diff() avrei solo un valore = e ! perche .astype(int) mi converte i valori booleani in interi
                #calcolo giornalmente l'aumento percentuale del prezzo di chiusura ['Close'] rispetto al giorno precedente: .pct_change() = Fractional change between the current and a prior element. //documentazione su https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pct_change.html
                # moltiplico per il signal shiftato di 1 giorno perche l'operazione avviene il giorno dopo il segnale 1 o -1, (i segnali avvengono alla chiusura del mercato)
    data_signal['entry'] = 0
    data_signal['exit'] = 0
    data_signal['position'] = 0  # 0 = no position, 1 = long position, -1 = short position
    return data_signal

def cross_over(data_signal):
    data_fn = data_signal[data_signal.index != 'Ticker']
    for i in range(1, len(data_fn)):
        if data_fn['signal'].iloc[i] == 1:
             # Long entry
            data_fn.loc[data_fn.index[i], 'position'] = 1
            data_fn.at[data_fn.index[i], 'entry'] = data_fn['Close'].iloc[i].astype(float)
            print(f"Long entry at {data_fn.index[i]} price {data_fn['Close'].iloc[i]}")

    return data_fn
