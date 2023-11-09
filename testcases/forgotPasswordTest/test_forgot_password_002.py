# Import necessary modules and classes
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities import ReadXyFile
from Utilities.recordLogger import recordLogger
from Utilities.ReadProperties import ReadProperties
from PageObjects.LoginObjects.LoginPageObject import loginObject
from PageObjects.ForgotPassword.forgotPasswordObjectPage import forgot_password


class Test_Login:
    # Initialize class variables with URLs, logger instance, and Excel file path
    URL = ReadProperties.getPageURL()  # Get main page URL from configuration
    forgot_Password_URl = ReadProperties.forgotPasswordURL()  # Get forgot password page URL from configuration
    logger = recordLogger.log_generator_info()  # Initialize logger instance
    PATH = ".\\TestData\\LUMA e-commerce Test Plan and Matrix.xlsx"  # Excel file path

    # Method to log the start of a test
    def log_test_start(self, test_name):
        self.logger.info(f"****** STARTING TEST: {test_name} ******")

    # Method to log the end of a test
    def log_test_end(self, test_name):
        self.logger.info(f"****** ENDING TEST: {test_name} ******")

    # Method to open the website
    def open_website(self, setup, url):
        self.log_test_start("Open Website")
        self.driver = setup
        self.driver.get(url)
        self.driver.maximize_window()
        self.log_test_end("Open Website")

    # Test functionality of the forgot password link
    def test_functionality_of_the_forgot_Password_link_007(self, setup):
        self.log_test_start("***** test_functionality_of_the_forgot_Password_link_007 *****")
        self.open_website(setup, self.URL)
        self.LO = loginObject(self.driver)

        # Click on forgot password link
        self.LO.click_signin_link()
        self.LO.click_on_forgot_password_button()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.title_contains("Forgot Your Password?"))
        email_field = wait.until(EC.visibility_of_element_located((By.ID, "email_address")))

        # Assertions and logging
        assert self.driver.title == "Forgot Your Password?", self.logger.info("***** Incorrect page title *****")
        assert email_field.is_displayed(), self.logger.info("****** Email address field not visible on the page ******")

        self.logger.info("**** Forgot Password Link functionality tested successfully *****")
        self.log_test_end("**** test_functionality_of_the_signin_link_007 *****")
        self.driver.quit()

    # Test forgot password for invalid user
    def test_forgot_password_for_invalid_user_008(self, setup):
        self.log_test_start("**** test_forgot_password_for_invalid_user_008 ****")
        # Retrieve user email from Excel sheet
        self.open_website(setup, self.forgot_Password_URl)
        self.FP = forgot_password(self.driver)
        self.rowcount = ReadXyFile.getRowCount(self.PATH, "test data")

        for r in range(11, self.rowcount):
            self.userEmail = ReadXyFile.readData(self.PATH, "test data", r, 2)
        self.logger.info(f"***** data gotten form the excel sheet. Email is {self.userEmail} ******")
        self.FP.inputEmaiAddress(self.userEmail)
        self.FP.clickResetButton()

        # Get and verify the displayed message in the popup
        displayed_message = self.FP.alert_popup()

        assert displayed_message == f" There is no account associated with {self.userEmail}.", self.logger.info(
            "*** TEST FAILED: THE POPUP DID NOT COME UP")

        self.logger.info("**** TEST PASSED: PASSWORD RESET AND LINK WAS SENT")
        self.driver.quit()
        self.log_test_end("**** test_forgot_password_for_invalid_user_008 ****")

    # Test forgot password for valid user
    def test_forgot_password_for_valid_user_009(self, setup):
        self.log_test_start("***** test_forgot_password_for_valid_user_009 *****")
        # Retrieve user email from Excel sheet
        self.open_website(setup, self.forgot_Password_URl)
        self.FP = forgot_password(self.driver)
        self.rowcount = ReadXyFile.getRowCount(self.PATH, "test data")

        for r in range(12, self.rowcount + 1):
            self.userEmail = ReadXyFile.readData(self.PATH, "test data", r, 2)
        self.logger.info(f"***** data gotten form the excel sheet. Email is {self.userEmail} ******")
        self.FP.inputEmaiAddress(self.userEmail)
        self.FP.clickResetButton()

        # Get and verify the displayed message in the popup
        displayed_message = self.FP.alert_popup()

        assert displayed_message == f"If there is an account associated with {self.userEmail} you will receive an email " \
                                    "with a link to reset your password.", self.logger.info("*** TEST FAILED: THE "
                                                                                            "POPUP DID NOT COME UP")

        self.logger.info("**** TEST PASSED: PASSWORD RESET AND LINK WAS SENT")
        self.driver.quit()
        self.log_test_end("*** test_forgot_password_for_valid_user_009 ****")
