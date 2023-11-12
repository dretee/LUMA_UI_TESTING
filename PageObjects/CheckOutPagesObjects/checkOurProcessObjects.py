import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class checkOutProcessObjects:
    # ids are dynamic
    cart_name = "//a[@class='action showcart']"
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
    country_input_xpath = "//div[@name='shippingAddress.country_id']//div[@class='control']"
    country_xpath = "//select[@name='country_id']"
    state_input_xpath = "//div[@name='shippingAddress.region_id']//div[@class='control']"
    state_xpath = "//select[@name='region_id']"
    ship_to_selector = "[class =shipping-information-content]"

    def __init__(self, driver):
        self.driver = driver

    def proceedToCheckOut(self):
        wait = WebDriverWait(self.driver, 10, 2)
        cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.cart_name)))
        cart_button.click()

        self.driver.find_element(By.ID, self.proceed_to_checkout_id).click()
        return self.driver.title

    def inputFirstName(self, firstname):
        wait = WebDriverWait(self.driver, 10, 2)
        inputFirstName = wait.until(EC.element_to_be_clickable((By.XPATH, self.first_name_xpath)))
        inputFirstName.clear()
        inputFirstName.send_keys(firstname)

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
        self.driver.find_element(By.XPATH,self.state_input_xpath ).click()
        time.sleep(4)
        state = Select(self.driver.find_element(By.XPATH, self.city_xpath))

        state.select_by_value(option)
        time.sleep(2)

    def chooseCountry(self, option):
        self.driver.find_element(By.XPATH, self.country_input_xpath).click()
        time.sleep(5)
        country = Select(self.driver.find_element(By.XPATH, self.city_xpath))
        time.sleep(2)
        country.select_by_value(option)

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


