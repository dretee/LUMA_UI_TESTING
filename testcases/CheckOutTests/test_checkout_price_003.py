import time

from Utilities.recordLogger import recordLogger
from Utilities.ReadProperties import ReadProperties
from PageObjects.LoginObjects.LoginPageObject import loginObject

from PageObjects.ItemsForMenPagesObjects.hoodiesAndSweatshirtObjects import hoodiesobjects
from PageObjects.ItemsForMenPagesObjects.PantsObjects import PantsObjects
from PageObjects.ItemsForWomenPagesObjects.JacketsObjects import WomenJacketsObjects
from PageObjects.ItemsForWomenPagesObjects.ShortsObjects import WomenShortsObjects
from PageObjects.ItemsForWomenPagesObjects.PantsObjects import WomenPantsObjects
from PageObjects.CheckOutPagesObjects.CartObjectPage import cartObject


class Test_checkout_003:
    LoginURL = ReadProperties.LoginURL()
    MenHoodiesAndSweatshirtPageURL = ReadProperties.getMenHoodiesAndSweatshirtPageURL()
    MenPantsPageURL = ReadProperties.getMenPantsPageURL()
    WomenJacketURL = ReadProperties.getWomenJacketsPageURL()
    WomenPantsShortsURL = ReadProperties.getWomenShortsPageURL()
    WomenPantsPageURL = ReadProperties.getWomenPantsPageURL()
    cartURL = ReadProperties.getCartURL()
    EXISTING_EMAIL = ReadProperties.getEmail()
    EXISTING_PASSWORD = ReadProperties.getPassword()
    logger = recordLogger.log_generator_info()

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

    def test_checkout_total_amount_013(self, setup):
        self.log_test_start("**** test_checkout_total_013 ****")
        self.open_login_to_website(setup)
        # ADD ITEMS TO THE CART
        # GET THE PANTS PAGE FOR MEN
        self.driver.get(self.MenPantsPageURL)
        self.PO = PantsObjects(self.driver)
        pants_price_list_for_men, pants_name_list_for_men = self.PO.choiceForSizeAndColor()
        # GET THE JACKETS PAGE FOR WOMEN
        self.driver.get(self.WomenJacketURL)
        self.WHO = WomenJacketsObjects(self.driver)
        jackets_price_list_for_women, jackets_name_list_for_women = self.WHO.choiceForSizeAndColor()

        # GET THE GENERAL LIST OF ALL THE PRICES FOR ALL THE ITEMS
        print(pants_price_list_for_men, jackets_price_list_for_women)
        general_price_list = pants_price_list_for_men + jackets_price_list_for_women
        total_price = 0
        for prices in general_price_list:
            total_price += float(prices)

        self.CO = cartObject(self.driver)
        displayed_total_price = self.CO.get_price_of_items(self.cartURL)
        displayed_total_price = (displayed_total_price.replace("$", "").replace(".00", ""))

        # ASSERT THE CHECKOUT PRICE TO THE CALCULATED TOTAL
        assert total_price == float(displayed_total_price), self.logger.info(
            "**** TEST FAILED: THE TOTAL IS NOT CORRECT ***")

        self.logger.info("***** TEST PASSED: THE TOTAL DISPLAYED IS CORRECT *****")
        self.driver.get(self.cartURL)
        self.CO = cartObject(self.driver)
        self.CO.removeItemsFromCart()
        self.log_test_end("**** test_checkout_total_013 ****")
        self.driver.quit()

    def est_removal(self, setup):
        self.open_login_to_website(setup)
        self.driver.get(self.cartURL)
        self.CO = cartObject(self.driver)
        self.CO.removeItemsFromCart()
