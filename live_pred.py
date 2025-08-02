import streamlit as st
import pandas as pd
import yfinance as yf
import joblib
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Load trained model
model = joblib.load(r'\coca_cola_rf_model.pkl')

# App title
st.title(" Coca-Cola Stock Price Prediction")
st.subheader("Live Forecasting using Random Forest and yFinance")

# Sidebar for options
st.sidebar.header("🔧 Settings")

# Date range selector
start_date = st.sidebar.date_input("Start Date", datetime(2023, 1, 1))
end_date = st.sidebar.date_input("End Date", datetime.today())

# Check date validity
if start_date >= end_date:
    st.error(" End date must be after start date.")
    st.stop()

# Toggle moving averages
show_sma_20 = st.sidebar.checkbox("Show 20-Day SMA", value=True)
show_sma_50 = st.sidebar.checkbox("Show 50-Day SMA", value=True)

# Fetch stock data
df = yf.download('KO', start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
df.reset_index(inplace=True)

# Feature Engineering
df['Close_Lag1'] = df['Close'].shift(1)
df['Daily_Return'] = df['Close'].pct_change()
df['SMA_20'] = df['Close'].rolling(window=20).mean()
df['SMA_50'] = df['Close'].rolling(window=50).mean()
df.dropna(inplace=True)

# Predict next closing price
latest = df[['Close_Lag1', 'SMA_20', 'SMA_50', 'Daily_Return']].iloc[-1:]
prediction = model.predict(latest)[0]

# Display prediction
st.markdown(f"### Predicted Next Closing Price: **${prediction:.2f}**")

# Show data
st.write("###  Recent Data Sample")
st.dataframe(df.tail())

# Plotting
st.write("### Coca-Cola Stock Price Chart")

plt.figure(figsize=(12, 5))
plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')

if show_sma_20:
    plt.plot(df['Date'], df['SMA_20'], label='20-Day SMA', linestyle='--', color='orange')
if show_sma_50:
    plt.plot(df['Date'], df['SMA_50'], label='50-Day SMA', linestyle='--', color='green')

plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.title("Coca-Cola Stock Price with Optional SMAs")
plt.legend()
plt.grid(True)
st.pyplot(plt)

