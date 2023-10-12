import time
from selenium.webdriver.common.by import By
from PageObjects.createAccountObjects import accountCreationObjects
from Utilities.recordLogger import recordLogger


class TestCreationAndSignin:
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
        time.sleep(2)
        # assert "Thank you for registering with Main Website Store." in body_text, self.logger.info("****** ACCOUNT CREATION FAILED *****")
        # self.logger.info("****** MESSAGE SEEN IN THE BODY OF THE PAGE ****")
        self.logger.info("****** ACCOUNT SUCCESSFULLY CREATED ****")

    def verify_invalid_names(self, setup, firstname, lastname, email):
        self.logger.info("**** VERIFICATION PROCESS ***")
        self.AO = accountCreationObjects(self.driver)
        self.AO.createAccount()
        self.AO.inputNames(firstname, lastname)
        self.AO.inputEmail(email)
        self.AO.inputPasswords(self.EXISTING_PASSWORD)
        self.AO.createButton()
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert self.EXISTING_EMAIL not in body_text and firstname not in body_text and lastname not in body_text, \
            self.logger.info(f"*** TEST FAILED: Account created with invalid names: {firstname}, {lastname} ***")
        self.logger.info(
            f"***** TEST PASSED: No account was created with invalid names: {firstname}, {lastname} ******")

    def verify_existing_user_creation(self):
        self.logger.info("**** VERIFICATION PROCESS ***")
        self.AO.createButton()
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        assert "There is already an account with this email address." in body_text, \
            self.logger.info("*** TEST FAILED: Another account was created for the user ***")
        self.logger.info("***** TEST PASSED: No account was created for the user ******")

    def est_valid_details_account_creation_01(self, setup):
        self.log_test_start("******* Valid Details Account Creation *******")
        self.open_website(setup)
        self.AO = accountCreationObjects(self.driver)
        self.AO.createAccount()
        self.AO.inputNames("Deo", "John")
        email = self.AO.email_generator()
        self.AO.inputEmail(email)
        self.AO.inputPasswords("ri?cHa2rd13")
        self.verify_account_creation("Deo John", email)
        time.sleep(3)
        self.AO.log_dropdown("logout")
        self.driver.quit()
        self.log_test_end("Valid Details Creation")

    def est_multiple_accounts_for_existing_user_02(self, setup):
        self.log_test_start("Multiple Accounts for Existing User")
        self.open_website(setup)
        self.AO = accountCreationObjects(self.driver)
        self.AO.createAccount()
        self.AO.inputNames("ubong", "phlip")
        self.AO.inputEmail(self.EXISTING_EMAIL)
        self.AO.inputPasswords(self.EXISTING_PASSWORD)
        self.verify_existing_user_creation()
        self.driver.quit()
        self.log_test_end("Multiple Accounts for Existing User")

    def est_invalid_names_creation_03(self, setup):
        self.log_test_start("Test for the creation of an account with an Invalid Names(integer)")
        self.open_website(setup)
        self.AO = accountCreationObjects(self.driver)
        self.verify_invalid_names(setup, "12300", "5672222", self.AO.email_generator())

    def est_invalid_names_creation_with_special_charters_04(self, setup):
        self.log_test_start("Test for the creation of an account with an Invalid Names(special charters)")
        self.open_website(setup)
        self.AO = accountCreationObjects(self.driver)
        self.verify_invalid_names(setup, "TR1?EY", "UG&OTE", self.AO.email_generator())
        self.log_test_end("Invalid Names Creation")

    def test_welcome_page_links_05(self, setup):
        ## we will check all the links on the page to and verify the content on the pages that will be opened
        # a list of what the result should give will aid this.
        # The content of the list will be the string of all the text of the page
        self.log_test_start("******* Test for the welcome page *******")
        self.open_website(setup)
        self.AO = accountCreationObjects(self.driver)
        title_of_pages = ["My Account", "My Orders", "My Downloadable Products",
                          "My Wish List", "Add New Address", "Edit Account Information",
                          "Stored Payment Methods", "My Product Reviews"]
        # log in and go to the welcome page
        self.AO.path_to_signinButton()
        self.AO.emailSignin("ubongphilip2200@gmail.com")
        self.AO.passwordSignin("Ubong123?")
        self.AO.signinButton()
        time.sleep(3)

        self.AO.log_dropdown("my account")
        time.sleep(3)

        # verification and appending to a list begins
        displayed_list = [self.driver.title]
        print(displayed_list)
        links_to_list = self.AO.list_of_prompt_on_welcomepage()
        for link in links_to_list:
            link.click()
            displayed_list.append(self.driver.title)
            print(displayed_list, links_to_list)

        assert title_of_pages == displayed_list, self.logger.info("**** TEST FAILED *****")
        self.logger.info("***** TEST SUCCESSFUL *****")







