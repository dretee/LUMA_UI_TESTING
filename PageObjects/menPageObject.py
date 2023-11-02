import time
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class MenPageObject:
    add_to_cart_button_id = "product-addtocart-button"
    men_catalog_link_xpath = "//span[normalize-space()='Men']"
    top_xpath = "//a[contains(text(),'Tops')]"
    hoodies_sweatshirt_xpath = "//a[contains(text(),'Hoodies & Sweatshirts')]"
    list_of_item_in_hoodies_sweatshirt_xpath = "//div[@class='product details product-item-details']//a[@class='product-item-link']"
    jackets_xpath = "//a[contains(text(),'Jackets')]"
    list_of_item_in_jackets_xpath = "//a[@class='product-item-link']"
    tees_xpath = "//a[contains(text(),'Tees')]"
    list_of_item_in_tees_xpath = "//a[@class='product-item-link']"
    tanks_xpath = "//a[contains(text(),'Tanks')]"
    list_of_item_in_bras_tanks_xpath = "//a[@class='product-item-link']"
    bottom_xpath = "//a[contains(text(),'Bottoms')]"
    pants_xpaths = "//a[contains(text(),'Pants')]"
    list_of_item_in_pants_xpath = "//a[@class='product-item-link']"
    shorts_xpaths = "//a[contains(text(),'Shorts')]"
    list_of_item_in_shorts_xpath = "//a[@class='product-item-link']"

    color_list_xpath1 = "//div[@role='listbox' and @aria-labelledby = 'option-label-color-93' ]//div[1]"
    color_list_xpath2 = "//div[@role='listbox' and @aria-labelledby = 'option-label-color-93' ]//div[2]"
    color_list_xpath3 = "//div[@role='listbox' and @aria-labelledby = 'option-label-color-93' ]//div[3]"

    size_list_xpath = ["//div[@class='swatch-option text' and @role='option'][1]",
                       "//div[@class='swatch-option text' and @role='option'][2]",
                       "//div[@class='swatch-option text' and @role='option'][3]",
                       "//div[@class='swatch-option text' and @role='option'][4]",
                       "//div[@class='swatch-option text' and @role='option'][5]"]

    cart_name = "//a[@class='action showcart']"
    edit_cart_xpath = "//a[@class='action viewcart']"
    checkOut_xpath = "//button[@id='top-cart-btn-checkout']"
    cart_items_list_xpath = "//table[@id='shopping-cart-table']//div[@class='product-item-details']//a"
    deleteFromCart = "a[class='action action-delete']"

    color_xpaths = {
        1: color_list_xpath1,
        2: color_list_xpath2,
        3: color_list_xpath3
    }

    def __init__(self, driver):
        self.driver = driver

    def addToCart(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.add_to_cart_button_id))).click()

    def menCatalog(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.men_catalog_link_xpath))).click()

    def topsCatalog(self):
        self.driver.find_element(By.XPATH, self.top_xpath).click()

    def bottomCatalog(self):
        self.driver.find_element(By.XPATH, self.bottom_xpath).click()


    def addHoodies_sweatshirtToCart2(self):
        # Click on the element identified by the XPATH for hoodies/sweatshirts
        self.driver.find_element(By.XPATH, self.hoodies_sweatshirt_xpath).click()

        catalogHoodies_seatshirtXpath = ["//div[@class='product details product-item-details']//a[@class='product-item-link']",
                                         "//a[normalize-space()='Ajax Full-Zip Sweatshirt']",
                                         "//a[normalize-space()='Grayson Crewneck Sweatshirt']",
                                         "//a[normalize-space()='Oslo Trek Hoodie']"]

        return catalogHoodies_seatshirtXpath


    def addJacketsToCart(self):
        # Click on the element identified by the XPATH for Jackets
        self.driver.find_element(By.XPATH, self.jackets_xpath).click()

    def addTeesToCart(self):
        # Click on the element identified by the XPATH for Tees
        self.driver.find_element(By.XPATH, self.tees_xpath).click()

    def addTanksToCart(self):
        # Click on the element identified by the XPATH for Tanks
        self.driver.find_element(By.XPATH, self.tanks_xpath).click()

    def addPantsToCart(self):
        # Click on the element identified by the XPATH for Pants
        self.driver.find_element(By.XPATH, self.pants_xpaths).click()

    def addShortsToCart(self):
        # Click on the element identified by the XPATH for Shorts
        self.driver.find_element(By.XPATH, self.shorts_xpaths).click()

    def sizePicker(self, size):
        wait = WebDriverWait(self.driver, 10)
        # Find all size elements using the provided XPATH
        sizes = self.size_list_xpath

        # Check the provided size and click the corresponding element
        if size == "XS":
            wait.until(EC.element_to_be_clickable((By.XPATH, sizes[0]))).click()  # Click on the XS size element
        elif size == "S":
            wait.until(EC.element_to_be_clickable((By.XPATH, sizes[1]))).click()  # Click on the S size element
        elif size == "M":
            wait.until(EC.element_to_be_clickable((By.XPATH, sizes[2]))).click()  # Click on the M size element
        elif size == "L":
            wait.until(EC.element_to_be_clickable((By.XPATH, sizes[3]))).click()  # Click on the L size element
        elif size == "XL":
            wait.until(EC.element_to_be_clickable((By.XPATH, sizes[4]))).click()  # Click on the XL size element

    def colorPicker(self, number):
        # Check if the number is a valid key in the color_xpaths dictionary
        if number in self.color_xpaths:
            color_xpath = self.color_xpaths[number]

            # Wait for the color element to be clickable
            color_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, color_xpath))
            )

            # Click the color element
            color_element.click()
        else:
            raise ValueError(f"Invalid color number: {number}. Please provide a valid color number.")

    def cart_items(self):
        # Clicks on the cart icon in the web page
        self.driver.find_element(By.XPATH, self.cart_name).click()
        time.sleep(2)
        # Clicks on the 'Edit Cart' button
        self.driver.find_element(By.XPATH, self.edit_cart_xpath).click()
        # Finds all items in the cart based on the specified XPATH
        items = self.driver.find_elements(By.XPATH, self.cart_items_list_xpath)
        # Calculates the number of items in the cart
        numberOfItems = len(items)
        # Initializes an empty list to store text attributes of cart items
        verifying_list_from_cart = []

        # Iterates through the found items and retrieves their text attributes
        for item in items:
            verifying_list_from_cart.append(item.get_attribute("text"))

        # Returns the list containing text attributes of cart items and the count of items in the cart
        return verifying_list_from_cart

    def removeItemsFromCart(self):

        self.driver.find_element(By.XPATH, self.cart_name).click()
        if not self.driver.find_element(By.CSS_SELECTOR, "strong[class='subtitle empty']").is_displayed():
            print('no item in the cart')
        else:
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.edit_cart_xpath).click()
            # Wait for elements to be present before interacting with them
            wait = WebDriverWait(self.driver, 10)
            delete_buttons = self.driver.find_elements(By.CSS_SELECTOR, self.deleteFromCart)
            print(len(delete_buttons))

            for number in range(len(delete_buttons)):
                # Click the first delete button
                delete_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.deleteFromCart)))
                delete_button.click()

                # Handling a confirmation
                try:
                    alert = wait.until(EC.alert_is_present())
                    alert.accept()
                except TimeoutException:
                    print("No alert is present.")



