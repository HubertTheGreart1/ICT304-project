import numpy as np
import yfinance as yf
from keras.models import load_model # type: ignore
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime, timedelta
import pandas as pd
import os

# Load model once (make sure path is correct relative to your manage.py)
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'bhp_stock_lstm_model.keras')
model = load_model(MODEL_PATH)

def fetch_stock_data(symbol: str, look_back_days: int = 60) -> pd.DataFrame:
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=look_back_days * 2)).strftime('%Y-%m-%d')

    df = yf.download(symbol, start=start_date, end=end_date)

    if df.empty:
        raise ValueError("No data found for symbol: " + symbol)

    return df.tail(look_back_days)

def predict_stock_price(symbol: str, months: int) -> tuple[list[float], list[str]]:
    df = fetch_stock_data(symbol)
    close_prices = df[['Close']].values

    # Normalize the data
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(close_prices)

    # Start with last 60 days
    input_seq = scaled[-60:].reshape(1, 60, 1)

    predictions_scaled = []
    days_to_predict = months * 30

    for _ in range(days_to_predict):
        pred = model.predict(input_seq)[0][0]
        predictions_scaled.append(pred)

        # Add new pred and remove oldest
        input_seq = np.append(input_seq[:, 1:, :], [[[pred]]], axis=1)

    # Reverse scaling
    predictions = scaler.inverse_transform(np.array(predictions_scaled).reshape(-1, 1)).flatten().tolist()

    # Generate future date labels
    last_date = df.index[-1]
    future_dates = [(last_date + timedelta(days=i+1)).strftime('%Y-%m-%d') for i in range(days_to_predict)]

    return predictions, future_dates
