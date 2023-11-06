import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.ItemsForMenPagesObjects import common_funtions


class ShortsObjects:
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
        "//a[normalize-space()='Pierce Gym Short']",
        "//a[normalize-space()='Orestes Fitness Short']",
        "//a[normalize-space()='Torque Power Short']",
        "//a[normalize-space()='Apollo Running Short']"]

    def __init__(self, driver):
        self.driver = driver

    def addToCart(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.add_to_cart_button_id))).click()

    def choiceForSizeAndColor(self):
        time.sleep(2)

        sizes = ['32', '33', '34', '35', '36']
        numbers = [1, 2, 3]
        wait = WebDriverWait(self.driver, 10)
        list_of_prices = []
        for xpath in self.catalogShortsXpath:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()

            # getting a random size for the item
            size, number = random.choice(sizes), random.choice(numbers)

            common_funtions.sizePicker(self.driver, size, self.size_list_xpath)

            common_funtions.colorPicker(self.driver, number, self.color_xpaths)

            price = self.driver.find_element(By.XPATH, self.price_locator).get_attribute("data-price-amount")
            list_of_prices.append(price)

            self.addToCart()
            time.sleep(3)
            self.driver.back()
