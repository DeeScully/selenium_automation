from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure



class SideBar:
    def __init__(self, driver):
        self.driver = driver
        self.search_bar = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-field')))
        self.submit = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'search-submit')))

    @allure.step('Search_for_article')
    def search_for_article(self, article_title):
        self.search_bar.send_keys(article_title)
        self.submit.click()

