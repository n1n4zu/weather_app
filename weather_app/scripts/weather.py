import requests
import json


def Weather(city):

    try:
        host = json.loads(requests.get(f'your weather API from weatherapi.com').content)
        lattitude = host['location']['lat']
        long = host['location']['lon']
        temperature = host['current']['temp_c']
        wind = host['current']['wind_kph']
        wind_dir = host['current']['wind_dir']
        condition = host['current']['condition']['text']
        img = host['current']['condition']['icon']
        localtime = host['location']['localtime']
        pressure = host['current']['pressure_mb']
        feelslike = host['current']['feelslike_c']

        weather_dict = {'lattitude': lattitude,
                        'long': long,
                        'temperature': temperature,
                        'wind': wind,
                        'wind_dir': wind_dir,
                        'condition': condition,
                        'img': img,
                        'localtime': localtime,
                        'pressure': pressure,
                        'feelslike': feelslike}

        return weather_dict
    except:
        return 'ERROR 404'
