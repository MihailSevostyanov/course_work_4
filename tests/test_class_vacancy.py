import pytest


@pytest.mark.usefixtures("test_correct_init_vacancy")
def test_init(test_correct_init_vacancy):
    assert test_correct_init_vacancy.name == "Дегустатор электронных сигарет"
    assert test_correct_init_vacancy.salary == 250000
    assert test_correct_init_vacancy.url == "https://hh.ru/applicant/vacancy_response?vacancyId=97244650"



