from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Browsers_Selenium\\Chrome\\ChromeDriver.exe")
driver.maximize_window()
#Save website URL in variable
URL = "https://seleniumhq.github.io/selenium/docs/api/java/index.html"
#Navigate to the URL
driver.get(URL)

#Switch to First Frame
driver.switch_to.frame("packageListFrame")
textlink = driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(3)

driver.switch_to.default_content()

#Switch to Second Frame
driver.switch_to.frame("packageFrame")
driver.find_element_by_xpath("//*[@href='WebDriver.html']").click()
print("Switch to Second Frame link text")

driver.quit()