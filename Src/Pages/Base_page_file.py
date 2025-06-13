from Common.Find.Custom_find_file import CustomFindClass


class BasePageClass:
    def __init__(self, driver, debugMode=False, sleepTime=1):
        self.driver = driver
        self.find = CustomFindClass(driver)
        self.debugMode = debugMode
        self.sleepTime = sleepTime
