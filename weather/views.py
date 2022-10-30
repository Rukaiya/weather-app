import imp
from urllib import response
import requests
from django.shortcuts import render
from decouple import config
from .models import City
from .forms import CityForm
# Create your views here.

def index(request):
    APP_KEY = config('APP_KEY')
    print(APP_KEY)
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units={}'
    units = 'metric'

    if request.method == 'POST':
        print(request.POST)

    form = CityForm()
    weather_data = []
    cities = City.objects.all()
    
    for city in cities:
        response = requests.get(url.format(city, APP_KEY, units)).json()

        city_weather = {
            'city': city.name,
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    print(weather_data)
    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/main.html', context)