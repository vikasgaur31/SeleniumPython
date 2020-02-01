from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
URL = "http://www.google.com"
driver.get(URL)
search_box = driver.find_element('xpath', '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
search_box.send_keys('bizyug')
search_box.send_keys(Keys.DOWN)
search_box.send_keys(Keys.DOWN)
search_btn = driver.find_element('xpath', '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
search_btn.click()
