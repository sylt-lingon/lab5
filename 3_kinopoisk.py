import requests
import textwrap

API = 'EXJ45X6-NF9MGN7-JA5CJJQ-M14FMA9'
URL = 'https://api.kinopoisk.dev/v1.4/movie/random'


def get_random_anime(length, genres, url=URL):
    headers = {'X-API-KEY': API}
    params = {
        'notNullFields': ['name', 'description'],
        'type': ['anime'],
        'rating.kp': ['6-10'],
        'totalSeriesLength': length,
        'genres.name': genres
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        name = data['name']
        description = data['description']
        year = data['year']
        status = data['status']

        print(f'Название: {name}')
        print()
        print(f'Описание: {textwrap.fill(description, 100)}')
        print()
        print(f'Год выхода: {year}')
        print(f'Статус выхода серий: {status}')

    else:
        print('Не удалось подключиться:(')


anime_length = [input('Введите количество серий (напрмер 1-100): ')]
anime_genres = input('Введите через запятую какие жанры предпочитаете: ').split(', ')
print()
get_random_anime(anime_length, anime_genres)
