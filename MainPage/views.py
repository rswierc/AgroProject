import requests
from django.shortcuts import render

# Create your views here
def weather(request):
    city = ['Wrocław', 'Opole', 'Kobylno', 'Bierdzany']
    r = []
    weather = []
    for count, i in enumerate(city):
        url = f'https://api.openweathermap.org/data/2.5/weather?q={i}&APPID=8ba66185083e4093fce75a96ace553fc'
        r.append(requests.get(url.format(i)).json())

        weather_city = {
            'city' : i,
            'temperature' : round(int(r[count]['main']['temp'])-273.15, 1),
            'feels_like' : round(int(r[count]['main']['feels_like'])-273.15, 1),
            'temp_min' : r[count]['main']['temp_min'],
            'temp_max' : r[count]['main']['temp_max'],
            'icon' : r[count]['weather'][0]['icon'],
            'clouds' : r[count]['clouds']['all'],
            'wind' : r[count]['wind']['speed'],
        }
       
        weather.append(weather_city)


 
    context = {'weather': weather}
    return render(request, "MainPage/home_page.html", context)