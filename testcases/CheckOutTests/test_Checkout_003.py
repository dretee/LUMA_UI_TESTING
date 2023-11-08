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

    def getItemsIntoCart(self, setup):
        self.driver.get(self.MenHoodiesAndSweatshirtPageURL)

    def test_checkout_total_amount_011(self, setup):
        self.log_test_start("**** test_checkout_total_011 ****")
        self.open_login_to_website(setup)
        # ADD ITEMS TO THE CART
        # GET THE HOODIES PAGE FOR MEN
        # self.driver.get(self.MenHoodiesAndSweatshirtPageURL)
        # # initializing the object of the class for the addition of items from the hoodies catalog
        # self.HO = hoodiesobjects(self.driver)
        # time.sleep(3)
        # hoodies_list_for_men = self.HO.choiceForSizeAndColor()
        # # GET THE PANTS PAGE FOR MEN
        # self.driver.get(self.MenPantsPageURL)
        # self.PO = PantsObjects(self.driver)
        # pants_list_for_men = self.PO.choiceForSizeAndColor()
        # # GET THE JACKETS PAGE FOR WOMEN
        # self.driver.get(self.WomenJacketURL)
        # self.WHO = WomenJacketsObjects(self.driver)
        # jackets_list_for_women = self.WHO.choiceForSizeAndColor()
        # # GET THE PANTS PAGE FOR WOMEN
        # self.driver.get(self.WomenPantsPageURL)
        # self.WPO = WomenPantsObjects(self.driver)
        # pants_list_for_women = self.WPO.choiceForSizeAndColor()

        self.driver.get(self.WomenPantsShortsURL)
        self.WSO = WomenShortsObjects(self.driver)
        self.WSO.choiceForSizeAndColor()

        # GET THE GENERAL LIST OF ALL THE PRICES FOR ALL THE ITEMS
        # print(hoodies_list_for_men, pants_list_for_women, pants_list_for_men, jackets_list_for_women)
        # general_price_list = hoodies_list_for_men + pants_list_for_women + pants_list_for_men + jackets_list_for_women
        total_price = 0
        # for prices in general_price_list:
        #     total_price += int(prices)

        self.CO = cartObject(self.driver)
        displayed_total_price = self.CO.open_cart()
        displayed_total_price = float(displayed_total_price.replace("$", ""))
        # ASSERT THE CHECKOUT PRICE TO THE CALCULATED TOTAL
        assert total_price == displayed_total_price, self.logger.info("**** TEST FAILED: THE TOTAL IS NOT CORRECT ***")

        self.logger.info("***** TEST PASSED: THE TOTAL DISPLAYED IS CORRECT *****")
        self.log_test_end("**** test_checkout_total_011 ****")
        self.driver.quit()

    def est_items_added_to_cart_012(self, setup):
        self.log_test_start("***** test_items_added_to_cart_012 *****")
        self.open_login_to_website(setup)
        # ADD ITEMS TO THE CART
        # GET THE HOODIES PAGE FOR MEN
        self.driver.get(self.MenHoodiesAndSweatshirtPageURL)
        # initializing the object of the class for the addition of items from the hoodies catalog
        self.HO = hoodiesobjects(self.driver)
        time.sleep(3)
        hoodies_list_for_men = self.HO.choiceForSizeAndColor()
        # GET THE PANTS PAGE FOR WOMEN
        self.driver.get(self.WomenPantsPageURL)
        self.WPO = WomenPantsObjects(self.driver)
        pants_list_for_women = self.WPO.choiceForSizeAndColor()



    def est_removal(self, setup):
        self.open_login_to_website(setup)
        self.driver.get(self.cartURL)
        self.CO = cartObject(self.driver)
        self.CO.removeItemsFromCart()
