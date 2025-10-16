from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#  #Example 1
# driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# time.sleep(5)
# driver.maximize_window()
# time.sleep(5)
# driver.find_element(By.ID,"user-name").send_keys("problem_user")
# time.sleep(5)
# driver.close()


#Example 2
driver=webdriver.Chrome()
driver.get("https://www.nykaa.com/")
time.sleep(5)
driver.maximize_window()
time.sleep(5)
print(driver.find_element(By.ID,"category").text)
time.sleep(5)
driver.close()


