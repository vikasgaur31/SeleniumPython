from selenium import webdriver

driver = webdriver.Firefox()

#Get the now of rows and columns of text box
print("Get the now of rows and columns of text box")
print("============================================")
URL = "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_textarea"
driver.get(URL)
box = driver.find_element_by_tag_name('textarea')
box_text = box.get_attribute('value')
box_no_of_row = box.get_attribute('rows')
box_no_of_col = box.get_attribute('cols')
print(box_text)
print(box_no_of_row)
print(box_no_of_col)

#Get the title value of element
print("Get the title value of element")
print("============================================")
URL = "https://www.w3schools.com/"
driver.get(URL)
title_name = driver.find_element_by_xpath('/html/body/div[5]/div/a[2]')
title_value_translate = title_name.get_attribute('title')
print(title_value_translate)

title_name = driver.find_element_by_xpath('/html/body/div[5]/div/a[1]')
title_search_value = title_name.get_attribute('title')
print(title_search_value)
driver.quit()