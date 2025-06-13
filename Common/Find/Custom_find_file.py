from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CustomFindClass:
    def __init__(self, driver):
        self.driver = driver

    def custom_find_element(self, locator: tuple[str, str]):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))

    def custom_find_elements(self, locator: tuple[str, str]):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located(locator))
