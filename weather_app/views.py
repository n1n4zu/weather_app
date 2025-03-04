from django.shortcuts import render, redirect
from .scripts.weather import Weather

def base(request):
    return render(request, 'base.html')

def process_form(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        return redirect('city_view', city=city)
    return redirect('base')

def city_view(request, city):
    dict = Weather(city)
    context = {'city': city,
               'lattitude': dict['lattitude'],
               'long': dict['long'],
               'temperature': dict['temperature'],
               'wind': dict['wind'],
               'condition': dict['condition'],
               'img': dict['img'],
               'localtime': dict['localtime']}
    return render(request, 'city_template.html', context)