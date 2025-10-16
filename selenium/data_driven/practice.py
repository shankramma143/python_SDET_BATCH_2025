import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.Utilities import XLUtil

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
driver=webdriver.Chrome(options=ops)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
time.sleep(5)


#elements
Principal_ele=driver.find_element(By.NAME, "principal")
Rate_Interest_ele=driver.find_element(By.ID,"interest")
Period_ele=driver.find_element(By.NAME,"tenure")

#find drop_down element
Type_of_Period_ele_drop_down=Select(driver.find_element(By.ID,"tenurePeriod"))
#Type_of_Period_ele_drop_down.Select_by_visible_text("year(s)")

#find drop_down element
Frequency_ele_drop_down=Select(driver.find_element(By.ID,"frequency"))
#Frequency_ele_drop_down.select_by_value("0")

Calculate_ele=driver.find_element(By.XPATH,"//div[@class='CTR PT15']/a[1]/img")
Clear_ele=driver.find_element(By.XPATH,"//div[@class='CTR PT15']/a[2]/img")
Actual_Maturity_value=driver.find_element(By.XPATH,"//span[@class='gL_27']/strong")

Expected_maturity_value="112000.00"

#sending values
Principal_ele.send_keys("100000")
Rate_Interest_ele.send_keys("12")
Period_ele.send_keys("1")
Type_of_Period_ele_drop_down.select_by_visible_text("year(s)")
Frequency_ele_drop_down.select_by_value("0")
Calculate_ele.click()
time.sleep(5)
Actual_maturity_value=driver.find_element(By.XPATH,"//span[@class='gL_27']/strong").text
print(Actual_maturity_value)
time.sleep(5)
if Expected_maturity_value==Actual_maturity_value:
    print("test pass")
else:
    print("test fail")
driver.close()



