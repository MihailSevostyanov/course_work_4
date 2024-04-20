import os

from config import ROOT_DIR
from src.sorting import sorted_by_salary, filter_by_salary
from src.class_actions import JSONWorker


class Functions:

    @staticmethod
    def request():
        """
        выводит поисковый запрос для запроса вакансий из hh.ru
        """
        return input('Введите поисковый запрос для поска вакансий: ')

    @staticmethod
    def top_vacancies(vacancies):
        """
        выдает топ N вакансий по зарплате
        """
        num = int(input('Какое количчество вакансий вам выдать? '))
        sorted_vacancies = sorted_by_salary(vacancies)
        for i in sorted_vacancies[0: num]:
            print(i)

    