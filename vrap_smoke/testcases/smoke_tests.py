import unittest
import allure
import pageobjects.tflx.loginscreen
from webdriver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from values import strings


class TestAllApps(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        # self.driver.navigate(strings.base_url)

    @allure.step('tflx log in with proper creds')
    def test_tflx_login(self):
        screen = pageobjects.tflx.loginscreen.TflxLogInScrn(self.driver)
        screen.test_tflx_login()
        # self.driver.navigate(strings.tflx_p_url)
        # user_name_field = WebDriverWait(self.driver.instance, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, ".//input[@id='username']")))
        # password_field = WebDriverWait(self.driver.instance, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, ".//input[@id='password']")))
        # log_in_btn = WebDriverWait(self.driver.instance, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, ".//button[@id='loginButton']")))
        #
        # user_name_field.send_keys(strings.shared_un)
        # password_field.send_keys(strings.shared_pw)
        # log_in_btn.click()
        #
        # tflx_header = WebDriverWait(self.driver.instance, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, ".//div[@id='mainheadercontainer']")))
        # assert tflx_header.is_displayed()


    # @allure.step('tflx randomly select a category')
    # def test_tflx_select_cat(self):
    #




    def tearDown(self):
        self.driver.instance.quit()

"""to gen report run tests: py -m pytest ./testcases/smoke_tests.py --alluredir ./results
then allure serve ./results/
"""

if __name__ == '__main__':
    unittest.main()