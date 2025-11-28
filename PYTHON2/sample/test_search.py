#case1 without conftest
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
# def test_search_for_a_valid_products(setup_and_teardown):
#    print("Testing test_search_for_a_valid_products")
#
#
# def test_search_for_a_Invalid_products(setup_and_teardown):
#    print("Testing test_search_for_a_Invalid_products")


# Case 2 : create a conftest.py file as a common for all test files inside the same package and add setup_and_teardown() method into it.

def test_search_for_a_valid_products(setup_and_teardown):
   print("Testing test_search_for_a_valid_products")


def test_search_for_a_Invalid_products(setup_and_teardown):
   print("Testing test_search_for_a_Invalid_products")