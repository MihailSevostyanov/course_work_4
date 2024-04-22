import pytest
from src.class_vacancy import Vacancy

@pytest.fixture()
def test_correct_init_vacancy():
    return Vacancy("Дегустатор электронных сигарет", "https://hh.ru/applicant/vacancy_response?vacancyId=97244650", 250000,  "RUR", "4. Разбираться в электронных сигаретах.", "1. Оценивать тестовые варианты электронных сигарет(можно ли запускать продукцию в продажу магазинов Escobar). 2. Писать отчет об вкусе, насыщенности...")
