import requests

City = "Cherkasy"
API_KEY = "cc1c0f6f6e4208dab599c4b403d7cdb1"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={City}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

print (data)
