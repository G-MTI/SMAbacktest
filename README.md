# SMA Backtest Website

**SMA Backtest Website** is a web application designed to help users test simple moving average (SMA) trading strategies directly in the browser.
The goal of the project is to make financial backtesting accessible and intuitive, even for those without professional trading tools, by providing an interactive interface, customizable parameters, and clear visual results.

**Features**
- **Dynamic inputs:** Users can choose a stock ticker (e.g., AAPL), a date range, and set periods for two moving averages (fast and slow).
- **Real market data:** The app automatically fetches historical price data using the `yfinance` API.
- **Automated backtest:** The script calculates buy/sell signals when the two SMAs cross and computes the cumulative performance of the strategy.
* **Interactive charts:** Results are displayed using Plotly with dynamic price charts that show both SMAs and colored buy/sell markers.
- **Responsive interface:** The Streamlit-based UI updates results instantly, allowing users to experiment with different strategies and parameters in seconds.

**Tech Stack**
The project is built entirely in **Python**, using:
- **Streamlit** – for the web interface
- **Pandas** and **NumPy** – for data manipulation and statistical calculations
- **Yfinance** – for downloading historical market data
- **Plotly** – for creating interactive charts

---

This project taught me a lot about:
- Handling and analyzing financial data with **Pandas**
- Building web apps entirely in Python using **Streamlit**
- Working with market data APIs and asynchronous data fetching
- Creating **interactive time series visualizations** with **Plotly**
- Managing project environments (`venv`, `.gitignore`, `requirements.txt`)
