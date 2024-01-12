import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            print(f"Weather in {location}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Weather Conditions: {data['weather'][0]['description']}")
        else:
            print(f"Error: {data['message']}")

    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    api_key = "475425450dffb26c1377685812fe4b52"
    location = input("Enter a city or ZIP code: ")

    get_weather(api_key, location)
