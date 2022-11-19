"""
Selenium-scraping Google Flights
Lisbon, Portugal - Nov 19, 2022
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# test inputs
site = "https://www.google.com/flights?hl=en"
source_city = "Ahmeda"
destination_city = "Mumbai"
departure_date = "2021-11-21" # YYYY-MM-DD
return_date = "2022-02-27"

# XPATH List of the UI elements
source_city_XPATH = '//*[@id="yDmH0d"]/'
dropdown_selection_XPATH = "//*[@id='i6']/div[6]/div[2]/div[2]/div[1]/div/input"
destination_XPATH = "//*[@id='i6']/div[4]/div/div/div[1]/div/div/input"
departure_date_XPATH = '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div/c-wiz/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input'
return_date_XPATH = '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div/c-wiz/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/div/input'
search_button_XPATH = '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div/c-wiz/div[2]/div[1]/div[2]/div/button'
calendar_date_XPATH = '//div[@data-iso = "{date}"]//div[@class="lkvzbb KQqAEc"]'
calendar_submit_button_XPATH = '//*[@id="ow59"]/div[2]/div/div[3]/div[3]/div/button'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get(site)  # Open Site in new chrome window

time.sleep(5)

 # source_city selection steps
fly_from = driver.find_element(By.XPATH, source_city_XPATH)
fly_from.click()
# fly_from_text = driver.find_element(By.XPATH, dropdown_selection_XPATH)
# fly_from_text.send_keys(source_city)
# fly_from_text.send_keys(Keys.ENTER)

# # destination_city selection steps
# fly_to = driver.find_element(By.XPATH, destination_XPATH)
# fly_to.click()
# fly_to_text = driver.find_element(By.XPATH, dropdown_selection_XPATH)
# fly_to_text.send_keys(destination_city)
# fly_to_text.send_keys(Keys.ENTER)

# # departure_date selection steps
# departure_date_element = driver.find_element(By.XPATH, departure_date_XPATH)
# departure_date_element.click()
# time.sleep(2)
# calendar_div = driver.find_element(By.XPATH, calendar_date_XPATH.format(date=departure_date))
# calendar_div.click() 

# # return_date selection steps
# return_date_calendar_div = driver.find_element(By.XPATH, calendar_date_XPATH.format(date=return_date))
# return_date_calendar_div.click()

# # click on the Done button in calendar picker
# submit_button = driver.find_element(By.XPATH, calendar_submit_button_XPATH)
# submit_button.click()
