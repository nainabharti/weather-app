import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve API key
api_key = os.getenv("OPENWEATHER_API_KEY")

print("===== WEATHER APP =====")

# Take city name from user
city = input("Enter the city name: ")

#Display entered city
print(f"\nFetching weather information for {city}...")