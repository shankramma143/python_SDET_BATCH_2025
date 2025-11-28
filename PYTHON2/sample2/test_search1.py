
# This method having 3 test methods which we are running with pytest
import pytest
import allure
from allure_commons.types import AttachmentType

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.mark.usefixtures("setup_and_teardown")

class TestSearch:
  def test_search_for_a_valid_products(self):
     self.driver.find_element(By.NAME,"search").send_keys("HP")
     self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
     assert self.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()
     allure.attach(self.driver.get_screenshot_as_png(), name="search_for_a_valid_products",
                   attachment_type=AttachmentType.PNG)

     time.sleep(5)


  def test_search_for_a_invalid_products(self):
     self.driver.find_element(By.NAME, "search").send_keys("QACircle")
     self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
     expected_result="There is no product that matches the search criteria."
     assert self.driver.find_element(By.XPATH, "//input[@id='button-search']//following-sibling::p").text.__eq__(expected_result)
     time.sleep(5)


  def test_search_without_providing_any_products(self):
     self.driver.find_element(By.NAME, "search").send_keys("")
     self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
     expected_result = "There is no product that matches the search criteria."
     assert self.driver.find_element(By.XPATH, "//input[@id='button-search']//following-sibling::p").text.__eq__(expected_result)
     time.sleep(5)