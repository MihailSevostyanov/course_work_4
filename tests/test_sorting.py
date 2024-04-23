import random

import pytest

from src.sorting import sorted_by_salary, filter_by_salary


# def test_sorted_by_salary(big_list_vacancies):
#     assert sorted_by_salary(big_list_vacancies, 250000)[-1].__dict__ == {
#         "name": "Дегустатор электронных сигарет",
#         "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97244650",
#         "salary": 250000,
#         "salary_for_filtering": 250000,
#         "currency": "RUR",
#         "requirement": "4. Разбираться в электронных сигаретах.",
#         "responsibility": "1. Оценивать тестовые варианты электронных сигарет(можно ли запускать продукцию в продажу магазинов Escobar). 2. Писать отчет об вкусе, насыщенности..."
#     }


# @pytest.mark.usefixtures("big_list_vacancies")
# def test_filter_by_salary(big_list_vacancies):
#     assert type(filter_by_salary(big_list_vacancies)) == list
