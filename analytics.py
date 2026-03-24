def get_info (data):
    if not data:
        return "Any information for analisis"
    city = data.get('name')
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    description = data['weather'][0]['description']

    report = (
        f"Weather in {city}: {description}. "
        f"The temperature is {temp}°C, the humidity is {humidity}%, "
        f"and the wind speed is {wind_speed} m/s."
    )
    return report 

'''
    return {
        "city":city,
        "temp": temp,
        "humidity": humidity,
        "wind": wind_speed
    }
'''
