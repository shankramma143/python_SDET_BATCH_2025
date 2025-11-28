import pytest
@pytest.fixture(autouse=True,scope="session")
def setup_and_teardown():
   print("Launch browser")
   print("Open the application URL in the browser")
   yield
   print("Close Browser")