import unittest
from selenium import webdriver


class BaseTestClass(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.debugMode = False
        # self.init_chrome_driver()
        self.init_edge_driver()

    def init_edge_driver(self):
        if self.debugMode:
            print("Info: Init 'Edge' driver")
        from selenium.webdriver.edge.options import Options
        edgeOptions = Options()
        edgeOptions.add_experimental_option("detach", True)
        self.driver = webdriver.Edge(options=edgeOptions)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)

    def init_chrome_driver(self):
        if self.debugMode:
            print("Info: Init 'Chrome' driver")
        from selenium.webdriver.chrome.options import Options
        chromeOptions = Options()
        chromeOptions.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chromeOptions)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
