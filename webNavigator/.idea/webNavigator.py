from selenium import webdriver

isbn_list = ['978-1-4503-5589-6']
article_titles = ['A Cross-Cultural Analysis of Trust in Recommender Systems']

# Use chrome to access the web
driver = webdriver.Chrome(executable_path = "C:\\bin\\chromedriver.exe")

# Open the website
driver.get("https://dl.acm.org/advsearch.cfm?coll=DL&dl=ACM")

# select the 'Where' drop down and click it
criteria_1 = driver.find_element_by_id("fld0")
criteria_1.click()

# select the 'Title' option and click it
title_option = driver.find_element_by_css_selector('[value = "acmdlTitle:"]')
title_option.click()

# find the entry field for the first search criteria and enter
title_box = driver.find_element_by_id("val0")
title_box.send_keys(article_titles[0])

# find the 'add criteria' button and click it
add_crit = driver.find_element_by_id("add0")
add_crit.click()

driver.implicitly_wait(2)

# find criteria 2 drop down and click it
criteria_2 = driver.find_element_by_id("fld1")
criteria_2.click()

# find and select the isbn/issn option
isbn_option = driver.find_element_by_css_selector('[value = "isbnissn.isbnissn:"]')
isbn_option.click()


# find the input field for criteria 2
isbn_box = driver.find_element_by_id("val1")
isbn_box.send_keys(isbn_list[0])

# find the search button and click it
search_btn = driver.find_element_by_css_selector('[src = "/images/search_small.jpg"')
search_btn.click()




