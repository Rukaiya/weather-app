from urllib import response
import requests
from django.shortcuts import render
from decouple import config
# Create your views here.

def index(request):
    APP_KEY = config('APP_KEY')
    print(APP_KEY)
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units={}'
    city = 'Dhaka'
    units = 'metric'
    response = requests.get(url.format(city, APP_KEY, units)).json()

    city_weather = {
        'city': city,
        'temperature': response['main']['temp'],
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
    }

    context = {'city_weather': city_weather}
    return render(request, 'weather/main.html', context)