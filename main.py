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

# Parameters for API request
params = {
    "q": city,
    "limit": 1,
    "appid": api_key
}

# Send GET request
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

    else:
        print("Unable to fetch location information.")
        print("Status code:",response.status_code)