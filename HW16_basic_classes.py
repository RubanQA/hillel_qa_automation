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
    count = 0
    amount = []

    """Company model"""

    def __init__(self, company_name: str, foundation_year: int, country: str, employees_number: int, income: int):
        """Initialization company attributes"""
        self.company_name = company_name
        self.foundation_year = foundation_year
        self.country = country
        self.employees_number = employees_number
        self.income = income
        Company.count += 1
        Company.amount.append(income)

    """count company age"""

    def company_age(self):
        now = date.today().year
        return now - self.foundation_year

    """Show company info"""

    def view_conpany_info(self):
        print(f'Company name: {self.company_name}\nAge: {self.company_age()}\nCompany country: {self.country} '
              f'\ncompany income: {self.income}')

    """Avg income company"""

    @classmethod
    def get_avg_income(cls, *income: list):
        summ = sum(income[0])
        avg = round(summ / Company.count, 2)
        print(f'Income companies: {avg}')
        return avg

    """Avg salary"""

    @staticmethod
    def get_avg_salary(income, employees):
        salary = income / employees
        print(f"Avg salary of company: {salary}")


itrex = Company("ITrex", 2011, "Ukraine", 300, 700000)
m2e = Company("M2E", 2005, "Ukraine", 50, 300000)
epam = Company("Epam", 2002, "Ukraine", 10000, 12700000)

companies = [itrex, m2e, epam]
rates = [company.income for company in companies]

itrex.view_conpany_info()
m2e.view_conpany_info()
epam.view_conpany_info()

Company.get_avg_salary(200000, 300)
Company.get_avg_income(rates)


class Employee:
    empAmount = 0
    overtime_bonus = 0

    'Constructor'

    def __init__(self, name, years, specialty, salary, ):
        self.name = name
        self.years = years
        self.specialty = specialty
        self.salary = salary
        Employee.empAmount += 1

    'The method shows the employee`s salary'

    def show_emp_salary(self):
        print(f'Name : {self.name}, Salary: {self.salary}')

    'The method shows the employee`s specialty'

    def show_emp_specialty(self):
        print(f'Name : {self.name}, Specialty: {self.specialty}')

    'The class method show the overtime bonus'

    @classmethod
    def show_overtime_bonus_for_employees(cls):
        print(f'Bonus amount for overtime: {cls.overtime_bonus}')

    'The method shows the number of all employees'

    @staticmethod
    def show_emp_amount():
        print(f'Total Employee: {Employee.empAmount}')

    'The method shows the assigned tasks by specialties'

    @staticmethod
    def assigned_task(specialty):
        print('Your assigned tasks:')
        if specialty == 'Dev':
            requirement = ['dev_task_1', 'dev_task_2', 'dev_task_3']
        elif specialty == 'QA':
            requirement = ['qa_task_1', 'qa_task_2']
        elif specialty == 'PM':
            requirement = ['pm_task_1', 'pm_task_2']
        else:
            requirement = ['other_task_1']
        return requirement


emp_Denis = Employee("Denis", 32, "QA", 3000)
emp_Denis.show_emp_amount()
emp_Denis.show_emp_salary()
emp_Denis.show_emp_specialty()
print(emp_Denis.assigned_task("Dev"))
Employee.overtime_bonus = 1000
Employee.show_overtime_bonus_for_employees()
emp_Denis.show_overtime_bonus_for_employees()