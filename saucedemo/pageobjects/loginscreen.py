from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.basepage import BasePage
from values import strings
import allure
import string
import random


class LogInScreen(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.title = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.TAG_NAME, "title")))
        self.user_name_field = self.user_comment = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//input[@data-test = 'username']")))
        self.password_field = self.user_comment = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//input[@data-test = 'password']")))
        self.login_btn = self.user_comment = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//input[@class = 'login-button']")))

    def log_in_error_msg(self):
        return WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//h3[@data-test='error']")))
        # self.error_msg_txt = self.log_in_error_msg.gettext()
        # print(self.error_msg_txt)

    @allure.step('Log in with proper creds')
    def log_in_proper_creds(self):
        self.user_name_field.send_keys(strings.user_name)
        self.password_field.send_keys(strings.password)
        self.login_btn.click()



    @allure.step('Log in with improper user name')
    def log_in_improper_user_name(self):
        self.user_name_field.send_keys(''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(6, 15))))
        print('before pw')
        self.password_field.send_keys(strings.password)
        print('before click')
        self.login_btn.click()
        print('after click')
        error_msg = self.log_in_error_msg() #does this work?!?
        print('found error msg')
        error_msg_text = error_msg.text
        print('this is the text it\'s grabbing' + error_msg_text) #sanity
        assert error_msg.is_displayed()





    @allure.step('Log in with improper password')
    def log_in_improper_password(self):
        self.user_name_field.send_keys(strings.user_name)
        self.password_field.send_keys(''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(6, 15))))
        self.login_btn.click()