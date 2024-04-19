import json
from abc import ABC, abstractmethod


import requests


class APIVacancies(ABC):
    @abstractmethod
    def get_vacancies_data(self, name):
        pass


class HeadHunterAPI(APIVacancies):

    def __init__(self):
        self.url_hh = 'https://api.hh.ru/vacancies'

    def get_vacancies_data(self, name):
        response = requests.get(self.url_hh, params={'text': name})
        result = response.json()
        with open('vacancies.json', 'wt', encoding='utf-8') as file:
            json.dump(result['items'], file, ensure_ascii=False, indent=4)

