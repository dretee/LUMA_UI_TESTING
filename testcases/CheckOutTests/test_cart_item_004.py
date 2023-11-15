# Import necessary modules and classes
from Utilities.recordLogger import recordLogger
from Utilities.ReadProperties import ReadProperties
from PageObjects.LoginObjects.LoginPageObject import loginObject
from PageObjects.ItemsForMenPagesObjects.PantsObjects import PantsObjects
from PageObjects.ItemsForWomenPagesObjects.PantsObjects import WomenPantsObjects
from PageObjects.CheckOutPagesObjects.CartObjectPage import cartObject


class Test_checkout_003:
    # Initialize class variables with URLs and logger instance
    LoginURL = ReadProperties.LoginURL()  # Get login URL from configuration
    MenPantsPageURL = ReadProperties.getMenPantsPageURL()  # Get men's pants page URL from configuration
    WomenPantsPageURL = ReadProperties.getWomenPantsPageURL()  # Get women's pants page URL from configuration
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

    # Test method to check if items added to the cart are correct
    def test_items_added_to_cart_014(self, setup):
        self.log_test_start("***** test_items_added_to_cart_012 *****")
        self.open_login_to_website(setup)
        self.driver.get(self.cartURL)
        self.CO = cartObject(self.driver)
        self.CO.removeItemsFromCart()

        # Navigate to men's pants page and add items to the cart
        self.driver.get(self.MenPantsPageURL)
        self.PO = PantsObjects(self.driver)
        _, pants_name_list_for_men = self.PO.choiceForSizeAndColor()

        # Navigate to women's pants page and add items to the cart
        self.driver.get(self.WomenPantsPageURL)
        self.WPO = WomenPantsObjects(self.driver)
        _, pants_name_list_for_women = self.WPO.choiceForSizeAndColor()

        # Combine and normalize the names of items in the cart and the displayed items
        general_list_of_name_of_items = pants_name_list_for_women + pants_name_list_for_men
        general_list_of_name_of_items = [items.strip() for items in general_list_of_name_of_items]
        self.CO = cartObject(self.driver)
        displayed_items_in_cart = self.CO.cart_items(self.cartURL)
        displayed_items_in_cart = [items.strip() for items in displayed_items_in_cart]

        # Check if all items in the cart match the expected items
        all_items_are_present = all(items in general_list_of_name_of_items for items in displayed_items_in_cart)

        # Log test result and clean up the cart
        assert all_items_are_present, self.logger.info("**** TEST FAILED: THE ITEMS ARE NOT CORRECT ***")
        self.logger.info("***** TEST PASSED: THE ITEMS DISPLAYED IS CORRECT *****")
        self.driver.get(self.cartURL)
        self.CO = cartObject(self.driver)
        self.CO.removeItemsFromCart()
        self.log_test_end("**** test_items_added_to_cart_014 ****")
        self.driver.quit()
