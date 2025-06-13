import time
from selenium.webdriver.common.by import By
from Src.Pages.Base_page_file import BasePageClass
from Src.Variables.Variables_file import VariablesClass
from selenium.webdriver.common.keys import Keys


class FillDataPageClass(BasePageClass):
    def __init__(self, driver, debugMode=False, sleepTime=1):
        super().__init__(driver, debugMode, sleepTime)
        self.locators = FillDataPageLocatorsClass()
        self.variablesObj = VariablesClass()
        if self.debugMode:
            print("Info: The debug mode is enabled for 'Fill Data' page.")
            print(f"Info: All functions slowed down by sleep {self.sleepTime} sec.")

    def fill_child_soc_card(self, socNum: str = None):
        if socNum is None:
            socNum = self.variablesObj.childSocialCard
        childSocFieldElem = self.find.custom_find_element(self.locators.childSocFieldLocator)
        childSocFieldElem.send_keys(socNum)
        if self.debugMode:
            print("Info: Filled 'child' soc card field:", socNum)
            time.sleep(self.sleepTime)

    def fill_parent_soc_card(self, socNum: str = None):
        if socNum is None:
            socNum = self.variablesObj.parentSocialCard
        parentSocFieldElem = self.find.custom_find_element(self.locators.parentSocFieldLocator)
        parentSocFieldElem.send_keys(socNum)
        if self.debugMode:
            print("Info: Filled 'parent' soc card field:", socNum)
            time.sleep(self.sleepTime)

    def fill_parent_first_name(self, firstName: str = None):
        if firstName is None:
            firstName = self.variablesObj.parentName
        parentFirstNameFieldElem = self.find.custom_find_element(self.locators.parentFirstNameFieldLocator)
        parentFirstNameFieldElem.send_keys(firstName)
        if self.debugMode:
            print("Info: Filled 'parent' first name field:", firstName)
            time.sleep(self.sleepTime)

    def fill_parent_last_name(self, lastName: str = None):
        if lastName is None:
            lastName = self.variablesObj.parentLastName
        parentLastNameFieldElem = self.find.custom_find_element(self.locators.parentLastNameFieldLocator)
        parentLastNameFieldElem.send_keys(lastName)
        if self.debugMode:
            print("Info: Filled 'parent' last name field:", lastName)
            time.sleep(self.sleepTime)

    def fill_parent_phone_number(self, phoneNum: str = None):
        if phoneNum is None:
            phoneNum = self.variablesObj.parentPhoneNumber
        parentPhoneNumberFieldElem = self.find.custom_find_element(self.locators.parentPhoneNumberFieldLocator)
        parentPhoneNumberFieldElem.send_keys(phoneNum)
        if self.debugMode:
            print("Info: Filled 'parent' phone number field:", phoneNum)
            print("Info: Pressing RETURN ...")
            time.sleep(self.sleepTime)
        parentPhoneNumberFieldElem.send_keys(Keys.RETURN)

    def click_submit_button(self):
        submitButtonElem = self.find.custom_find_element(self.locators.submitButtonLocator)
        if self.debugMode:
            try:
                print(f"Info: Clicking on button: '{submitButtonElem.text}'")
            except Exception as ec:
                print("Warning: Couldn't get the 'submit' button text:", ec)
            time.sleep(self.sleepTime)
        submitButtonElem.click()


class FillDataPageLocatorsClass:
    childSocFieldLocator = (By.NAME, "child_soc")
    parentSocFieldLocator = (By.NAME, "parent_soc")
    parentFirstNameFieldLocator = (By.NAME, "parent_firstname")
    parentLastNameFieldLocator = (By.NAME, "parent_lastname")
    parentPhoneNumberFieldLocator = (By.NAME, "parent_email")
    submitButtonLocator = (By.CSS_SELECTOR, "button.submit_button ")
