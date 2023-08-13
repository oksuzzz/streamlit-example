import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.exprees as px
st.title("ilk cloud streamlit projem")

btc=yf.download("BTC-USD","2008-01-01","2023-08-13")

st.table(btc)
