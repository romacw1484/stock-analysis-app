from flask import Flask, render_template, request, flash
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

# Import your stock functions from stock_functions.py
from stock_functions import (
    Download_StockData, 
    Visualize_StockData,
    compare_stock_prices
)

app = Flask(__name__)
app.secret_key = "SOME_SECRET_KEY"

@app.route("/", methods=["GET", "POST"])
def index():
    chart_html = None
    comparison_html = None
    strategy_html = None
    active_tab = "chart"  # Default tab

    if request.method == "POST":
        form_type = request.form.get("form_type")

        # ----- TAB A: Show Price Chart -----
        if form_type == "chart":
            active_tab = "chart"
            symbol = request.form.get("symbol", "").strip().upper()
            start_date = request.form.get("start_date")
            end_date = request.form.get("end_date")

            stock_data = Download_StockData(symbol, start_date, end_date)
            if stock_data.empty:
                flash(f"No data found for {symbol}. Please try again.")
            else:
                chart_html = Visualize_StockData(stock_data, symbol, start_date, end_date)

        # ----- TAB B: Compare Stocks -----
        elif form_type == "compare":
            active_tab = "compare"
            symbol1 = request.form.get("symbol1", "").strip().upper()
            symbol2 = request.form.get("symbol2", "").strip().upper()
            start_date = request.form.get("start_date")
            end_date = request.form.get("end_date")

            comparison_html = compare_stock_prices(symbol1, symbol2, start_date, end_date)
            if comparison_html is None:
                flash("One or both stock data sets are empty. Please try again.")

        # ----- TAB C: Strategies (placeholder) -----
        elif form_type == "strategy":
            active_tab = "strategy"
            symbol = request.form.get("symbol", "").strip().upper()
            flash("Trading strategies functionality not yet implemented.")
            # strategy_html = ... call your strategy function here

        # Additional elif blocks for D, E, F as needed

    return render_template(
        "index.html",
        chart_html=chart_html,
        comparison_html=comparison_html,
        strategy_html=strategy_html,
        active_tab=active_tab
    )

if __name__ == "__main__":
    app.run(debug=True)
