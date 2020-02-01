from selenium import webdriver
from selenium import webdriver as driver

browser = driver.Chrome("C:\\Browsers_Selenium\\Chrome\\ChromeDriver.exe")
browser.maximize_window()
browser.get("http://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
browser.find_element_by_xpath("/html/body/button").click()

def is_alert_present():
    try:
        alert_obj = driver.switch_to.alert()
        # Retrieve the message on the Alert window
        message = alert_obj.text
        print("Alert shows following message: " + message)
        return True
    except:
        return False
        print("Alert not available", message)

def assert_alert_present():
    if not is_alert_present():
        raise AssertionError('There is no alert present')

