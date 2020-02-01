from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Browsers_Selenium\\Chrome\\ChromeDriver.exe")
driver.maximize_window()
#Save website URL in variable
URL = "http://corporate.walmart.com"
#Navigate to the URL
driver.get(URL)




#Get the number window open in browser
def get_num_of_windows():
    window = driver.window_handles
    num_of_windows_opens = len(window)
    return num_of_windows_opens

#Switch to browser window as provided number index
def switch_to_window_number(index):
    try:
        index = int(index)
    except ValueError:
        raise Exception('The index number request is not a number. please pass the number as integer')

    total_win = get_num_of_windows()

    if index > total_win:
        raise Exception('The request index is more than the available window')

    all_windows = driver.window_handles
    requested_window = all_windows[index]
    driver.switch_to.window(requested_window)
    return

#Verify Current Title Browser Page
#def assert_currect_title(title_text):


#Test Multple Window activity if correct browser page is opening
def my_walmart_test():
    expected_second_window_title = 'Walmart Careers | Submit a Walmart Job Application Online'

    main_window_title = driver.title
    print('Main Window Title - ', main_window_title)
    driver.find_element_by_link_text("Careers").click()

    time.sleep(5)
    switch_to_window_number(1)
    new_window_title = driver.title

    if new_window_title != expected_second_window_title:
        print(new_window_title)
        print(expected_second_window_title)
        raise AssertionError(
            'The focus did not switch to the desired window, or the new tab is not the correct page opened')
    else:
        print('Verified successfully and correct webpage is opened - ', new_window_title)


#calling my_walmart_test method to start testing
my_walmart_test()