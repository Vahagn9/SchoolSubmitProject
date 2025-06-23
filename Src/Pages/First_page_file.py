import time
from selenium.webdriver.common.by import By
from Src.Pages.Base_page_file import BasePageClass
from selenium.webdriver.support.ui import Select
from Src.Variables.Variables_file import VariablesClass
from selenium.webdriver.common.keys import Keys


class FirstPageClass(BasePageClass):
    def __init__(self, driver, debugMode=False, sleepTime=1):
        super().__init__(driver, debugMode, sleepTime)
        self.locators = FirstPageLocatorsClass()
        self.variablesObj = VariablesClass()
        if self.debugMode:
            print("Info: The debug mode is enabled for 'First' page.")
            print(f"Info: All functions slowed down by sleep {self.sleepTime} sec.")

    def select_marz_by_visible_text(self, marzName: str = None):
        if marzName is None:
            marzName = self.variablesObj.marz
        marzDropdownElem = self.find.custom_find_element(self.locators.marzDropdownLocator, 5)
        selectElem = Select(marzDropdownElem)
        selectElem.select_by_visible_text(marzName)
        if self.debugMode:
            print("Info: Selected 'Marz' by text:", marzName)
            time.sleep(self.sleepTime)

    def select_region_by_visible_text(self, regionName: str = None):
        if regionName is None:
            regionName = self.variablesObj.region
        regionDropdownElem = self.find.custom_find_element(self.locators.regionDropdownLocator)
        selectElem = Select(regionDropdownElem)
        selectElem.select_by_visible_text(regionName)
        if self.debugMode:
            print("Info: Selected 'Region' by text:", regionName)
            time.sleep(self.sleepTime)

    def fill_school_field(self, schoolNum: str = None):
        if schoolNum is None:
            schoolNum = self.variablesObj.schoolNumber
        searchSchoolFieldElem = self.find.custom_find_element(self.locators.searchSchoolFieldLocator)
        searchSchoolFieldElem.send_keys(schoolNum)
        if self.debugMode:
            print("Info: Filled 'School number' field:", schoolNum)
            print("Info: Pressing RETURN ...")
            time.sleep(self.sleepTime)
        searchSchoolFieldElem.send_keys(Keys.RETURN)


class FirstPageLocatorsClass:
    marzDropdownLocator = (By.NAME, "marzField")
    regionDropdownLocator = (By.NAME, "regionField")
    searchSchoolFieldLocator = (By.NAME, "searchSchoolField")
