import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.ItemsForWomenPagesObjects import common_funtions


class WomenShortsObjects:
    add_to_cart_button_id = "product-addtocart-button"
    size_list_xpath = ["//div[@class='swatch-option text' and @role='option'][1]",
                       "//div[@class='swatch-option text' and @role='option'][2]",
                       "//div[@class='swatch-option text' and @role='option'][3]",
                       "//div[@class='swatch-option text' and @role='option'][4]",
                       "//div[@class='swatch-option text' and @role='option'][5]"]

    color_list_xpath1 = "//div[@role='listbox' and @aria-labelledby = 'option-label-color-93' ]//div[1]"
    color_list_xpath2 = "//div[@role='listbox' and @aria-labelledby = 'option-label-color-93' ]//div[2]"

    color_list_xpath3 = "//div[@role='listbox' and @aria-labelledby = 'option-label-color-93' ]//div[3]"
    price_locator = "//span[ @data-price-type='finalPrice']"

    color_xpaths = {
        1: color_list_xpath1,
        2: color_list_xpath2,
        3: color_list_xpath3
    }

    catalogShortsXpath = [
        "//a[normalize-space()='Gwen Drawstring Bike Short']",
        "//a[normalize-space()='Artemis Running Short']",
        "//a[normalize-space()='Mimi All-Purpose Short']",
        "//a[normalize-space()='Ina Compression Short']"]

    def __init__(self, driver):
        self.driver = driver

    def addToCart(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.add_to_cart_button_id))).click()

    def choiceForSizeAndColor(self):
        time.sleep(2)

        sizes = ['28', '29', '30', '31', '32']
        numbers = [1, 2, 3]

        returns = common_funtions.choosing_action_of_items(self.driver, sizes, numbers, self.catalogShortsXpath,
                                                           self.size_list_xpath, self.color_xpaths,
                                                           self.add_to_cart_button_id, self.price_locator)
        list_of_prices, list_of_items = returns

        return list_of_prices, list_of_items

