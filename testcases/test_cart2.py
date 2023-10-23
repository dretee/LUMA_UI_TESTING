import time
from selenium.webdriver.common.by import By
from PageObjects.WomenPageObject import WomenPageObject
from PageObjects.createAccountObjects import accountCreationObjects
from Utilities.recordLogger import recordLogger
from PageObjects.menPageObject import MenPageObject
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random
import requests


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

    def MenCatalog(self, setup):
        self.log_test_start("******* Test for the welcome page *******")
        # initiate browser
        # navigate to the webpage
        self.open_website(setup)
        self.AO = accountCreationObjects(self.driver)
        # Log in and go to the welcome page
        self.AO.path_to_signinButton()
        self.AO.emailSignin("ubongphilip2200@gmail.com")
        self.AO.passwordSignin("Ubong123?")
        self.AO.signinButton()
        # navigate to the men url for item selection
        self.MC = MenPageObject(self.driver)
        self.MC.menCatalog()

    def testAddMenHoodieToCart(self, setup):
        self.MenCatalog(setup)
        time.sleep(2)
        self.MC = MenPageObject(self.driver)
        # Define the locators for the items and pick 4 items and add to the cart
        ItemsOfHoodiesPage = self.MC.addHoodies_sweatshirtToCart()           # take you to the catalog for the hoodies
        ListOfAddedItems = []
        time.sleep(2)

        # defining the sizes
        sizes = ['XS', 'S', 'M', 'L', 'XL']         # INDEX ERROR
        numbers = [1, 2, 3]

        for items in range(0, len(ItemsOfHoodiesPage), 1):
            print(ItemsOfHoodiesPage[items])
            time.sleep(2)
            # Check if the current index is within the valid range
            if items < len(ItemsOfHoodiesPage):
                # ListOfAddedItems.append(ItemsOfHoodiesPage[items].get_attribute("text"))  ## NO TEXT ATTRIBUTE
                # print(ListOfAddedItems)
                time.sleep(4)
                ItemsOfHoodiesPage[items].click()
                # getting a random size for the item
                size = random.choice(sizes)
                number = random.choice(numbers)
                self.MC.sizePicker(size)

                self.MC.colorPicker(number)
            else:
                break  # Exit the loop if the index is out of range

            self.MC.addToCart()
            time.sleep(3)
            self.driver.back()

        # call on the items in the cart and verify the correct addition of the items tot eh cart
        CartItems = self.MC.cart_items()
        time.sleep(2)

        assert set(ListOfAddedItems).issubset(set(CartItems)), self.logger.info("***** TEST FAILED: ITEMS NOT ADDED TO THE CART ****")

        self.logger.info("**** TEST SUCCESSFUL: ITEMS WERE ADDED TO THE CART *******")


