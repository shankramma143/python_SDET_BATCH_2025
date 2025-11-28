#case1
#
# import pytest
# import allure
# @pytest.fixture
# def setup_and_teardown():
#    print("Launch browser")
#    print("Open the application URL in the browser")
#    yield
#    print("Close Browser")
#
#
# def test_register_with_mandatory_fields(setup_and_teardown):
#    print("Testing test_register_with_mandatory_fields")
#
#
# def test_register_with_all_fields(setup_and_teardown):
#    print("Testing test_register_with_all_fields")


#case2: create a conftest.py file as a common for all test files inside the same package and add setup_and_teardown() method into it.

def test_register_with_mandatory_fields(setup_and_teardown):
   print("Testing test_register_with_mandatory_fields")


def test_register_with_all_fields(setup_and_teardown):
   print("Testing test_register_with_all_fields")