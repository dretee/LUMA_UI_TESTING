from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def sizePicker(driver, size, size_list_xpath):
    wait = WebDriverWait(driver, 10)
    # Find all size elements using the provided XPATH
    sizes = size_list_xpath

    # Check the provided size and click the corresponding element
    if size == "XS" or "36":
        wait.until(EC.element_to_be_clickable((By.XPATH, sizes[0]))).click()  # Click on the XS size element
    elif size == "S" or "35":
        wait.until(EC.element_to_be_clickable((By.XPATH, sizes[1]))).click()  # Click on the S size element
    elif size == "M" or "34":
        wait.until(EC.element_to_be_clickable((By.XPATH, sizes[2]))).click()  # Click on the M size element
    elif size == "L" or "33":
        wait.until(EC.element_to_be_clickable((By.XPATH, sizes[3]))).click()  # Click on the L size element
    elif size == "XL" or "32":
        wait.until(EC.element_to_be_clickable((By.XPATH, sizes[4]))).click()  # Click on the XL size element


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
