#1)refresh
#2)backward
#3)forward

"""from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.firstcry.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//span[text()='Track Order']").click()
driver.refresh()
driver.back()
driver.forward()
driver.close()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.firstcry.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Track Order']").click()
time.sleep(10)
driver.refresh()
time.sleep(5)
driver.back()
time.sleep(10)
driver.forward()
time.sleep(5)
driver.close()"""


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/r.php")
driver.maximize_window()
time.sleep(5)
x=driver.find_element(By.XPATH,"//div[text()='First name']")
print(x.text)
print(x.get_attribute("class"))
print(x.get_attribute("aria-hidden"))
print(x.get_attribute("id"))
print(x.get_attribute("type"))
print("********")
driver.close()



