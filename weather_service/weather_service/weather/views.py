from django.http import JsonResponse
import requests


def get_weather(request):
    city = request.GET.get('city', 'Paris')  # par défaut Paris
    api_key = 'afc19c498e0d34b22cfd08da01ad5f60'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    
    # Extract weather information
    weather_description = data['weather'][0]['description']
    temperature_kelvin = data['main']['temp']  # température en Kelvin
    temperature_celsius = temperature_kelvin - 273.15  # conversion de Kelvin à Celsius
    humidity = data['main']['humidity']  # humidité en pourcentage
    wind_speed_meter_sec = data['wind']['speed']  # vitesse du vent en mètres par seconde
    wind_speed_km_hr = wind_speed_meter_sec * 3.6  # conversion de m/s à km/h
    
    # Extract weather icon code
    icon_code = data['weather'][0]['icon']
    # Construct URL for weather icon
    icon_url = f'http://openweathermap.org/img/wn/{icon_code}.png'

    # Construct JSON response including weather icon URL
    response_data = {
        'city': city,
        'weather': weather_description,
        'temperature': temperature_celsius,
        'humidity': humidity,
        'wind_speed': wind_speed_km_hr,
        'icon_url': icon_url  # Include weather icon URL in the response
    }
    
    response = JsonResponse(response_data)
    response["Access-Control-Allow-Origin"] = "*"
    return response