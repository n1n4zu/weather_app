from django.shortcuts import render, redirect, HttpResponse
from .scripts.weather import Weather

def base(request):
    return render(request, 'base.html')

def process_form(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        return redirect('city_view', city=city)
    return redirect('base')

def error_404(request, exception):
    return render(request, '404.html')

def error_500(request):
    return render(request, '404.html')

def city_view(request, city):
    print(city)
    if city is not '':
        dict = Weather(city)
        context = {'city': city,
                    'lattitude': dict['lattitude'],
                    'long': dict['long'],
                    'temperature': dict['temperature'],
                    'wind': dict['wind'],
                    'wind_dir': dict['wind_dir'],
                    'condition': dict['condition'],
                    'img': dict['img'],
                    'localtime': dict['localtime'],
                    'pressure': dict['pressure'],
                    'feelslike': dict['feelslike']}
        return render(request, 'city_template.html', context)
    else:
        return redirect('base')