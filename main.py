import csv
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def read_csv(file_path):
    """Reads a CSV file and returns a list of stock ticker symbols and their quantities."""
    stocks = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            ticker = row['Stock Ticker Symbol']
            quantity = float(row['Quantity'])
            stocks.append((ticker, quantity))
    return stocks

def fetch_stock_data(ticker, start_date, end_date):
    """Fetches historical stock data from Yahoo Finance."""
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data['Adj Close'] if 'Adj Close' in stock_data else None

def plot_stock_percent_increase(stocks):
    """Plots the percentage increase of stocks over the past three months."""
    end_date = datetime.today()
    start_date = end_date - timedelta(days=90)  # Approximately three months

    plt.figure(figsize=(10, 6))

    for ticker, quantity in stocks:
        prices = fetch_stock_data(ticker, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
        if prices is not None:
            percent_increase = ((prices - prices.iloc[0]) / prices.iloc[0]) * 100
            plt.plot(prices.index, percent_increase, label=f"{ticker}")
        else:
            print(f"No data found for {ticker}")

    plt.title("Stock Percentage Increase Over the Last Three Months")
    plt.xlabel("Date")
    plt.ylabel("Percentage Increase (%)")
    plt.legend()
    plt.grid()
    plt.show()

def main():
    # Replace 'example.csv' with the path to your CSV file
    csv_file_path = 'example.csv'
    stocks = read_csv(csv_file_path)
    plot_stock_percent_increase(stocks)

if __name__ == "__main__":
    main()
