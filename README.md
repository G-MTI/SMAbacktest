# SMA Backtest Website

SMA Backtest Website is a web application designed to help users test simple moving average (SMA) trading strategies directly in the browser. The goal of the project is to make financial backtesting accessible and intuitive, even for those without professional trading tools, by providing an interactive interface, customizable parameters, and clear visual results.

**Whow it works:**
Users can choose a stock ticker (AAPL, etc.), a date range, and set periods for two moving averages (fast and slow), the app fetches historical data using the yfinance API, then calculates buy/sell signals when the two SMAs cross and computes the cumulative results. Results are showed with dynamic price charts made with Plotly

**This project taught me a lot about:**
- Streamlit, for the web interface
- Pandas and NumPy, for data manipulation and statistical calculations
- Yfinance, for downloading historical market data
- Plotly, for creating interactive charts
- venv, for creating isolated virtual environments
