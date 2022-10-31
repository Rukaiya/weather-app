from email import message
import imp
from unicodedata import name
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
    units = 'imperial'
    err_msg = ''
    message = ''
    message_class = ''
    if request.method == 'POST':
       form = CityForm(request.POST)

       if form.is_valid():
        new_city = form.cleaned_data['name']
        existing_city_count = City.objects.filter(name=new_city).count()
        if existing_city_count == 0:
            response = requests.get(url.format(new_city, APP_KEY, units)).json()
    
            if response['cod'] == 200: 
                form.save() 
            else:
                err_msg = 'City not found'
        else:
            err_msg = 'City already exists'
        
        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'City successfully added'
            message_class = 'is-success'
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
    context = {
        'weather_data': weather_data, 
        'form': form,
        'message': message,
        'message_class': message_class
        }
    return render(request, 'weather/main.html', context)
    