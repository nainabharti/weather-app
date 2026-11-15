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


# Function 3: Select temperature unit
def get_temperature_unit():

    while True:
        print("\nSelect Temperature Unit:")
        print("1. Celsius (°C)")
        print("2. Fahrenheit (°F)")
        print("3. Kelvin (K)")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            return "metric"
        elif choice == "2":
            return "imperial"
        elif choice == "3":
            return "standard"
        else:
            print("Invalid choice! Please select 1, 2, or 3.")


# Function 4: Fetch latitude and longitude
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


# Function 5: Fetch current weather information
def get_weather(latitude, longitude, api_key, unit):

    weather_url = "https://api.openweathermap.org/data/2.5/weather"

    weather_params = {
        "lat": latitude,
        "lon": longitude,
        "appid": api_key,
        "units": unit
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


# Function 6: Get weather condition icon
def get_weather_icon(weather_id):

    if 200 <= weather_id <= 232:
        return "⛈️"

    elif 300 <= weather_id <= 321:
        return "🌦️"

    elif 500 <= weather_id <= 531:
        return "🌧️"

    elif 600 <= weather_id <= 622:
        return "❄️"

    elif 701 <= weather_id <= 781:
        return "🌫️"

    elif weather_id == 800:
        return "☀️"

    elif weather_id == 801:
        return "🌤️"

    elif weather_id == 802:
        return "⛅"

    elif 803 <= weather_id <= 804:
        return "☁️"

    else:
        return "🌍"


# Function 7: Display weather report
def display_weather(city_name, weather_data, unit):

    temperature = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    humidity = weather_data["main"]["humidity"]
    description = weather_data["weather"][0]["description"]
    wind_speed = weather_data["wind"]["speed"]

    weather_id = weather_data["weather"][0]["id"]
    icon = get_weather_icon(weather_id)

    # Select temperature symbol
    if unit == "metric":
        symbol = "°C"
    elif unit == "imperial":
        symbol = "°F"
    else:
        symbol = "K"

    print("\n===== WEATHER REPORT =====")
    print(f"City: {city_name}")
    print(f"Temperature: {temperature}{symbol}")
    print(f"Feels Like: {feels_like}{symbol}")
    print(f"Humidity: {humidity}%")
    print(f"Weather: {icon} {description}")
    print(f"Wind Speed: {wind_speed} m/s")


# Function 8: Main function
def main():

    print("===== WEATHER APP =====")

    # Get API key
    api_key = get_api_key()

    if api_key is None:
        return

    # Select temperature unit
    unit = get_temperature_unit()

    # Multiple city search
    while True:

        # Get city name
        city = get_city()

        if city is None:
            continue

        print(f"\nFetching weather information for {city}...")

        # Get geographical coordinates
        location = get_coordinates(city, api_key)

        if location is None:
            continue

        latitude, longitude, city_name = location

        print("\nLocation found successfully!")

        # Fetch weather data
        weather_data = get_weather(
            latitude, longitude, api_key, unit
        )

        if weather_data is None:
            continue

        # Display weather information
        display_weather(city_name, weather_data, unit)

        # Ask user for another search
        while True:

            choice = input(
                "\nDo you want to search another city? (yes/no): "
            ).strip().lower()

            if choice == "yes":
                break

            elif choice == "no":
                print("\nThank you for using Weather App!")
                return

            else:
                print("Invalid choice! Please enter yes or no.")


# Program execution starts here
if __name__ == "__main__":
    main()