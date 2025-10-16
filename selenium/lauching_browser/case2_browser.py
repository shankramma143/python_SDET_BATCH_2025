"""#Chrome Browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver=webdriver.Chrome()
driver.get("https://qacircle.com/")
print(driver.title)
driver.close()


#Mozilla Firefox Browser
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
driver=webdriver.Firefox()
driver.get("https://qacircle.com/")
driver.maximize_window()
print(driver.title)
driver.close()"""


#Microsoft Edge Browser
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
driver=webdriver.Edge()
driver.get("https://qacircle.com/")
driver.maximize_window()
time.sleep(5)
expected_title="QACircle Software Training Academy"
actual_title=driver.title
if expected_title==actual_title:
   print("Test Pass")
else:
   print("Test Fail")
driver.close()