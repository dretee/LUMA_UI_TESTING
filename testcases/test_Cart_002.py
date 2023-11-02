import random
import requests
from selenium.webdriver.common.by import By
from Utilities.recordLogger import recordLogger
from PageObjects.menPageObject import MenPageObject
from PageObjects.WomenPageObject import WomenPageObject
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.createAccountObjects import accountCreationObjects


class Test_cart_002:
    URL = "https://magento.softwaretestingboard.com"
    EXISTING_EMAIL = "ubongphilip2200@gmail.com"
    EXISTING_PASSWORD = "Ubong123?"
    logger = recordLogger.log_generator_info()

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

    def WomenCatalog(self, setup):
        # navigate to the women catalog url
        self.WC = WomenPageObject(self.driver)
        self.WC.womenCatalog()

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

    def addOddItemsToCart(self, locator):
        """
        Adds odd-indexed items to the cart from the provided locator.

        Args:
            locator (str): XPATH locator for the items.

        Returns:
            list: List of added item texts.
        """
        try:
            items = self.driver.find_elements(By.XPATH, locator)
            list_of_added_items = []
            for index in range(0, len(items), 2):
                item = items[index]
                list_of_added_items.append(item.get_attribute("text"))
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, item))).click()
                sizes = ["XS", "S", "M", "L", "XL"]
                size = random.choice(sizes)
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.MO.size_list_xpath))).click()
                self.MO.sizeChoice(size)
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.ID, self.MO.add_to_cart_button_id))).click()
                self.driver.back()

            self.driver.back()
            return list_of_added_items
        except Exception as e:
            self.logger.error(f"Error occurred: {e}")
            raise e

        # Your other methods remain the same with the suggested improvements

    def addItemsToCartFromCatalogSection(self, catalog_section_xpath):
        self.driver.find_element(By.XPATH, catalog_section_xpath).click()
        return self.addOddItemsToCart(catalog_section_xpath)

    def test_addAndRemoveItemsToCart(self, setup):
        self.MenCatalog(setup)
        self.MO = MenPageObject(self.driver)
        try:
            # ... (setup and other test-related code remains the same)


            for catalog_section in [self.MO.hoodies_sweatshirt_xpath, self.MO.jackets_xpath,
                                    self.MO.tees_xpath, self.MO.tanks_xpath, self.MO.shorts_xpaths,
                                    self.MO.pants_xpaths]:
                items_added = self.addItemsToCartFromCatalogSection(catalog_section)
                total_items_added = (self.MO.men_combined_list())
                assert items_added == total_items_added, self.logger.error(
                    f"TEST FAILED: Missing items in cart. Cart Items: {items_added}, Expected: {total_items_added}")

            self.logger.info("TEST PASSED: All the items were added successfully.")
        except Exception as e:
            self.logger.error(f"TEST FAILED: {e}")
            raise e



    def est_links_on_page_women(self, setup):
        # navigationToTheWomenCatalog
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
        self.WC = WomenPageObject(self.driver)
        self.WC.womenCatalog()

        # get all the links using their tag names
        all_links = self.driver.find_elements(By.TAG_NAME, "a")
        print(f"The total number of links on this page is : {len(all_links)}")
        broken_links_list = []
        count_broken_links = 0
        for link in all_links:
            url = link.get_attribute("href")
            try:
                response = requests.head(url)
            except:
                response = None

            if response is not None and response.status_code >= 400:

                count_broken_links += 1
                broken_links_list.append(link)
            else:
                self.logger.info(f"**** This link: {link} is functional ******")

            self.logger.info(
                f"**** The total number of functional links are {len(all_links) - count_broken_links} and the total non-functional links are{count_broken_links} on the women's page. ****")
            print(f"Women broken links :{broken_links_list}")
            assert count_broken_links == 0, self.logger.info(
                "****** TEST FAILED: SOME OF THE LINKS ARENT FUNCTIOANL ******")

            self.logger.info("**** TEST PASSED: ALL THE LINKS ARE FUNCTIONAL ****")

    def est_links_on_page_men(self, setup):
        # navigationToTheMenCatalog
        self.MenCatalog(setup)
        self.MO = MenPageObject(self.driver)

        # get all the links from the page
        all_links = self.driver.find_elements(By.TAG_NAME, "a")
        broken_link_list = []
        functional_link_list = []
        count_broken_links = 0
        for link in all_links:
            url = link.get_attribute("href")

            try:
                response = requests.head(url)
            except:
                response = None

            if response is not None and response.status_code >= 400:
                count_broken_links += 1
                broken_link_list.append(link)
            else:
                functional_link_list.append(link)
                self.logger.info(f"*** This link : {link} is functinal *****")

            self.logger.info(
                f"**** The total number of functional links are {len(all_links) - count_broken_links} and the total non-functional links are{count_broken_links} on the men's page. ****")

            print(f"Women broken links :{broken_link_list}")

            assert count_broken_links == 0, self.logger.info(
                "****** TEST FAILED: SOME OF THE LINKS ARENT FUNCTIOANL ******")

            self.logger.info("**** TEST PASSED: ALL THE LINKS ARE FUNCTIONAL ****")
