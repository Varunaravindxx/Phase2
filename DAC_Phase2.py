import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv('Dataset.csv')

# Convert the 'date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Sort the data by date
data = data.sort_values(by='Date')

# Calculate total sales per customer
data['Total_Sales'] = data['S-P1'] + data['S-P2'] + data['S-P3'] + data['S-P4']

# Calculate the average order value (AOV) per customer
data['AOV'] = data['Total_Sales'] / (data['Q-P1'] + data['Q-P2'] + data['Q-P3'] + data['Q-P4'])

# You can plot and analyze customer behavior here
# For example, you can plot the AOV trend over time
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['AOV'], label='Average Order Value (AOV)')
plt.xlabel('Date')
plt.ylabel('AOV')
plt.title('Average Order Value (AOV) Trend Over Time')
plt.legend()
plt.show()
