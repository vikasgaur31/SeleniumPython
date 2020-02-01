from selenium import webdriver



driver = webdriver.Chrome("C:\\Browsers_Selenium\\Chrome\\ChromeDriver.exe")
driver.maximize_window()
#Save website URL in variable
URL = "http://corporate.walmart.com"
#Navigate to the URL
driver.get(URL)

