from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class checkOutObjects:
    # define all the elements and their locators
    proceed_to_checkout_id = "top-cart-btn-checkout"
    first_name_xpath = "//input[@class='input-text' and @id='US5T5MK']"
    last_name_xpath = "//input[@class='input-text' and @id='MG1PTOQ']"
    company_xpath = "//input[@class='input-text' and @id='U57MC4O']"
    street_address_xpath = "//input[@class='input-text' and @id='JP2XYEP']"
    city_xpath = "//input[@class='input-text' and @id='K30LXDL']"
    zip_code_xpath = "//input[@class='input-text' and @id='NGGL4GY']"
    phone_number_xpath = "//input[@class='input-text' and @id='U3D5O0M']"
    save_checkbox_id = "shipping-save-in-address-book"
    ship_here_button_xpath = "//button[@class='action primary action-save-address' and @type='button']"
    next_button_selector = "[data-role='opc-continue']"
    place_order_selector = "[title='Place Order']"
