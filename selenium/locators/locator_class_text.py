from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Example 1
driver=webdriver.Chrome()
location_file="C://Users//Satish//PycharmProjects//Python2025//.venv//python//selenium//locators//class.html"
driver.get(location_file)
driver.maximize_window()
print(driver.find_element(By.CLASS_NAME,"content").text)
time.sleep(5)
driver.close()




"""#Example 2
driver=webdriver.Chrome()
location_file="https://www.nykaa.com/"
driver.get(location_file)
driver.maximize_window()
print(driver.find_element(By.CLASS_NAME,"css-1gzc5zn").text)
time.sleep(5)
driver.close()"""
