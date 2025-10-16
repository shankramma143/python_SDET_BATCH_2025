# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# time.sleep(5)
#
# source=driver.find_element(By.ID,"draggable")
# target=driver.find_element(By.ID,"droppable")
#
# act=ActionChains(driver)
# act.drag_and_drop(source,target).perform()
# time.sleep(5)
# driver.close()


#Example 4 : Slider
# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://jqueryui.com/slider/")
# driver.maximize_window()
# driver.implicitly_wait(10)
#
#
# driver.switch_to.frame(0)
# min_slider=driver.find_element(By.XPATH,"//div[@id='slider']/span")
# print(min_slider.location)
#
#
# act=ActionChains(driver)
# act.drag_and_drop_by_offset(min_slider,200,200).perform()
# time.sleep(5)
# print(min_slider.location)
# driver.close()


#Scrolling the Page

#Example 1 ==> Scroll by pixel
# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://jqueryui.com/slider/")
# driver.maximize_window()
# driver.implicitly_wait(10)
#
#
# value=driver.execute_script("return window.pageYOffset;")
# print("The scroll pixel initial value =",value)
#
#
# #Scroll down the page by pixel
# driver.execute_script("window.scrollBy(0,500)","")
# time.sleep(5)
#
#
# value=driver.execute_script("return window.pageYOffset;")
# print("The Number of Pixel Moved =",value)
# time.sleep(5)
#
#
# driver.close()



#Scrolling the Page doubt
#Example 2 ==> Scroll till the element is visible
# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# driver.implicitly_wait()
#
#
# driver.switch_to.frame("frame-one796456169")
# submit_button=driver.find_element(By.XPATH,"//input[@name='Submit']")

# driver.execute_script("arguments[0].scrollIntoView();",submit_button)
# time.sleep(5)

# value=driver.execute_script("return window.pageYOffset;")
# print("The Number of Pixel Moved =",value)
# driver.refresh()
# time.sleep(5)

# #Scroll till end of the page
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# value=driver.execute_script("return window.pageYOffset;")
# print("The Number of Pixel Moved =",value)
# time.sleep(5)

#Scroll to the Starting Position
# driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
# value=driver.execute_script("return window.pageYOffset;")
# print("The Number of Pixel Moved =",value)
# time.sleep(5)
# driver.close()

#How to Handle Bootstrap Dropdown :
# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
# driver.maximize_window()
# driver.implicitly_wait(10)
#
#
# driver.find_element(By.ID,"select2-billing_country-container").click()
# time.sleep(5)
#
#
# countries=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
# print(len(countries))
#
#
# for country in countries:
#    if country.text=='India':
#        print(country.text)
#        country.click()
#        break
#
#
# time.sleep(5)
#
#
# driver.close()


#How to Handle Bootstrap Dropdown :


#
#
#
# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
# driver.maximize_window()
# driver.implicitly_wait(10)
#
#
# driver.find_element(By.ID,"select2-billing_country-container").click()
# time.sleep(5)
#
#
# countries=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
# print(len(countries))
#
#
# for country in countries:
#    if country.text=='India':
#        print(country.text)
#        country.click()
#        break
#
#
# time.sleep(5)
#
#
# driver.close()



