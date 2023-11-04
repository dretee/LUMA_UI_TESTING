import time
from selenium.webdriver.common.by import By
from Utilities.recordLogger import recordLogger
from Utilities.ReadProperties import ReadProperties
from PageObjects.LoginPageObject import loginObject


class Test_checkout_003:

    URL = ReadProperties.LoginURL()
    MenHoodiesAndSweatshirtPageURL = ReadProperties.getMenHoodiesAndSweatshirtPageURL()
    MenPantsPageURL = ReadProperties.getMenPantsPageURL()
    WomenJacketURL = ReadProperties.getWomenJacketsPageURL()
    WomenPantsPageURL = ReadProperties.getWomenPantsPageURL()
    EXISTING_EMAIL = ReadProperties.getEmail()
    EXISTING_PASSWORD = ReadProperties.getPassword()
    logger = recordLogger.log_generator_info()

    def log_test_start(self, test_name):
        self.logger.info(f"****** STARTING TEST: {test_name} ******")

    def log_test_end(self, test_name):
        self.logger.info(f"****** ENDING TEST: {test_name} ******")

    def open_login_to_website(self, setup):
        self.log_test_start("Open Website")
        self.driver = setup
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.LO = loginObject(self.driver)
        self.LO.inputEmail(self.EXISTING_EMAIL)
        self.LO.inputPassword(self.EXISTING_PASSWORD)

    def getItemsIntoCart(self, setup):
        self.driver.get(self.MenHoodiesAndSweatshirtPageURL)












    def test_checkout_total_011(self, setup):
        self.log_test_start("**** test_checkout_total_011 ****")
        self.open_login_to_website(setup)
        # ADD ITEMS TO THE CART


        # ASSERT THE CHECKOUT PRICE TO THE CALCULATED TOTAL






