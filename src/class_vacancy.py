class Vacancy:
    def __init__(self, name, area, salary, requirement, responsibility, schedule, experience, employment, url):
        self.name = name
        self.area = area
        self.salary = salary
        self.requirement = requirement
        self.responsibility = responsibility
        self.schedule = schedule
        self.experience = experience
        self.employment = employment
        self.url = url

    def __repr__(self):
        return (f"{self.__class__.__name__}: {self.name}, {self.area}, {self.salary}, {self.requirement}, "
                f"{self.responsibility}, {self.schedule}, {self.experience}, {self.employment}, {self.url}")

    def __lt__(self, other):
        if self.salary is not None and other.salary is not None:
            if self.salary['to'] < other.salary['to']:
                return self
            else:
                return other
        return 'Зарплата не указана'

    def __gt__(self, other):
        if self.salary is not None and other.salary is not None:
            if self.salary['to'] > other.salary['to']:
                return self
            else:
                return other
        return 'Зарплата не указана'
