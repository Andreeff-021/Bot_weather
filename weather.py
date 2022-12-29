import requests
from config import KEY

def weather_city(city):
    r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={KEY}")
    data = r.json()

    name_city = data['name']
    description = data['weather'][0]['description']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    visibility = data['visibility']
    speed = data['wind']['speed']

    return f'{name_city} \n{description} \nТемпература воздуха {temp}' \
           f'\nОщущается как {feels_like} \nДавление {pressure} мм рт. ст. \nВлажность {humidity}' \
           f'\n Видимиость {visibility} м \nСкорость ветра {speed} м/с'