import os
import requests
from dotenv import load_dotenv


# Function 1: Load and verify API key
def get_api_key():
    load_dotenv()

    api_key = os.getenv("OPENWEATHER_API_KEY")

    if api_key:
        print("API key loaded successfully!")
        return api_key
    else:
        print("API key not found. Please check your .env file.")
        return None


# Function 2: Take and validate city name
def get_city():
    city = input("Enter city name: ").strip()

    if not city:
        print("Please enter a city name.")
        return None

    return city


# Function 3: Fetch latitude and longitude
def get_coordinates(city, api_key):

    geo_url = "https://api.openweathermap.org/geo/1.0/direct"

    params = {
        "q": city,
        "limit": 1,
        "appid": api_key
    }

    try:
        response = requests.get(geo_url, params=params, timeout=10)

    except requests.exceptions.RequestException:
        print("Network error! Please check your internet connection.")
        return None

    if response.status_code == 200:

        location_data = response.json()

        if location_data:
            latitude = location_data[0]["lat"]
            longitude = location_data[0]["lon"]
            city_name = location_data[0]["name"]

            return latitude, longitude, city_name

        else:
            print("City not found. Please enter a valid city name.")
            return None

    else:
        print("Unable to fetch location information.")
        print("Status code:", response.status_code)

        if response.status_code == 401:
            print("Invalid or inactive API key.")
        elif response.status_code == 429:
            print("API request limit exceeded.")
        elif response.status_code >= 500:
            print("OpenWeather server error.")
        else:
            print("Please check your request and try again.")

        return None


# Function 4: Fetch current weather information
def get_weather(latitude, longitude, api_key):

    weather_url = "https://api.openweathermap.org/data/2.5/weather"

    weather_params = {
        "lat": latitude,
        "lon": longitude,
        "appid": api_key,
        "units": "metric"
    }

    try:
        weather_response = requests.get(
            weather_url,
            params=weather_params,
            timeout=10
        )

    except requests.exceptions.RequestException:
        print("Network error! Please check your internet connection.")
        return None

    if weather_response.status_code == 200:
        return weather_response.json()

    else:
        print("Unable to fetch weather information.")
        print("Status code:", weather_response.status_code)

        if weather_response.status_code == 401:
            print("Invalid or inactive API key.")
        elif weather_response.status_code == 429:
            print("API request limit exceeded.")
        elif weather_response.status_code >= 500:
            print("OpenWeather server error.")
        else:
            print("Please check your request and try again.")

        return None


# Function 5: Display weather report
def display_weather(city_name, weather_data):

    temperature = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    humidity = weather_data["main"]["humidity"]
    description = weather_data["weather"][0]["description"]
    wind_speed = weather_data["wind"]["speed"]

    print("\n===== WEATHER REPORT =====")
    print(f"City: {city_name}")
    print(f"Temperature: {temperature}°C")
    print(f"Feels Like: {feels_like}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather: {description}")
    print(f"Wind Speed: {wind_speed} m/s")


# Function 6: Main function
def main():

    print("===== WEATHER APP =====")

    # Get API key
    api_key = get_api_key()

    if api_key is None:
        return

    # Get city name
    city = get_city()

    if city is None:
        return

    print(f"\nFetching weather information for {city}...")

    # Get geographical coordinates
    location = get_coordinates(city, api_key)

    if location is None:
        return

    latitude, longitude, city_name = location

    print("\nLocation found successfully!")

    # Fetch weather data
    weather_data = get_weather(latitude, longitude, api_key)

    if weather_data is None:
        return

    # Display weather information
    display_weather(city_name, weather_data)


# Program execution starts here
if __name__ == "__main__":
    main()