from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Locating elements by partial link text
#Example 1
driver=webdriver.Chrome()
driver.get("https://www.selenium.dev/")
driver.maximize_window()
driver.find_element(By.PARTIAL_LINK_TEXT,"talk.").click()
time.sleep(5)
driver.close()

#Example 2
driver=webdriver.Chrome()
driver.get("https://www.selenium.dev/")
driver.maximize_window()
driver.find_element(By.PARTIAL_LINK_TEXT,"Down").click()
time.sleep(5)
driver.close()