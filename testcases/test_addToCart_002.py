import time
from selenium.webdriver.common.by import By
from PageObjects.createAccountObjects import accountCreationObjects
from Utilities.recordLogger import recordLogger


class Test_cart_002:

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

    def test_for_links_on_page_women(self, setup):
        self.log_test_start("**** TEST FOR THE LINKS ON THE WOMEN PAGE ****")
        self.open_website(setup)
        self.AO =
