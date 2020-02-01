from selenium import webdriver
import os

driver = webdriver.Firefox()

url = 'https://www.w3schools.com/'
driver.get(url)

left_nav = driver.find_element_by_class_name('w3-bar-block')
print(left_nav.text)


'''driver.find_element("xpath", "//a[contains(text(),'Gmail')]").click()
print("Gmail page opens")
print("website open and closed in Firefox Browser")
driver.quit()
'''
#dir = os.path.dirname("C:\Browsers Selenium\chromedriver_win32")
#chrome_driver_path = dir + "\chromedriver.exe"

#ChromeDriverPath = "C:/Browsers_Selenium/chromedriver_win32/chromedriver.exe"

'''driver = webdriver.Chrome()
driver.get('http://www.bizyug.com')
print("website open and closed in Chrome Browser")
driver.quit()'''