import time

from selenium.webdriver.common.by import By
from Src.Pages.Base_page_file import BasePageClass


class AddApplicationPageClass(BasePageClass):
    def __init__(self, driver, debugMode=False, sleepTime=1):
        super().__init__(driver, debugMode, sleepTime)
        self.locators = AddApplicationPageLocatorsClass()
        if self.debugMode:
            print("Info: The debug mode is enabled for 'Add Application' page.")
            print(f"Info: All functions slowed down by sleep {self.sleepTime} sec.")

    def try_get_available_places_text(self):
        retVal = True
        try:
            availablePlacesElem = self.find.custom_find_element(self.locators.availablePlacesElemLocator)
            availablePlacesText = availablePlacesElem.text
            filledPlaces, allPlaces = [int(char.strip()) for char in availablePlacesText.split("/")]
            availablePlaces = allPlaces - filledPlaces
            print(f"Information about current vacancies: {availablePlaces} Available / from {allPlaces}")
            if availablePlaces < 1:
                print("Warning: No available places left :(")
                retVal = False
        except Exception as ec:
            print("Warning: Couldn't get available_places", ec)
        if self.debugMode:
            time.sleep(self.sleepTime)
        return retVal

    def click_on_submit_button(self):
        submitButton = self.find.custom_find_element(self.locators.submitButtonLocator)
        if self.debugMode:
            print("Info: Clicking on submit button ...")
            time.sleep(self.sleepTime)
        submitButton.click()


class AddApplicationPageLocatorsClass:
    availablePlacesElemLocator = (By.CSS_SELECTOR, "div.ml-sm-auto.d-block.d-sm-inline-flex")
    submitButtonLocator = (By.CLASS_NAME, "submit_button")
