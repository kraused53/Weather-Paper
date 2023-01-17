# File contatins private information <DO NOT SHARE SECRETS.py>
from SECRETS import API_KEY, ZIP_CODE
# Used to access weather web API
from requests import get
import json

def get_weather_forecast():
    api_url = 'https://api.weatherapi.com/v1/forecast.json?key={}&q={}&'\
              'days=7&aqi=yes&alerts=yes'.format(API_KEY, ZIP_CODE)
    weather_data = json.loads(get(api_url))
    
    return weather_data


if __name__ == '__main__':
    data = get_weather_forecast()
