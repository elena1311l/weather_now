import requests

API_KEY = "cc1c0f6f6e4208dab599c4b403d7cdb1".strip()
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data (what_city):
    params = {
        'q': what_city,
        'appid': API_KEY,
        'units': 'metric'
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as r:
        print (f"Помилка {r}")
        return None 
