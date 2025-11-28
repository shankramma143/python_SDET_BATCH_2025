
# This method having 3 test methods which we are running with pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_search_for_a_valid_products():
   driver=webdriver.Chrome()
   driver.get("https://tutorialsninja.com/demo/")
   driver.maximize_window()
   driver.find_element(By.NAME,"search").send_keys("HP")
   driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
   assert driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()
   driver.quit()


def test_search_for_a_invalid_products():
   driver = webdriver.Chrome()
   driver.get("https://tutorialsninja.com/demo/")
   driver.maximize_window()
   driver.find_element(By.NAME, "search").send_keys("QACircle")
   driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
   expected_result="There is no product that matches the search criteria."
   assert driver.find_element(By.XPATH, "//input[@id='button-search']//following-sibling::p").text.__eq__(expected_result)
   driver.quit()


def test_search_without_providing_any_products():
   driver = webdriver.Chrome()
   driver.get("https://tutorialsninja.com/demo/")
   driver.maximize_window()
   driver.find_element(By.NAME, "search").send_keys("")
   driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
   expected_result = "There is no product that matches the search criteria."
   assert driver.find_element(By.XPATH, "//input[@id='button-search']//following-sibling::p").text.__eq__(
       expected_result)
   driver.quit()