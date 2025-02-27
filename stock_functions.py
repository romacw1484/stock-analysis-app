import pandas as pd
import yfinance as yf
from datetime import date
from dateutil.relativedelta import relativedelta
import plotly.graph_objects as go

def Download_StockData(ticker, start_date, end_date):
    """
    Downloads historical stock data from Yahoo Finance.
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    
    return data



def Visualize_StockData(data, symbol, start_date, end_date, color_list=None):
    import plotly.graph_objects as go
    fig = go.Figure()

    if not isinstance(data, list):
        data = [data]
        symbol = [symbol]

    default_colors = ['lime', 'orange', 'blue', 'red', 'purple']
    if color_list is None:
        color_list = default_colors[:len(data)]

    for stock_data, stock_symbol, color in zip(data, symbol, color_list):
        if stock_data.empty:
            print(f"No data found for {stock_symbol}. Cannot plot.")
            continue

        if isinstance(stock_data.columns, pd.MultiIndex):
            try:
                stock_data = stock_data.xs(stock_symbol, axis=1, level='Ticker')
            except KeyError:
                print(f"No data found for ticker {stock_symbol}.")
                continue

        if 'Close' not in stock_data.columns:
            print(f"'Close' column not found for {stock_symbol}. Cannot plot.")
            continue

        stock_data = stock_data.reset_index()
        stock_data['Date'] = pd.to_datetime(stock_data['Date'])
        stock_data = stock_data.dropna(subset=['Close'])

        fig.add_trace(
            go.Scatter(
                x=stock_data['Date'],
                y=stock_data['Close'],
                line=dict(color=color, width=3),
                name=f'{stock_symbol} Close Price'
            )
        )

    fig.update_layout(
        title=f'{" vs ".join(symbol)} Stock Prices from {start_date} to {end_date}',
        title_font=dict(size=22, color='white', family='Optima, sans-serif', weight='bold'),
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        plot_bgcolor='#000000',
        paper_bgcolor='#000000',
        font=dict(color='white'),
        xaxis=dict(showgrid=True, gridcolor='lightgray', zeroline=False),
        yaxis=dict(showgrid=True, gridcolor='lightgray', zeroline=False),
        margin=dict(l=60, r=40, t=80, b=50),
        title_x=0.5
    )

    return fig.to_html(full_html=False, include_plotlyjs='cdn')

def compare_stock_prices(symbol1, symbol2, start_date, end_date):
    """
    Compares two stocks by plotting their closing prices on the same graph.
    Returns an HTML string of the Plotly figure.
    """
    data1 = Download_StockData(symbol1, start_date, end_date)
    data2 = Download_StockData(symbol2, start_date, end_date)

    # If either data set is empty, return None or a suitable message
    if data1.empty or data2.empty:
        return None

    # Assign distinct colors to each stock
    color_list = ['blue', 'orange']

    # Pass both DataFrames to Visualize_StockData
    chart_html = Visualize_StockData(
        [data1, data2], 
        [symbol1, symbol2], 
        start_date, 
        end_date, 
        color_list
    )
    return chart_html


if __name__ == '__main__':
    # Test the function with a sample ticker, e.g., 'AAPL'
    ticker = 'AAPL'
    data = Download_StockData(ticker)
    print(data.head())
