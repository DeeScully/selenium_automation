from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure



class SideBar:
    def __init__(self, driver):
        self.driver = driver
        self.search_bar = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-field')))
        self.search_submit = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'search-submit')))
        self.user_comment = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//li[@class='recentcomments'][1]")))
        self.archive_link = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//section[@id='archives-2']//li[1]/a")))
        self.category_link = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//section[@id='categories-2']//li[1]/a")))

    @allure.step('Search for article')
    def search_for_article(self, article_title):
        self.search_bar.send_keys(article_title)
        self.search_submit.click()

    @allure.step('Click user comment')
    def click_user_comment(self):
        self.user_comment.click()

    @allure.step('Click archive')
    def click_archive(self):
        self.archive_link.click()

    @allure.step('Click cagagory')
    def click_category(self):
        self.category_link.click()

