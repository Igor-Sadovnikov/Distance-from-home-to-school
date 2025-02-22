import sys
import requests
from get_distance import get_distance


def get_coords(address):
    api_key = "8013b162-6b42-4997-9691-77b7074026e0"
    server_address = 'http://geocode-maps.yandex.ru/1.x/?'
    geocoder_request = f'{server_address}apikey={api_key}&geocode={address}&format=json'
    response = requests.get(geocoder_request)
    if response:
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        toponym_coodrinates = toponym["Point"]["pos"]
        toponym_coodrinates = toponym_coodrinates.replace(' ', ',')
        return toponym_coodrinates
    else:
        print('Неверный запрос')
        sys.exit(0)


coords_home = get_coords(input('Введите адрес дома: '))
coords_school = get_coords(input('Введите адрес школы: '))
print('Расстояние от дома до школы =', round(get_distance(coords_home, coords_school), 2), 'метров.')