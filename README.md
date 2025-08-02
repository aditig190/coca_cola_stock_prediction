# 📈 Coca-Cola Stock Price Predictor

This Streamlit app uses a trained Random Forest model to predict the next closing price of Coca-Cola (KO) stock using live data from Yahoo Finance.

## 🚀 Features

- Real-time data fetching via `yfinance`
- Feature engineering (SMA, lag, returns)
- Interactive controls (date selector, SMA toggles)
- Easy deployment on Streamlit Cloud

## 🧠 Model

- Random Forest Regressor trained on data from 2015–2025
- Features used: `Close_Lag1`, `SMA_20`, `SMA_50`, `Daily_Return`

## 📦 Installation

Clone the repo and run:

```bash
pip install -r requirements.txt
streamlit run app.py
