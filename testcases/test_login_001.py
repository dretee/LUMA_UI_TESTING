import time
from selenium.webdriver.common.by import By
from Utilities import ReadXyFile
from Utilities.recordLogger import recordLogger
from PageObjects.LoginPageObject import loginObject
from Utilities.ReadProperties import ReadProperties


class Test_Login:
    URL = ReadProperties.getPageURL()
    EXISTING_EMAIL = ReadProperties.getEmail()
    EXISTING_PASSWORD = ReadProperties.getPassword()
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

    def test_valid_login_001(self, setup):
        self.log_test_start("***** test_valid_login_001 ******")
        self.open_website(setup)
        self.LO = loginObject(self.driver)
        self.LO.click_signin_link()
        self.logger.info("***** input the email and the password in to the necessary fields ******")
        self.LO.inputEmail(self.EXISTING_EMAIL)
        self.LO.inputPassword(self.EXISTING_PASSWORD)
        self.logger.info("*** Click on the login button *****")
        self.LO.click_login_button()
        time.sleep(4)
        self.logger.info("*** Collect the entire text of the page body and check for the presence of welcome message "
                         "*****")
        text_of_body = self.driver.find_element(By.TAG_NAME, "body").text
        welcome_text = self.LO.login_alert()
        self.LO.click_logout()
        self.driver.quit()
        assert welcome_text in text_of_body, self.logger.info("*** TEST FAILED: LOGING PROCESS FAILED ***")
        self.logger.info("*** TEST SUCCESSFUL: LOGIN PROCESS SUCCESSFUL ***")
        self.log_test_end("******* test_valid_login_001*******")
        self.driver.quit()

    def test_invalid_login_002(self, setup):
        self.log_test_start("**** test_invalid_login_002 ")
        self.open_website(setup)
        self.LO = loginObject(self.driver)
        self.LO.click_signin_link()
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
            bodyText = self.driver.find_element(By.TAG_NAME, "body").text
            error_alert = self.LO.error_alert()
            if error_alert in bodyText:
                if self.expected_title == "pass":
                    actual_result.append("pass")
                elif self.expected_title == "fail":
                    actual_result.append("fail")
            elif error_alert not in bodyText:
                actual_result.append("pass")

        print(actual_result, expected_result)
        assert all(items in actual_result for items in expected_result), self.logger.info(
            "*** TEST FAILED: LOGIN WAS SUCCESSFUL WITH INVALID DETAILS ****")

        self.logger.info("**** TEST SUCCESSFUL: THE USER WAS NOT LOGGED IN WIT INVALID CREDENTIAL")
        self.log_test_end("test_invalid_login_002")
        self.driver.quit()


