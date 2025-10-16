#title ===>
#current_url
#page source
#get method

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.nykaa.com/") #To open an application get method is used
print(driver.title)  #To get the title of the page
print("*****************************")
print(driver.current_url) #To get the current URL
print("*****************************")
print(driver.page_source)
time.sleep(5)
driver.close()
