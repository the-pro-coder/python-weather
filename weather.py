from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def getCurrentWeather(city="Durango"):
    if (len(city.strip(" ")) == 0):
        city = "Durango"
    else:
        city = city.strip()
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"
    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n***Get Current Weather Conditions***\n')
    city = input("\nPlease enter a city: ")
    weather_data = getCurrentWeather(city)

    print("\n")
    pprint(weather_data)