from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# #Example 1 using ID
# driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,"#user-name").send_keys("Hello Good Morning")
# time.sleep(5)
# driver.close()

# #Example 2 using class
# driver=webdriver.Chrome()
# driver.get("https://mamaearth.in")
# driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,".link-color").click()
# time.sleep(5)
# driver.close()


# # Example 3 using attribute
# driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,"input[name='user-name']").send_keys("Hello Good Morning")
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,"input[class='input_error form_input'][name='user-name']").clear()
# time.sleep(5)
# driver.close()

# #Example 4 find next sibling using of nth type
driver=webdriver.Chrome()
driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
driver.maximize_window()
print(driver.find_element(By.CSS_SELECTOR,"#Recordlist li:nth-of-type(3)+li").text)
time.sleep(5)
driver.close()
#
#
# #Example 5 using Prefixes / Partial Attribute Match
# #driver.find_element(By.CSS_SELECTOR, "input[placeholder*='Last']")  # Contains 'Last'
# #driver.find_element(By.CSS_SELECTOR, "input[placeholder^='Enter']")  # Starts with 'Enter'
# #driver.find_element(By.CSS_SELECTOR, "input[placeholder$='Name']")   # Ends with 'Name'
#
#
# #Example 6 using By Parent > Child (Employee Name text field)
# #driver.find_element(By.CSS_SELECTOR, "#content >div input[name='emp_name']")
#
#
# #Example 7 By Descendant (any level)
# driver.find_element(By.CSS_SELECTOR, "form input")  # Any input inside form"""
#
# #Day 6:  11/09/2025
#
# #Example 8
# #First Child :
# driver=webdriver.Chrome()
# driver.get("https://device.pcloudy.com/signup")
# driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,".iti__selected-flag").click()
# time.sleep(5)
# print(driver.find_element(By.CSS_SELECTOR,"#iti-0__country-listbox >li:first-child").text)
# time.sleep(5)
# driver.close()
#
#
# #Example 9
# #Last Child :
# driver=webdriver.Chrome()
# driver.get("https://device.pcloudy.com/signup")
# driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,".iti__selected-flag").click()
# time.sleep(5)
# print(driver.find_element(By.CSS_SELECTOR,"#iti-0__country-listbox >li:last-child").text)
# time.sleep(5)
# driver.close()




