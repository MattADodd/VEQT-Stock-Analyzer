import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Read historical stock data from Yahoo Finance into a DataFrame
df = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/VEQT.TO?period1=1524700800&period2=1682467200&interval=1d&events=history&includeAdjustedClose=true')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Display the DataFrame with stock data
print(df)

# Create a DataFrame with a date range to cover the desired plotting period
df2 = pd.DataFrame({'Date': pd.date_range(start='2019-02-05', end='2024-04-26', freq="B")})

# Fit a linear regression line to the historical stock closing prices
z = np.polyfit(df.index, df['Close'], 1)
p = np.poly1d(z)

# Plot the linear regression line with a dashed blue line
plt.plot(df2['Date'], p(df2.index), color='b', linestyle='--')

# Set the plot style to 'ggplot'
plt.style.use('ggplot')

# Plot the historical stock closing prices
plt.plot(df['Date'], df['Close'], color='k')

# Set plot title, x-axis label, and y-axis label
plt.title('VEQT Stock Price by Date')
plt.xlabel('Date')
plt.ylabel('Stock Price (CAD)')

# Show the plot
plt.show()
