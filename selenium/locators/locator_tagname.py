from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#
#
# #Example 1 (You will get empty string output because no text is associated to the element)
# driver=webdriver.Chrome()
# location_file="C://Users//Satish//PycharmProjects//Python2025//.venv//python//tagname11.html"
# driver.get(location_file)
# driver.maximize_window()
# print(driver.find_element(By.TAG_NAME,"h1"))
# time.sleep(5)
# driver.close()


#Example 2
driver=webdriver.Chrome()
driver.get("https://www.nykaa.com/")
driver.maximize_window()
l=driver.find_elements(By.TAG_NAME,"a")
print(len(l))
for i in l:
   print(i.text)
time.sleep(5)
driver.close()
