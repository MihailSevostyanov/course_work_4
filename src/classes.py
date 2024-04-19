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


class Vacancy:
    def __init__(self, name, area, salary, requirement, responsibility, schedule, experience, url):
        self.name = name
        self.area = area
        if salary is None:
            self.salary = 0
        else:
            self.salary = salary
        self.requirement = requirement
        self.responsibility = responsibility
        self.schedule = schedule
        self.experience = experience
        self.url = url

    def __repr__(self):
        return (f"{self.__class__.__name__}: {self.name}, {self.area}, {self.salary}, {self.requirement}, "
                f"{self.responsibility}, {self.schedule}, {self.experience}, {self.url}")

    def __lt__(self, other):
        if self.salary != 0 and other.salary != 0:
            if self.salary['from'] is not None and other.salary['from'] is not None:
                if self.salary['from'] < other.salary['from']:
                    return True
                return False
            return False
        return False
