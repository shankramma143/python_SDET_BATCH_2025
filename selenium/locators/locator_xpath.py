#Absolute Xpath
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://qacircle.com/")
text=driver.find_element(By.XPATH,"/html/body/nav/div[2]/div/div[3]/ul/li[3]/a").text
print(text)
time.sleep(5)
driver.close()

#Relative Xpath
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.nykaa.com/")
text=driver.find_element(By.XPATH,"//button[@class='css-1gzc5zn']").text
print(text)
time.sleep(5)
driver.close()
