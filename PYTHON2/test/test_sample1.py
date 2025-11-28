#case1

import pytest
@pytest.fixture
def setup():
   print("Launch browser")
   print("Open the application URL in the browser")



def test_login_with_Valid_credentials(setup):
   print("Login with valid credentials")
   print("logout")


def test_login_with_Invalid_credentials(setup):
   print("Login with Invalid credentials")

#case2

import pytest
@pytest.fixture
def setup_and_teardown():
   print("Launch browser")
   print("Open the application URL in the browser")
   yield
   print("Close Browser")


def test_login_with_Valid_credentials(setup_and_teardown):
   print("Login with valid credentials")
   print("logout")


def test_login_with_Invalid_credentials(setup_and_teardown):
   print("Login with Invalid credentials")

