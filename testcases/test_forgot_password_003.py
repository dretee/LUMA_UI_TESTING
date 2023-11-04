

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities import ReadXyFile
from Utilities.recordLogger import recordLogger
from PageObjects.LoginPageObject import loginObject
from PageObjects.forgotPasswordObjectPage import forgot_password
from Utilities.ReadProperties import ReadProperties


class Test_Login:
    URL = ReadProperties.getPageURL()
    forgot_Password_URl = ReadProperties.forgotPasswordURL()
    logger = recordLogger.log_generator_info()
    PATH = ".\\TestData\\LUMA e-commerce Test Plan and Matrix.xlsx"

    def log_test_start(self, test_name):
        self.logger.info(f"****** STARTING TEST: {test_name} ******")

    def log_test_end(self, test_name):
        self.logger.info(f"****** ENDING TEST: {test_name} ******")

    def open_website(self, setup, URL):
        self.log_test_start("Open Website")
        self.driver = setup
        self.driver.get(URL)
        self.driver.maximize_window()
        self.log_test_end("Open Website")

    def test_functionality_of_the_forgot_Password_link_000(self, setup):
        self.log_test_start("***** test_functionality_of_the_forgot_Password_link_000 *****")
        self.open_website(setup, self.URL)
        self.LO = loginObject(self.driver)

        self.LO.click_signin_link()
        self.LO.click_on_forgot_password_button()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.title_contains("Forgot Your Password?"))
        email_field = wait.until(EC.visibility_of_element_located((By.ID, "email_address")))

        # Assertions and logging
        assert self.driver.title == "Forgot Your Password?", self.logger.info("***** Incorrect page title *****")
        assert email_field.is_displayed(), self.logger.info("****** Email address field not visible on the page ******")

        self.logger.info("**** Forgot Password Link functionality tested successfully *****")
        self.log_test_end("**** test_functionality_of_the_signin_link_000 *****")
        self.driver.quit()

    def test_forgot_password_for_invalid_user_008(self, setup):
        self.log_test_start("**** test_forgot_password_for_invalid_user_008 ****")
        self.logger.info("*** user email is not on the database *****")
        self.logger.info("*** page navigates directly to the forgot password page *****")
        self.open_website(setup, self.forgot_Password_URl)
        self.FP = forgot_password(self.driver)
        self.rowcount = ReadXyFile.getRowCount(self.PATH, "test data")

        for r in range(11, self.rowcount):
            self.userEmail = ReadXyFile.readData(self.PATH, "test data", r, 2)
        self.logger.info(f"***** data gotten form the excel sheet. Email is {self.userEmail} ******")
        self.FP.inputEmaiAddress(self.userEmail)
        self.FP.clickResetButton()

        displayed_message = self.FP.alert_popup()

        assert displayed_message == f" There is no account associated with {self.userEmail}.", self.logger.info(
            "*** TEST FAILED: THE POPUP DID NOT COME UP")

        self.logger.info("**** TEST PASSED: PASSWORD RESET AND LINK WAS SENT")
        self.driver.quit()
        self.log_test_end("**** test_forgot_password_for_invalid_user_008 ****")

    def test_forgot_password_for_valid_user_009(self, setup):
        self.log_test_start("***** test_forgot_password_for_valid_user_009 *****")
        self.logger.info("*** page navigates directly to the forgot password page *****")
        self.open_website(setup, self.forgot_Password_URl)
        self.FP = forgot_password(self.driver)
        self.rowcount = ReadXyFile.getRowCount(self.PATH, "test data")

        for r in range(12, self.rowcount + 1):
            self.userEmail = ReadXyFile.readData(self.PATH, "test data", r, 2)
        self.logger.info(f"***** data gotten form the excel sheet. Email is {self.userEmail} ******")
        self.FP.inputEmaiAddress(self.userEmail)
        self.FP.clickResetButton()

        displayed_message = self.FP.alert_popup()

        assert displayed_message == f"If there is an account associated with {self.userEmail} you will receive an email " \
                                    "with a link to reset your password.", self.logger.info("*** TEST FAILED: THE "
                                                                                            "POPUP DID NOT COME UP")

        self.logger.info("**** TEST PASSED: PASSWORD RESET AND LINK WAS SENT")
        self.driver.quit()
        self.log_test_end("*** test_forgot_password_for_valid_user_009 ****")

