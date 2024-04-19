from abc import ABC, abstractmethod
import requests


class APIVacancies(ABC):
    @abstractmethod
    def get_vacancies_data(self, name):
        pass


class HeadHunterAPI(APIVacancies):

    def __init__(self, url_hh='https://api.hh.ru/vacancies'):
        self.url_hh = url_hh

    def get_vacancies_data(self, keyword):
        response = requests.get(self.url_hh, params={'text': keyword, 'area': '113', 'per_page': 100})
        result = response.json()
        return result
