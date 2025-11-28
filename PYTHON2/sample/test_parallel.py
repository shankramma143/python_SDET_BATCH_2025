# Case 1:
# Step 1:  pip install pytest-xdist package for invoking multiple browser
# Step 2: Create test_parallel.py
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
#You can write with class or only test method also can write
#if i write any test method inside class i should pass self as first parameter as default.
class TestLogin:
   def test_login_chrome(self):
       self.driver=webdriver.Chrome()
       #This driver belongs to this method
       self.driver.get("https://www.saucedemo.com/")
       self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
       self.driver.find_element(By.ID,"password").send_keys("secret_sauce")
       self.driver.find_element(By.ID,"login-button").click()
       assert self.driver.title=="Swag Labs"
       self.driver.quit()


   def test_login_edge(self):
       self.driver=webdriver.Edge()
       #This driver belongs to this method
       self.driver.get("https://www.saucedemo.com/")
       self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
       self.driver.find_element(By.ID,"password").send_keys("secret_sauce")
       self.driver.find_element(By.ID,"login-button").click()
       assert self.driver.title=="Swag Labs"
       self.driver.quit()


   def test_login_firefox(self):
       self.driver=webdriver.Firefox()
       #This driver belongs to this method
       self.driver.get("https://www.saucedemo.com/")
       self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
       self.driver.find_element(By.ID,"password").send_keys("secret_sauce")
       self.driver.find_element(By.ID,"login-button").click()
       assert self.driver.title=="Swag Labs"
       self.driver.quit()