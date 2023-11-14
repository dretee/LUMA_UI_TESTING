import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class loginObject:
    # define all the page elements via their locator
    signin_xpath = "//a[contains(text(),'Sign In')]"
    email_id = "email"
    password_id = "pass"
    login_button_id = "send2"
    forgot_password_cssselector = "a[class='action remind']"
    welcome_message_selector = "span[class='logged-in']"
    dropdown_selector = "button[type= 'button']"
    logout_xpath = "//a[contains(text(),'Sign Out')]"
    error_alert_xpath = "//div[@role='alert']/div/div"


    def __init__(self, driver):
        self.driver = driver

    def click_signin_link(self):
        self.driver.find_element(By.XPATH, self.signin_xpath).click()

    def inputEmail(self, email):
        self.driver.find_element(By.ID, self.email_id).clear()
        self.driver.find_element(By.ID, self.email_id).send_keys(email)
        return self.driver.find_element(By.ID, self.email_id).is_displayed()

    def inputPassword(self, password):
        self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(password)
        return self.driver.find_element(By.ID, self.password_id).is_displayed()

    def click_login_button(self):
        self.driver.find_element(By.ID, self.login_button_id).click()

    def click_on_forgot_password_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.forgot_password_cssselector).click()

    def login_alert(self):
        wait = WebDriverWait(self.driver, 10)
        time.sleep(4)
        alert = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.welcome_message_selector)))
        return alert.text

    def error_alert(self):
        wait = WebDriverWait(self.driver, 10)
        time.sleep(5)
        alert = wait.until(EC.visibility_of_element_located((By.XPATH, self.error_alert_xpath)))
        return alert.text

    def click_logout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.dropdown_selector).click()
        self.driver.find_element(By.XPATH, self.logout_xpath).click()