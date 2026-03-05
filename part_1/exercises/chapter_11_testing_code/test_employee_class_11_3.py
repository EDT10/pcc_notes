"""
Write a class called Employee. The __init__() method should take in a first name, 
a last name, and an annual salary, and store each of these as attributes. 
Write a method called give_raise() that adds $5000 to the annual salary by default 
but also accepts a different raise amount.
Write a test file for Employee with two test functions, test_give_default_raise() 
and test_give_custom_raise(). Write your tests once without using a fixture, 
and make sure they both pass. Then write a fixture so you don’t have to create a 
new employee instance in each test function. Run the tests again, 
and make sure both tests still pass.
"""


import pytest
from employee_11_3 import Employee


@pytest.fixture
def employee_info():
    test_user_1 = Employee("Johnny", "Boy", 10000)
    return test_user_1


def test_give_default_raise(employee_info):
    """Tests the default raise amount 0f 5000"""  
    assert employee_info.give_raise() == 15000

def test_give_custom_raise(employee_info):
    """Test a custom raise amount of 8000"""
    assert employee_info.give_raise(8000) == 18000