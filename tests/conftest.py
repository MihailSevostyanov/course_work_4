import pathlib

import pytest

from config import ROOT_DIR
from src.class_actions import JSONWorker
from src.class_vacancy import Vacancy

TEST_FILE_PATH = pathlib.Path.joinpath(ROOT_DIR, 'data', 'test.json')


@pytest.fixture()
def test_JSONWorker():
    return JSONWorker(TEST_FILE_PATH)


@pytest.fixture()
def test_correct_init_vacancy():
    return Vacancy("Дегустатор электронных сигарет", "https://hh.ru/applicant/vacancy_response?vacancyId=97244650",
                   250000, "RUR", "4. Разбираться в электронных сигаретах.",
                   "1. Оценивать тестовые варианты электронных сигарет(можно ли запускать продукцию в продажу магазинов Escobar). 2. Писать отчет об вкусе, насыщенности...")


@pytest.fixture()
def test_list_vacancies():
    return [
        {
            "name": "Дегустатор электронных сигарет",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97244650",
            "salary": 250000,
            "salary_for_filtering": 250000,
            "currency": "RUR",
            "requirement": "4. Разбираться в электронных сигаретах.",
            "responsibility": "1. Оценивать тестовые варианты электронных сигарет(можно ли запускать продукцию в продажу магазинов Escobar). 2. Писать отчет об вкусе, насыщенности..."
        }
    ]


@pytest.fixture()
def test_list_vacancies_2():
    return [
        {
            "name": "Дегустатор электронных сигарет",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97244650",
            "salary": 250000,
            "salary_for_filtering": 250000,
            "currency": "RUR",
            "requirement": "4. Разбираться в электронных сигаретах.",
            "responsibility": "1. Оценивать тестовые варианты электронных сигарет(можно ли запускать продукцию в продажу магазинов Escobar). 2. Писать отчет об вкусе, насыщенности..."
        }
    ]


@pytest.fixture()
def list_object_vacancies(test_list_vacancies):
    return Vacancy.cast_to_object_list(test_list_vacancies)

@pytest.fixture
def big_list_object_vacancies(big_list_dict_vacancies):
    return Vacancy.cast_to_object_list(big_list_dict_vacancies)


@pytest.fixture()
def big_list_vacancies():
    return [
        {
            "name": "Дегустатор электронных сигарет",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97244650",
            "salary": 250000,
            "salary_for_filtering": 250000,
            "currency": "RUR",
            "requirement": "4. Разбираться в электронных сигаретах.",
            "responsibility": "1. Оценивать тестовые варианты электронных сигарет(можно ли запускать продукцию в продажу магазинов Escobar). 2. Писать отчет об вкусе, насыщенности..."
        },
        {
            "name": "Тестировщик",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97710742",
            "salary": [
                50000,
                65000
            ],
            "salary_for_filtering": 57500.0,
            "currency": "RUR",
            "requirement": "Иметь хорошие теоретические знания и опыт работы на коммерческих проектах от 6 мес. (за исключением периода обучения). Знать REST, обязательно...",
            "responsibility": "Тестировать веб и мобильные приложения. Проводить регрессионное, интеграционное и функциональное тестирование. Работать с тестовой документацией (чек-листы, тест-кейсы, баг..."
        },
        {
            "name": "Junior QA Engineer",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97659117",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "API testing knowledge and experience. Excellent analytical and problem- solving skills to create and execute test plans. Strong verbal, written...",
            "responsibility": "Testing APIs. Conducting regression tests. Performing UI testing. Reporting and investigating bugs. Creating and documenting test cases to align with..."
        },
        {
            "name": "Frontend developer",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97103466",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Хорошие знание js, react, redux. Опыт работы с next, nodejs, koa. Опыт работы с single-spa.",
            "responsibility": "Задачи в проектах UGC (Журнал, qna, Отзывы, Организации, Курсы валют, Рейтинги и др). Взаимодействие с другими разработчками, <highlighttext>тестировщиками</highlighttext> и ПМ."
        },
        {
            "name": "Стажер-тестировщик",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=95101486",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Умение составлять SQL запросы и работать с СУБД. Базовые знания о различных видах тестирования: функциональное (белый, черный ящик), регрессионное, модульное...",
            "responsibility": "Разработка тест-кейсов (написание новых проверок, актуализация существующих). Анализ проблем в функционале: локализация ошибки, выявление причин возникновения на разных средах..."
        },
        {
            "name": "Тестировщик / Специалист по тестированию программного обеспечения",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97703581",
            "salary": 2000,
            "salary_for_filtering": 2000,
            "currency": "BYR",
            "requirement": "Опыт работы от 1 года. Опыт анализа технической документации, составления чек-листов, тест-кейсов, программ и методик испытаний. ",
            "responsibility": "Функциональное тестирование прикладных программных продуктов («черный ящик», дымовое тестирование, регрессионное тестирование), юзабилити (UX/UI) тестирование. Составление тестовой документации (тест планы..."
        },
        {
            "name": "QA тестировщик",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97712683",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Локализовывать проблемы и уметь их описывать. Работать в мотивированной Agile команде. Hard skills: - Базовых знаний html/css, json, REST API. - ",
            "responsibility": "Ручное функциональное тестирование, работа с автотестами в продуктах компании а также интеграционное тестирование смежных и внешних сервисов, а также тестирование..."
        },
        {
            "name": "Геймер-тестировщик",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=95972427",
            "salary": [
                50000,
                70000
            ],
            "salary_for_filtering": 60000.0,
            "currency": "RUR",
            "requirement": "Наличие игрового опыта. Умение грамотно и четко формулировать мысли в письменном виде. Внимательность, аккуратность. Для работы нужен ПК/Ноутбук или...",
            "responsibility": "Тестирование игр в жанре MMO RPG. Проверка игрового функционала. Поиск ошибок локализации. Составление багрепортов JiraQASE."
        },
        {
            "name": "Тестировщик (Middle)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=96404816",
            "salary": [
                100000,
                100000
            ],
            "salary_for_filtering": 100000.0,
            "currency": "RUR",
            "requirement": "Обязательно: Желание и умение докапываться до корневой проблемы (которая часто не на поверхности). Умение четко и кратко выражать свои мысли...",
            "responsibility": "В команде продукта и разработки 30 человек, в QA 4 человека. QA у нас занимается ручным тестированием. Специалисты QA активно..."
        },
        {
            "name": "QA Инженер / Тестировщик",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=96428592",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Знание SQL на уровне — прочитать данные из таблицы с фильтрами, соединить две таблицы по ключевым полям. Умение работать с системами...",
            "responsibility": "Проводить функциональное, регрессионное тестирование: fullstack (фронт, бэк) + мобильные версии для android. Тестирование локализации. Писать понятную тестовую документацию (чек-листы..."
        },
        {
            "name": "Стажер-тестировщик / QA Engineer (Junior / Intern)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=96021278",
            "salary": [
                100000,
                120000
            ],
            "salary_for_filtering": 110000.0,
            "currency": "RUR",
            "requirement": "Индивидуальный подход: Ваше обучение и развитие будет адаптировано под ваши потребности и уровень знаний. Реальный опыт: В процессе сотрудничества с...",
            "responsibility": "информация не была найдена"
        },
        {
            "name": "QA-engineer / Инженер по тестированию веб-сервисов",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=96747083",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Опыт тестирования веб приложений/сервисов от 2 лет (обязательно). Опыт написания тестовой документации (обязательно). Понимание принципов клиент-серверного взаимодействия. ",
            "responsibility": "Функциональное ручное тестирование веб-сервисов. Интеграционное тестирование. Тестирование и анализ требований к продукту (Яндекс Wiki). Разработка тестовой документации (составление и..."
        },
        {
            "name": "Тестировщик (Junior QA Tester)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97593282",
            "salary": 1000,
            "salary_for_filtering": 1000,
            "currency": "USD",
            "requirement": "Разделять наши ценности (см. описание компании). 1-3 года опыта в тестировании веб или мобильных приложений (курсы и стажировки могут...",
            "responsibility": "Ручное тестирование веб-приложений и мобильных приложений. Формирование отчетов и ведение документации по тестированию, баг-трекинг, большое количество рутинной работы..."
        },
        {
            "name": "Тестировщик (стажер)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97648719",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Знание пакета Microsoft Office (Excel, Project). Уверенное знание методологии тестирования. Базовые знания учётных информационных систем класса ERP.",
            "responsibility": "Написание сценариев тестирования. Тестирования функциональности согласно сценариев. Подготовка отчетности по испытаниям."
        },
        {
            "name": "Тестировщик ПО",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97690735",
            "salary": 110000,
            "salary_for_filtering": 110000,
            "currency": "RUR",
            "requirement": "От 2 лет коммерческого опыта в тестировании. Опыт работы с инструментами управления тестированием и баг-трекинга Jira, Confluence. ",
            "responsibility": "Выполнение функционального, регрессионного, интеграционного, кроссбраузерного тестирования. Тестирование API. Написание тест-кейсов и локализация дефектов. Работа с инструментами управления тестированием и..."
        },
        {
            "name": "Web-программист - стажер",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=96507348",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "...что такое тест планы, чек листы и протокол тестирования, свободно владеть ЯП Python, быть приспособленным к монотонной работе (для <highlighttext>тестировщика</highlighttext>).",
            "responsibility": "Как правильно работать с git-ом в команде. Писать автотесты на базе Selenium/Python (<highlighttext>тестировщик</highlighttext>). Создавать web-дизайны для реальных..."
        },
        {
            "name": "Junior QA Engineer",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97595949",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Good communication and negotiating skills. - Knowledge of general principles and common testing methodologies. - Experience in writing test cases, making checklists. - ",
            "responsibility": "Analyzing requirements and specifications. - Functional and non-functional testing. - Writing and updating manual test case and test suites. - "
        },
        {
            "name": "QA Engineer Manual",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97632669",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Полное понимание всех процессов выпуска релизов продукта. Ожидаем от будущего коллеги: Опыт тестирования от 2 - 2.5 лет и выше. ",
            "responsibility": "Функциональное, интеграционное и регрессионное тестирования. Разработка тест-кейсов и чек-листов, определение стратегии тестирования продукта. Установка задач на тестовые стенды..."
        },
        {
            "name": "Python разработчик Стажер (Удаленно)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=96126868",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Понимание архитектуры клиент-серверных приложений. Опыт работы с фреймворками для веб-разработки, такими как Django или Flask. Знание принципов работы...",
            "responsibility": "...обсуждениях и принятие технических решений. Работа в тесном взаимодействии с другими членами команды, включая разработчиков мобильных приложений, дизайнеров и <highlighttext>тестировщиков</highlighttext>."
        },
        {
            "name": "Тестировщик",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97577115",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Образовательный уровень –средне-специальное, незаконченное высшее, высшее рекомендуемо. Владение основами делового этикета, навыки ведения деловой переписки и телефонных переговоров. ",
            "responsibility": "Тестирование функциональности и производительности системы контактного центра банка. Планирование, дизайн и выполнение тестовых сценариев для различных компонентов системы. "
        },
        {
            "name": "Тестировщик (Junior QA Tester)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97593283",
            "salary": 1000,
            "salary_for_filtering": 1000,
            "currency": "USD",
            "requirement": "Разделять наши ценности (см. описание компании). 1-3 года опыта в тестировании веб или мобильных приложений (курсы и стажировки могут...",
            "responsibility": "Ручное тестирование веб-приложений и мобильных приложений. Формирование отчетов и ведение документации по тестированию, баг-трекинг, большое количество рутинной работы..."
        },
        {
            "name": "QA Automation Engineer Java",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=96385394",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Обязателен коммерческий опыт работы <highlighttext>тестировщиком</highlighttext> от 6 месяцев на языке Java. Опыт работы с одним из фреймворков тестирования на Java...",
            "responsibility": "Разработка автотестов. Локализация проблем и их документирование. Разработка инфраструктуры автотестирования. Интеграция тестовой инфраструктуры. Модификация процесса тестирования под нужны проекта. "
        },
        {
            "name": "Middle Frontend разработчик",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=90777449",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Опыт работы front-end разработчиком от 2-х лет. Понимание архитектуры веб-приложений. Отличные знания JavaScript, TypeScript, React и Redux. ",
            "responsibility": "Участие в архитектурном проектирование модулей системы. Взаимодействие с другими участниками команды (владелец продукта, аналитики, <highlighttext>тестировщики</highlighttext>), а также со смежными командами. "
        },
        {
            "name": "Тестировщик / QA engineer strong junior",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97627337",
            "salary": [
                150000,
                300000
            ],
            "salary_for_filtering": 225000.0,
            "currency": "KZT",
            "requirement": "Опыт работы в платформах JIRA , Trello или подобных системах багтрекинга и платформах тестирования систем. Умение составления тест плана, тест кейсов...",
            "responsibility": "Осуществлять локализацию найденных при тестировании ошибок и составлять детальные баг-репорты. Координировать процесс тестирования, обеспечивая своевременное и качественное тестирование. "
        },
        {
            "name": "QA engineer/Инженер по тестированию (удаленно)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97545039",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Опыт тестирования ПО от 1+ года. Опыт разработки планов тестирования/анализа кейсов. Понимание процесса тестирования и его видов. ",
            "responsibility": "Выполнять функциональное тестирование ПО. Проводить интеграционное тестирование. Участвовать в проведении регрессионного тестирования. Вести и актуализировать тест-кейсы и чек -листы..."
        },
        {
            "name": "Инженер по тестированию ПО",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97686086",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Опыт тестирования в продуктовой компании не менее 2 лет. Высшее техническое образование (обязательное требование). Понимание жизненного цикла ПО. ",
            "responsibility": "Составление баг-репортов в Jira и участие в контроле их исполнения. Взаимодействие с разработчиками, <highlighttext>тестировщиками</highlighttext> и бизнес-аналитиками внутри команды."
        },
        {
            "name": "QA-инженер",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97688180",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Опыт коммерческого тестирования Mobile/Web приложений и Backend'a от 2 лет. К сожалению, после курсов не рассматриваем. ",
            "responsibility": "Нужно будет обеспечивать качество продукта на всех этапах разработки. Проводить функциональное, регрессионное, интеграционное и другие виды тестирования (Apps/Web/Backend). "
        },
        {
            "name": "Junior QA Engineer/ Младший специалист по тестированию",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97114455",
            "salary": 60000,
            "salary_for_filtering": 60000,
            "currency": "RUR",
            "requirement": "Релевантный опыт от 1 года. Умение грамотно и лаконично писать. Знание основных методов тестирования и умение составлять тест-кейсы. ",
            "responsibility": "Проводить ручное функциональное тестирование разрабатываемого ПО. Составлять тест-кейсы, баг-репорты, проводить оценку требований ТЗ и их соответствия продукту. "
        },
        {
            "name": "Тестировщик ПО",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97157956",
            "salary": [
                25000,
                25000
            ],
            "salary_for_filtering": 25000.0,
            "currency": "RUR",
            "requirement": "Прислать ”ping” в сопроводительном письме (пункт на внимательность). Желание тестировать, заводить баги и снова тестировать. Грамотная речь и письмо. ",
            "responsibility": "Выявление багов в приложении Android, приложении Windows, веб-сайте. Постановка задач разработчикам по исправлению багов. Работа в паре с разработчиком. "
        },
        {
            "name": "QA Engineer (тестировщик ПО, ученик)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97510790",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Ожидания к соискателю: Желание стать <highlighttext>тестировщиком</highlighttext> ПО и далее развиваться в сфере QA! Базовые знания C#. Готовность к чтению технической...",
            "responsibility": "Общее представление о методологии тестирования."
        },
        {
            "name": "Тестировщик устройств Яндекса с Алисой",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=96231495",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Готовы работать в офисе: ул. Льва Толстого, 16, Бизнес-центр «Красная роза» (2-3 дня в неделю). ​​​​​​​учитесь на курсах...",
            "responsibility": "Воспроизводить пользовательские сценарии, чтобы проверить ошибки, о которых сообщают в поддержку. Выполнять несложные исследовательские задачи. Взаимодействовать с командами <highlighttext>тестировщиков</highlighttext> и..."
        },
        {
            "name": "Manual QA Engineer",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97618305",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Аналогичный опыт работы от 1 года. Умение работать с DevTools. Понимание работы REST и WebSocket. Опыт работы со Swagger, Postman...",
            "responsibility": "Тестирование веб-приложения для консультирования на сайтах. Тестирование REST API."
        },
        {
            "name": "Manual QA Engineer",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97398566",
            "salary": [
                100000,
                150000
            ],
            "salary_for_filtering": 125000.0,
            "currency": "RUR",
            "requirement": "Опыт ручного тестирования web-приложений от 1 года обязательно. Базовые знания SQL. Умение задавать вопросы и коммуницировать с разработчиками. ",
            "responsibility": "Тестирование web-приложений. Тестировать фичеры. Разрабатывать тест-кейсы и тест-планы. Фиксировать дефекты, составлять отчетность."
        },
        {
            "name": "Тестировщик программного обеспечения Junior ( удаленно)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97540222",
            "salary": [
                50000,
                80000
            ],
            "salary_for_filtering": 65000.0,
            "currency": "RUR",
            "requirement": "Знание методов и методик тестирования опыт тестирования web-приложений (frontend & backend). Опыт работы с Postman или Rest-client аналоги, dev...",
            "responsibility": "написание и поддержка тестовой документации. - тест-кейсы, чек-листы, сценарии; работа с артефактами тестирования. – написание баг-репортов; написание автотестов; анализ..."
        },
        {
            "name": "Тестировщик",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=96379597",
            "salary": 120000,
            "salary_for_filtering": 120000,
            "currency": "RUR",
            "requirement": "...в сопроводительном письме вы напишете слово \"ping\". Базовые знания SQL приветствуются. Опыт работы с docker приветствуется. Опыт работы <highlighttext>тестировщиком</highlighttext> приветствуется.",
            "responsibility": "Работу в компании с нормальным руководством."
        },
        {
            "name": "Стажер QA/Тестировщик",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=95724873",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Обучаешься на IT/математической/технической специальности на старших курсах бакалавриата, в магистратуре или недавно окончил ВУЗ. Готов совмещать работу с...",
            "responsibility": "Проектировать, разрабатывать и внедрять решения, поддерживающие бизнес-процессы клиентов из разных индустрий. Выполнять работы по функциональному тест-дизайну (например, валидировать..."
        },
        {
            "name": "QA Engineer / Тестировщик",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97609501",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "информация не была найдена",
            "responsibility": "информация не была найдена"
        },
        {
            "name": "Тестировщик ПО Junior",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97683502",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Отсрочка от армии, ИТ-ипотека и другие преимущества Аккредитованных ИТ-компаний. Высокий уровень ответственности и возможность самостоятельно принимать решения.",
            "responsibility": "Тестирование серверной части веб и мобильных приложений. ЧТО ВАМ ДЛЯ ЭТОГО НЕОБХОДИМО: Создание и поддержка тестовых сценариев, тест-кейсов и..."
        },
        {
            "name": "Тестировщик (смартфоны)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97428707",
            "salary": [
                65000,
                140000
            ],
            "salary_for_filtering": 102500.0,
            "currency": "RUR",
            "requirement": "Образование среднее-профессиональное (желательно техническое). - Можно без опыта работы - расскажем, покажем, научим. - Ответственное отношение к работе. - Пунктуальность. - Внимательность.",
            "responsibility": "Проверка мобильных устройств: А) на предмет нарушения товарного вида (наличие повреждений, сколов и т.п.). Б) работоспособность (включение/выключение устройства..."
        },
        {
            "name": "Аналитик / Тестировщик",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=95895682",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Понимание принципов тестирования и внедрения ПО. Знание методологии разработки и тестирования ПО. Ответственность, исполнительность, активная жизненная позиция. Навыки деловой переписки...",
            "responsibility": "Организация процесса и непосредственное участие в тестировании и внедрении ПО. Участие в приведении изменений, вносимых в информационные системы, в соответствие..."
        },
        {
            "name": "Ассистент (экзаменатор в Центр тестирования) / тестер РКИ",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97503570",
            "salary": 60000,
            "salary_for_filtering": 60000,
            "currency": "RUR",
            "requirement": "1. Образование по направлениям «Филология», «Лингвистика», «Юриспруденция» или «История» (обязательное требование). 2. Наличие удостоверения о повышении квалификации в области методики...",
            "responsibility": "Центр тестирования РГПУ им. А. И. Герцена занимается проведением экзамена по русскому языку как иностранному, истории России и основам законодательства..."
        },
        {
            "name": "Тестировщик ПО",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97041581",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Желательно опыт тестирования web-приложений. Желательно знание методов и методик тестирования. Желательно опыт работы в командной строке linux-подобных операционных...",
            "responsibility": "Тестирование различных IT проектов компании: web, мобильные платформы, standalone приложения и т.д.. Обнаружение, документирование и отслеживание дефектов. "
        },
        {
            "name": "Frontend разработчик",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=96502767",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Работать в команде настоящих профессионалов, увлечённых своим делом и нацеленных на результат. Обязательно уверенное знание следующих технологий: HTML, CSS, JS...",
            "responsibility": "ПРОЕКТ: развитие цифровой платформы «Единое фронтальное решение», обеспечивающей бесшовный кросс-канальный доступ для всех банковских продуктов и сервисов, а также..."
        },
        {
            "name": "Стажер QA/Тестировщик",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=95724874",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Обучаешься на IT/математической/технической специальности на старших курсах бакалавриата, в магистратуре или недавно окончил ВУЗ. Готов совмещать работу с...",
            "responsibility": "Проектировать, разрабатывать и внедрять решения, поддерживающие бизнес-процессы клиентов из разных индустрий. Выполнять работы по функциональному тест-дизайну (например, валидировать..."
        },
        {
            "name": "Тестировщик / QA Engineer",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=96990276",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Опыт работы в тестировании от года. Опыт интеграционного тестирования. Умение анализировать логи. Опыт написания тестовой документации (тест-кейсов, чек-листов). ",
            "responsibility": "Проводить функциональное, регрессионное и интеграционное тестирование. Разрабатывать и писать тестовую документацию (тест-кейсы, чек-листы, методики тестирования). Искать, мониторить и..."
        },
        {
            "name": "Тестировщик игр / QA",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=96454971",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Базовые знания основ тестирования. Грамотная письменная речь, общая техническая грамотность. Интерес к играм. Внимательность, усидчивость и ответственность за результат. ",
            "responsibility": "Тестировать мобильные и web приложения. Проведение всех видов ручного тестирования: функционального, регрессионного, нагрузочного тестирования различных компонентов приложения. Грамотно, чётко и..."
        },
        {
            "name": "Frontend-разработчик (React)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=96526223",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Умели применять на практике ООП, знали, как применить эти принципы к JavaScript. Знали native JavaScript, TypeScript, CSS3, HTML5. ",
            "responsibility": "Написание кода и отладка программ и их частей. Разработка и выполнение модульного тестирования (unit-тестов) по разрабатываемой функциональности. "
        },
        {
            "name": "Тестировщик-стажер",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=96436046",
            "salary": 45000,
            "salary_for_filtering": 45000,
            "currency": "RUR",
            "requirement": "Высшее образование. Уверенные теоретические знания основ тестирования. Понимание принципов работы систем управления тест-кейсами и баг-трекинговых систем. ",
            "responsibility": "Проведение ручного, функционального тестирования мобильных приложений. Написание тест-кейсов на основе требований. Взаимодействие с командами разработки и аналитики по вопросам..."
        },
        {
            "name": "Дизайнер интерфейсов",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97637317",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Коммерческий опыт в дизайне интерфейсов для мобильных устройств от 1 года (курсов, учебных проектов и полгода работы на фрилансе, к...",
            "responsibility": "Работать в команде с аналитиками, менеджерами продукта и менеджерами проекта, разработчиками и <highlighttext>тестировщиками</highlighttext>. Следить за трендами мобильного дизайна. "
        },
        {
            "name": "Тестировщик",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=96491034",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Понимание теории тестирования, тест-анализа и тест-дизайна. Будет преимуществом знание языка программирования Python и framework playwright. Подтвержденный опыт тестирования...",
            "responsibility": "Функциональное и интеграционное ручное тестирование сервисов. Анализ соответствия продукта требованиям. Составление сопроводительной документации тестирования (тест-кейсы, тестовые наборы, описание принципов..."
        },
        {
            "name": "Тестировщик",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97237428",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Высшее образование, желательно математическое или техническое. Опыт работы <highlighttext>тестировщиком</highlighttext> от 2-х лет, желательно в финансовой или страховой компании. ",
            "responsibility": "Разрабатывать тест-кейсы, методики и сценарии тестирования. Анализировать причины возникновения проблем в продуктовой среде. Решать инциденты совместно с другими членами..."
        },
        {
            "name": "Специалист по ручному тестированию",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97628284",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Имеет опыт работы на позиции «<highlighttext>тестировщик</highlighttext>» от одного года. Microsoft Office (Word, Excel, PowerPoint, Visio). Google Docs, draw.io. ",
            "responsibility": "Написание sql-запросов."
        },
        {
            "name": "Тестировщик / QA (web) / Middle QA (web)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97544931",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Понимание особенностей тестирования web и mobile, коммерческий опыт тестирования от 1,5/2-х лет. Опыт разработки тестовой документации (тест...",
            "responsibility": "Ручное тестирование web приложения. Фиксация обнаруженных ошибок для последующего исправления. Ревью ТЗ, разработка и поддержание в актуальном состоянии тесткейсов в..."
        },
        {
            "name": "Тестировщик / QA (web) / Middle QA (web)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97544932",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Понимание особенностей тестирования web и mobile, коммерческий опыт тестирования от 1,5/2-х лет. Опыт разработки тестовой документации (тест...",
            "responsibility": "Ручное тестирование web приложения. Фиксация обнаруженных ошибок для последующего исправления. Ревью ТЗ, разработка и поддержание в актуальном состоянии тесткейсов в..."
        },
        {
            "name": "Middle+ QA Engineer",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97694695",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Знание способов и методик тестирования. Опыт тестирования сложных технологических решений или систем (например системы с микросервисной архитектурой, программно-аппаратные комплексы...",
            "responsibility": "Тестировать новые модули и функции продукта. Участвовать в построении процесса тестирования (регресс, смоук, тестирование фичей, процесс выкатки, ретроспектива релиза). "
        },
        {
            "name": "QA Manual",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=95918918",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Высшее образование, релевантный опыт от 2-х лет. Общие знания HTML, CSS, HTTP/HTTPS, JSON/XML. Понимание специфики тестирования веб...",
            "responsibility": "Разработка приемочных критериев, подготовка тестовых данных. Ревью тест-кейсов других <highlighttext>тестировщиков</highlighttext>. Участие во всех активностях проекта (митинги, планирование и.т..."
        },
        {
            "name": "Junior QA Engineer / Тестировщик WEB-приложений",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97652646",
            "salary": 750,
            "salary_for_filtering": 750,
            "currency": "EUR",
            "requirement": "Опыт работы в коммерческих проектах от полугода (мы рассматриваем специалистов уровней Junior и Middle). Хорошее понимание основ и принципов и...",
            "responsibility": "Тестировать вручную фронт и бэк наших web-приложений, преимущественно методом черного, серого ящиков. Писать подробные баг-репорты и заносить их..."
        },
        {
            "name": "Тестировщик ПО",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97607267",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Опыт тестирования продуктовых решений от 1 года. Понимание концепции тестирования, структурированный подход к работе. Знание SQL на уровне простых запросов. ",
            "responsibility": "Ручное тестирование в соответствии с требованиями заказчика. Написание тест-кейсов, чек-листов, актуализация тестовой документации, поиск и подготовка сценариев для..."
        },
        {
            "name": "QA специалист / тестировщик middle",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97654308",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Опыт ручного тестирования (функционального, интеграционного, регрессионного) от 2х лет. Понимание принципов работы web-приложений. Опыт тестирования верстки (pixel perfect...",
            "responsibility": "Аккредитованная IT-компания заказной разработки с мощной экспертизой в продуктовом подходе – создаем для своих клиентов сервисы, которые приносят прибыль бизнесу..."
        },
        {
            "name": "Web-дизайнер (UX/UI)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97707304",
            "salary": [
                100000,
                100000
            ],
            "salary_for_filtering": 100000.0,
            "currency": "RUR",
            "requirement": "Уверенный уровень владения Figma, Photoshop. Развитое чувство стиля, композиции, типографики, теории цвета, знание принципов юзабилити. Навыки графического дизайна. ",
            "responsibility": "Дизайн баннеров для сайта и рекламных кампаний. Разработка лендингов для маркетинговых акций. Взаимодействие с frontend-разработчиками и <highlighttext>тестировщиками</highlighttext>. "
        },
        {
            "name": "Manual QA Engineer (Junior+)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97318915",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Коммерческий опыт работы от 1 года. Опыт тестирования веб-приложений. Опыт тестирования мобильных приложений. Опыт проектирования тест-кейсов. Быстрая обучаемость. ",
            "responsibility": "Поиск, локализация и качественное заведение дефекта в баг-трекинговой системе. Проведение функционального тестирования системы, а именно осуществление имитации фактического использования..."
        },
        {
            "name": "Тестировщик (QA инженер) на проект ДОМ.Логин",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97621326",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Понимание тестирования и обеспечения качества, знание жизненного цикла продукта. Умение анализировать требования к продукту, анализировать потенциальные риски. Наличие практических навыков...",
            "responsibility": "ИНФОРМАЦИЯ О ПРОЕКТЕ: Ручным функциональным тестированием. Написанием, подготовкой тест кейсов / чек листов, сценариев тестирования, матрицы покрытия. Обработкой результатов тестирования, описанием..."
        },
        {
            "name": "QA-engineer",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97636366",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Навыки тестирования REST API. Опыт тестирования интеграций, мокирование запросов. Опыт работы с Kafka. Знание языка SQL на уровне написания запросов...",
            "responsibility": "Тестировать функционал в вебе. Тестировать API (Postman), поддержка коллекции запросов. Тестировать интеграции со сторонними сервисами. Тестировать работу БД. "
        },
        {
            "name": "Тестировщик ПО (удаленно)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97616794",
            "salary": 50000,
            "salary_for_filtering": 50000,
            "currency": "RUR",
            "requirement": "Желание обучаться в сфере IT. Понимание жизненного цикла разработки ПО будет преимуществом. Аналитическое мышление, внимательность к деталям. Хорошие коммуникативные навыки. ",
            "responsibility": "Планирование и проведение тестирования платформы. Анализ требований к продукту и разработка тестовой документации. Выявление, документирование и отслеживание дефектов. "
        },
        {
            "name": "Junior QA Engineer",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97117960",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Выс шее / неокончнное высшее профильное образование. Представление о процессах тестирования. Умение быстро обрабатывать информацию и переключаться между задачами. ",
            "responsibility": "Тестирование продуктов компании и клиентских конфигураций продуктов. Разработка и поддержание тестовых сценариев. Автоматизация тестовых сценариев в специализированном ПО для проведения..."
        },
        {
            "name": "Тестировщик",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97615427",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Опыт ручного тестирования программного обеспечения, веб-приложений, мобильных приложений или обучающих курсов от 1 года. Знание теории и методов функционального...",
            "responsibility": "Функциональное тестирование программных продуктов (программного обеспечения, веб-приложений, мобильных приложений, презентаций, обучающих курсов и т.п.) . Занесение обнаруженных ошибок в..."
        },
        {
            "name": "Тестировщик ПО",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97710552",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Уверенное знание теории тестирования. Опыт работы с системами ведения тестовой документации (ТМС). Опыт работы с системами отслеживания задач (jira). ",
            "responsibility": "Составление тестовой документации и подготовка отчетов по результатом тестовых прогонов. Тестирование веб сервисов и мобильных приложений. Регистрация дефектов."
        },
        {
            "name": "Тестировщик ПО",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=96425681",
            "salary": 80000,
            "salary_for_filtering": 80000,
            "currency": "RUR",
            "requirement": "Опыт тестирования desktop приложений. Знание общих принципов, понимание целей и задач тестирования и его места в разработке ПО. ",
            "responsibility": "Проведение ручного тестирования приложений под Windows и Linux. Создание тестовых сценариев, тест планов. Создание, запуск, анализ, ревью и приемка авто..."
        },
        {
            "name": "Тестировщик мобильных игр",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97126431",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Наличие компьютера (на Windows или ее эмуляторе), микрофона и стабильного подключения к интернету. Знание английского не ниже уровня Intermediate. ",
            "responsibility": "Ручное тестирование мобильных игр различных жанров (казуальные, free-to-play и др.). Изучение всех материалов к игре (лор, глоссарии и..."
        },
        {
            "name": "Тестировщик ПО (ручное)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97221859",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Высшее образование - предпочтительно техническое. Опыт тестирования от 1.5 лет. Знание и опыт применения различных методик тестирования. Опыт работы с...",
            "responsibility": "Тестирование функционала информационных систем. Разработка тест-кейсов для нового функционала. Ведение и актуализация тест-кейсов. Поддержка и развитие процесса тестирования. "
        },
        {
            "name": "QA engineer",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97633722",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Опыт работы с DevTool, Swagger, Postman (и/или другими полезными для <highlighttext>тестировщиков</highlighttext> инструментами). Опыт работы с Linux, Mac OS. ",
            "responsibility": "Быстро погрузиться в процесс тестирования в компании. Функциональное/регрессионное и другие виды тестирования в области IP телефонии. Анализ требований и..."
        },
        {
            "name": "Junior QA Engineer",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=91293820",
            "salary": 60000,
            "salary_for_filtering": 60000,
            "currency": "RUR",
            "requirement": "Ты ответственный, способный самостоятельно работать, вовлеченный в общие процессы. Знаешь теорию тестирования и умеешь правильно применять знания на практике. ",
            "responsibility": "Тестировать различные интересные фичи iOS/Android/Web. Участвовать регрессионном тестирование. Дефект-менеджмент (баг репорты, работа с тикетами и досками в..."
        },
        {
            "name": "Специалист по тестированию",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97702180",
            "salary": 60000,
            "salary_for_filtering": 60000,
            "currency": "RUR",
            "requirement": "Высшее профильное образование. Внимательность к деталям. Логическое и системное мышление: способность видеть взаимосвязи и влияние тестирования на систему в целом...",
            "responsibility": "Успешно пройти обучение по программе 1С:Itilium в нашей Компании. Разрабатывать нагрузочные тесты. Разрабатывать сценарии тестирования. Проводить тестирования (полнофункциональное..."
        },
        {
            "name": "Специалист по тестированию",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97230269",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Опыт тестирования (не менее 2-х лет) в области высоконагруженных Java-приложений в продуктовых компаниях, либо интеграторах. Опыт ручного тестирования...",
            "responsibility": "Разработка планов тестирования, включая функциональное, нагрузочное тестирование и тестирование безопасности в области высоконагруженных приложений. Подготовка и согласование планов и методик..."
        },
        {
            "name": "Тестировщик (Junior QA Tester)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97593281",
            "salary": 1000,
            "salary_for_filtering": 1000,
            "currency": "USD",
            "requirement": "Разделять наши ценности (см. описание компании). 1-3 года опыта в тестировании веб или мобильных приложений (курсы и стажировки могут...",
            "responsibility": "Ручное тестирование веб-приложений и мобильных приложений. Формирование отчетов и ведение документации по тестированию, баг-трекинг, большое количество рутинной работы..."
        },
        {
            "name": "Специалист по тестированию",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97710582",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Знание принципов клиент-серверной архитектуры, методологий разработки и жизненного цикла программного обеспечения. Знание принципов и методов тестирования. Навыки тестирования веб...",
            "responsibility": "Тестировании веб-приложений, API и интеграционных сервисов. Построение процессов тестирования. Создание и поддержание тестовой документации. Участие в анализе результатов тестирования..."
        },
        {
            "name": "Стажер-тестировщик",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97226988",
            "salary": [
                22100,
                22100
            ],
            "salary_for_filtering": 22100.0,
            "currency": "RUR",
            "requirement": "Интерес к процессу тестирования и обеспечению качества. Желание развиваться в данной профессиональной области. Базовое понимание основных этапов и принципов тестирования...",
            "responsibility": "информация не была найдена"
        },
        {
            "name": "Ведущий frontend разработчик",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97696699",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Знание и опыт работы с ReactJS. Знание и опыт работы с Next.JS. Знания HTML, CSS, а также CSS препроцессоров (SASS...",
            "responsibility": "Взаимодействие с другими командами: backend-разработчиками; <highlighttext>тестировщиками</highlighttext>, аналитиками. Исправление инцидентов/дефектов возникающих в системе. Опыт работы в продуктовой команде. "
        },
        {
            "name": "QA Engineer",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97600695",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Have English language proficiency at least at the Upper-Intermediate level. Possess a minimum of 1,5 years of relevant...",
            "responsibility": "Ensuring the quality standards of the released project. Identifying and analyzing errors. Collaborating closely with the development team. "
        },
        {
            "name": "Специалист по тестированию (Junior)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97589176",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Смотрите раздел \"Цели\"!). Понимание роли и ответственности <highlighttext>тестера</highlighttext> в проектах внедрения и разработки ПО (Опять сомневаетесь? Ну... вы знаете куда...",
            "responsibility": "Повышение уровня знаний до middle+ не позднее, чем за пол года. Минимизация количества критических сбоев и отказов в обслуживании разрабатываемого..."
        },
        {
            "name": "Fullstack QA engineer",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97146613",
            "salary": 250000,
            "salary_for_filtering": 250000,
            "currency": "RUR",
            "requirement": "Находимся сейчас в поиске уверенного Middle QA <highlighttext>тестировщика</highlighttext> на международный проект с опытом от года в автоматизации на Python. ",
            "responsibility": "Какие текущие задачи необходимо решать: Сопровождение задач начиная с анализа требования до проверок их в боевой среде. Проектирование тест-кейсов..."
        },
        {
            "name": "Тестировщик-стажер",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97613445",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "3 курс выпускник технического ВУЗа (ИТ направление-это важно!). Выраженный интерес к сфере тестирования программного обеспечения. Понимание процесса разработки программного...",
            "responsibility": "Функциональное, регрессионное и интеграционное тестирование нашего программного обеспечения (более подробно о наших проектах на нашем сайте). Составление тест-кейсов, чек..."
        },
        {
            "name": "Front-end разработчик",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97353741",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Отличные знания Vue.js(2), JS, HTML, CSS, SCSS. Опыт в настройке конфигурации Webpack. Плюсом будет знание Vue.js(3), React.js, TS. ",
            "responsibility": "Работа в продуктовой команде (менеджер продукта, UX\\UI дизайнер, аналитики, разработчики frontend и backend, <highlighttext>тестировщики</highlighttext>) по развитию цифровых сервисов Компании. "
        },
        {
            "name": "Manual QA Engineer (Офис)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97624626",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Опыт тестирования API. Понимание принципов работы клиент-серверного приложения. Теория тестирования, тест-дизайн. Работа с Docker. Linux-терминал (подключиться по...",
            "responsibility": "Ручное тестирование облачных компонентов. Проведение функционального и регрессионного тестирования. Настройка и обновление тестовых стендов. Поддержка и пополнение базы тесткейсов. "
        },
        {
            "name": "Тестировщик",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97643924",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Опыт тестирования веб-приложений от 2х лет. Умение создавать сценарии тестирования, работать с инструментами разработчика в браузере. ",
            "responsibility": "Мы поддерживаем нестандартное мышление. Передовые идеи и инновации. Энергию предпринимательского духа. Мы вдохновляемся научными разработками и созданием уникальных продуктов в..."
        },
        {
            "name": "QA engineer",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97188271",
            "salary": [
                200000,
                300000
            ],
            "salary_for_filtering": 250000.0,
            "currency": "RUR",
            "requirement": "Опыт работы в ручном тестировании от 3 лет, от 1 года работы на банковском проекте. Уверенные знания методологий, процесса разработки...",
            "responsibility": "Ручное функциональное тестирование приложений. Тестирование системы ДБО. Работа с БД, тестирование API. Подготовка тестовых данных. Анализ, разработка и использование тестовой..."
        },
        {
            "name": "Тестировщик",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97343948",
            "salary": 170000,
            "salary_for_filtering": 170000,
            "currency": "RUR",
            "requirement": "Знание теории тестирования и техник тест-дизайна. Понимание клиент-серверной архитектуры приложений. Опыт тестирования WEB и/или мобильных приложений. ",
            "responsibility": "Писать тестовую документацию: чек-листы, тест-кейсы и т.д.. Взаимодействовать с разработчиками серверной части, <highlighttext>тестировщиками</highlighttext>, аналитиками, дизайнерами. "
        },
        {
            "name": "QA Engineer / Инженер по качеству",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97539634",
            "salary": [
                60000,
                200000
            ],
            "salary_for_filtering": 130000.0,
            "currency": "RUR",
            "requirement": "Знание теории тестирования. Умение четко и ясно излагать свои мысли. Общая техническая грамотность. Понимание принципов построения современных Web и mobile...",
            "responsibility": "Ручное тестирование продуктов компании: кроссплатформенных игр и сервисных приложений, клиентской и серверной частей. Составление тест-кейсов и их поддержание в..."
        },
        {
            "name": "Тестировщик (QA Engineer)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97334172",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Опыт работы в тестировании программного обеспечения. Знание английского языка в совершенстве. Понимание методологий тестирования и процессов разработки. Опыт работы с...",
            "responsibility": "Разработка кроссплатформенного решения для рынка США и СНГ на Flutter, SQLite, Bloc, RESTfull API. Тестирование программного обеспечения на соответствие требованиям..."
        },
        {
            "name": "QA Engineer (Middle)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=96121551",
            "salary": [
                150000,
                250000
            ],
            "salary_for_filtering": 200000.0,
            "currency": "RUR",
            "requirement": "Релевантной опыт работы от 2 лет. Опыт работы со стеоком: DevTools, Postman, Charles/Proxyman, REST API. Опыт работы в тасктреккинговой...",
            "responsibility": "Выполнение функционального, регрессионного, санитарного, smoke- тестирования. Написание тест-кейсов. Заведение баг-репортов. Оценивать удобство использования нашего решения и помогать сделать..."
        },
        {
            "name": "QA Engineer",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97089789",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Опыт тестирования приложений или сервисов от 2 лет. SQL на хорошем уровне: join, оконные функции, подзапросы и т.д. ",
            "responsibility": "Возможность использовать передовые технологии и стратегии и менять бизнес наших клиентов к лучшему. Проекты в разных индустриальных направлениях с передовыми..."
        },
        {
            "name": "Middle+ QA Engineer (Инженер по тестированию)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97635824",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Коммерческий опыт работы в командах в роли <highlighttext>тестировщика</highlighttext> от 3 лет. Опыт тестирования API (Postman, Swagger). Опыт работы с БД...",
            "responsibility": "Проведением ручного функционального, регрессионного, интеграционного тестирования. Подготовкой и выпуском релизов сервисов. Обработкой результатов тестирования, описанием ошибок в баг-трекинговых системах..."
        },
        {
            "name": "Junior QA Engineer (Минск)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=95468671",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Our perfect teammate: Speaks good English and has great communication skills. Is attentive to details. Has diligent approach to performing...",
            "responsibility": "Finished QA courses. Is able to write testing documentation (test cases, checklists etc.)."
        },
        {
            "name": "Инженер-тестировщик GIS направления",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=96187721",
            "salary": 100000,
            "salary_for_filtering": 100000,
            "currency": "RUR",
            "requirement": "Уверенные знания основ тестирования программного обеспечения. Опыт ручного тестирования клиент-серверных desktop-приложений (linux). Уверенные знания и навыки работы в...",
            "responsibility": "Готовить тестовую документацию, требования к тестовому окружению. Участвовать в создании стендов совместно с инженерами. Функциональным, регрессионным и интеграционным тестированием разрабатываемого..."
        },
        {
            "name": "Специалист по тестированию ПО",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97380907",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Владение навыками составления тест-кейсов, чек-листов, баг-репортов. Опыт тестирования клиент-серверных приложений. Опыт тестирования API. Использование в работе...",
            "responsibility": "Тестирование GUI. Работа с базами данных. Ручное функциональное тестирование. Составление и анализ сценариев использования продукта. Интеграционное тестирование сервисов. Тестирование API. "
        },
        {
            "name": "Middle Frontend разработчик",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=96819332",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "SASS (SCSS). Знание современного ES2023. Vue 3. Git. Npm/Yarn, мы работаем на Yarn. Вёрстка по Figma. Docker. ",
            "responsibility": "Поддержка и оптимизация сайтов Азбуки Вкуса. Активное участие в поддержке и развитии архитектуры ключевых внутренних и внешних сервисов. "
        },
        {
            "name": "Junior+ QA Engineer",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97235731",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Knowledge of software development life cycle. Good understanding of software QA methodologies, tools and processes. Ability to describe test logic...",
            "responsibility": "Creating test artifacts and documentation, such as checklists, test cases, bug reports, test plans etc. Writing automation tests (to prepare..."
        },
        {
            "name": "Инженер-тестировщик",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97619934",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Понимание процесса тестирования ПО и желание развиваться в этом направлении. Знание основ работы сетевых ОС и протоколов семейства TCP/IP. ",
            "responsibility": "Ручное тестирование на основе тест-кейсов. Создание и актуализация тест-планов. Исследовательское тестирование. Приёмочное тестирование. Ревью документации и требований. "
        },
        {
            "name": "QA engineer (back)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97629344",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Опыт написания тестовых сценариев, планов тестирования, стратегии тестирования. Опыт тестирования обратной совместимости. Опыт тестирования web UI. Опыт тестриование API. ",
            "responsibility": "Поддержка системы репортинга (Allure). Помощь команде разработки в выборе фреймворков для тестирования. Code-review тестов разработчиков и <highlighttext>тестировщиков</highlighttext>. Интеграционное тестирование."
        },
        {
            "name": "QA-инженер (Auto)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=95651997",
            "salary": 0,
            "salary_for_filtering": 0,
            "currency": "валюта не указана",
            "requirement": "Навыки автоматизации тестирования на Java — UI и API. Умение работать с CSV, XML, JSON. Опыт работы с Selenide, Java 17...",
            "responsibility": "Автоматизация тестовых сценариев функционального и регрессионного UI / API функционального тестирования. Отладка существующих автоматических сценариев. Настройка и использование тестового инструментария и..."
        },
        {
            "name": "Junior QA engineer (Web UI)",
            "url": "https://hh.ru/applicant/vacancy_response?vacancyId=97692350",
            "salary": 90000,
            "salary_for_filtering": 90000,
            "currency": "RUR",
            "requirement": "Опыт работы с JIRA, Git, TeamCity. Знание хотя бы одного ЯП (желательно Java) на уровне понимания чужого кода. ",
            "responsibility": "Подготовкой и проведением ручного функционального/регрессионного тестирования для проектов на различных стеках технологий (Angular, JavaScript). Локализацией дефектов на различных этапах..."
        }
    ]
