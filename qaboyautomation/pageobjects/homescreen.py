from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from values import strings
from pageobjects.basepage import BasePage

class HomeScreen(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.post_list = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'article')))

    def validate_posts_are_visible(self):
        assert len(self.post_list) > 0


