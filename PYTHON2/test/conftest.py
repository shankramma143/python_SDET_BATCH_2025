import pytest
@pytest.fixture()
def setup_and_teardown():
   print("Launch browser")
   print("Open the application URL in the browser")
   yield
   print("Close Browser")