import time
from selenium.webdriver.common.by import By

from PageObjects.LoginPageObject import loginObject
from Utilities import ReadXyFile
from Utilities.recordLogger import recordLogger
from PageObjects.forgotPasswordObjectPage import forgot_password


class Test_Login:
    URL = "https://magento.softwaretestingboard.com"
    logger = recordLogger.log_generator_info()
    PATH = ".\\TestData\\LUMA e-commerce Test Plan and Matrix.xlsx"

    def log_test_start(self, test_name):
        self.logger.info(f"****** STARTING TEST: {test_name} ******")

    def log_test_end(self, test_name):
        self.logger.info(f"****** ENDING TEST: {test_name} ******")

    def open_website(self, setup):
        self.log_test_start("Open Website")
        self.driver = setup
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.log_test_end("Open Website")

    def test_forgot_password_for_invalid_user(self, setup):
        self.open_website(setup)
        self.LO = loginObject(self.driver)
        self.LO.click_signin_link()
        self.LO.click_on_forgot_password_button()
        self.FP = forgot_password(self.driver)
        self.rowcount = ReadXyFile.getRowCount(self.PATH, "test data")

        for r in range(11, self.rowcount):
            self.userEmail = ReadXyFile.readData(self.PATH, "test data", r, 2)

        self.FP.inputEmaiAddress(self.userEmail)
        self.FP.clickResetButton()

        displayed_message = self.FP.alert_popup()

        assert displayed_message == f" There is no account associated with {self.userEmail}.", self.logger.info("*** TEST FAILED: THE POPUP DID NOT COME UP")

        self.logger.info("**** TEST PASSED: PASSWORD RESET AND LINK WAS SENT")
        self.driver.quit()

    def test_forgot_password_for_valid_user(self, setup):
        self.open_website(setup)
        self.LO = loginObject(self.driver)
        self.LO.click_signin_link()
        self.LO.click_on_forgot_password_button()
        self.FP = forgot_password(self.driver)
        self.rowcount = ReadXyFile.getRowCount(self.PATH, "test data")

        for r in range(12, self.rowcount+1):
            self.userEmail = ReadXyFile.readData(self.PATH, "test data", r, 2)

        self.FP.inputEmaiAddress(self.userEmail)
        self.FP.clickResetButton()

        displayed_message = self.FP.alert_popup()

        assert displayed_message == f"If there is an account associated with {self.userEmail} you will receive an email " \
                                    "with a link to reset your password.", self.logger.info("*** TEST FAILED: THE "
                                                                                            "POPUP DID NOT COME UP")

        self.logger.info("**** TEST PASSED: PASSWORD RESET AND LINK WAS SENT")
        self.driver.quit()


