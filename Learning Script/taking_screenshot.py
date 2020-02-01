from selenium import webdriver

driver = webdriver.Chrome("C:\\Browsers_Selenium\\Chrome\\ChromeDriver.exe")
driver.maximize_window()
#Save website URL in variable
URL = "http://seleniumhq.org"
#Navigate to the URL
driver.get(URL)

#screenshot for whole webpage
driver.get_screenshot_as_file('screenshot_demo1.jpg')

