import requests
import logging

# Setup logging
logging.basicConfig(filename='weather.log', level=logging.INFO, format='%(asctime)s - %(message)s')

API_KEY = "d67b4ebd23543b7778bfba68dec85411"  # Replace with your OpenWeatherMap API Key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data['cod'] != 200:
            raise Exception(data.get("message", "Failed to retrieve data"))

        weather = {
            'City': data['name'],
            'Temperature': data['main']['temp'],
            'Humidity': data['main']['humidity'],
            'Wind Speed': data['wind']['speed'],
            'Condition': data['weather'][0]['description']
        }

        logging.info(f"Weather fetched for {city}: {weather}")
        return weather
    except Exception as e:
        logging.error(f"Error fetching weather for {city}: {e}")
        return None

def display_weather(info):
    if info:
        print("\nWeather Report:")
        for key, value in info.items():
            print(f"{key}: {value}")
    else:
        print("Could not retrieve weather information.")

def main():
    while True:
        city = input("Enter a city name (or 'exit' to quit): ")
        if city.lower() == 'exit':
            break
        weather_info = get_weather(city)
        display_weather(weather_info)

if __name__ == "__main__":
    main()