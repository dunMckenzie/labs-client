# Program: employee_class.py
# Programmer: Lorenzo Openito
# Date: 09/08/2024
# Description: Employee class with methods to manage employee details and give raises

class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        self.annual_salary += amount
