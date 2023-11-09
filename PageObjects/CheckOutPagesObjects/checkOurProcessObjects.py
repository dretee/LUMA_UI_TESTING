import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class checkOutProcessObjects:
    cart_selector = "action showcart active"
    proceed_to_checkout_id = "top-cart-btn-checkout"
    first_name_xpath = "//input[@class='input-text' and @name='firstname']"
    last_name_xpath = "//input[@class='input-text' and @name='lastname']"
    company_xpath = "//input[@class='input-text' and @name='company']"
    street_address_xpath = "//input[@class='input-text' and @name='street[0]']"
    city_xpath = "//input[@class='input-text' and@name='city']"
    zip_code_xpath = "//input[@class='input-text' and @name='postcode']"
    phone_number_xpath = "//input[@class='input-text' and @name='telephone']"
    save_checkbox_id = "shipping-save-in-address-book"
    ship_here_button_xpath = "//button[@class='action primary action-save-address' and @type='button']"
    next_button_selector = "[data-role='opc-continue']"
    place_order_selector = "[title='Place Order']"
    country_xpath = "//select[@id = 'DOBNEWI']"
    state_xpath = "//select[@id = 'NJQ1KVP']"
    ship_to_selector = "[class =shipping-information-content]"

    def __init__(self, driver):
        self.driver = driver

    def proceedToCheckOut(self):
        wait = WebDriverWait(self.driver, 10, 2)
        cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.cart_selector)))
        cart_button.click()
        self.driver.find_element(By.ID, self.proceed_to_checkout_id).click()
        return self.driver.title

    def inputFirstName(self, firstname):
        self.driver.find_element(By.XPATH, self.first_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.first_name_xpath).send_keys(firstname)

    def inputLastName(self, lastname):
        self.driver.find_element(By.XPATH, self.last_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.last_name_xpath).send_keys(lastname)

    def inputCompany(self, company):
        self.driver.find_element(By.XPATH, self.company_xpath).clear()
        self.driver.find_element(By.XPATH, self.company_xpath).send_keys(company)

    def inputStreetAddress(self, address):
        self.driver.find_element(By.XPATH, self.street_address_xpath).clear()
        self.driver.find_element(By.XPATH, self.street_address_xpath).send_keys(address)

    def inputCity(self, city):
        self.driver.find_element(By.XPATH, self.city_xpath).clear()
        self.driver.find_element(By.XPATH, self.city_xpath).send_keys(city)

    def chooseState(self, option):
        state = Select(self.driver.find_element(By.XPATH, self.city_xpath))
        time.sleep(2)
        state.select_by_visible_text(option)
        time.sleep(2)

    def chooseCountry(self, option):
        country = Select(self.driver.find_element(By.XPATH, self.city_xpath))
        time.sleep(2)
        country.select_by_visible_text(option)

    def inputPhoneNumber(self, number):
        self.driver.find_element(By.XPATH, self.phone_number_xpath).clear()
        self.driver.find_element(By.XPATH, self.phone_number_xpath).send_keys(number)

    def clickOnNextButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.next_button_selector).click()
        wait = WebDriverWait(self.driver, 10, 2)
        shipping_infor = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.ship_to_selector)))
        return shipping_infor.text

    def clickPlaceOrder(self):
        wait = WebDriverWait(self.driver, 10, 2)
        place_Order = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.place_order_selector)))
        place_Order.click()


