from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#Example 1
driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.find_element(By.NAME,"user-name").send_keys("shankru")
time.sleep(5)
driver.close()


#Example 2
driver=webdriver.Chrome()
driver.get("https://www.linkedin.com/login")
driver.maximize_window()
driver.find_element(By.NAME,"session_key").send_keys("shankru")
time.sleep(5)
driver.close()

