import time
from selenium.webdriver.common.by import By
from Utilities.recordLogger import recordLogger
from PageObjects.createAccountObjects import accountCreationObjects



class Test_checkout_003:

    URL = "https://magento.softwaretestingboard.com"
    EXISTING_EMAIL = "ubongphilip2200@gmail.com"
    EXISTING_PASSWORD = "Ubong123?"
    logger = recordLogger.log_generator_info()

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


