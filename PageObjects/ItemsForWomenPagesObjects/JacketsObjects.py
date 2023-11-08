import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.ItemsForWomenPagesObjects import common_funtions


class WomenJacketsObjects:
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

    catalogWomenJacketsXpath = [
        "//a[normalize-space()='Olivia 1/4 Zip Light Jacket']",
        "//a[normalize-space()='Jade Yoga Jacket']",
        "//a[normalize-space()='Ingrid Running Jacket']",
        "//a[normalize-space()='Josie Yoga Jacket']"]

    def __init__(self, driver):
        self.driver = driver

    def addToCart(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.add_to_cart_button_id))).click()

    def choiceForSizeAndColor(self):
        time.sleep(2)

        sizes = ['XS', 'S', 'M', 'L', 'XL']
        numbers = [1, 2, 3]

        returns = common_funtions.choosing_action_of_items(self.driver, sizes, numbers, self.catalogWomenJacketsXpath,
                                                           self.size_list_xpath, self.color_xpaths,
                                                           self.add_to_cart_button_id, self.price_locator)
        list_of_prices, list_of_items = returns

        return list_of_prices, list_of_items
