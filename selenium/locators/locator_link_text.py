from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# #Example 1
# driver=webdriver.Chrome()
# driver.get("https://www.selenium.dev/")
# driver.maximize_window()
# driver.find_element(By.LINK_TEXT,"Submit your talk.").click()
# time.sleep(5)
# driver.close()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.selenium.dev/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Downloads").click()
time.sleep(5)
driver.close()
