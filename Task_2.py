import requests
from yandex_token import TOKEN
import unittest


def yandex_disk_directory_create(token, directory_name):
    base_url = 'https://cloud-api.yandex.net'
    headers = {'Authorization': f'OAuth {token}'}
    params = {'path': directory_name}
    response = requests.put(f'{base_url}/v1/disk/resources',
                            headers=headers,
                            params=params)
    if response.status_code in [200, 201]:
        return f'Директория {directory_name} - успешно создана!'
    elif response.status_code == 401:
        return f'Указан неверный токен авторизации!'
    elif response.status_code == 409:
        return f'Директория {directory_name} - уже существует!'
    else:
        return 'Неизвестная ошибка!'


def yandex_disk_directory_delete(directory_name):
    base_url = 'https://cloud-api.yandex.net'
    headers = {'Authorization': f'OAuth {TOKEN}'}
    params = {'path': directory_name}
    response = requests.delete(f'{base_url}/v1/disk/resources',
                            headers=headers,
                            params=params)
    return response.status_code


class test_yandex_api(unittest.TestCase):
    test_directory = 'test_directory'

    def tearDown(self):
        yandex_disk_directory_delete(self.test_directory)

    def test_directory_create(self):
        directory_name = self.test_directory
        self.assertEquals(yandex_disk_directory_create('', directory_name), f'Указан неверный токен авторизации!')
        self.assertEquals(yandex_disk_directory_create(TOKEN, directory_name), f'Директория {directory_name} - успешно создана!')
        self.assertEquals(yandex_disk_directory_create(TOKEN, directory_name), f'Директория {directory_name} - уже существует!')






