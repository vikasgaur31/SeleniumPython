from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Browsers_Selenium\\Chrome\\ChromeDriver.exe")
driver.maximize_window()
#Save website URL in variable
URL = "http://corporate.walmart.com"
#Navigate to the URL
driver.get(URL)

def assert_url_contain_text(expected_text):
    current_url = driver.current_url

    if expected_text not in current_url:
        raise AssertionError("The text '%s' is not in the url. The current url is:'%s'", current_url)
    else:
        print('The text is present in the url')

def get_url_link(element):
    tag_type = element.tag_name
    if tag_type != 'a':
        print('The element is not a link')
        child_element = element.find_element_by_tag_name('a')

        num_of_links = len(child_element)

        if num_of_links == 0:
            raise Exception ('The element is not a link')
        elif num_of_links >1:
            raise Exception('There are multiple element. Please provide specific element')
        else:
            link_url = child_element[0].get_attribute('href')
    else:
        link_url = element.get_attribute('href')
    return link_url

#calling assert_url_contain_text
assert_url_contain_text('corporate')

#xpath list
career_link_xpath = "//*[@href='http://careers.walmart.com']"
contactus_link_xpath = "//*[@href='https://corporate.walmart.com/contact-us']"

#calling get_url_link
url_text = driver.find_element_by_xpath(contactus_link_xpath)
url_link = get_url_link(url_text)
print(url_link)