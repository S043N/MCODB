-- Този проект отваря приложение за да виждаш времето какво ще е --
-- Преди да стартирате кода, ще трябва да се регистрирате за безплатен API ключ в OpenWeatherMap и да замените "YOUR_API_KEY" с действителния си API ключ. Този код ще ви даде текущото описание на температурата, налягането, влажността и времето за града, който въвеждате.--
-- Python -- 

import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city_name}"
    response = requests.get(complete_url)
    return response.json()

def main():
    api_key = 'YOUR_API_KEY'  # Replace with your own API key
    city_name = input("Enter city name: ")
    weather_data = get_weather(city_name, api_key)
    
    if weather_data['cod'] != '404':
        main_info = weather_data['main']
        current_temperature = main_info['temp']
        current_pressure = main_info['pressure']
        current_humidity = main_info['humidity']
        weather_description = weather_data['weather'][0]['description']
        
        print(f"Weather in {city_name}:")
        print(f"Temperature: {current_temperature - 273.15:.2f}°C")
        print(f"Atmospheric Pressure: {current_pressure} hPa")
        print(f"Humidity: {current_humidity}%")
        print(f"Description: {weather_description.capitalize()}")
    else:
        print("City not found. Please check the name and try again.")

if __name__ == "__main__":
    main()
