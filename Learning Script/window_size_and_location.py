from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Browsers_Selenium\\Chrome\\ChromeDriver.exe")
driver.maximize_window()
#Save website URL in variable
URL = "http://corporate.walmart.com"
#Navigate to the URL
driver.get(URL)

time.sleep(3)
driver.set_window_size(width=500, height=800)

time.sleep(3)
driver.set_window_size(width=800, height=500)

time.sleep(3)
driver.set_window_size(width=400, height=400)

time.sleep(3)
print(driver.get_window_position())

time.sleep(3)
driver.maximize_window()

driver.quit()