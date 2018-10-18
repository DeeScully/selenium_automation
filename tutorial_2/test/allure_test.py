import unittest
import pytest
import allure
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DemoAllure(unittest.TestCase):

    def test_site_loads(self):
        # with allure.step("Launch site"):
        #     driver = webdriver.Chrome()
        #     driver.get("http://qaboy.com/")
        # with allure.step("Verify Title loaded"):
        #     wait = WebDriverWait(driver, 5)
        #     wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "site-title")))

        #decorator way
        self.launch_site()
        self.verify_site()

    @allure.step("Launch site")
    def launch_site(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://qaboy.com/")

    @allure.step("Verify Title loaded")
    def verify_site(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "site-title")))


if __name__ == '__main__':
    unittest.main()