# Willy's WallStreet Stock Analysis App
<img width="1470" alt="Screenshot 2025-02-27 at 6 37 27 PM" src="https://github.com/user-attachments/assets/0b0ab775-f939-43d8-bcbc-f5d169c393b9" />
Willy's WallStreet is a web-based stock analysis application that helps users visualize stock data, compare stocks, and evaluate trading strategies—all from a single, intuitive interface.

## Features

- **Price Chart**  
  View an interactive Plotly chart of a stock's closing prices over a user-selected date range using an intuitive slider.

- **Stock Comparison**  
  Compare the closing prices of two stocks on the same graph. Each stock is plotted in a distinct color, with an interactive date range selector.

- **Trading Strategies**  
  Evaluate different trading strategies for a stock, including:
  - **Moving Average Crossover Strategy**  
    Configurable short and long moving averages to signal potential entry and exit points.
  - **Mean Reversion (Bollinger Bands) Strategy**  
    Uses Bollinger Bands to identify overbought or oversold conditions.
  - **RSI-Based Strategy**  
    Applies the Relative Strength Index (RSI) to help determine potential reversal points.

- **Planned/Placeholder Features**  
  Future enhancements include:

## Built With

- **Python 3.x**
- **Flask** – Web framework for the server-side application.
- **Pandas** – Data manipulation and analysis.
- **yfinance** – Downloading historical market data from Yahoo Finance.
- **Plotly** – Creating interactive charts.
- **Ion.RangeSlider** – Interactive date range sliders integrated into the front-end.

## Directory Structure (so far) 
stock-analysis-app/
├── app.py
├── stock_functions.py
├── templates/
│   └── index.html
└── static/
    ├── index.css        (optional)
    └── date_slider.js


