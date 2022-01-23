import requests
import os
from datetime import datetime

def get_weather():
    u_api = os.environ["curr_weather"]
    loc = input("Enter the name of the city: ")

    complete_api = "https://api.openweathermap.org/data/2.5/weather?q=" + loc + "&appid=" + u_api

    ap_link = requests.get(complete_api)
    api_data = ap_link.json()

    if api_data['cod'] == '404':
        print("Wrong City: {}, Retype city name.".format(loc))
    else:
        temperature = ((api_data['main']['temp']) - 273.15)
        description = api_data['weather'][0]['description']
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        wind_speed = api_data['wind']['speed']
        humidity = api_data['main']['humidity']

        print("-------------------------------------------------------------")
        print("Weather Statistics: - {}  || {}".format(loc.upper(), date_time))
        print("-------------------------------------------------------------")

        print("Current temperature: {:.2f} deg C".format(temperature))
        print("Current weather description  :", description)
        print("Current Humidity      :", humidity, '%')
        print("Current Wind Speed    :", wind_speed, 'km per hour')
