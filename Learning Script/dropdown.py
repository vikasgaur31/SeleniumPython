from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium import webdriver as driver
from selenium.webdriver.common.by import By

browser = driver.Chrome("C:\\Browsers_Selenium\\Chrome\\ChromeDriver.exe")
browser.maximize_window()
browser.get("http://www.amazon.in")

#Function for Select dropdown value by visible text
def select_dropdown_by_visible_text(element, select_text):
    assert_element_is_dropdown(element)
    all_options = element.find_elements_by_tag_name('option')
    for option in all_options:
        #all_options_dropdown_value = Select(all_options)
        #option_text = all_options_dropdown_value.select_by_visible_text(select_text)
        option_text = option.text
        print(option_text)
        option_found = False
        if option_text == select_text:
            #driver.implicitly_wait(10000)
            option.click()
            option_found = True
            break

    if not option_found:
        raise ('The requested value was not found in the dropdown')
    return

#Function for select dropdown value by value
def select_dropdown_by_value(element, select_value):
    assert_element_is_dropdown(element)
    all_options = element.find_elements_by_tag_name('value')
    for option in all_options:
        option_text = option.get_attribute('value')
        option_found = False
        if option_text == select_value:
            option.click()
            option_found = True
            break

    if not option_found:
        raise ('The requested value was not found in the dropdown')
    return

#function for wether element is dropdown or not
def assert_element_is_dropdown(element):
    if element.get_attribute('type') not in ['select-one', 'select-multi']:
        raise AssertionError('This is not a dropdown')
    return

my_dropdown = browser.find_element_by_xpath("//*[@id='searchDropdownBox']")
print("my_dropdown - ", my_dropdown)

#select_dropdown_by_visible_text(my_dropdown,'Books')
select_dropdown_by_value(my_dropdown,'Baby')