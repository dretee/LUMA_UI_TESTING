import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def sizePicker(driver, size, size_list_xpath):
    wait = WebDriverWait(driver, 10)
    # Find all size elements using the provided XPATH
    sizes = size_list_xpath

    # Check the provided size and click the corresponding element
    if size == "XS" or "28":
        wait.until(EC.element_to_be_clickable((By.XPATH, sizes[0]))).click()  # Click on the XS size element
    elif size == "S" or "29":
        wait.until(EC.element_to_be_clickable((By.XPATH, sizes[1]))).click()  # Click on the S size element
    elif size == "M" or "30":
        wait.until(EC.element_to_be_clickable((By.XPATH, sizes[2]))).click()  # Click on the M size element
    elif size == "L" or "31":
        wait.until(EC.element_to_be_clickable((By.XPATH, sizes[3]))).click()  # Click on the L size element
    elif size == "XL" or "32":
        wait.until(EC.element_to_be_clickable((By.XPATH, sizes[4]))).click()  # Click on the XL size element
    else:
        wait.until(EC.element_to_be_clickable((By.XPATH, sizes[0]))).click()  # Click on the XS size element


def colorPicker(driver, number, color_xpaths):
    # Check if the number is a valid key in the color_xpaths dictionary
    if number in color_xpaths:
        color_xpath = color_xpaths[number]

        # Wait for the color element to be clickable
        color_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, color_xpath))
        )

        # Click the color element
        color_element.click()
    else:
        colour_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, color_xpaths[1])))

        colour_element.click()
        raise ValueError(f"Invalid color number: {number}. Please provide a valid color number.")


def addToCart(driver, ID):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, ID))).click()


def choosing_action_of_items(driver, sizes, numbers, catalogXpath, size_list_xpath, color_xpaths, ID, price_locator):
    list_of_prices = []
    list_of_items = []
    wait = WebDriverWait(driver, 10)
    for xpath in catalogXpath:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        item_name = element.text
        element.click()

        # getting a random size for the item
        size, number = random.choice(sizes), random.choice(numbers)

        sizePicker(driver, size, size_list_xpath)

        colorPicker(driver, number, color_xpaths)

        price = driver.find_element(By.XPATH, price_locator).get_attribute("data-price-amount")
        list_of_prices.append(price)
        list_of_items.append(item_name)

        addToCart(driver, ID)
        time.sleep(3)
        driver.back()

    return list_of_prices, list_of_items
