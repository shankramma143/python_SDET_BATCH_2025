"""#Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://qacircle.com/")
print(driver.title)
driver.close()


#Firefox
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://qacircle.com/")
expected_title="QACircle Software Training Academy"
actual_title=driver.title
if expected_title==actual_title:
   print("Test Pass")
else:
   print("Test Fail")
driver.close()"""


#Edge
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get("https://google.com/")
expected_title="QACircle Software training Academy"
actual_title=driver.title
if expected_title==actual_title:
   print("Test Pass")
   print(driver.title)
else:
   print("Test Fail")
   print(driver.title)
driver.close()


#Edge
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get("https://google.com/")
expected_title="QACircle Software Training Academy"
actual_title=driver.title
if expected_title==actual_title:
   print("Test Pass")
   print(driver.title)
else:
   print("Test Fail")
   print(driver.title)
driver.close()

