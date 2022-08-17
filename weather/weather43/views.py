from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from .models import City
from .forms import CityForm
def index(request):
    appid = '0c72058207acf776aee1fb6e7a060c3c'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+appid
    if request.method =='POST':
        form = CityForm(request.POST)
        form.save()
        return HttpResponseRedirect('/')

    form = CityForm
    cities = City.objects.all()
    
    all_cities=[]
    for city in cities:
        res = requests.get(url.format(city)).json()
        city_info={
            'city':city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
    }
        all_cities.append(city_info)
    context={
        'all_info':all_cities, 'form': form
    }

    return render(request,'weather/index.html',context)

def street(request):
    return render(request,'weather/street.html')