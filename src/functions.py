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
        return input('Введите поисковый запрос для поиска вакансий: ')

    @staticmethod
    def top_vacancies(vacancies) -> str:
        """
        выдает топ N вакансий по зарплате
        """
        num = int(input('Какое количество вакансий вам выдать? '))
        sorted_vacancies = sorted_by_salary(vacancies)
        for i in sorted_vacancies[0: num]:
            print(i)

    @staticmethod
    def work_with_user(vacancies_list):
        while True:
            print('Кнопки управления:\n'
                  '1 - вывести вакансии в терминал\n'
                  '2 - отфильтровать вакансии по З/П\n'
                  '3 - сортировать вакансии по убыванию З/П\n'
                  '4 - отсортировать топ N вакансий\n'
                  '5 - сохранить информацию о вакансиях в файл\n'
                  '6 - удалить все данные в файле\n'
                  '"stop" или "стоп" закончить работу\n')
            answer = input()
            if answer == "стоп" or answer == "stop":
                break
            try:
                answer = int(answer)
                if 1 <= answer <= 9:  # печатает вакансии в терминал
                    if answer == 1:
                        for i in vacancies_list:
                            print(i)

                    elif answer == 2:  # фильтрует вакансии по з/п
                        vacancies_list = filter_by_salary(vacancies_list)

                    elif answer == 3:  # сортирует вакансии по убыванию З/П
                        vacancies_list = sorted_by_salary(vacancies_list)
                        print('\nВакансии отсортированы\n')

                    elif answer == 4:  # отсортирует топ N вакансий
                        Functions.top_vacancies(vacancies_list)

                    elif answer == 5:  # сохраняет информацию о вакансиях в файл
                        file_name = input('Введите название файла для сохранения данных: (Пример: file) ')
                        file_path = os.path.join(ROOT_DIR, 'data', file_name + str('.json'))
                        json_saver = JSONWorker(file_path)
                        json_saver.write_vacancies(vacancies_list)

                    elif answer == 6:  # удаляет информацию о вакансиях из файла
                        file_name = input('Введите название файла для удаления данных: (Пример: file) ')
                        file_path = os.path.join(ROOT_DIR, 'data', file_name + str('.json'))
                        json_saver = JSONWorker(file_path)
                        json_saver.delete_vacancies()

                else:
                    print(f"Введите цифру от 1 до 9\n")

            except ValueError:
                print(f"Введите цифру от 1 до 9\n")
