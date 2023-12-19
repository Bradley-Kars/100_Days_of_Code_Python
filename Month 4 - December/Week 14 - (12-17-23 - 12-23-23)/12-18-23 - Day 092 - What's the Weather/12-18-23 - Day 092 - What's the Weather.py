import requests
import json
from prettytable import PrettyTable

timezone = "EST"
latitude = 28.266291
longitude = -81.594971

result = requests.get(
    f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")

weather_data = result.json()

table = PrettyTable()
table.field_names = ["Date", "Weather Description", "Max Temperature (°F)"]

for day, weather_code, temp_max in zip(weather_data['daily']['time'], weather_data['daily']['weathercode'],
                                       weather_data['daily']['temperature_2m_max']):
    temp_max_fahrenheit = (temp_max * 9/5) + 32

    weather_description = {
        1: "Clear sky",
        2: "Partly cloudy",
        3: "Cloudy",
        51: "Drizzle",
        80: "Thunderstorm"
    }

    description = weather_description.get(weather_code, "Unknown")

    table.add_row([day, description, f"{temp_max_fahrenheit:.1f}"])

print("\n5-Day Weather Forecast:")
print("------------------------")
print(table)
