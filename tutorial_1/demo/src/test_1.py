from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('https://www.yahoo.com')

driver.find_element_by_xpath('.//input[@id="uh-search-box"]').send_keys('danika mori')
driver.find_element_by_xpath('.//button[@id="uh-search-button"]').click()
sleep(5)
driver.close()

