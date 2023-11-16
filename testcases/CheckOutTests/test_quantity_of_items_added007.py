# Import necessary modules and classes
import time

from selenium.common import NoSuchElementException
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

    def test_boundaries_condition_for_invalid_input(self, setup):
        self.log_test_start("*** test_boundaries_condition_for_invalid_input ***")
        self.open_login_to_website(setup)
        self.driver.get(self.MenPantsPageURL)
        self.PO = PantsObjects(self.driver)
        self.PO.chioce_quantity_for_item()

        input_value = [0.99, 10000.1]   # values above the set boundary 10,000 and below the set boundary 1
        result = []
        expected_result = ["Pass", "Pass"]  # pass means no item was added to the cart with the inputted values
        for values in input_value:
            time.sleep(5)
            self.PO.quantity_input(values)

            self.PO.addToCart()
            try:
                message = self.driver.find_element(By.CSS_SELECTOR, "[id='qty-error']").text

                status = message == "Please enter a quantity greater than 0." or \
                         message == "The fewest you may purchase is 1." or \
                         message == "The maximum you may purchase is 10000."
            except NoSuchElementException:
                print("element was not found")
                status = False
            if status:
                result.append("Pass")
            else:
                result.append("Fail")

        assert result == expected_result, self.logger.info(
            f"*** TEST FAILED: THE INPUT {input_value} VALUE WAS ACCEPTED ***** ")

        self.logger.info(f"**** TEST PASSED: THE VALUE {input_value} WAS NOT ACCEPTED")
        self.driver.get(self.cartURL)
        self.CO = cartObject(self.driver)
        self.CO.removeItemsFromCart()
        self.log_test_end("**** test_boundaries_condition_for_invalid_input ****")
        self.driver.quit()

    def test_boundaries_condition_for_valid_input(self, setup):
        self.log_test_start("*** test_boundaries_condition_for_valid_input ***")
        self.open_login_to_website(setup)
        self.driver.get(self.MenPantsPageURL)
        self.PO = PantsObjects(self.driver)
        self.PO.chioce_quantity_for_item()
        wait = WebDriverWait(self.driver, 10, 2)

        input_value = [1, 2, 5000]  # values above the set boundary 10,000 and below the set boundary 1
        result = []
        expected_result = ["Pass", "Pass", "Pass"]  # pass means no item was added to the cart with the inputted values
        for values in input_value:
            time.sleep(5)
            self.PO.quantity_input(values)

            self.PO.addToCart()

            message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml("
                                                         "message.text)']"))).text
            name = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='base']")))
            time.sleep(4)
            status = message == f"You added {name.text} to your shopping cart."
            if status:
                result.append("Pass")
            else:
                result.append("Fail")

        print(result)

        assert result == expected_result, self.logger.info(
            f"*** TEST FAILED: THE INPUT {input_value} VALUE WAS NOT ACCEPTED ***** ")

        self.logger.info(f"**** TEST PASSED: THE VALUE {input_value} WAS ACCEPTED")
        self.driver.get(self.cartURL)
        self.CO = cartObject(self.driver)
        self.CO.removeItemsFromCart()
        self.log_test_end("**** test_boundaries_condition_for_valid_input ****")
        self.driver.quit()
