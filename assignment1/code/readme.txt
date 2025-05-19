# TradeX Intelligent Forecasting System

![Python](https://img.shields.io/badge/Python-3.7--3.11-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%2010%2B-lightgrey)
![Status](https://img.shields.io/badge/Status-Working-success)
![License](https://img.shields.io/badge/License-MIT-green)

The **TradeX Intelligent Forecasting System** is a smart, automated stock price prediction tool that uses deep learning (LSTM) to forecast future stock prices across global markets.

---

## Files Included

| File                             | Description                                      |
|----------------------------------|--------------------------------------------------|
| `bhp_stock_lstm_model.keras`     | Pre-trained LSTM model for stock price prediction |
| `readme`                         | Basic notes or documentation                     |
| `requirements.txt`               | Required Python libraries                        |
| `run_stock_predictor.bat`        | Main batch file to launch the system             |
| `stock_prediction_final.ipynb`   | Jupyter Notebook used to train the model         |
| `stock_predictor.py`             | Core Python script that handles prediction logic |

---

## Prerequisites

To run the system via `run_stock_predictor.bat`, ensure the following:

- **Windows 10 or later (64-bit)**
- **Python 3.7 to 3.11** (must be installed and added to your system PATH)
- **Visual C++ Redistributable for Visual Studio 2015–2022 (x64)**  
  Required for TensorFlow to work correctly on Windows.

---

## How to Use

1. **Download** and unzip `ict304_assign1_final.zip` to any directory.
2. **Double-click** `run_stock_predictor.bat`.

### You’ll be prompted to:

- Enter a stock symbol (e.g., `AAPL`)
- Enter a prediction date (format: `YYYY-MM-DD`)

> Note: This process might take several minutes on first run because:
> - It creates and activates a Python virtual environment
> - Automatically installs all required packages
> - Executes the prediction script

---

### Example Prompt

```bash
Enter Stock Symbol (e.g., AAPL): AAPL
Enter Prediction Date (YYYY-MM-DD): 2024-01-15
