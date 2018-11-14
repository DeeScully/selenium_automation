from selenium import webdriver

class Driver:

    def __init__(self):
        self.instance = webdriver.Chrome()
        # self.instance = webdriver.Firefox() #need to add geckodriver to root dir

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)

        else:
            raise TypeError('URL must be a string')
