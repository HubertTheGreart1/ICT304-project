#!/bin/bash

# Check if Python 3 is installed
if ! command -v python3 &>/dev/null; then
    echo "Python 3 is not installed. Please install Python 3 and try again."
    exit 1
fi

# Create a virtual environment named "stock_predictor_env"
python3 -m venv stock_predictor_env

# Activate the virtual environment
source stock_predictor_env/bin/activate

# Upgrade pip to the latest version
pip install --upgrade pip

# Install the dependencies from requirements.txt
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found! Please make sure you have created it."
    exit 1
fi

echo "Setup complete! The virtual environment 'stock_predictor_env' has been created and all dependencies have been installed."
