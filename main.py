import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve API key
api_key = os.getenv("OPENWEATHER_API_KEY")

print("===== WEATHER APP =====")

# Check API key
if api_key:
    print("API key loaded successfully!")
else:
    print("API key not found. Please check your .env file.")
    exit()

# Take city name from user
city = input("Enter city name: ").strip()

# Display entered city
print(f"\nFetching weather information for {city}...")

# Geocoding API endpoint
geo_url = "https://api.openweathermap.org/geo/1.0/direct"

# Parameters for Geocoding API
params = {
    "q": city,
    "limit": 1,
    "appid": api_key
}

# Send GET request to Geocoding API
response = requests.get(geo_url, params=params)

# Check response status
if response.status_code == 200:

    # Convert JSON response into Python data
    location_data = response.json()

    if location_data:
        latitude = location_data[0]["lat"]
        longitude = location_data[0]["lon"]

        print("\nLocation found successfully!")
        print(f"City: {location_data[0]['name']}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")

        # Current Weather API endpoint
        weather_url = "https://api.openweathermap.org/data/2.5/weather"

        # Parameters for Current Weather API 
        weather_params = {
            "lat": latitude,
            "lon": longitude,
            "appid": api_key,
            "units": "metric"
        }

        # Send GET request to Current Weather API 
        weather_response = requests.get(weather_url, params=weather_params)

        # Check Current Weather API response
        if weather_response.status_code == 200:
            weather_data = weather_response.json()

            # Extract weather details
            temperature = weather_data["main"]["temp"]
            feels_like = weather_data["main"]["feels_like"]
            humidity = weather_data["main"]["humidity"]
            description = weather_data["weather"][0]["description"]
            wind_speed = weather_data["wind"]["speed"]

            # Display weather report
            print("\n===== WEATHER REPORT =====")
            print(f"City: {location_data[0]['name']}")
            print(f"Temperature: {temperature}°C")
            print(f"Feels like: {feels_like}°C")
            print(f"Humidity: {humidity}%")
            print(f"Weather: {description}")
            print(f"Wind Speed: {wind_speed}m/s")

        else:
            print("\nUnable to fetch weather information.")
            print("Status code:",weather_response.status_code)

    else:
        print("City not found. Please enter a valid city name.")

else:
    print("Unable to fetch location information.")
    print("Status code:",response.status_code)