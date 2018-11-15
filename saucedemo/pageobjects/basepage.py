from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:

    @allure.step('Validate hamburger present')
    def validate_hamburger_present(self):
        hamburger = WebDriverWait(self.driver.instance, 10).until(EC.visibility_of_element_located((By.XPATH, ".//button[contains(text(), 'Open Menu')]")))
        assert hamburger.is_displayed()
    #