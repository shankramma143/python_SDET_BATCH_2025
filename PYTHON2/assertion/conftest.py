import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture()
def setup_and_teardown():
  #make drive as global, Otherwise we will get problem
  global driver
  driver = webdriver.Chrome()
  driver.get("https://tutorialsninja.com/demo/")
  driver.maximize_window()
  yield
  driver.quit()