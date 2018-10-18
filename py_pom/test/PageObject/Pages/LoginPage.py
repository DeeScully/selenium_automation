
from py_pom.test.PageObject.Locators import Locator
from selenium.webdriver.support.select import select
from selenium.webdriver.common.by import By
from selenium import webdriver


class Login():

    def __init__(self, driver):
        self.driver = driver

        #define LoginPage Locators
        self.title = driver.find_element(By.XPATH, Locator.title)
        self.log_in_email = driver.find_element(By.XPATH, Locator.log_in_email)
        self.log_in_pw = driver.find_element(By.XPATH, Locator.log_in_pw)
        self.log_in_button = driver.find_element(By.XPATH, Locator.log_in_button)


    def get_Title(self):
        return self.title

    def get_Log_In_Email(self):
        return self.log_in_email

    def get_Log_In_Pw(self):
        return self.log_in_pw

    def get_Log_In_Button(self):
        return self.log_in_button
