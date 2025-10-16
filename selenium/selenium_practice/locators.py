#1)BY ID
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.healthkart.com/sv/healthkart-hk-vitals-multivitamin-with-zinc-n-vitamin-c/SP-39873?navKey=VRNT-72769&itracker=w:menuLanding||;p:2|;e:72769|;")
# driver.maximize_window()
# driver.find_element(By.ID,"hk-header-wrapper")
# time.sleep(5)
# driver.close()

#
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.nykaa.com/")
# driver.maximize_window()
# driver.find_element(By.ID,"category").click()
# time.sleep(5)
# driver.close()

#
# #2)BY NAME
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
# driver.find_element(By.NAME,"user-name").click()
# time.sleep(5)
# name=driver.find_element(By.NAME,"user-name").send_keys("good morning")
# time.sleep(5)
# driver.close()

#3)tag name
#
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.google.com/")
# driver.maximize_window()
# driver.find_element(By.TAG_NAME,"a")
# time.sleep(5)
# driver.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.nykaa.com/")
# driver.maximize_window()
# l=driver.find_elements(By.TAG_NAME,"a")
# print(len(l))
# for i in l:
#    print(i.text)
# time.sleep(5)
# driver.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.healthkart.com/")
# driver.maximize_window()
# l=driver.find_elements(By.CLASS_NAME,"hk-app")
# print(len(l))
# for i in l:
#    print(i.text)
# time.sleep(5)
# driver.close()


#4)link_text


# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.healthkart.com/")
# driver.maximize_window()
# driver.find_element(By.LINK_TEXT,"fat burner supplements").click()
# time.sleep(5)
# driver.close()

#5)partial link text

# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.healthkart.com/")
# driver.maximize_window()
# driver.find_element(By.PARTIAL_LINK_TEXT,"fat burner").click()
# time.sleep(5)
# driver.close()

#6) class

# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.healthkart.com/")
# driver.maximize_window()
# l=driver.find_element(By.CLASS_NAME,"top-menu-link").click()
# time.sleep(5)
# driver.close()

#7)css selector
# #
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,"#user-name").click()
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,"#user-name").send_keys("standard_user")
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,"#password").click()
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,"#password").send_keys("secret_sauce")
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,"#user-name").clear()
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,"#password").clear()
# driver.close()


#Example 2 using class
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.nykaa.com/")
# driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,".css-37632m").click()
# time.sleep(5)
# driver.close()

#Example 3 using attribute
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,"input[name='user-name']").send_keys("Hello Good Morning")
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,"input[class='input_error form_input'][name='user-name']").clear()
# time.sleep(5)
# driver.close()

#Example 4 find next sibling using of nth type (doubt)
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.nykaa.com/")
# driver.maximize_window()
# print(driver.find_element(By.CSS_SELECTOR,".HeaderNav css-f7ogli li:nth-of-type(3)+li").text)
# time.sleep(5)
# driver.close()

# #Example 8
# #First Child :
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://device.pcloudy.com/signup")
# driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,".iti__selected-flag").click()
# time.sleep(5)
# print(driver.find_element(By.CSS_SELECTOR,"#iti-0__country-listbox >li:first-child").text)
# time.sleep(5)
# driver.close()

