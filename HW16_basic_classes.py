# 1. Создать классы Employee (сотрудник) и Company (компания).
# Классы должны содержать:
# минимум два поля экземпляров и одно поле класса
# минимум два метода экземпляра
# минимум один метод класса
# минимум один статический метод
# К методам добавить строки документации.
# Методы должные быть НЕ get/set поле, а что-то оригинальнее:) (но если надо их, тоже можно добавить)
# Написать код который создает несколько экземпляров и взаимодействует с объектами. Задание в том числе и на фантазию

from datetime import date

class Company:

    """Company model"""
    def _init_(self, name: str, country: str, foundation_year: int, employees: int, projects: int):
        """Initialization company attributes"""
        self.name = name
        self.country = country
        self.foundation_year = foundation_year
        self.employees = employees
        self.projects = projects

    """count company age"""
    def company_age(self):
        now = date.today().year
        return now - self.foundation_year

    """average number of employees on the projects"""
    def avg_employees_on_projects(self, employees, projects):
        return self.employees // self.projects

    """average company income"""
    @staticmethod
    def avg_year_income(self):
        return self.avg_year_income // 12

    """Add field to class"""
    @classmethod
    def add_class_attribute(cls, attr, value=None):
        if not hasattr(cls, attr):
            setattr(cls, attr, value)
            return f'{attr} attribute is added to class {cls.__name__}'
        else:
            return f'Attribute {attr} exists already'

    """Check attribute in class"""
    @classmethod
    def check_attribute(self, attr):
        self.attr = attr
        return hasattr(self, attr)

    """delete class field"""
    @classmethod
    def delete_class_attribute(cls, attr):
        delattr(cls, attr)

    """about company"""
    def company_info(self):
        print(f'Company name: {self.name}')
        print(f'Company name: {self.country}')
        print(f'Company age: {self.company_age()}')
        print(f'Employees: {self.employees}')
        print(f'Active projects: {self.projects}')



class Employee:
    department = 'Web Development'
    count = 0

    def __init__(self, name, surname, experience, salary):
        """Initialization company attributes"""
        self.name = name
        self.surname = surname
        self.work_experience = experience
        self.salary = salary
        self.english_level = 'upper-intermediate'
        Employee.count += 1

    def change_name(self, new_name):
        """Change name employee"""
        self.name = new_name
        print(f'New name: {self.name}')

    def change_surname(self, new_surname):
        """Change surname employee"""
        self.surname = new_surname
        print(f'New surname: {self.surname}')

    def change_english_level(self, new_english_level):
        """Change english level of employee"""
        self.english_level = new_english_level
        print(f'New english level: {self.english_level}')

    def print_employee_info(self):
        """Info about employee"""
        print(
            f'Name: {self.name},\nSurname: {self.surname},\nExpirence: {self.work_experience},\nSalary: {self.salary},\nDepartment: {Employee.department}\n')

    @staticmethod
    def get_salary_total(*salary: list):
        """Total salary budget"""
        summ = sum(salary[0])
        print(f'Salary budget: {summ}')
        return summ

    @classmethod
    def change_raise_salary(cls, new_value):
        """Check raise salary"""
        cls.year_salary_raise_value = new_value
        return new_value

    @staticmethod
    def start_work():
        """View start working"""
        print('Start.')