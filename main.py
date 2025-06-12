import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import pytz
import matplotlib.pyplot as plt
import time
import os  # Added for potential file operations, like saving CSV


def get_dividends_last_6_months(ticker_symbol):
    """
    Fetch dividends for the given ticker symbol from the last 6 months.
    """
    try:
        ticker = yf.Ticker(ticker_symbol)
        dividends = ticker.dividends

        if dividends.empty:
            print(f"No dividend history found for {ticker_symbol}.")
            return pd.Series(dtype='float64')

        # Ensure the dividends index has a timezone for accurate comparison
        if dividends.index.tz is None:
            # If the index is naive, assume UTC (common for yfinance
            # historical data)
            dividends.index = dividends.index.tz_localize('UTC')

        # Convert current time to the timezone of the dividends index for
        # a proper comparison
        tzinfo = dividends.index.tz
        now_in_tz = datetime.now(pytz.utc).astimezone(tzinfo)

        # Calculate 6 months ago (approx. 182 days) from the current time
        # in the relevant timezone
        six_months_ago = pd.Timestamp(now_in_tz - timedelta(days=182))

        # Filter dividends + only those on or after the calculated date
        recent_dividends = dividends[dividends.index >= six_months_ago]

        return recent_dividends

    except Exception as e:
        print(f"Error fetching dividends for {ticker_symbol}: {e}")
        return pd.Series(dtype='float64')


def analyze_dividends(dividends):
    """
    Calculate summary statistics and quarterly sums of the dividends.
    """
    if dividends.empty:
        return {}

    mean_div = dividends.mean()
    median_div = dividends.median()
    total_div = dividends.sum()

    df = dividends.reset_index()
    df.columns = ['Date', 'Dividends']
    df['Quarter'] = df['Date'].dt.to_period('Q')
    quarterly_sum = df.groupby('Quarter')['Dividends'].sum()

    return {
        'mean': mean_div,
        'median': median_div,
        'total': total_div,
        'quarterly_sum': quarterly_sum
    }


def plot_quarterly_dividends(quarterly_sum, ticker_symbol):
    """
    Create a bar chart to visualize quarterly dividend sums.
    """
    if quarterly_sum.empty:
        print(f"No quarterly data to plot for {ticker_symbol}.")
        return

    plt.figure(figsize=(10, 6))  # Added for consistent figure sizing
    quarterly_sum.plot(
        kind='bar',
        title=(f'Quarterly Dividends for {ticker_symbol} '
               '(Last 6 Months)'),
        color='skyblue'
    )   # Title adjusted for consistency
    plt.xlabel('Quarter')
    plt.ylabel('Dividend Sum ($)')  # Added '$' for clarity
    plt.xticks(rotation=45)  # Rotate labels for better readability
    plt.tight_layout()  # Adjust layout to prevent labels from overlapping
    plt.show()


def compare_top_stocks(top_stocks):
    """
    Compare total dividends of top dividend-paying stocks / last 6 months.
    """
    results = []
    print("\nFetching data for comparison stocks...")

    for symbol in top_stocks:
        time.sleep(2)  # Added a small delay to avoid hitting API rate limits
        try:
            dividends = get_dividends_last_6_months(symbol)
            if dividends.empty:
                print(f"No recent dividends for {symbol}. Skipping.")
                continue

            stats = analyze_dividends(dividends)
            if not stats:  # Check if analysis yielded any stats
                print(f"No analysis data for {symbol}. Skipping.")
                continue

            ticker = yf.Ticker(symbol)
            # Use parentheses to break long line
            company_name = ticker.info.get("longName", symbol)

            results.append({
                "Ticker": symbol,
                "Company": company_name,
                "Total Dividend": round(stats["total"], 4),
                "Average Dividend": round(stats["mean"], 4)
            })

        except Exception as e:
            print(f"Skipping {symbol} due to error: {e}")
            continue

    df = pd.DataFrame(results)
    if df.empty:
        print("No comparison data could be generated.")
        return

    df_sorted = df.sort_values(by="Total Dividend", ascending=False)

    # Export comparison data to CSV file as per README feature
    output_filename = "dividend_comparison.csv"
    try:
        df_sorted.to_csv(
            output_filename,
            index=False
        )  # index=False prevents writing DataFrame index
        print(f"\nComparison data exported to {output_filename}")
    except Exception as e:
        print(f"Error exporting comparison data to CSV: {e}")

    print("\nTop 10 Dividend Stocks (Last 6 Months):")
    print(df_sorted.to_string(index=False))

    plt.figure(figsize=(12, 7))  # Added for consistent figure sizing
    df_sorted.set_index("Ticker")["Total Dividend"].plot(
        kind="bar",
        title=("Top Dividend Stocks - Total Payout (Last 6 Months)"),
        color='lightcoral'
    )   # Title adjusted for consistency
    plt.xlabel("Ticker Symbol")  # Added x-label for clarity
    plt.ylabel("Total Dividend ($)")
    plt.tight_layout()
    plt.show()


def main():
    """
    Main function to run the dividend analysis project.
    Prompts for a ticker, analyzes its dividends, and offers comparison.
    """
    print("Welcome to the Dividend Data Analyzer!")
    symbol = input("Enter ticker symbol (e.g. AAPL): ").upper()
    print(f"\nAnalyzing: {symbol}")

    dividends = get_dividends_last_6_months(symbol)

    if dividends.empty:
        print(f"No dividends found for {symbol} in the last 6 months. Exiting.")
        return

    print(f"\nDividends for {symbol} in the last 6 months:")
    print(dividends)

    stats = analyze_dividends(dividends)
    if not stats:  # Check if analysis yielded any stats
        print(f"Could not analyze dividends for {symbol}. Exiting.")
        return

    print(f"\nTotal dividend sum: {stats['total']:.4f}")
    print(f"Average dividend: {stats['mean']:.4f}")
    print(f"Median dividend: {stats['median']:.4f}")
    print("\nQuarterly dividend sums:")
    # Used .to_string() for better console output
    print(stats['quarterly_sum'].to_string())

    plot_quarterly_dividends(stats['quarterly_sum'], symbol)

    compare_choice = input("\nCompare with top dividend stocks? (y/n): ").lower()
    if compare_choice == "y":
        # This list of top dividend stocks is used for the comparison feature
        top_dividend_stocks = [
            "AAPL", "MSFT", "KO", "PG", "JNJ", "XOM",
            "PFE", "CVX", "VZ", "PEP"
        ]
        compare_top_stocks(top_dividend_stocks)

    print("\nAnalysis complete.")


if __name__ == "__main__":
    main()





