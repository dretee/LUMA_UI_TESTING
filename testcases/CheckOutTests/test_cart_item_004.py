import time

from Utilities.recordLogger import recordLogger
from Utilities.ReadProperties import ReadProperties
from PageObjects.LoginObjects.LoginPageObject import loginObject


from PageObjects.ItemsForMenPagesObjects.PantsObjects import PantsObjects
from PageObjects.ItemsForWomenPagesObjects.JacketsObjects import WomenJacketsObjects
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

    def test_items_added_to_cart_014(self, setup):
        self.log_test_start("***** test_items_added_to_cart_012 *****")
        self.open_login_to_website(setup)
        # ADD ITEMS TO THE CART
        # GET THE PANTS PAGE FOR MEN
        self.driver.get(self.MenPantsPageURL)
        self.PO = PantsObjects(self.driver)
        pants_price_list_for_men, pants_name_list_for_men = self.PO.choiceForSizeAndColor()
        # GET THE PANTS PAGE FOR WOMEN
        self.driver.get(self.WomenPantsPageURL)
        self.WPO = WomenPantsObjects(self.driver)
        pants_price_list_for_women, pants_name_list_for_women = self.WPO.choiceForSizeAndColor()

        general_list_of_name_of_items = pants_name_list_for_women + pants_name_list_for_men
        general_list_of_name_of_items = [items.strip() for items in general_list_of_name_of_items]
        self.CO = cartObject(self.driver)
        displayed_items_in_cart = self.CO.cart_items(self.cartURL)
        print(displayed_items_in_cart, general_list_of_name_of_items)
        displayed_items_in_cart = [items.strip() for items in displayed_items_in_cart]

        all_items_are_present = all(items in general_list_of_name_of_items for items in displayed_items_in_cart)
        print(all_items_are_present)

        assert all_items_are_present,  self.logger.info(
            "**** TEST FAILED: THE ITEMS ARE NOT CORRECT ***")

        self.logger.info("***** TEST PASSED: THE ITEMS DISPLAYED IS CORRECT *****")

        self.driver.get(self.cartURL)
        self.CO = cartObject(self.driver)
        self.CO.removeItemsFromCart()
        self.log_test_end("**** test_items_added_to_cart_014 ****")
        self.driver.quit()
