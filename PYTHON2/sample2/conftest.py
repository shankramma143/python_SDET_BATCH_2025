import pytest
from selenium import webdriver

@pytest.fixture()
def setup_and_teardown(request):
   global driver
   driver = webdriver.Chrome()
   driver.get("https://tutorialsninja.com/demo/")
   driver.maximize_window()
#This will pass driver to the each class
   request.cls.driver = driver
   yield
   driver.quit()

