import time
from selenium.webdriver.common.by import By
from Utilities.recordLogger import recordLogger
from PageObjects.CreateAccountObjects.createAccountObjects import accountCreationObjects
from Utilities.ReadProperties import ReadProperties


class TestCreationAndSignin:
    URL = ReadProperties.getPageURL()
    createAccountURL = ReadProperties.getAccountCreationURL()
    EXISTING_EMAIL = ReadProperties.getEmail()
    EXISTING_PASSWORD = ReadProperties.getPassword()
    logger = recordLogger.log_generator_info()

    # Method to log the start of a test
    def log_test_start(self, test_name):
        self.logger.info(f"****** STARTING TEST: {test_name} ******")

    # Method to log the end of a test
    def log_test_end(self, test_name):
        self.logger.info(f"****** ENDING TEST: {test_name} ******")

    # Method to open the website
    def open_website(self, setup, url):
        self.log_test_start("Open Website")
        self.driver = setup
        self.driver.get(url)
        self.driver.maximize_window()
        self.log_test_end("Open Website")

    ## VERIFICATION METHODS
    # Method to verify account creation
    def verify_account_creation(self, displayed_username, email):
        self.logger.info("**** VERIFICATION PROCESS ****")
        self.AO.createButton()
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        time.sleep(2)
        assert email in body_text, self.logger.info("****** ACCOUNT CREATION FAILED *****")
        self.logger.info("****** EMAIL IS IN THE BODY OF THE PAGE ****")
        time.sleep(2)
        assert displayed_username in body_text, self.logger.info("****** ACCOUNT CREATION FAILED *****")
        self.logger.info("****** USERNAME IS IN THE BODY OF THE PAGE ****")
        self.logger.info("****** ACCOUNT SUCCESSFULLY CREATED ****")

    # Method to verify invalid names during account creation
    def verify_invalid_names(self, firstname, lastname, email):
        self.logger.info("**** VERIFICATION PROCESS ***")
        self.AO = accountCreationObjects(self.driver)
        self.logger.info("**** INPUT FIRSTNAME, LASTNAME, EMAIL AND PASSWORD***")
        self.AO.inputNames(firstname, lastname)
        self.AO.inputEmail(email)
        self.AO.inputPasswords(self.EXISTING_PASSWORD)
        self.AO.createButton()
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert self.EXISTING_EMAIL not in body_text and firstname not in body_text and lastname not in body_text, \
            self.logger.info(f"*** TEST FAILED: Account created with invalid names: {firstname}, {lastname} ***")
        self.logger.info(
            f"***** TEST PASSED: No account was created with invalid names: {firstname}, {lastname} ******")

    # Method to verify creation of an account with existing user's email
    def verify_existing_user_creation(self):
        self.logger.info("**** VERIFICATION PROCESS ***")
        self.AO.createButton()
        time.sleep(3)
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "There is already an account with this email address. If you are sure that it is your email address, " \
               "click here to get your password and access your account." in body_text, \
            self.logger.info("*** TEST FAILED: Another account was created for the user ***")
        self.logger.info("***** TEST PASSED: No account was created for the user ******")

    ## VERIFICATION METHODS
    ## TESTING METHODS
    # TEST TO VERIFY THE FUNCTIONALITY OF THE CREATE ACCOUNT LINK
    def test_verify_create_account_link(self, setup):
        self.log_test_start("***** test_verify_create_account_link ****")
        self.open_website(setup, self.URL)
        status = self.AO.createAccount()
        assert status, self.logger.info("*** TEST FAILED: PAGE DISPLAYED DOES NOT HAVE "
                                        "TITLE: Create New Customer Account")
        self.logger.info("**** TEST PASSED: PAGE DISPLAYED HAS THE CORRECT TITLE ***** ")

    # Test for creating an account with valid details
    def test_valid_details_account_creation_003(self, setup):
        self.log_test_start("*******test_valid_details_account_creation_01 *******")
        self.open_website(setup, self.createAccountURL)
        self.AO = accountCreationObjects(self.driver)
        self.AO.inputNames("Deo", "John")
        self.logger.info("**** RANDOMLY GENERATE THE EMAIL USED FOR THIS SEQUENCE****")
        email = self.AO.email_generator()
        self.AO.inputEmail(email)
        self.AO.inputPasswords("ri?cHa2rd13")
        self.verify_account_creation("Deo John", email)
        time.sleep(3)
        self.AO.log_dropdown("logout")
        self.driver.quit()
        self.log_test_end("***** test_valid_details_account_creation_01 ****")

    # Test for creating multiple accounts with an existing user's email
    def test_multiple_accounts_for_existing_user_004(self, setup):
        self.log_test_start("test_multiple_accounts_for_existing_user_02")
        self.logger.info("CREATION OF AN ACCOUNT WITH AN EMAIL THAT HAS BEEN USED ALREADY IN THE DATABASE ***")
        self.open_website(setup, self.createAccountURL)
        self.AO = accountCreationObjects(self.driver)
        self.AO.inputNames("ubong", "phlip")
        self.AO.inputEmail(self.EXISTING_EMAIL)
        self.AO.inputPasswords(self.EXISTING_PASSWORD)
        self.verify_existing_user_creation()
        self.driver.quit()
        self.log_test_end("test_multiple_accounts_for_existing_user_02")

    # Test for creating an account with invalid names (integer)
    def test_invalid_names_creation_005(self, setup):
        self.log_test_start("***** test_invalid_names_creation_005 *****")
        self.logger.info("**** CREATION OF ACCOUNT WITH THE USE OF DIGITS FOR THE FIRSTNAME AND LASTNAME ***")
        self.open_website(setup, self.createAccountURL)
        self.AO = accountCreationObjects(self.driver)
        self.verify_invalid_names("12300", "5672222", self.AO.email_generator())
        self.driver.quit()
        self.log_test_end("***** test_invalid_names_creation_005 *****")

    # Test for creating an account with invalid names (special characters)
    def test_invalid_names_creation_with_special_charters_006(self, setup):
        self.log_test_start("***** test_invalid_names_creation_with_special_charters_006  ***** ")
        self.logger.info("Test for the creation of an account with invalid names (special characters)")
        self.open_website(setup, self.createAccountURL)
        self.AO = accountCreationObjects(self.driver)
        self.verify_invalid_names("TR1?EY", "UG&OTE", self.AO.email_generator())
        self.driver.quit()
        self.log_test_end("***** test_invalid_names_creation_with_special_charters_006 *****")

    # Test for verifying links on the welcome page
    def test_welcome_page_links_007(self, setup):
        self.log_test_start("***** test_welcome_page_links_007 *****")
        self.logger.info("******* Test for the welcome page *******")
        self.open_website(setup, self.URL)
        self.AO = accountCreationObjects(self.driver)
        title_of_pages = ["My Account", "My Orders", "My Downloadable Products",
                          "My Wish List", "Add New Address", "Account Information",
                          "Stored Payment Methods", "My Product Reviews"]
        # Log in and go to the welcome page
        self.AO.path_to_signinButton()
        self.AO.emailSignin("ubongphilip2200@gmail.com")
        self.AO.passwordSignin("Ubong123?")
        self.AO.signinButton()
        time.sleep(3)

        self.AO.log_dropdown("my account")
        time.sleep(3)

        # Verification and appending to a list begin
        list_of_all_page_title = self.AO.list_of_prompt_on_welcomepage()
        print(list_of_all_page_title)
        assert title_of_pages == list_of_all_page_title, self.logger.info("**** TEST FAILED *****")
        self.logger.info("***** TEST SUCCESSFULLY DONE *****")
        self.driver.quit()
        self.log_test_end("**** test_welcome_page_links_007 *****")


