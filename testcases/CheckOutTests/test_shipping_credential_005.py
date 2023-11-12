import time

from selenium.webdriver.common.by import By


from Utilities.recordLogger import recordLogger
from Utilities.ReadProperties import ReadProperties

from PageObjects.LoginObjects.LoginPageObject import loginObject
from PageObjects.CheckOutPagesObjects.CartObjectPage import cartObject
from PageObjects.ItemsForMenPagesObjects.PantsObjects import PantsObjects
from PageObjects.CheckOutPagesObjects.checkOurProcessObjects import checkOutProcessObjects


class Test_Shipping_details_004:
    LoginURL = ReadProperties.LoginURL()
    WomenJacketURL = ReadProperties.getWomenJacketsPageURL()
    MenPantsPageURL = ReadProperties.getMenPantsPageURL()
    cartURL = ReadProperties.getCartURL()
    EXISTING_EMAIL = ReadProperties.getEmail()
    EXISTING_PASSWORD = ReadProperties.getPassword()
    logger = recordLogger.log_generator_info()
    firstname = "Collins"
    lastname = "Bravo"
    company = "NileWays"
    street = "1 Bravo avenue"
    phoneNumber = "08133363256"
    city = "Arizona"


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
        # self.driver.get(self.WomenJacketURL)
        # self.WHO = WomenJacketsObjects(self.driver)
        # self.WHO.choiceForSizeAndColor()
        # proceed to checking out
        self.driver.get("https://magento.softwaretestingboard.com/checkout/#shipping")
        self.CO = checkOutProcessObjects(self.driver)  # navigates to the shipping details page

        #self.CO.proceedToCheckOut()
        self.CO.inputFirstName(self.firstname)
        self.CO.inputLastName(self.lastname)
        self.CO.inputCompany(self.company)
        self.CO.inputCity(self.city)
        self.CO.inputStreetAddress(self.street)
        time.sleep(3)
        self.CO.chooseCountry("US")
        time.sleep(3)
        self.CO.chooseState("3")
        time.sleep(3)
        self.CO.inputPhoneNumber(self.phoneNumber)
        time.sleep(3)
        shipping_information = self.CO.clickOnNextButton()  # navigates to the review and the payment page
        # expected result: details are saved
        shipping_details = [self.firstname, self.lastname, self.company, self.street, self.phoneNumber, self.city]

        assert all(items in shipping_details for items in shipping_information), self.logger.info("*** TEST FAILED: "
                                                                                                  "SHIPPING "
                                                                                                  "INFORMATION WRONG")
        self.logger.info("*** TEST PASSED: SHIPPING INFORMATION CORRESPONDS")
        self.driver.get(self.cartURL)
        self.CO = cartObject(self.driver)
        self.CO.removeItemsFromCart()
        self.log_test_end("**** test_checkout_total_013 ****")
        self.driver.quit()

    def est_add_shipping_details_when_user_is_not_logged_in_013(self, setup):
        self.log_test_start("**** test_add_shipping_details_when_user_is_not_logged_in_013  ****")
        self.logger.info("**** Test for the addition of the shipping details when the user is not logged in ****")
        self.log_test_start("Open Website")
        self.driver = setup
        # add items to cart
        self.driver.get(self.MenPantsPageURL)
        self.MP = PantsObjects(self.driver)
        self.MP.choiceForSizeAndColor()
        # proceed to check out
        self.CO = checkOutProcessObjects(self.driver)  # navigates to the shipping details page
        self.CO.proceedToCheckOut()
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        self.LO = loginObject(self.driver)
        email_inbox_status = self.LO.inputEmail("Ubongphilp2200@gmail.com")
        password_inbox_status = self.LO.inputPassword("Ubong123?")

        assert "Order Summary" in body_text
        assert email_inbox_status and password_inbox_status, \
            self.logger.info("*** TEST FAILED: THE ORDER SUMMARY AND THE EMAIL/PASSWORD INPUT BOX ARE NOT AVAILABLE ")
        self.logger.info("*** TEST TO VERIFY THE"
                         " DISPLAY OF THE INPUT BOXES WAS SUCCESSFUL AND THE ORDER SUMMARY WAS DISPLAYED")

        self.CO.inputFirstName(self.firstname)
        self.CO.inputLastName(self.lastname)
        self.CO.inputCompany(self.company)
        self.CO.inputCity(self.city)
        self.CO.inputStreetAddress(self.street)
        self.CO.chooseCountry("United State")
        self.CO.chooseState("Arizona")
        self.CO.inputPhoneNumber(self.phoneNumber)
        self.CO.clickOnNextButton()
        self.CO.clickPlaceOrder()
        time.sleep(3)
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "Thank you for your purchase!" not in body_text, self.logger.info("*** TEST FAILED: THE "
                                                                                 "ORDER SUMMARY AND THE EMAIL/"
                                                                                 "PASSWORD INPUT BOX ARE NOT AVAILABLE")
        self.logger.info("*** TEST TO VERIFY THE"
                         " DISPLAY OF THE INPUT BOXES WAS SUCCESSFUL AND THE ORDER SUMMARY WAS DISPLAYED")
