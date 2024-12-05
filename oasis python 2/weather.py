import requests

def get_weather(api_key, location):
    """Fetch weather data from OpenWeatherMap API for the specified location."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            raise ValueError("Invalid API key. Please check your OpenWeatherMap API key.")
        elif response.status_code == 404:
            raise ValueError(f"Location '{location}' not found. Please enter a valid city name.")
        else:
            raise Exception(f"Failed to fetch weather data. HTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"An error occurred while fetching weather data: {e}")

def display_weather(data):
    """Display the weather information."""
    city = data["name"]
    country = data["sys"]["country"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print("\n--- Weather Report ---")
    print(f"Location: {city}, {country}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Conditions: {description.capitalize()}")
    print("----------------------\n")

def main():
    """Main function to run the weather app."""
    print("Welcome to the Command-Line Weather App!")
    api_key = "112a60c3ed44cde29d0684b28b82de1e"  # Replace with your OpenWeatherMap API key

    while True:
        location = input("Enter a city name (or type 'exit' to quit): ").strip()
        if location.lower() == "exit":
            print("Exiting the weather app. Goodbye!")
            break

        # Validate city name
        if not location.replace(" ", "").isalpha():
            print("Invalid input. Please enter a valid city name consisting only of letters and spaces.")
            continue

        try:
            weather_data = get_weather(api_key, location)
            display_weather(weather_data)
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
