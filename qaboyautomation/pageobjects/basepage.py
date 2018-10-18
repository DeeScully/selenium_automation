from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def validate_title_is_present(self):
        title = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'site-title')))
        assert title.is_displayed()

    def validate_icon_is_present(self):
        icon = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'custom-logo')))
        assert icon.is_displayed()

    def validate_menu_options_are_present(self):
        top_menu = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.ID, 'top-menu')))
        assert top_menu.is_displayed()

    def validate_social_media_links(self):
        twitter_button = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, './/span[contains(text(), "Twitter")]')))
        linkedin_button = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, './/span[contains(text(), "LinkedIn")]')))
        assert twitter_button.is_displayed()
        assert linkedin_button.is_displayed()

    def click_about_me_link(self):
        about_me_link = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "ABOUT ME")))
        about_me_link.click()
