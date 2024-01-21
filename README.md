# VEQT-Stock-Analyzer

A Python script that fetches historical stock data for the ETF symbol 'VEQT.TO' from Yahoo Finance and visualizes it. The script uses the pandas library for data manipulation, numpy for polynomial fitting, and matplotlib for plotting.

How It Works

The script performs the following steps:

    Reads historical stock data from Yahoo Finance using a provided URL.
    Converts the 'Date' column to datetime format for proper time-series handling.
    Creates a linear regression line using polynomial fitting (numpy.polyfit and numpy.poly1d).
    Visualizes the historical stock closing prices along with the linear regression line using matplotlib.

Input Data

The script fetches historical stock data from Yahoo Finance using the following URL:

python

'https://query1.finance.yahoo.com/v7/finance/download/VEQT.TO?period1=1524700800&period2=1682467200&interval=1d&events=history&includeAdjustedClose=true'

Output

The script generates a plot showing historical stock closing prices in black and a linear regression line in blue dashed lines.
Requirements

    Python 3.x
    pandas library
    numpy library
    matplotlib library

Author

Matthew Dodd
