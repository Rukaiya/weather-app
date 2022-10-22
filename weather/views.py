from django.shortcuts import render
from decouple import config
# Create your views here.

def index(request):
    APP_KEY = config('APP_KEY')
    url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&appid={APP_KEY}&units=metric'
    city = 'Dhaka'
    return render(request, 'weather/main.html')