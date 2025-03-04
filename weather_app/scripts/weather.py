import requests
import json


def Weather(city):

    try:
        host = json.loads(requests.get(f'your weather API from weatherapi.com').content)
        lattitude = host['location']['lat']
        long = host['location']['lon']
        temperature = host['current']['temp_c']
        wind = host['current']['wind_kph']
        condition = host['current']['condition']['text']
        img = host['current']['condition']['icon']
        localtime = host['location']['localtime']

        weather_dict = {'lattitude': lattitude,
                        'long': long,
                        'temperature': temperature,
                        'wind': wind,
                        'condition': condition,
                        'img': img,
                        'localtime': localtime}

        return weather_dict
    except:
        return 'ERROR 404'
