# Program: employee_test.py
# Programmer: Lorenzo Openito
# Date: 09/08/2024
# Description: Unit tests for the Employee class

import pytest
from employee_class import Employee

@pytest.fixture
def employee():
    return Employee("Eric", "Matthes", 65000)

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.annual_salary == 70000

def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.annual_salary == 75000
