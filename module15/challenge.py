#In the end of the class each student should get these tasks done:

#1.Temperature Overview:
#a.Find the average temperature
#for the entire dataset and format it to 2 decimal points.

#2.Monthly Temperature:
#a.Calculate the average
#temperature for each month.

#b.Visualize the monthly average
#temperature using a bar plot.

#3. Highs and Lows:
#a.Identify the hottest and coldest
#days based on temperature and display
#the entire row with that data.

#4.Temperature Trends:
#a.Create a simple line graph showing how temperature
#changes over time.

#b.Seasonal Average Temperature:

#Define seasons based on months and determine
#the average temperature
#for each season(e.g.winter, fall, spring, summer).

#Visualize the seasonal average
#temperature using a line plot.

#weather_tokyo_data = df.groupby('Tokyo')
#plt.figure(figsize = (10,10))
#plt.plot(weather_tokyo_data['day'], weather_tokyo_data['temperature'])
#plt.plot(weather_tokyo_data['year'])
#.plot(weather_tokyo_data.atmospheric_pressure)
#plt.plot(weather_tokyo_data.humidity)
#plt.title('Average Weather in Tokyo')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('weather_tokyo_data.csv')

