import functools
import time
from Base_test_file import BaseTestClass
from Src.Pages.First_page_file import FirstPageClass
from Src.Pages.Add_application_page_file import AddApplicationPageClass
from Src.Pages.Fill_data_page_file import FillDataPageClass
from Src.Variables.Variables_file import VariablesClass


class SubmitTestClass(BaseTestClass):
    def setUp(self):
        self.debugMode = False
        self.sleepTime = 0.1
        self.closeInEnd = False

        self.maxTryCount = 2 if self.debugMode else 10

        self.variablesObj = VariablesClass()

        self.firstPageObj = FirstPageClass(self.driver, self.debugMode, self.sleepTime)
        self.addApplicationPageObj = AddApplicationPageClass(self.driver, self.debugMode, self.sleepTime)
        self.fillDataPageObj = FillDataPageClass(self.driver, self.debugMode, self.sleepTime)

    def check_and_accept_alert(self):
        try:
            alert = self.driver.switch_to.alert
            print("Alert text:", alert.text)
            if self.debugMode:
                print("Info: Accepting the alert ... ")
                time.sleep(self.sleepTime)
            alert.accept()
            return True
        except Exception as ec:
            if self.debugMode:
                print("Info: Alert is not present:\n", ec)
            return False

    @staticmethod
    def try_rerun_decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            if self.debugMode:
                print("Info: --- Starting:", func.__name__)
            succeeded = False
            for tryCounter in range(1, self.maxTryCount + 1):
                print("Attempt to submit num:", tryCounter)
                try:
                    func(self, *args, **kwargs)
                    if self.check_and_accept_alert():
                        print("Warning: Should not be an alert.")
                except Exception as ec:
                    print("Submit attempt num:", tryCounter, "Failed")
                    print("Error:", ec)
                else:
                    succeeded = True
                    print("Successfully submitted !!!")
                    break
            self.closeInEnd = not succeeded
            self.assertTrue(succeeded, f"Failed to submit after {self.maxTryCount} attempts")
            if self.debugMode:
                print("Info: --- Finished:", func.__name__)

        return wrapper

    @try_rerun_decorator
    def test_submit(self):
        # Opening browser and go to mainUrl
        if self.debugMode:
            print("Info: Opening the main url:", self.variablesObj.mainUrl)
            time.sleep(self.sleepTime)
        self.driver.get(self.variablesObj.mainUrl)
        # Check the title
        if self.debugMode:
            print("Info: Checking if a correct title:", self.variablesObj.pageTitle)
            time.sleep(self.sleepTime)
        self.assertIn(self.variablesObj.pageTitle, self.driver.title)
        # Fill marz
        self.firstPageObj.select_marz_by_visible_text()
        # Fill region
        self.firstPageObj.select_region_by_visible_text()
        # Fill school number and press RETURN
        self.firstPageObj.fill_school_field()
        # Should go to the next page

        # Try to check available places/vacations and print
        self.addApplicationPageObj.try_get_available_places_text()
        # Confirm/submit
        self.addApplicationPageObj.click_on_submit_button()
        # Should go to the next page

        # Fill child soc card number
        self.fillDataPageObj.fill_child_soc_card()
        # Fill Parent soc card number
        self.fillDataPageObj.fill_parent_soc_card()
        # Fill parent name
        self.fillDataPageObj.fill_parent_first_name()
        # Fill parent last name
        self.fillDataPageObj.fill_parent_last_name()
        # Fill a parent phone number and press RETURN
        self.fillDataPageObj.fill_parent_phone_number()

    def tearDown(self):
        if self.closeInEnd:
            self.driver.quit()
