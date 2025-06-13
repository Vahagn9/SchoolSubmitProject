import time
from selenium.webdriver.common.by import By
from Src.Pages.Base_page_file import BasePageClass
from Src.Variables.Variables_file import VariablesClass


class VerifyPageClass(BasePageClass):
    def __init__(self, driver, debugMode=False, sleepTime=1):
        super().__init__(driver, debugMode, sleepTime)
        self.locators = VerifyPageLocatorsClass()
        self.variablesObj = VariablesClass()
        if self.debugMode:
            print("Info: The debug mode is enabled for 'Verify' page.")
            print(f"Info: All functions slowed down by sleep {self.sleepTime} sec.")

    def fill_child_soc_card(self, socNum: str = None):
        if socNum is None:
            socNum = self.variablesObj.childSocialCard
        socCartFieldElem = self.find.custom_find_element(self.locators.socCartFieldLocator)
        socCartFieldElem.send_keys(socNum)
        if self.debugMode:
            print("Info: Filled 'child' soc card field:", socNum)
            time.sleep(self.sleepTime)

    def click_submit_button(self):
        submitButtonElem = self.find.custom_find_element(self.locators.submitButtonLocator)
        if self.debugMode:
            try:
                print(f"Info: Clicking on button: '{submitButtonElem.get_property("value")}'")
            except Exception as ec:
                print("Warning: Couldn't get 'submit' button text:", ec)
            time.sleep(self.sleepTime)
        submitButtonElem.click()


class VerifyPageLocatorsClass:
    socCartFieldLocator = (By.NAME, "chSFCHEKK")
    submitButtonLocator = (By.CLASS_NAME, "submit_button")
    resultLocator = (By.CLASS_NAME, "resultCHECKSOC")
