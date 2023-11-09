import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class cartObject:
    add_to_cart_button_id = "product-addtocart-button"
    cart_name = "//a[@class='action showcart']"
    edit_cart_xpath = "//a[@class='action viewcart']"
    checkOut_xpath = "//button[@id='top-cart-btn-checkout']"
    cart_items_list_xpath = "//table[@id='shopping-cart-table']//div[@class='product-item-details']//a"
    deleteFromCart = "`a[class='action action-delete']`"
    delete_item_class_name = "a[class='action action-delete']"
    sum_total_xpath = "//div[@class='cart-totals']//tbody/tr[1]//span[@class='price']"
    order_total_xpath = "//div[@class='cart-totals']//tbody/tr[4]//span[@class='price']"
    discount_xpath = "//div[@class='cart-totals']//tbody/tr[2]//span[@class='price']"
    tax_xpath = "//div[@class='cart-totals']//tbody/tr[3]//span[@class='price']"

    def __init__(self, driver):
        self.driver = driver

    def openCart(self, Url):
        # Clicks on the cart icon to open the cart page
        cart_icon = self.driver.find_element(By.XPATH, self.cart_name)
        cart_icon.click()

        # Clicks on the 'Edit Cart' button
        edit_cart_button = self.driver.find_element(By.XPATH, self.edit_cart_xpath)
        edit_cart_button.click()

    def get_price_of_items(self, Url):
        self.driver.get(Url)
        # Waits for the subtotal element to be present in the DOM
        wait = WebDriverWait(self.driver, 10, 2)
        subtotal_element = wait.until(EC.presence_of_element_located((By.XPATH, self.sum_total_xpath)))

        # Retrieves and prints the subtotal value
        subtotal_value = subtotal_element.text
        print("Subtotal Value:", subtotal_value)

        return subtotal_value

    def cart_items(self, Url):
        self.driver.get(Url)
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
        time.sleep(2)
        items = self.driver.find_elements(By.CSS_SELECTOR, self.delete_item_class_name)
        number_of_items = len(items)
        wait = WebDriverWait(self.driver, 10, 2)
        for delete_action in range(number_of_items):
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.delete_item_class_name))).click()






