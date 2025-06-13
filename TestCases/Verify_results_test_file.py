import time
from Base_test_file import BaseTestClass
from Src.Pages.Verify_page_file import VerifyPageClass
from Src.Variables.Variables_file import VariablesClass


class RunSubmitRerunTestClass(BaseTestClass):
    def setUp(self):
        self.debugMode = False
        self.sleepTime = 0.5
        self.closeInEnd = False

        self.variablesObj = VariablesClass()
        self.verifyPageObj = VerifyPageClass(self.driver, self.debugMode, self.sleepTime)

    # Davit
    def test_verify_child1(self):
        if self.debugMode:
            print("Info: Opening the verify page url:", self.variablesObj.checkSubmissionPageUrl)
            time.sleep(self.sleepTime)
        self.driver.get(self.variablesObj.checkSubmissionPageUrl)
        self.verifyPageObj.fill_child_soc_card(self.variablesObj.childSocialCard)
        self.verifyPageObj.click_submit_button()

    # Gayane
    def test_verify_child2(self):
        if self.debugMode:
            print("Info: Opening the verify page url:", self.variablesObj.checkSubmissionPageUrl)
            time.sleep(self.sleepTime)
        self.driver.get(self.variablesObj.checkSubmissionPageUrl)
        self.verifyPageObj.fill_child_soc_card(self.variablesObj.childSocialCard2)
        self.verifyPageObj.click_submit_button()

    # Hayk
    def test_verify_child3(self):
        if self.debugMode:
            print("Info: Opening the verify page url:", self.variablesObj.checkSubmissionPageUrl)
            time.sleep(self.sleepTime)
        self.driver.get(self.variablesObj.checkSubmissionPageUrl)
        self.verifyPageObj.fill_child_soc_card(self.variablesObj.childSocialCard3)
        self.verifyPageObj.click_submit_button()

    def tearDown(self):
        if self.closeInEnd:
            self.driver.quit()
