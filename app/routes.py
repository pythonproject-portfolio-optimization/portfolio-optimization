from app import app
from flask import render_template, request, redirect, url_for
from app.forms import TickerForm
from portfolio_optimization_func_clone import optimize_portfolio


@app.route("/", methods=["GET","POST"])
@app.route("/index", methods=["GET","POST"])
def index():
    ticker_form = TickerForm()
    return render_template("index.html", title="Homepage", form = ticker_form)

@app.route("/ticker", methods=["GET","POST"])
def ticker():
    ticker_list = []
    ticker1 = request.form.get("ticker1")
    ticker2 = request.form.get("ticker2")
    ticker3 = request.form.get("ticker3")
    ticker4 = request.form.get("ticker4")
    ticker_list.append(ticker1)
    ticker_list.append(ticker2)
    ticker_list.append(ticker3)
    ticker_list.append(ticker4)

    portfolio_returns = optimize_portfolio(ticker_list)

    return render_template("ticker.html", title= "Portfolio Weights", portfolio_returns = portfolio_returns, ticker_list = ticker_list)

 