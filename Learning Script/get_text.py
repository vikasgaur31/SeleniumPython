from selenium import webdriver

driver = webdriver.Firefox()

#Save website URL in variable
URL = "http://www.w3schools.com"

#Navigate to the URL
driver.get(URL)

#Get the list text of the block
left_nav_list = driver.find_element_by_class_name("w3-bar-block")
left_nav_text = left_nav_list.text
print("=====================")
print(left_nav_text)
print("=====================")

#Get the text on Header
header_text = driver.find_element_by_xpath("//*[@id='main']/div[1]/div[2]/div/h3")
header_top_text = header_text.text

print("=====================")
print(header_top_text)
print("=====================")


#Get the text on Block Header Text
HTML_block_header_text = driver.find_element_by_xpath("//*[@id='main']/div[1]/div[2]/div/h3")
HTML_block_text = HTML_block_header_text.text

print("=====================")
print(HTML_block_text)
print("=====================")

#Get the text on Block
HTML_block_header_block = driver.find_element_by_xpath("//*[@id='main']/div[1]/div[2]/div/div")
HTML_block_header_block_text = HTML_block_header_block.text

print("=====================")
print(HTML_block_header_block_text)
print("=====================")

#Get the text on table Text
driver.get("https://www.w3schools.com/tags/tag_table.asp")
HTML_Table = driver.find_element_by_xpath("//*[@id='main']/table[2]/tbody/tr[1]/th[1]")
#HTML_Table = driver.find_element_by_xpath("//*[@id='main']/table[2]")
HTML_Table_Text = HTML_Table.text

print("=====================")
print(HTML_Table_Text)
print("=====================")




driver.quit()