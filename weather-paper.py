# File contatins private information <DO NOT SHARE SECRETS.py>
from SECRETS import API_KEY
# Used to access weather web API
from requests import get
from location import get_location
import json


def get_weather_forecast():
    loc = get_location()
    api_url = 'https://api.weatherapi.com/v1/forecast.json?key={}&q={},{}&'\
              'days=7&aqi=yes&alerts=yes'.format(API_KEY, loc[2], loc[3])
    print('API call:' + api_url)
    
    return get(api_url).json()


if __name__ == '__main__':
    data = get_weather_forecast()
