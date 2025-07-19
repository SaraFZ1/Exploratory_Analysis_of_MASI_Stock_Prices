""""
MASI Stock Data Analysis and Visualization

This script loads MASI stock data from Excel, performs basic exploration,
and visualizes trends in stock prices using matplotlib.
"""

##########################
#Import Required packages
#########################

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import numpy as np

###########################
# Load Data
###########################

df = pd.read_excel('MASI_2007.xlsx', index_col=0, parse_dates=True)
df

###########################
# Basic Data Exploration
###########################

# First and last few rows
print(df.head())
print(df.tail())


# Index range
print("start date", df.index[0])
print("end date", df.index[-1])

# Column names
print("Columns:", df.columns.tolist())

#Show the size of a DataFrame using "Shape"
print(df.shape)

#Show summary statistics of a DataFrame
df.describe()

############################
#Data Selection
############################

### Locate a particular row of data using "Selection by label"

#select all price data for 2007-01-02.
df_2007 = df.loc['2007-01-02']
df_2007

#select just the Close price for 2007-01-02.
df_07 = df.loc['2007-01-02', 'Close']
df_07

#select Close prices for Jannuary.
df_2007 = df.loc['2007-01-02' : '2007-01-31', 'Close']
df_2007

### Locate a particular row of data using "Selection by position"

# print the opening price of the first row
print(df.iloc[0, 0])

# print the opening price of the last row
print(df.iloc[-1, 0])

#################################
# Visualization
################################

# General Close price plot
plt.figure(figsize=(10, 8))
df['Close'].plot(color='red', grid=True, title='MASI Stock Price', label='Close')
plt.legend()
plt.show()

# January 2007 - All OHLC prices
plt.figure(figsize=(10, 8))
df.loc['2007-01-02' : '2007-01-31', 'Close'].plot(color='red', title='MASI Stock Price', label='Close')
df.loc['2007-01-02' : '2007-01-31', 'Open'].plot(color='blue', label='Open')
df.loc['2007-01-02' : '2007-01-31', 'High'].plot(color='green', label='High')
df.loc['2007-01-02' : '2007-01-31', 'Low'].plot(color='yellow', label='Low')
plt.legend()
plt.show()"
