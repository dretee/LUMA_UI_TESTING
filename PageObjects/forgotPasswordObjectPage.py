from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class forgot_password:
    # locators to elements on the page
    email_id = "email_address"
    reset_password_selector = "button[class='action submit primary']"
    alert_popup_xpath = "//div[@role='alert']/div/div"

    def __init__(self, driver):
        self.driver = driver

    def inputEmaiAddress(self, email):
        self.driver.find_element(By.ID, self.email_id).clear()
        self.driver.find_element(By.ID, self.email_id).send_keys(email)

    def clickResetButton(self):
        self.driver.find_element(By.CSS_SELECTOR, self.reset_password_selector).click()

    def alert_popup(self):
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.visibility_of_element_located((By.XPATH, self.alert_popup_xpath)))
        return alert.text




