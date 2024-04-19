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


class VacanciesActions(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancy(self, tags):
        pass

    @abstractmethod
    def del_vacancy(self, vacancy_id):
        pass


class VacanciesFile(VacanciesActions):
    def __init__(self, file='vacancies.json'):
        self.file = file

    def add_vacancy(self, vacancy):
        with open(self.file, 'rt', encoding='utf-8') as file:
            vacancy_list = json.load(file)
        with open(self.file, 'wt', encoding='utf-8') as file:
            vacancy_list.append(vacancy)
            json.dump(vacancy_list, file, ensure_ascii=False, indent=4)

    def get_vacancy(self, tags):
        pass

    def del_vacancy(self, vacancy_id):
        with open(self.file, 'rt', encoding='utf-8') as file:
            vacancies = json.load(file)
        with open(self.file, 'wt', encoding='utf-8') as file:
            for vacancy in vacancies:
                if str(vacancy_id) == vacancy['id']:
                    vacancies.remove(vacancy)
            json.dump(vacancies, file, ensure_ascii=False)
