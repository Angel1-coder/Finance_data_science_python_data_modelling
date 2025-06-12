<<<<<<< HEAD
No problem! Here's the `README.md` file for your project, presented clearly and concisely.

# Dividend Data Analysis for Last 6 Months

This Python project fetches and analyzes dividend payments for a specified stock ticker symbol over the last 6 months using the `yfinance` library.

## Features

* **Fetch Dividend History:** Retrieve dividend data for any given stock ticker.
* **Filter Data:** Focuses analysis on dividend payments made within the last 6 months.
* **Calculate Key Metrics:** Determine the total, average, and median dividends paid.
* **Quarterly Summary:** Summarize dividend payments by calendar quarters for easy trend analysis.
* **Stock Comparison:** Compare the total dividends of your selected stock against a predefined list of top dividend-paying stocks.
* **Data Visualization:** Generate bar charts to visualize quarterly dividend sums and comparison data.
* **Export Data:** Save comparison data to a CSV file for further analysis.

---

## Getting Started

Follow these steps to get the project up and running on your local machine.

### Prerequisites

Make sure you have:

* **Python 3.7 or higher**
* **`yfinance`**
* **`pandas`**
* **`matplotlib`**
* **`pytz`**

### Installation

1.  **Clone the Repository (or create your project folder):** If you're using Git, clone this repository to your local machine. Otherwise, simply create a new folder for your project.
2.  **Navigate to the Project Directory:** Open your terminal or command prompt and change your directory to the project folder:
    ```bash
    cd your_project_folder
    ```
3.  **Create a Virtual Environment (Recommended):** To keep your project dependencies isolated, create and activate a virtual environment:
    ```bash
    python -m venv .venv
    # On Windows:
    .venv\Scripts\activate
    # On macOS/Linux:
    source .venv/bin/activate
    ```
4.  **Install Required Packages:** With your virtual environment activated, install all necessary libraries using `pip`:
    ```bash
    pip install yfinance pandas matplotlib pytz
    ```

### Running the Project

1.  **Save the Code:** Ensure the Python script (e.g., `main.py`) containing the project's logic is saved in your project directory.
2.  **Execute the Script:** Run the main script from your terminal:
    ```bash
    python main.py
    ```
3.  **Follow Prompts:** The program will prompt you to **enter a ticker symbol** (e.g., `AAPL`). It will then display dividend data and ask if you wish to compare it with a list of top dividend stocks.

---

## Usage

* **Enter a Ticker Symbol:** When prompted, provide a stock ticker symbol.
* **View Analysis:** The terminal will display a dividend summary and a quarterly breakdown for the chosen stock.
* **Initiate Comparison:** To compare with top dividend stocks, enter `y` when asked.
* **Visualize Data:** Bar charts will automatically appear, illustrating dividend distributions.
* **Access Comparison Data:** If you choose to compare, a CSV file named **`dividend_comparison.csv`** will be created in your project folder, containing the comparison data.

### Output

* **Console Output:** Dividend summaries and quarterly breakdowns are printed directly to the terminal.
* **Bar Charts:** Visualizations show dividend sums per quarter for the selected stock and total dividends for the comparison group.
* **CSV File:** `dividend_comparison.csv` provides a structured output of total and average dividends for the compared stocks.

---

## Notes

* **Data Availability:** Dividend data relies on availability from Yahoo Finance. Some stocks may have incomplete or missing historical dividend information.
* **API Errors:** Occasionally, you might encounter API rate limiting or authorization errors (HTTP 401) during comparisons. The script handles these gracefully by skipping the problematic tickers.
* **Timezone Warnings:** You may see timezone warnings during execution due to datetime conversions. These are generally benign and do not impact the accuracy of the analysis.

## Author

Evangelos Anthony Dimitras



=======
# Finance_data_science_python_data_modelling
>>>>>>> 1efb3a22bf8e1f6007f38e4ebe7411f30a0c01cc
