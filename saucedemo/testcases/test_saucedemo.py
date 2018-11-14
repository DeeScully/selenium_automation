import unittest
from webdriver import Driver
from values import strings
from pageobjects.loginscreen import LogInScreen

class TestSauceDemo(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_log_in_screen(self):
        log_in_screen = LogInScreen(self.driver)
        log_in_screen.log_in_proper_creds()
        log_in_screen.log_in_improper_user_name()


    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()

