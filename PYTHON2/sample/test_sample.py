#case1

# import pytest
#
# @pytest.fixture
# def setup_and_teardown():
#    print("Launch browser")
#    print("Open the application URL in the browser")
#    yield
#    print("Close Browser")
#
#
# def test_login_with_Valid_credentials(setup_and_teardown):
#    print("Login with valid credentials")
#    print("logout")
#
#
# def test_login_with_Invalid_credentials(setup_and_teardown):
#    print("Login with Invalid credentials")


# Case 2 : create a conftest.py file as a common for all test files inside the same package and add setup_

def test_login_with_Valid_credentials(setup_and_teardown):
   print("Login with valid credentials")
   print("logout")


def test_login_with_Invalid_credentials(setup_and_teardown):
   print("Login with Invalid credentials")