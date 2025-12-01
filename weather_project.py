print("Welcome to Australia Weather Project ")

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("weather.csv")
data.head()

print("\nHere is the weather data:")
print(data.head())

cities = data['city'].tolist()
print("\nAvailable cities:", ",".join(cities))

city_name = input("\nEnter a city to see the weather: ")


# Filter the data
city_data = data[data['city'].str.lower() == city_name.lower()]


if not city_data.empty:
    temp = city_data.iloc[0]['temperature']
    rain = city_data.iloc[0]['rainfall']
    print(f"\nWeather in {city_name}: Temperature = {temp}°C, Rainfall = {rain}mm")
else:
    print("\nCity not found. Please check spelling or choose from the available cities.")

plt.figure(8.5)
plt.bar(data['city'], data['temperature'], color = "darkgreen")
plt.title("Weather in the Australian Cities")
plt.xlabel("city")
plt.ylabel('temperature')
plt.show()
