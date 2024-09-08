from dotenv import load_dotenv
load_dotenv()
# load_dotenv(override=True) # use this when the .env is updated but not loading

import requests
import os
from pprint import pprint

def get_current_weather(city="Benin City"):

    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("OPEN_WEATHER_API_KEY")}&q={city}&units=imperial'

    weather_data = requests.get(request_url).json()

    # print("API_KEY", os.getenv("OPEN_WEATHER_API_KEY"))

    return weather_data


if __name__ == "__main__":
    print("\n*** Get Current Weather Conditions ***\n")

    city = input("\nPlease enter a city name: ")

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)
