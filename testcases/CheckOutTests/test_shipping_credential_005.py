from Utilities.recordLogger import recordLogger
from Utilities.ReadProperties import ReadProperties

from PageObjects.LoginObjects.LoginPageObject import loginObject
from PageObjects.CheckOutPagesObjects.checkOutPageObject import CheckOutObject

from PageObjects.ItemsForMenPagesObjects.PantsObjects import PantsObjects
from PageObjects.ItemsForWomenPagesObjects.JacketsObjects import WomenJacketsObjects


class Test_Shipping_details_004:
    LoginURL = ReadProperties.LoginURL()
    WomenJacketURL = ReadProperties.getWomenJacketsPageURL()
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

    def test_add_shipping_details_when_user_logs_in_013(self, setup):
        self.log_test_start("**** Test_add_shipping_details_when_user_logs_in_013  ****")
        self.logger.info("**** Test for the addition of the shipping details when the user is logged in ****")
        self.open_login_to_website(setup)
        # add items to the cart
        # GET THE JACKETS PAGE FOR WOMEN
        self.driver.get(self.WomenJacketURL)
        self.WHO = WomenJacketsObjects(self.driver)
        self.WHO.choiceForSizeAndColor()
        # proceed to checking out
        self.checkout = CheckOutObject()

        # expected result: details are saved

    def test_add_shipping_details_when_user_is_not_logged_in_013(self, setup):
        self.log_test_start("**** test_add_shipping_details_when_user_is_not_logged_in_013  ****")
        self.logger.info("**** Test for the addition of the shipping details when the user is not logged in ****")
        self.open_login_to_website(setup)
        # add items to cart

        # proceed to check out

        # expected result: user is able to add details and display for login option os available
        # when next is clicked the user is asked to log in or sign up if no account is owned by the user
