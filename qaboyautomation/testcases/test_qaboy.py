import unittest
from webdriver import Driver
from values import strings
from pageobjects.homescreen import HomeScreen
from pageobjects.aboutscreen import AboutScreen


class TestQaBoy(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_home_screen_components(self):
        home_screen = HomeScreen(self.driver)
        home_screen.validate_title_is_present()
        home_screen.validate_icon_is_present()
        # home_screen.validate_menu_options_are_present()
        home_screen.validate_posts_are_visible()
        home_screen.validate_social_media_links()

    def test_about_screen_components(self):
        home_screen = HomeScreen(self.driver)
        home_screen.click_about_me_link()

        about_screen = AboutScreen(self.driver)
        about_screen.validate_title_is_present()
        about_screen.validate_icon_is_present()
        # about_screen.validate_menu_options_are_present()
        about_screen.validate_social_media_links()
        about_screen.validate_about_me_header()
        about_screen.validate_about_me_post()


    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()

