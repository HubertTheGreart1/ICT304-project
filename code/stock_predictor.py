import argparse
import numpy as np
import yfinance as yf
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime

# Load the pre-trained LSTM model
model = load_model('bhp_stock_lstm_model.keras')

# Function to preprocess the stock data
def preprocess_data(input_data, look_back=60):
    # Extract 'Close' prices from the data
    df = input_data[['Close']]
    
    # Normalize data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(df)
    
    # Create input sequences for the LSTM
    X_input = []
    X_input.append(scaled_data[-look_back:])  # Use the last 'look_back' prices
    X_input = np.array(X_input)
    
    return X_input, scaler

# Function to make predictions
def make_prediction(stock_symbol, prediction_date):
    # Get today's date for the end date
    today = datetime.today().strftime('%Y-%m-%d')
    
    # Download stock data using yfinance with dynamic end date
    stock_data = yf.download(stock_symbol, start="2015-01-01", end=today)
    
    # Convert prediction date string to datetime
    prediction_date = datetime.strptime(prediction_date, '%Y-%m-%d')
    
    # Find the closest available date (if the exact date is not present)
    if prediction_date not in stock_data.index:
        available_dates = stock_data.index
        closest_date = min(available_dates, key=lambda x: abs(x - prediction_date))
        print(f"Exact date {prediction_date.strftime('%Y-%m-%d')} is not available. Using closest available date: {closest_date.strftime('%Y-%m-%d')}")
        prediction_date = closest_date
    
    # Preprocess the data up until the given date
    stock_data_up_to_date = stock_data.loc[:prediction_date]
    
    # Preprocess the data
    X_input, scaler = preprocess_data(stock_data_up_to_date)
    
    # Make the prediction
    predicted_price_scaled = model.predict(X_input)
    
    # Convert the prediction back to original scale
    predicted_price = scaler.inverse_transform(predicted_price_scaled)
    
    return predicted_price[0][0]

# Command-line interface to input the stock symbol and prediction date
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Stock Price Prediction using LSTM")
    parser.add_argument('--symbol', type=str, help='Stock symbol (e.g., BHP)', required=True)
    parser.add_argument('--date', type=str, help='Date for prediction (format: YYYY-MM-DD)', required=True)
    args = parser.parse_args()
    
    # Get prediction for the given stock symbol and date
    predicted_price = make_prediction(args.symbol, args.date)
    
    if predicted_price:
        # Output the predicted stock price
        print(f"Predicted Stock Price for {args.symbol} on {args.date}: {predicted_price}")
