from selenium import webdriver
driver = webdriver.Firefox()

#Get the now of rows and columns of text box
print("Get the now of rows and columns of text box")
URL = "https://www.w3schools.com/html/html_tables.asp"

driver.get(URL)
#box = driver.find_element_by_tag_name('textarea')


def get_number_of_table_rows(my_table):
    all_rows = my_table.find_elements_by_tag_name('tr')
    number_of_rows = len(all_rows)
    return number_of_rows

def assert_number_of_rows_in_table(my_table, expected_num_of_rows):
    actual_num_rows = get_number_of_table_rows(my_table)

    if expected_num_of_rows != actual_num_rows:
        raise AssertionError("The number of row did not match.")
    return


