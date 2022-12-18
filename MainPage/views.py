import requests
from django.shortcuts import render

# Create your views here
def weather(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q=Wrocław&APPID=8ba66185083e4093fce75a96ace553fc'
    city = 'Wroclaw'

    r = requests.get(url.format(city)).json()
    
    city_weather = {
        'city' : city,
        'temperature' : r['main']['temp'],
        'feels_like' : r['main']['feels_like'],
        'temp_min' : r['main']['temp_min'],
        'temp_max' : r['main']['temp_max'],
        'icon' : r['weather'][0]['icon'],
        'clouds' : r['clouds']['all'],
    }

    
    return render(request, "MainPage/home_page.html", city_weather)