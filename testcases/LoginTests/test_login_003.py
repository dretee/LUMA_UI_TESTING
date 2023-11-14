# Import necessary modules and classes
import time
from Utilities import ReadXyFile
from selenium.webdriver.common.by import By
from Utilities.recordLogger import recordLogger
from Utilities.ReadProperties import ReadProperties
from PageObjects.LoginObjects.LoginPageObject import loginObject


class Test_Login:
    # Initialize class variables with URLs, logger instance, and Excel file path
    URL = ReadProperties.getPageURL()  # Get main page URL from configuration
    accountURL  = ReadProperties.getAccountURL()
    loginPageUrl = ReadProperties.LoginURL()  # Get login page URL from configuration
    EXISTING_EMAIL = ReadProperties.getEmail()  # Get existing email from configuration
    EXISTING_PASSWORD = ReadProperties.getPassword()  # Get existing password from configuration
    logger = recordLogger.log_generator_info()  # Initialize logger instance
    PATH = ".\\TestData\\LUMA e-commerce Test Plan and Matrix.xlsx"  # Excel file path
    name_of_account_user = "Ubong Philip"

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
        print(url)
        self.driver.get(url)
        self.driver.maximize_window()
        self.log_test_end("Open Website")

    # Test functionality of the signin link
    def test_functionality_of_the_signin_link_010(self, setup):
        self.log_test_start("**** test_functionality_of_the_signin_link_010 *****")
        self.open_website(setup, self.URL)
        self.LO = loginObject(self.driver)

        # Click on signin link
        self.LO.click_signin_link()
        assert self.driver.title == "Customer Login", self.logger.info("*** TEST FAILED: THE PAGE PRESENTED ISN'T THE "
                                                                       "LOGIN PAGE ****")
        self.logger.info("**** TEST PASSED: THE LOGIN PAGE WAS SHOWN ON CLICKING THE LINK")
        self.log_test_end("**** test_functionality_of_the_signin_link_010 *****")
        self.driver.quit()

    # Test valid login
    def test_valid_login_011(self, setup):
        self.log_test_start("***** test_valid_login_011 ******")
        self.open_website(setup, self.loginPageUrl)
        self.LO = loginObject(self.driver)
        self.logger.info("***** input the email and the password into the necessary fields ******")
        self.LO.inputEmail(self.EXISTING_EMAIL)
        self.LO.inputPassword(self.EXISTING_PASSWORD)
        self.logger.info("*** Click on the login button *****")
        self.LO.click_login_button()
        time.sleep(4)
        self.logger.info("*** Collect the entire text of the page body and"
                         " check for the presence of the welcome message "
                         "*****")
        self.driver.get(self.accountURL)
        text_of_body = self.driver.find_element(By.TAG_NAME, "body").text
        time.sleep(5)
        # name of the account holder
        assert self.EXISTING_EMAIL in text_of_body, self.logger.info("*** TEST FAILED: LOGIN PROCESS FAILED ***")
        self.logger.info("*** TEST SUCCESSFUL: LOGIN PROCESS SUCCESSFUL ***")
        self.LO.click_logout()
        self.log_test_end("******* test_valid_login_011*******")
        self.driver.quit()

    # Test invalid login
    def test_invalid_login_012(self, setup):
        self.log_test_start("**** test_invalid_login_012 ")
        self.open_website(setup, self.loginPageUrl)
        self.LO = loginObject(self.driver)
        self.logger.info("**** Read the data from the excel sheet ******")
        self.rowCount = ReadXyFile.getRowCount(self.PATH, "test data")
        self.logger.info(f"Total rows to process: {self.rowCount}")
        print(self.rowCount-9)
        actual_result = []
        expected_result = []
        count = 0
        for r in range(3, self.rowCount-6):
            self.userEmail = ReadXyFile.readData(self.PATH, "test data", r, 2)
            self.password = ReadXyFile.readData(self.PATH, "test data", r, 3)
            self.expected_title = ReadXyFile.readData(self.PATH, "test data", r, 4)
            self.logger.info(f"Processing row {r}: username='{self.userEmail}', password='{self.password}', "
                             f"expected_title='{self.expected_title}'")
            count += 1
            self.logger.info(f"****** input the email and password data into the allocated fields for data {count} **** ")
            self.LO.inputEmail(self.userEmail)
            time.sleep(3)
            expected_result.append(self.expected_title)
            self.LO.inputPassword(self.password)
            self.logger.info("*** login button click ****")
            self.LO.click_login_button()
            error_alert = self.LO.error_alert()
            if error_alert == "The account sign-in was incorrect or your account is disabled temporarily. Please wait " \
                              "and try again later.":
                if self.expected_title == "pass":
                    actual_result.append("pass")
                elif self.expected_title == "fail":
                    actual_result.append("fail")
            elif error_alert != "The account sign-in was incorrect or your account is disabled temporarily. Please " \
                                "wait and try again later.":
                actual_result.append("pass")

        print(actual_result, expected_result)
        assert all(items in actual_result for items in expected_result), self.logger.info(
            "*** TEST FAILED: LOGIN WAS SUCCESSFUL WITH INVALID DETAILS ****")

        self.logger.info("**** TEST SUCCESSFUL: THE USER WAS NOT LOGGED IN WITH INVALID CREDENTIALS")
        self.log_test_end("test_invalid_login_012")
        self.driver.quit()
