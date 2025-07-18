# app/main.py

import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY is not set.")
        return

    city = "Paris"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

    print(f"Performing request to Weather API for city {city}...")
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        location = data["location"]
        current = data["current"]

        print(f"{location['name']}/{location['country']} {location['localtime']} "
              f"Weather: {current['temp_c']} Celsius, {current['condition']['text']}")
    except requests.RequestException as e:
        print("Request failed:", e)
    except KeyError:
        print("Unexpected response format.")


if __name__ == "__main__":
    get_weather()
