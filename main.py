from src.class_actions import VacanciesFile
from src.class_api import HeadHunterAPI

vac = HeadHunterAPI()
name = vac.get_vacancies_data('водитель')
a = VacanciesFile()
result = a.save_vacancies(name)