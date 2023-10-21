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

    def verifyBoundaryAmountForQuantity(self):


    def verifyItemInCart(self):



    def navigationToTheMenCatalog(self):

    # initiate browser

    # navigate to the webpage

    # Login user

    # navigate to the men url for item selection

    # add items from the men sections

    def navigationToTheWomenCatalog(self):

    # navigate to the women url for item selection

    # add items from the men sections


    def test_addAndRemoveItemsToCart(self):

    # navigationToTheMenCatalog

    # add items from all sections of the catalog

    # verify the items in the list

    # navigate to the women url for item selection and add items from the women sections

    # add items from all sections of the catalog

    # verify the items in the list

    # remove items from the cart and verify their removal


    def test_addMaximumQuantityForItem(self):

    # navigationToTheMenCatalog and add item

    # navigate to the women url for item selection and add items from the women sections

    # add items from all sections of the catalog

    # Remove the items using the provided means

    def test_addMinimumQuantityForItem(self):

    # navigationToTheMenCatalog and add items

    # Navigate to the women section to add items

    # Remove the items using the provided means

    def test_addNegativeQuantityForItem(self):

    # navigationToTheMenCatalog

    # Navigate to the women section to add items

    # Remove the items using the provided means

    def test_addAboveMaximumQuantityForItem(self):

    # navigationToTheMenCatalog

    # Navigate to the men / women section to add items

    # Remove the items using the provided means

    def test_links_on_page_women(self, setup):
        # navigationToTheWomenCatalog


        self.log_test_start("**** TEST FOR THE LINKS ON THE WOMEN PAGE ****")

        self.open_website(setup)

    def test_links_on_page_men(self, setup):

    # navigationToTheMenCatalog








