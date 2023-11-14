import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.ItemsForMenPagesObjects import common_funtions


class PantsObjects:
    add_to_cart_button_id = "product-addtocart-button"
    size_list_xpath = ["//div[@class='swatch-option text' and @role='option'][1]",
                       "//div[@class='swatch-option text' and @role='option'][2]",
                       "//div[@class='swatch-option text' and @role='option'][3]",
                       "//div[@class='swatch-option text' and @role='option'][4]",
                       "//div[@class='swatch-option text' and @role='option'][5]"]
    quantity_input_selector = "[id ='qty']"
    color_list_xpath1 = "//div[@role='listbox' and @aria-labelledby = 'option-label-color-93' ]//div[1]"
    color_list_xpath2 = "//div[@role='listbox' and @aria-labelledby = 'option-label-color-93' ]//div[2]"
    color_list_xpath3 = "//div[@role='listbox' and @aria-labelledby = 'option-label-color-93' ]//div[3]"

    price_locator = "//span[ @data-price-type='finalPrice']"

    color_xpaths = {
        1: color_list_xpath1,
        2: color_list_xpath2,
        3: color_list_xpath3
    }

    catalogPantsXpath = [
        "//a[normalize-space()='Aether Gym Pant']",
        "//a[normalize-space()='Thorpe Track Pant']",
        "//a[normalize-space()='Kratos Gym Pant']",
        "//a[normalize-space()='Geo Insulated Jogging Pant']"]

    def __init__(self, driver):
        self.driver = driver

    def addToCart(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.add_to_cart_button_id))).click()

    def choiceForSizeAndColor(self):
        time.sleep(2)

        sizes = ['32', '33', '34', '35', '36']
        numbers = [1, 2, 3]
        returns = common_funtions.choosing_action_of_items(self.driver, sizes, numbers, self.catalogPantsXpath,
                                                           self.size_list_xpath, self.color_xpaths,
                                                           self.add_to_cart_button_id, self.price_locator)
        list_of_prices, list_of_items = returns

        return list_of_prices, list_of_items

    def chioce_quantity_for_item(self):
        choice = random.choice(self.catalogPantsXpath)
        time.sleep(2)

        sizes = ['32', '33', '34', '35', '36']
        numbers = [1, 2, 3]
        common_funtions.choosing_items_quantity(self.driver, sizes, numbers, choice,
                                                           self.size_list_xpath, self.color_xpaths)

    def quantity_input(self, quantity):
        self.driver.find_element(By.CSS_SELECTOR, self.quantity_input_selector).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.quantity_input_selector).send_keys(quantity)
