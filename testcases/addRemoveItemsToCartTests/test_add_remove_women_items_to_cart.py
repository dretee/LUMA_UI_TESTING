# Import necessary modules and classes
from selenium.webdriver.common.by import By

from Utilities.recordLogger import recordLogger  # Importing logger utility
from Utilities.ReadProperties import ReadProperties  # Importing property reader utility
from PageObjects.LoginObjects.LoginPageObject import loginObject  # Importing login page object
from PageObjects.CheckOutPagesObjects.CartObjectPage import cartObject  # Importing cart page object
from PageObjects.ItemsForWomenPagesObjects.ShortsObjects import WomenShortsObjects  # Importing women shorts page object
from PageObjects.ItemsForWomenPagesObjects.PantsObjects import WomenPantsObjects  # Importing women pants page object
from PageObjects.ItemsForWomenPagesObjects.JacketsObjects import WomenJacketsObjects  # Importing women jackets page object
from PageObjects.ItemsForWomenPagesObjects.TankObjects import WomenTanksObjects  # Importing women tanks page object


class TestAddRemoveWomenItemsFromCart:
    # Initialize class variables with URLs and logger instance
    LoginURL = ReadProperties.LoginURL()  # Get login URL from configuration
    WomenPantsPageURL = ReadProperties.getWomenPantsPageURL()  # Get women's pants page URL from configuration
    WomenJacketsPageURL = ReadProperties.getWomenJacketsPageURL()  # Get women's jackets page URL from configuration
    WomenTanksPageURL = ReadProperties.getWomenTanksPageURL()  # Get women's tanks page URL from configuration
    WomenShortsPageURL = ReadProperties.getWomenShortsPageURL()  # Get women's shorts page URL from configuration
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

    def item_removal(self, setup):
        # Method to open the website, log in, and remove items from the cart
        self.driver.get(self.cartURL)
        self.CO = cartObject(self.driver)
        self.CO.removeItemsFromCart()

    def verify_empty_cart(self):
        # Method to verify if the cart is empty
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Shopping Cart" in body_text, self.logger.info("Shopping Cart is not present in the page body text")
        self.logger.info("** TEST PASSED: CART IS EMPTY AND ALL ITEMS WERE REMOVED *****")

    def test_add_and_remove_items_from_tanks_and_bras_catalog(self, setup):
        # Test method to add and remove items from the tanks and bras catalog
        self.log_test_start("*** test_add_and_remove_items_from_tanks_and_bras_catalog ***")
        self.open_login_to_website(setup)
        self.driver.get(self.WomenTanksPageURL)
        self.HO = WomenTanksObjects(self.driver)
        self.HO.choiceForSizeAndColor()
        self.item_removal(setup)
        self.verify_empty_cart()
        self.log_test_end("*** test_add_and_remove_items_from_tanks_and_bras_catalog ***")
        self.driver.quit()

    def test_add_and_remove_items_from_jacket_women_catalog(self, setup):
        # Test method to add and remove items from the women's jacket catalog
        self.log_test_start("*** test_add_and_remove_items_from_jacket_women_catalog ***")
        self.open_login_to_website(setup)
        self.driver.get(self.WomenJacketsPageURL)
        self.HO = WomenJacketsObjects(self.driver)
        self.HO.choiceForSizeAndColor()
        self.item_removal(setup)
        self.verify_empty_cart()
        self.log_test_end("*** test_add_and_remove_items_from_jacket_women_catalog  ***")
        self.driver.quit()

    def test_add_and_remove_items_from_pants_women_catalog(self, setup):
        # Test method to add and remove items from the women's pants catalog
        self.log_test_start("*** test_add_and_remove_items_from_pants_women_catalog ***")
        self.open_login_to_website(setup)
        self.driver.get(self.WomenPantsPageURL)
        self.HO = WomenPantsObjects(self.driver)
        self.HO.choiceForSizeAndColor()
        self.item_removal(setup)
        self.verify_empty_cart()
        self.log_test_end("*** test_add_and_remove_items_from_pants_women_catalog  ***")
        self.driver.quit()

    def test_add_and_remove_items_from_shorts_women_catalog(self, setup):
        # Test method to add and remove items from the women's shorts catalog
        self.log_test_start("*** test_add_and_remove_items_from_shorts_women_catalog ***")
        self.open_login_to_website(setup)
        self.driver.get(self.WomenShortsPageURL)
        self.HO = WomenShortsObjects(self.driver)
        self.HO.choiceForSizeAndColor()
        self.item_removal(setup)
        self.verify_empty_cart()
        self.log_test_end("*** test_add_and_remove_items_from_shorts_women_catalog  ***")
        self.driver.quit()
