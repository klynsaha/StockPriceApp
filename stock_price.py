import yfinance as yf
import streamlit as st
from datetime import date, datetime, time

companies = {'Walmart': 'WMT', 'Amazon': 'AMZN', 'Facebook': 'FB', 'Google': 'GOOGL', 'Apple': 'AAPL', 'Tesla': 'TSLA'}
name = st.sidebar.selectbox('Stock Name', [x for x in companies.keys()])
start_date = st.sidebar.date_input('Start Date', value=date(year=2010,month=5, day=31), max_value=date.today())
end_date = st.sidebar.date_input('End Date', value=date.today(), max_value=date.today())

st.write("""
# Stock Price App
Shown are the stock ***closing price*** and ***volume***
""" + name + "!")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = companies[name]
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
@st.cache
def getData(period, start, end):
    Df = tickerData.history(period=period, start=start, end=end)
    return Df

tickerDf = getData('1d', start_date, end_date)
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)