# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
# time.sleep(5)
# driver.find_element(By.ID,"user-name").send_keys("standard_user")
# time.sleep(5)
# driver.find_element(By.NAME,"password").send_keys("secret_sauce")
# time.sleep(5)
# driver.find_element(By.NAME,"login-button").click()
# time.sleep(5)
# driver.close()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.nykaa.com/")
driver.maximize_window()
time.sleep(5)
# driver.find_element(By.CLASS_NAME,"css-1mavm7h").text
# time.sleep(5)
# driver.find_element(By.CLASS_NAME,"css-1mavm7h").click()
# time.sleep(5)

l=driver.find_element(By.TAG_NAME,"a").text
print(len(l))

print("*****************")
for i in l:
    print(i.text)
time.sleep(5)

driver.close()