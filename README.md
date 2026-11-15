🌤️ Weather App

A Python-based Weather App that fetches real-time weather information for different cities using the OpenWeather API. It allows users to search for multiple cities, choose temperature units, and view weather conditions with corresponding icons.

✨ Features

- Real-Time Weather: Fetches current weather information for any supported city.
- City Search: Search for multiple cities without restarting the application.
- Geocoding API: Converts city names into geographical coordinates.
- Temperature Units: Choose between Celsius, Fahrenheit, and Kelvin.
- Weather Icons: Displays emojis according to weather conditions.
- Weather Details: Shows temperature, feels-like temperature, humidity, weather description, and wind speed.
- Unit Conversion: Displays wind speed in the appropriate unit (m/s or mph).
- Input Validation: Handles empty city names and invalid user choices.
- Error Handling: Handles network errors, invalid API keys, and API request failures.
- Modular Programming: Organizes the application into separate functions for better readability and maintainability.

🛠️ Technologies Used

- Python – Main programming language
- Requests – To make HTTP requests to the weather API
- Python-dotenv – To manage environment variables
- OpenWeather API – To retrieve geographical and weather information

📁 Project Structure

weather-app/
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md

⚙️ Installation and Setup

1. Clone the repository

git clone https://github.com/nainabharti/weather-app.git

2. Navigate to the project directory

cd weather-app

3. Create a virtual environment

python -m venv .venv

4. Activate the virtual environment

For Windows PowerShell:

.venv\Scripts\Activate.ps1

5. Install dependencies

pip install -r requirements.txt

6. Get your API key

- Visit "OpenWeather" (https://openweathermap.org/api).
- Create an account.
- Generate an API key.

7. Configure environment variables

Create a ".env" file in the project root directory and add:

OPENWEATHER_API_KEY=your_api_key_here

Replace "your_api_key_here" with your actual API key.

Important: Never share your API key or upload your ".env" file to GitHub.

8. Run the application

python main.py

🌡️ Temperature Unit Options

Option| Temperature Unit| API Parameter
1| Celsius (°C)| metric
2| Fahrenheit (°F)| imperial
3| Kelvin (K)| standard

🔌 APIs Used

This project uses two OpenWeather API endpoints:

1. Geocoding API: Converts city names into latitude and longitude.
   
   https://openweathermap.org/api/geocoding-api

2. Current Weather API: Fetches current weather information using geographical coordinates.
   
   https://openweathermap.org/api/current

📚 Concepts Learned

Through this project, I practised:

- Python functions and modular programming
- Working with external APIs
- HTTP requests and JSON responses
- Exception handling
- Environment variables
- Input validation
- Conditional statements and loops
- Working with dictionaries and lists
- Python virtual environments
- Git and GitHub version control

🚀 Future Improvements

- Add a 5-day weather forecast.
- Display atmospheric pressure, visibility, and cloudiness.
- Improve the user interface.
- Add weather history and favourite cities.
- Develop a graphical user interface.

👩‍💻 Author

Naina Bharti

- GitHub: "@nainabharti" (https://github.com/nainabharti)

---

Built with Python as a hands-on project to practise API integration and modular programming.