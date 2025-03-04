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
    stock_data = yf.download(ticker, start=start_date, end=end_date, auto_adjust=False)
    if stock_data.empty:
        print(f"Warning: No data found for {ticker}")
        return None
    return stock_data['Adj Close']


def plot_stock_percent_increase(stocks):
    """Plots the percentage increase of stocks over the past three months."""
    end_date = datetime.today() - timedelta(days=1)  # Ensure market day
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

def plot_stock_total_change(stocks):
    """Plots the total dollar change for each stock in the portfolio."""
    end_date = datetime.today() - timedelta(days=1)  # Ensure market day
    start_date = end_date - timedelta(days=90)  # Approximately three months

    stock_changes = {}

    for ticker, quantity in stocks:
        prices = fetch_stock_data(ticker, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
        if prices is not None:
            initial_price = prices.iloc[0]
            final_price = prices.iloc[-1]
            total_change = float(quantity * (final_price - initial_price))  # Ensure it's a scalar
            stock_changes[ticker] = total_change
        else:
            print(f"No data found for {ticker}")

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.bar(stock_changes.keys(), stock_changes.values(), color=['green' if v >= 0 else 'red' for v in stock_changes.values()])
    plt.xlabel("Stock Ticker")
    plt.ylabel("Total $ Change")
    plt.title("Total Change in Dollar Value for Each Stock")
    plt.axhline(0, color='black', linewidth=0.8)  # Horizontal line at $0
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Annotate each bar with the value
    for i, (ticker, change) in enumerate(stock_changes.items()):
        plt.text(i, change, f"${change:.2f}", ha='center', va='bottom' if change >= 0 else 'top', fontsize=10)

    plt.show()



def main():
    # Replace 'example.csv' with the path to your CSV file
    csv_file_path = 'example.csv'
    stocks = read_csv(csv_file_path)
    # plot_stock_percent_increase(stocks)
    plot_stock_total_change(stocks)

    
if __name__ == "__main__":
    main()
