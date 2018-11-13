import allure


class PostScreen:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Validate article title')
    def validate_article_title(self, article_title):
        pass