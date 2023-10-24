import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class WomenPageObject:
    add_to_cart_button_id = "product-addtocart-button"
    women_catalog_link_xpath = "//a[@id='ui-id-4']"
    top_xpath = "//a[contains(text(),'Tops')]"
    hoodies_sweatshirt_xpath = "//a[contains(text(),'Hoodies & Sweatshirts')]"
    list_of_item_in_hoodies_sweatshirt_xpath = "//a[@class='product-item-link']"
    jackets_xpath = "//a[contains(text(),'Jackets')]"
    list_of_item_in_jackets_xpath = "//a[@class='product-item-link']"
    tees_xpath = "//a[contains(text(),'Tees')]"
    list_of_item_in_tees_xpath = "//a[@class='product-item-link']"
    bras_tanks_xpath = "//a[contains(text(),'Bras & Tanks')]"
    list_of_item_in_bras_tanks_xpath = "//a[@class='product-item-link']"
    bottom_xpath = "//a[contains(text(),'Bottoms')]"
    pants_xpaths = "//a[contains(text(),'Pants')]"
    list_of_item_in_pants_xpath = "//a[@class='product-item-link']"
    shorts_xpaths = "//a[contains(text(),'Shorts')]"
    list_of_item_in_shorts_xpath = "//a[@class='product-item-link']"
    size_list_xpath = "//div[@role='listbox' and @aria-labelledby = 'option-label-size-143' ]//div"
    color_list_xpath = "//div[@role='listbox' and @aria-labelledby = 'option-label-color-93' ]//div"

    def __init__(self, driver):
        self.driver = driver

    def womenCatalog(self):
        self.driver.find_element(By.XPATH, self.women_catalog_link_xpath).click()

    def topsCatalog(self):
        self.driver.find_element(By.XPATH, self.top_xpath).click()

    def bottomCatalog(self):
        self.driver.find_element(By.XPATH, self.bottom_xpath).click()

    def addHoodies_sweatshirtToCart(self):
        # Click on the element identified by the XPATH for hoodies/sweatshirts
        self.driver.find_element(By.XPATH, self.hoodies_sweatshirt_xpath).click()

        # Call the addEvenItemsToCart method, passing the XPATH of items in hoodies/sweatshirts category
        items = self.addOddItemsToCart(self.list_of_item_in_hoodies_sweatshirt_xpath)
        return items

    def addJacketsToCart(self):
        # Click on the element identified by the XPATH for Jackets
        self.driver.find_element(By.XPATH, self.jackets_xpath).click()

        # Call the addEvenItemsToCart method, passing the XPATH of items in jackets category
        items = self.addOddItemsToCart(self.list_of_item_in_jackets_xpath)
        return items

    def addTeesToCart(self):
        # Click on the element identified by the XPATH for Tees
        self.driver.find_element(By.XPATH, self.tees_xpath).click()

        # Call the addEvenItemsToCart method, passing the XPATH of items in Tees category
        items = self.addOddItemsToCart(self.list_of_item_in_tees_xpath)
        return items

    def addBras_tanksToCart(self):
        # Click on the element identified by the XPATH for Bras & Tanks
        self.driver.find_element(By.XPATH, self.bras_tanks_xpath).click()

        # Call the addEvenItemsToCart method, passing the XPATH of items in Bras & Tanks category
        items = self.addOddItemsToCart(self.list_of_item_in_bras_tanks_xpath)
        return items

    def addPantsToCart(self):
        # Click on the element identified by the XPATH for Pants
        self.driver.find_element(By.XPATH, self.pants_xpaths).click()

        # Call the addEvenItemsToCart method, passing the XPATH of items in Pants category
        items = self.addOddItemsToCart(self.list_of_item_in_pants_xpath)
        return items

    def addShortsToCart(self):
        # Click on the element identified by the XPATH for Shorts
        self.driver.find_element(By.XPATH, self.shorts_xpaths).click()

        # Call the addEvenItemsToCart method, passing the XPATH of items in Shorts category
        items = self.addOddItemsToCart(self.list_of_item_in_shorts_xpath)
        return items

    def sizeChoice(self, size):
        """
            Chooses the specified size from the available options.

            Args:
                size (str): Size to be selected (XS, S, M, L, XL).
            """
        # Indices of sizes in the 'sizes' list
        size_indices = {"XS": 1, "S": 2, "M": 3, "L": 4, "XL": 5}
        # Find all size elements using the provided XPATH
        sizes = self.driver.find_elements(By.XPATH, self.size_list_xpath)
        # Click the size corresponding to the provided size argument
        sizes[size_indices[size]].click()

    def addOddItemsToCart(self, locator):
        """
            Adds odd-indexed items to the cart from the provided locator.

            Args:
                locator (str): XPATH locator for the items.

            Returns:
                list: List of added item texts.
            """
        # Find elements matching the given locator using XPath
        items = self.driver.find_elements(By.XPATH, locator)
        list_of_added_items = []
        # Loop through odd-indexed items (increment by 3)
        for index in range(0, len(items), 3):
            item = items[index]
            list_of_added_items.append(item.get_attribute("text"))
            # Click on the item
            item.click()

            # Choose a random size from the available options
            sizes = ["XS", "S", "M", "L", "XL"]
            size = random.choice(sizes)
            self.sizeChoice(size)  # this method selects the chosen size

            # Choose a random color from the available options
            colour = random.choice(self.color_list_xpath)

            # Click on the chosen color
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, colour))).click()

            # Click the 'Add to Cart' button
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, self.add_to_cart_button_id))).click()

            # Navigate back to the previous page
            self.driver.back()

        # Navigate back to the original page after processing all items
        self.driver.back()
        return list_of_added_items

    def women_combined_list(self):
        """
            Combines items from different categories into a single list and returns it.

            Returns:
                list: Combined list of items from different categories.
            """
        men_list = (
                self.addPantsToCart() +
                self.addBras_tanksToCart() +
                self.addPantsToCart() +
                self.addTeesToCart() +
                self.addJacketsToCart() +
                self.addHoodies_sweatshirtToCart()
        )
        return men_list
