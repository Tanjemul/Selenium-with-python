from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("E:\\one drive\\OneDrive - Fintech Solutions\\Desktop\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.imdb.com/")
dropdown = driver.find_element_by_css_selector("#nav-search-form > div.SearchCategorySelector__StyledContainer-sc-18f40f7-0.fEgMct.search-category-selector > div > label > div")
dropdown.click()
time.sleep(1)
element = driver.find_element_by_link_text("Advanced Search")
element.click()
adv_title = driver.find_element_by_link_text("Advanced Title Search")
adv_title.click()
feature_film = driver.find_element_by_css_selector("#main > div:nth-child(4) > div.inputs > table > tbody > tr:nth-child(1) > td:nth-child(1) > label")
feature_film.click()
tv_movie = driver.find_element_by_css_selector("#main > div:nth-child(4) > div.inputs > table > tbody > tr:nth-child(1) > td:nth-child(2) > label")
tv_movie.click()

#movie years
#min

min_date = driver.find_element_by_css_selector("#main > div:nth-child(5) > div.inputs > input:nth-child(1)")
min_date.click()
min_date.send_keys("1900-01-12")

#max

max_date = driver.find_element_by_css_selector("#main > div:nth-child(5) > div.inputs > input:nth-child(2)")
max_date.click()
max_date.send_keys("2021-12-05")
 
#Select Rating

#min rating

min_rating = driver.find_element_by_css_selector("#main > div:nth-child(6) > div.inputs > select:nth-child(1)")
min_rating.click()
dropdown_min_rating = Select(min_rating)
dropdown_min_rating.select_by_visible_text("1.0")

#max Rating

max_rating = driver.find_element_by_css_selector("#main > div:nth-child(6) > div.inputs > select:nth-child(2)")
min_rating.click()
dropdown_max_rating = Select(max_rating)
dropdown_max_rating.select_by_visible_text("10")

#Language selection

language = driver.find_element_by_name("languages")
dropdown_language = Select(language)
dropdown_language.select_by_visible_text("English")

#Per page

per_page = driver.find_element_by_name("count")
#per_page.click()
dropdown_per_page = Select(per_page)
dropdown_per_page.select_by_visible_text("250 per page")


#Search

search = driver.find_element_by_css_selector("#main > p:nth-child(28) > button")
search.click()

