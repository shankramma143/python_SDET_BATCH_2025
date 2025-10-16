#is_displayed()
#is_enabled()
#is_selected()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()
driver.maximize_window()


"""#Example 1
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(5)
print(driver.find_element(By.XPATH,"//*[@id='APjFqb']").is_displayed())
print(driver.find_element(By.XPATH,"//*[@id='APjFqb']").is_selected())
print(driver.find_element(By.XPATH,"//*[@id='APjFqb']").is_enabled())
driver.close()"""


#Example 2
driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
driver.maximize_window()
time.sleep(5)
print(driver.find_element(By.XPATH,"//*[@id='checkboxes']/input[1]").is_displayed())
print(driver.find_element(By.XPATH,"//*[@id='checkboxes']/input[1]").is_selected())
print(driver.find_element(By.XPATH,"//*[@id='checkboxes']/input[1]").is_enabled())


driver.find_element(By.XPATH,"//*[@id='checkboxes']/input[1]").click()
time.sleep(5)
print(driver.find_element(By.XPATH,"//*[@id='checkboxes']/input[1]").is_selected())
driver.close()
