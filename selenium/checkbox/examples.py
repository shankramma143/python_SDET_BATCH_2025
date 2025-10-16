# #How to handle single checkbox
# import time
# from selenium import webdriver
#
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# single_checkbox=driver.find_element(By.ID,"monday")
# print(single_checkbox.is_enabled())
# print(single_checkbox.is_displayed())
# print(single_checkbox.is_selected())
# time.sleep(5)
# single_checkbox.click()
# print(single_checkbox.is_selected())
# time.sleep(5)
# driver.close()

#ex:2
# import time
# from selenium import webdriver
#
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
# driver.maximize_window()
# single_checkbox=driver.find_element(By.XPATH,"//input[@value='project-1']")
# print(single_checkbox.is_enabled())
# print(single_checkbox.is_displayed())
# print(single_checkbox.is_selected())
# time.sleep(5)
# single_checkbox.click()
# print(single_checkbox.is_selected())
# time.sleep(5)
# driver.close()


# #How to select multiple checkbox
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# multiple_checkboxs=driver.find_elements(By.XPATH,"//input[@class='form-check-input' and @type='checkbox']")
# print("Click on all the checkboxes")
# for check in multiple_checkboxs:
#     check.click()
# time.sleep(5)
# driver.close()

#ex:2   doubt
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
# driver.maximize_window()
# multiple_checkboxs=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
# print("Click on all the checkboxes")
# for check in multiple_checkboxs:
#     check.click()
# time.sleep(10)
# driver.close()


#How to select particular checkbox
#only Monday and Saturday
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# multiple_checkboxs=driver.find_elements(By.XPATH,"//input[@class='form-check-input' and @type='checkbox']")
# for checkbox in multiple_checkboxs:
#     day=checkbox.get_attribute('id')
#     if day=='monday' or day=='saturday':
                                                                        #         checkbox.click()
# time.sleep(5)
# driver.close()

#ex:2
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
# driver.maximize_window()
# multiple_checkboxs=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
# for checkbox in multiple_checkboxs:
#     day=checkbox.get_attribute('id')
#     if day=='project-1' or day=='project-4':
#         checkbox.click()
# time.sleep(5)
# driver.close()

#I want to select first 2 check boxes using range() function
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service ix  mport Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# multiple_checkboxs=driver.find_elements(By.XPATH,"//input[@class='form-check-input' and @type='checkbox']")
# print(multiple_checkboxs)
# print(len(multiple_checkboxs))
# for i in range(len(multiple_checkboxs)):
#     if i <2 :
#         multiple_checkboxs[i].click()
# time.sleep(5)
# driver.close()


#ex:2
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
# driver.maximize_window()
# multiple_checkboxs=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
# print(multiple_checkboxs)
# print(len(multiple_checkboxs))
# for i in range(len(multiple_checkboxs)):
#     if i <2 :
#         multiple_checkboxs[i].click()
# time.sleep(5)
# driver.close()


# #I want to select last 2 checkboxes using range() function
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# multiple_checkboxs=driver.find_elements(By.XPATH,"//input[@class='form-check-input' and @type='checkbox']")
# print(multiple_checkboxs)
# print(len(multiple_checkboxs))
# for i in range(len(multiple_checkboxs)-2,len(multiple_checkboxs)):
#        multiple_checkboxs[i].click()
# time.sleep(5)
# driver.close()


# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://tech-training-qacircle.github.io/locator-practice/src/locatorPractice.html")
# driver.maximize_window()
# multiple_checkboxs=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
# print(multiple_checkboxs)
# print(len(multiple_checkboxs))
# for i in range(len(multiple_checkboxs)-2,len(multiple_checkboxs)):
#         multiple_checkboxs[i].click()
# time.sleep(5)
# driver.close()