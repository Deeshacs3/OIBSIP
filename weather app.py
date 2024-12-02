import requests

def get_weather_data(location, api_key):
    # OpenWeatherMap API endpoint
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    
    # Sending a GET request to the API
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        data = response.json()  # Parse the JSON data
        
        # Check if the city is valid (e.g., if the city was found)
        if data['cod'] != 200:
            print("Error: City not found. Please try again with a valid city or ZIP code.")
            return
        
        # Extracting weather data
        city = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_conditions = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        pressure = data['main']['pressure']
        
        # Display the weather details
        print(f"\nWeather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_conditions.capitalize()}")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Pressure: {pressure} hPa")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: Could not retrieve data. {e}")
        return

def main():
    # Get the API key (replacing with your actual API key)
    api_key = "a24367eb3552440e672043cbc6038e22"
    
    # Ask the user for a city name or ZIP code
    location = input("Enter the city name or ZIP code: ")
    
    # Get and display the weather data
    get_weather_data(location, api_key)

if __name__ == "__main__":
    main()
