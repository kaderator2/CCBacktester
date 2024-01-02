# FOREX Correlation Coefficient Backtester

## Overview
The Correlation Coefficient Backtester is a simple Python-based application designed to help backtest a simple Correlation Coefficient technical strategy given previous market data. It provides insights into currency pair movements and their correlation. This tool primarily focuses on two major currency pairs: EUR/USD (Euro/US Dollar) and GBP/USD (British Pound/US Dollar), offering a graphical representation of their normalized values and the correlation coefficient over time.

## Key Features
1. **Data Parsing and Visualization**: The tool continuously parses updated data from specified text files (`EURUSD.csv` and `GBPUSD.csv`) and visually represents this data in real-time.
2. **Graphical Representation of Currency Pairs**: The application plots normalized values of the two major currency pairs, EUR/USD and GBP/USD, allowing users to compare their movements on a unified scale.
3. **Correlation Coefficient Calculation**: It calculates and displays the rolling correlation coefficient between these pairs, giving users insight into how closely the two currencies are related in their movements.
4. **Animation**: Utilizing Matplotlib's animation functionality, the tool updates its graphs in real-time, reflecting historical data. This feature allows a user to Backtest a given strategy as if it were in real-time.
5. **Data Validation and Synchronization**: The code includes logic to ensure data validity, checking for timestamp mismatches and ensuring synchronized datasets between the two currency pairs.

## Technical Description
- **Language and Libraries**: The project is developed in Python, leveraging libraries such as NumPy for numerical operations and Matplotlib for plotting and animating graphs.
- **Data Handling**: It employs efficient data handling techniques, reading and processing CSV files for historical data, and appending new data points from updated text files.
- **Animation and Interaction**: Matplotlib's animation module is utilized to refresh and update the plots dynamically at a set interval, providing an interactive experience.

This tool provides a valuable resource for anyone involved in the Forex market, combining real-time data processing with interactive graphical representations for enhanced market analysis.

## This is quite a old project of mine and was made back in 2019 while I was in highschool.
