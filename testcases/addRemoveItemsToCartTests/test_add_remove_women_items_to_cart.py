# Import necessary modules and classes
from selenium.webdriver.common.by import By

from Utilities.recordLogger import recordLogger
from Utilities.ReadProperties import ReadProperties
from PageObjects.LoginObjects.LoginPageObject import loginObject

from PageObjects.CheckOutPagesObjects.CartObjectPage import cartObject
from PageObjects.ItemsForWomenPagesObjects.ShortsObjects import WomenShortsObjects
from PageObjects.ItemsForWomenPagesObjects.PantsObjects import WomenPantsObjects
from PageObjects.ItemsForWomenPagesObjects.JacketsObjects import WomenJacketsObjects
from PageObjects.ItemsForWomenPagesObjects.TankObjects import WomenTanksObjects


class add_remove_men_items_from_cart:
    # Initialize class variables with URLs and logger instance
    LoginURL = ReadProperties.LoginURL()  # Get login URL from configuration
    WomenPantsPageURL = ReadProperties.getWomenPantsPageURL() # Get men's pants page URL from configuration
    WomenJacketsPageURL = ReadProperties.getWomenJacketsPageURL()  # Get men's jackets page URL from configuration
    WomenTanksPageURL = ReadProperties.getWomenTanksPageURL()  # Get men's hoodies page URL from configuration
    WomenShortsPageURL = ReadProperties.getWomenShortsPageURL()  # Get men's shorts page URL from configuration
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
        self.open_login_to_website(setup)
        self.driver.get(self.cartURL)
        self.CO = cartObject(self.driver)
        self.CO.removeItemsFromCart()

    def verify_empty_cart(self):
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Shopping Cart" in body_text

    def test_add_and_remove_items_from_tanks_catalog(self, setup):
        self.log_test_start("*** test_add_and_remove_items_from_hoodies_catalog ***")
        self.open_login_to_website(setup)
        self.driver.get(self.WomenTanksPageURL)
        self.HO = WomenTanksObjects(self.driver)
        self.HO.choiceForSizeAndColor()
        self.item_removal(setup)
        self.verify_empty_cart()

    def test_add_and_remove_items_from_jacket_catalog(self, setup):
        self.log_test_start("*** test_add_and_remove_items_from_hoodies_catalog ***")
        self.open_login_to_website(setup)
        self.driver.get(self.WomenJacketsPageURL)
        self.HO = WomenJacketsObjects(self.driver)
        self.HO.choiceForSizeAndColor()
        self.item_removal(setup)
        self.verify_empty_cart()

    def test_add_and_remove_items_from_pants_catalog(self, setup):
        self.log_test_start("*** test_add_and_remove_items_from_hoodies_catalog ***")
        self.open_login_to_website(setup)
        self.driver.get(self.WomenPantsPageURL)
        self.HO = WomenPantsObjects(self.driver)
        self.HO.choiceForSizeAndColor()
        self.item_removal(setup)
        self.verify_empty_cart()

    def test_add_and_remove_items_from_shorts_catalog(self, setup):
        self.log_test_start("*** test_add_and_remove_items_from_hoodies_catalog ***")
        self.open_login_to_website(setup)
        self.driver.get(self.WomenShortsPageURL)
        self.HO = WomenShortsObjects(self.driver)
        self.HO.choiceForSizeAndColor()
        self.item_removal(setup)
        self.verify_empty_cart()
