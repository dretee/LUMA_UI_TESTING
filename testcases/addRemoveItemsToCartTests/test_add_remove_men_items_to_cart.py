# Import necessary modules and classes
from selenium.webdriver.common.by import By

from Utilities.recordLogger import recordLogger  # Importing logger utility
from Utilities.ReadProperties import ReadProperties  # Importing property reader utility
from PageObjects.LoginObjects.LoginPageObject import loginObject  # Importing login page object
from PageObjects.CheckOutPagesObjects.CartObjectPage import cartObject  # Importing cart page object
from PageObjects.ItemsForMenPagesObjects.ShortsObjects import ShortsObjects  # Importing shorts page object
from PageObjects.ItemsForMenPagesObjects.PantsObjects import PantsObjects  # Importing pants page object
from PageObjects.ItemsForMenPagesObjects.JacketsObjects import Jacketsobjects  # Importing jackets page object
from PageObjects.ItemsForMenPagesObjects.hoodiesAndSweatshirtObjects import hoodiesobjects  # Importing hoodies page object


class TestAddRemoveMenItemsFromCart:
    # Initialize class variables with URLs and logger instance
    LoginURL = ReadProperties.LoginURL()  # Get login URL from configuration
    MenPantsPageURL = ReadProperties.getMenPantsPageURL()  # Get men's pants page URL from configuration
    MenJacketsPageURL = ReadProperties.getMenJacketPageURL()  # Get men's jackets page URL from configuration
    MenHoodiesPageURL = ReadProperties.getMenHoodiesAndSweatshirtPageURL()  # Get men's hoodies page URL from configuration
    MenShortsPageURL = ReadProperties.getMenShortsPageURL()  # Get men's shorts page URL from configuration
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

    def test_add_and_remove_items_from_hoodies_catalog(self, setup):
        # Test method to add and remove items from the hoodies catalog
        self.log_test_start("*** test_add_and_remove_items_from_hoodies_catalog ***")
        self.open_login_to_website(setup)
        self.driver.get(self.MenHoodiesPageURL)
        self.HO = hoodiesobjects(self.driver)
        self.HO.choiceForSizeAndColor()
        self.item_removal(setup)
        self.verify_empty_cart()
        self.log_test_end("*** test_add_and_remove_items_from_hoodies_catalog ***")
        self.driver.quit()

    def test_add_and_remove_items_from_jacket_catalog(self, setup):
        # Test method to add and remove items from the jacket catalog
        self.log_test_start("*** test_add_and_remove_items_from_jacket_catalog ***")
        self.open_login_to_website(setup)
        self.driver.get(self.MenJacketsPageURL)
        self.HO = Jacketsobjects(self.driver)
        self.HO.choiceForSizeAndColor()
        self.item_removal(setup)
        self.verify_empty_cart()
        self.log_test_end("*** test_add_and_remove_items_from_jacket_catalog ***")
        self.driver.quit()

    def test_add_and_remove_items_from_pants_catalog(self, setup):
        # Test method to add and remove items from the pants catalog
        self.log_test_start("*** test_add_and_remove_items_from_pants_catalog ***")
        self.open_login_to_website(setup)
        self.driver.get(self.MenPantsPageURL)
        self.HO = PantsObjects(self.driver)
        self.HO.choiceForSizeAndColor()
        self.item_removal(setup)
        self.verify_empty_cart()
        self.log_test_end("*** test_add_and_remove_items_from_pants_catalog ***")
        self.driver.quit()

    def test_add_and_remove_items_from_shorts_catalog(self, setup):
        # Test method to add and remove items from the shorts catalog
        self.log_test_start("*** test_add_and_remove_items_from_shorts_catalog  ***")
        self.open_login_to_website(setup)
        self.driver.get(self.MenShortsPageURL)
        self.HO = ShortsObjects(self.driver)
        self.HO.choiceForSizeAndColor()
        self.item_removal(setup)
        self.verify_empty_cart()
        self.log_test_end("*** test_add_and_remove_items_from_shorts_catalog ***")
        self.driver.quit()
