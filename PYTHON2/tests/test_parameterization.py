#Case 1 ⇒ test_parameterization.py
import pytest


@pytest.mark.parametrize("username ,password",[("QACirlce","Q@123"),("Training","QA@123"),("Academy","QAC@123")])
def test_sample(username,password):
   print(username,"====",password)

#Case 2 ⇒ test_parameterization.py
import pytest
class TestClass:
   @pytest.mark.parametrize('num1,num2',[(1,1),(3,5),(10,10),(5,10)])
   def test_calculation(self,num1,num2):
       assert num1==num2



#Case 3 Without using any looping Statements we can run multiple test data


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#need to pass parameters
class TestClass:
   @pytest.mark.parametrize('username,password',[("standard_user","secret_sauce"),("locked_out_user","secret_sauce"),("problem_user","secret_sauce"),("error_user","secret_sauce")])
   def test_swaglabs(self,username,password):
       self.driver = webdriver.Chrome()
       self.driver.get("https://www.saucedemo.com/")
       self.driver.find_element(By.ID, "user-name").send_keys(username)
       self.driver.find_element(By.ID, "password").send_keys(password)
       time.sleep(5)
       self.driver.find_element(By.ID, "login-button").click()
       time.sleep(5)
       try:
           self.status=self.driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").is_displayed()
           self.driver.close()
           assert self.status==True


       except:
           self.driver.close()
           assert self.status == False



