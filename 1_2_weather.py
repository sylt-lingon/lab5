import requests

TOKEN = '8d89d5ead4ee115272f82e229ce3dc3e'
URL = 'http://api.openweathermap.org/data/2.5/weather?'


def get_weather(city, token=TOKEN, url=URL):
    params = {'q': f'{city}',
              'appid': f'{token}',
              'units': 'metric',
              'lang': 'ru'
              }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        weather = response.json()
        temp = weather['main']['temp']
        details = weather['weather'][0]['description'].capitalize()
        pressure = weather['main']['pressure']
        humidity = weather['main']['humidity']

        print(f'Температура в городе {city}: {temp}°C')
        print(f'Погодные условия: {details}')
        print(f'Влажность: {humidity}%')
        print(f'Давление: {pressure} гПа')
    else:
        print("Не удалось получить погодные данные:(")

    print()
    print(response)  # 1 задание


city_name = input('В каком городе хотите узнать погоду: ')
print()
get_weather(city_name)  # 2 задание
