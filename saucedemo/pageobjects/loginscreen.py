from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from values import strings
import allure
import string
import random


class LogInScreen:

    def __init__(self, driver):
        self.driver = driver
        self.title = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "Swag Labs")))
        self.user_name_field = self.user_comment = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//input[@data-test = 'username']")))
        self.password_field = self.user_comment = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//input[@data-test = 'password']")))
        self.login_btn = self.user_comment = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//input[@class = 'login-button']")))

    def log_in_error_msg(self):
        self.log_in_error_msg = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//h3[contains(text(), 'Username and password do not match any user in this service')]")))

    @allure.step('Log in with proper creds')
    def log_in_proper_creds(self):
        self.user_name_field.send_keys(strings.user_name)
        self.password_field.send_keys(strings.password)
        self.login_btn.click()

    @allure.step('Log in with improper user name')
    def log_in_improper_user_name(self):
        self.user_name_field.send_keys(''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(6, 15))))
        self.password_field.send_keys(strings.password)
        self.login_btn.click()
        self.error_msg = log_in_error_msg() #not sure why this doesn't work





    @allure.step('Log in with improper password')
    def log_in_improper_user_name(self):
        self.user_name_field.send_keys(strings.user_name)
        self.password_field.send_keys(''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(6, 15))))
        self.login_btn.click()