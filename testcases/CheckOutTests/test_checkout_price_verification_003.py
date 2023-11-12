# Import necessary modules and classes
from Utilities.recordLogger import recordLogger
from Utilities.ReadProperties import ReadProperties
from PageObjects.LoginObjects.LoginPageObject import loginObject
from PageObjects.ItemsForMenPagesObjects.PantsObjects import PantsObjects
from PageObjects.ItemsForWomenPagesObjects.JacketsObjects import WomenJacketsObjects
from PageObjects.CheckOutPagesObjects.CartObjectPage import cartObject


class Test_checkout_003:
    # Initialize class variables with URLs and logger instance
    LoginURL = ReadProperties.LoginURL()  # Get login URL from configuration
    MenPantsPageURL = ReadProperties.getMenPantsPageURL()  # Get men's pants page URL from configuration
    WomenJacketURL = ReadProperties.getWomenJacketsPageURL()  # Get women's jackets page URL from configuration
    cartURL = ReadProperties.getCartURL()  # Get cart page URL from configuration
    EXISTING_EMAIL = ReadProperties.getEmail()  # Get existing user's email from configuration
    EXISTING_PASSWORD = ReadProperties.getPassword()  # Get existing user's password from configuration
    logger = recordLogger.log_generator_info()  # Initialize logger instance

    # Method to log the start of a test
    def log_test_start(self, test_name):
        self.logger.info(f"****** STARTING TEST: {test_name} ******")

    # Method to log the end of a test
    def log_test_end(self, test_name):
        self.logger.info(f"****** ENDING TEST: {test_name} ******")

    # Method to open the website and perform login
    def open_login_to_website(self, setup):
        self.log_test_start("Open Website")
        self.driver = setup
        self.driver.get(self.LoginURL)
        self.driver.maximize_window()
        self.LO = loginObject(self.driver)
        self.LO.inputEmail(self.EXISTING_EMAIL)
        self.LO.inputPassword(self.EXISTING_PASSWORD)
        self.LO.click_login_button()

    # Test method to check the total amount in the cart after adding items
    def test_checkout_total_amount_013(self, setup):
        self.log_test_start("**** test_checkout_total_013 ****")
        self.open_login_to_website(setup)

        # Navigate to men's pants page and add items to the cart
        self.driver.get(self.MenPantsPageURL)
        self.PO = PantsObjects(self.driver)
        pants_price_list_for_men, _ = self.PO.choiceForSizeAndColor()

        # Navigate to women's jackets page and add items to the cart
        self.driver.get(self.WomenJacketURL)
        self.WHO = WomenJacketsObjects(self.driver)
        jackets_price_list_for_women, _ = self.WHO.choiceForSizeAndColor()

        # Calculate total price of items in the cart
        general_price_list = pants_price_list_for_men + jackets_price_list_for_women
        total_price = sum(float(price) for price in general_price_list)

        # Get the displayed total price from the cart
        self.CO = cartObject(self.driver)
        displayed_total_price = self.CO.get_price_of_items(self.cartURL)
        displayed_total_price = displayed_total_price.replace("$", "").replace(".00", "")

        # Assert the checkout price with the calculated total
        assert total_price == float(displayed_total_price), self.logger.info(
            "**** TEST FAILED: THE TOTAL IS NOT CORRECT ***")

        # Log test result and clean up the cart
        self.logger.info("***** TEST PASSED: THE TOTAL DISPLAYED IS CORRECT *****")
        self.driver.get(self.cartURL)
        self.CO.removeItemsFromCart()
        self.log_test_end("**** test_checkout_total_013 ****")
        self.driver.quit()

    # Test method for item removal from the cart
    def est_removal(self, setup):
        self.open_login_to_website(setup)
        self.driver.get(self.cartURL)
        self.CO = cartObject(self.driver)
        self.CO.removeItemsFromCart()
