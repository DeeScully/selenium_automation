from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from values import strings
import allure
import string
import random


class TflxLogInScrn:

    def __init__(self, driver):
        self.driver = driver
        self.user_name_field = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//input[@id='username']")))
        self.password_field = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//input[@id='password']")))
        self.log_in_btn = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//button[@id='loginButton']")))


