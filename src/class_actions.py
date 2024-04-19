import json
from abc import ABC, abstractmethod
from config import file_path


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
    def __init__(self, file=file_path):
        self.file = file

    def save_vacancies(self,vacancies):
        with open(file_path, 'wt', encoding='utf-8') as file:
            vacancies_json = json.dumps(vacancies, ensure_ascii=False, indent=4)
            file.write(vacancies_json)

    def add_vacancy(self, vacancy):
        with open(file_path, "r", encoding="utf8") as file:
            list_vacancies = json.load(file)
        with open(file_path, "r", encoding="utf8") as file:
            list = json.load(file)
        for v in list_vacancies:
            if vacancy in v["name"]:
                list.append(v)
        list_vacancies_add = json.dumps(list, ensure_ascii=False, indent=4)

        with open(file_path, "w", encoding="utf8") as file:
            file.write(list_vacancies_add)
        return list_vacancies_add

    def get_vacancy(self, criterion):
        with open(file_path, "r", encoding="utf8") as file:
            vacancies = json.load(file)
            criterion_vac = []
            for vac in vacancies:
                if not vac["snippet"]["requirement"]:
                    continue
                else:
                    if criterion in vac["snippet"]["requirement"]:
                        criterion_vac.append(vac)
        return criterion_vac

    def del_vacancy(self):
        list_vacancies_del = []
        list = json.dumps(list_vacancies_del, ensure_ascii=False)
        with open(file_path, "w", encoding="utf8") as file:
            file.write(list)