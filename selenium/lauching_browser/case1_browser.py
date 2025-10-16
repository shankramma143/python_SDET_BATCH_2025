"""#Chrome Browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#chrome_service=Service("C://drivers//chromedriver.exe")
chrome_service=Service("C://drivers//chromedriver.exe")
driver=webdriver.Chrome(service=chrome_service)
driver.get("https://qacircle.com/")
print(driver.title)
driver.close()


#Mozilla Firefox Browser
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
firefox_service=Service("C://drivers//geckodriver.exe")
driver=webdriver.Firefox(service=firefox_service)
driver.get("https://qacircle.com/")
driver.maximize_window()
print(driver.title)
driver.close()"""

#Microsoft Edge Browser
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
edge_service=Service("C://drivers//msedgedriver.exe")
driver=webdriver.Edge(service=edge_service)
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

