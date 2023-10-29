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
    EXISTING_EMAIL = "dfghjkdfghjk@gmail.com"
    EXISTING_PASSWORD = "@ynR!TF6Xki8XWr"
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
        self.AO = accountCreationObjects(self.driver)
        # Log in and go to the welcome page
        self.AO.path_to_signinButton()
        self.AO.emailSignin(self.EXISTING_EMAIL)
        self.AO.passwordSignin(self.EXISTING_PASSWORD)
        self.AO.signinButton()
        # navigate to the men url for item selection

    def MenCatalog(self, setup):
        self.log_test_start("******* Test for the welcome page *******")
        self.MC = MenPageObject(self.driver)
        self.MC.menCatalog()

    def WomenCatalog(self, setup):
        self.log_test_start("******* Test for the welcome page *******")
        self.WE = WomenPageObject(self.driver)
        self.WE.womenCatalog()

    def choiceForSizeAndColor(self, setup, method):
        self.MC = MenPageObject(self.driver)
        ItemsOfHoodiesPage = method()             # take you to the catalog for the hoodies
        ListOfAddedItems = []
        time.sleep(2)

        sizes = ['XS', 'S', 'M', 'L', 'XL']
        numbers = [1, 2, 3]
        wait = WebDriverWait(self.driver, 10)

        for xpath in ItemsOfHoodiesPage:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            ListOfAddedItems.append(element.get_attribute("text"))
            element.click()

            # getting a random size for the item
            size, number = random.choice(sizes), random.choice(numbers)

            self.MC.sizePicker(size)

            self.MC.colorPicker(number)

            self.MC.addToCart()
            time.sleep(3)
            self.driver.back()
        cleanedList = [item.strip() for item in ListOfAddedItems]
        return cleanedList

    def testAddMenHoodieToCart(self, setup):
        self.open_website(setup)
        self.MC = MenPageObject(self.driver)
        time.sleep(2)
        numbers = self.driver.find_element(By.XPATH, "//span[@class='counter-number']")
        number = numbers.get_attribute("text")

        if number is not None:
            self.MC.removeItemsFromCart()

        self.MenCatalog(self.driver)
        # call on the items in the cart and verify the correct addition of the items to the cart
        addedItemsList = self.choiceForSizeAndColor(setup, self.MC.addHoodies_sweatshirtToCart2)
        CartItems = self.MC.cart_items()
        print(CartItems, addedItemsList)
        time.sleep(2)

        assert addedItemsList.__eq__(CartItems), self.logger.info(
            "***** TEST FAILED: ITEMS NOT ADDED TO THE CART ****")

        self.logger.info("**** TEST SUCCESSFUL: ITEMS WERE ADDED TO THE CART *******")






