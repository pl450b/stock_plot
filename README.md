# Stock Portfolio Analysis

This script fetches historical stock data from Yahoo Finance and generates visualizations for stock performance over the past three months. It reads stock ticker symbols and their quantities from a CSV file, then calculates and plots:

- Percentage increase in stock price over the last three months.
- Total dollar change for each stock in the portfolio.

## Installation & Setup

### 1. Create a Virtual Environment

#### Windows (Command Prompt):
```sh
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux (Terminal):
```sh
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
After activating the virtual environment, install the required dependencies using:
```sh
pip install -r requirements.txt
```

## How the CSV File Works

The script reads stock ticker symbols and their quantities from a CSV file. The expected format is:

```csv
Stock Ticker Symbol,Quantity
AAPL,10
MSFT,5
GOOGL,8
```

- **Stock Ticker Symbol**: The stock’s symbol (e.g., AAPL for Apple, MSFT for Microsoft).
- **Quantity**: The number of shares owned.

Ensure the CSV file follows this format for correct processing.

## Usage

1. Replace `'example.csv'` in `main()` with the path to your actual CSV file.
2. Run the script:
```sh
python main.py
```
3. The script will fetch stock data and generate relevant plots.

## Notes
- The script uses Yahoo Finance (`yfinance`) to fetch stock prices.
- Make sure your CSV file is correctly formatted and contains valid stock symbols.
- The script only retrieves data for the past three months.


