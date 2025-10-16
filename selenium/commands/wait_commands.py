#Example 1 doubt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
driver=webdriver.Chrome()
driver.get("https://www.google.com/")
driver.implicitly_wait(10)
driver.maximize_window()
search_box=driver.find_element(By.XPATH,"//textarea[@name='q']")
search_box.send_keys("selenium")
search_box.submit()
driver.find_element(By.XPATH,"//h3[@class='LC20lb MBeuO DKV0Md']").click()
driver.close()


#Example 2 doubt
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver=webdriver.Chrome()
# driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.find_element(By.ID,"dynamic_btn").click()
# time.sleep(5)
# driver.close()

#Example 1:
"""from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
driver.maximize_window()
try:
    wait=WebDriverWait(driver,10,3)
    dynamic_ele=wait.until(EC.element_to_be_clickable((By.ID,"dynamic_btn")))

except :
    dynamic_ele.click()

finally:
    driver.close()"""



# #example 2:
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.expected_conditions import *
# from selenium.common import *
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
# driver.maximize_window()
# try:
#    wait=WebDriverWait(driver,10,3,(NoSuchElementException,StaleElementReferenceException,ElementNotVisibleException,Exception))
#    dynamic_ele=wait.until(EC.element_to_be_clickable((By.ID,"send-sms")))
# except :
#    dynamic_ele.click()
# finally:
#    driver.close()

