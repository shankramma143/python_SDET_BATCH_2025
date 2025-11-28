# case1 soft assertion

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_opencart():
   driver=webdriver.Chrome()
   driver.get("https://tutorialsninja.com/demo/")
   driver.maximize_window()
   #Wring wrong expected result to fail script intentionally
   expected_title="your Store ABC"
   actual_title=driver.title
   #Both are not same it will fail
   assert actual_title.__eq__(expected_title)
   print("Test pass 1")
   #Search text field
   driver.find_element(By.NAME,"search").send_keys("HP")
   #Click on Search button
   driver.find_element(By.XPATH,"//button[contains(@class,'btn-default')]").click()
   #driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
   time.sleep(5)
  #wrong Element
   assert driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()
   print("Test pass 2")
   driver.quit()

