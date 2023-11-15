# Import necessary modules and classes
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.CheckOutPagesObjects.CartObjectPage import cartObject
from Utilities.recordLogger import recordLogger
from Utilities.ReadProperties import ReadProperties
from PageObjects.LoginObjects.LoginPageObject import loginObject
from PageObjects.ItemsForMenPagesObjects.PantsObjects import PantsObjects


class Test_quantity_of_item_added_to_cart:
    # Initialize class variables with URLs and logger instance
    LoginURL = ReadProperties.LoginURL()  # Get login URL from configuration
    MenPantsPageURL = ReadProperties.getMenPantsPageURL()  # Get men's pants page URL from configuration
    cartURL = ReadProperties.getCartURL()  # Get cart page URL from configuration
    EXISTING_EMAIL = ReadProperties.getEmail()  # Get existing user's email from configuration
    EXISTING_PASSWORD = ReadProperties.getPassword()  # Get existing user's password from configuration
    logger = recordLogger.log_generator_info()  # Initialize logger instance

    def log_test_start(self, test_name):
        self.logger.info(f"****** STARTING TEST: {test_name} ******")

    def log_test_end(self, test_name):
        self.logger.info(f"****** ENDING TEST: {test_name} ******")

    def open_login_to_website(self, setup):
        self.log_test_start("Open Website")
        self.driver = setup
        self.driver.get(self.LoginURL)
        self.driver.maximize_window()
        self.LO = loginObject(self.driver)
        self.LO.inputEmail(self.EXISTING_EMAIL)
        self.LO.inputPassword(self.EXISTING_PASSWORD)
        self.LO.click_login_button()

    def test_boundaries_condition_for_quantity_input(self, setup):
        self.log_test_start("*** test_boundaries_condition_for_quantity_input ***")
        self.open_login_to_website(setup)
        self.driver.get(self.cartURL)
        self.CO = cartObject(self.driver)
        self.CO.removeItemsFromCart()
        self.driver.get(self.MenPantsPageURL)
        self.PO = PantsObjects(self.driver)
        self.PO.chioce_quantity_for_item()
        wait = WebDriverWait(self.driver, 10, 2)

        # Boundary condition test for quantity input
        # Inputs: [0.99, 1, 2, 5000, 9999.9, 10000, 10000.1]
        verification_list = ["FAIL", "PASS", "PASS", "PASS", "FAIL", "FAIL", "FAIL"]
        result = []

        for input_value in [0.99, 1, 2, 5000, 9999.9, 10000, 10000.1]:
            self.logger.info(f"*** Input value is: {input_value} ***")

            # Check if the input is greater than 10000
            if input_value >= 10000:
                self.PO.quantity_input(input_value)
                time.sleep(4)
                self.PO.addToCart()
                message = self.driver.find_element(By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml("
                                                             "message.text)']").text

                if message == "The maximum you may purchase is 10000.":
                    result.append("FAIL")
                elif message == "The requested qty is not available":
                    result.append("FAIL")
                else:
                    result.append("PASS")

            # Check if the input is less than 1
            elif input_value < 1:
                self.PO.quantity_input(input_value)
                self.PO.addToCart()
                message = self.driver.find_element(By.CSS_SELECTOR, "[id='qty-error']").text

                if message == "Please enter a quantity greater than 0.":
                    result.append("FAIL")
                else:
                    result.append("PASS")
            # Check if the input is a float
            elif isinstance(input_value, float):
                self.PO.quantity_input(input_value)
                self.PO.addToCart()
                time.sleep(4)
                message = self.driver.find_element(By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml("
                                                             "message.text)']").text
                message_two = self.driver.find_element(By.ID, "qty-error").text

                if message == "You cannot use decimal quantity for this product." or message_two == "The fewest you may purchase is 1.":
                    result.append("FAIL")
                else:
                    result.append("PASS")
            # Default case for other inputs
            else:
                self.PO.quantity_input(input_value)
                self.PO.addToCart()
                time.sleep(4)
                message = self.driver.find_element(By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml("
                                                             "message.text)']").text
                name = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='base']")))
                time.sleep(4)
                if message == f"You added {name.text} to your shopping cart.":
                    result.append("PASS")
                else:
                    result.append("FAIL")
        print(f"Result list: {result}")
        print(f"Verification list: {verification_list}")
        assert verification_list == result, self.logger.info("*** TEST FAILED: ONE OF THE INPUT WAS LOGGED IN")

        self.logger.info("*** TEST PASSED: THE TEST PASSED AND ALL FUNCTIONALITY IS WORKING AS EXPECTED ")
        self.driver.get(self.cartURL)
        self.CO = cartObject(self.driver)
        self.CO.removeItemsFromCart()
        self.log_test_end("*** test_boundaries_condition_for_quantity_input ***")
