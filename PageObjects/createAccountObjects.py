import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class accountCreationObjects:

    accountCreation_xpath = "//div[@class='panel header']//a[normalize-space()='Create an Account']"
    fristname_input_id = "firstname"
    lastname_input_id = "lastname"
    email_input_xpath = "//input[@id='email_address']"
    password_input_xpath = "//input[@id='password']"
    confirm_password_input_xpath = "//input[@id='password-confirmation']"
    accountCreation_button_xpath = "//button[@title='Create an Account']"
    sign_in_link_xpath = "//div[@class='panel header']//a[contains(text(),'Sign In')]"
    sign_in_page_creation_button_xpath = "//a[@class='action create primary']"
    email_sign_in_input_xpath = "//input[@id='email']"
    password_sign_in_input_xpath = "//fieldset[@class='fieldset login']//input[@id='pass']"
    sign_button_name = "send"
    logout_drop_down_xpath = "//div[@class='panel header']//button[@type='button']"
    Logout_xpath = "//div[@aria-hidden='false']//a[normalize-space()='Sign Out']"  # has three links to return
    list_of_the_welcompage_xapath = "//ul[@class='nav items']//a"
    My_account_xpath = "//div[@aria-hidden='false']//a[normalize-space()='My Account']"
    wish_list_xpath = "//div[@aria-hidden='false']//a[normalize-space()='My Wish List']"
    myorder_xpath = "//a[normalize-space()='My Orders']"
    Downloadable_Products_xpath = "//a[normalize-space()='My Downloadable Products']"
    mywish_list_xpath = "//li[@class='nav item']//a[normalize-space()='My Wish List']"
    address_book_xpath = "//a[normalize-space()='Address Book']"
    address_info_xpath = "//a[normalize-space()='Account Information']"
    Stored_Payment_Methods_xpath = "//a[normalize-space()='Stored Payment Methods']"
    product_review_xpath = "//a[normalize-space()='My Product Reviews']"
    accountCreation_xpath = "//div[@class='panel header']//a[normalize-space()='Create an Account']"

    # ... (other variables)

    def __init__(self, driver):
        self.driver = driver

    # Objects and their action definition for the creation of an account
    def createAccount(self):
        # Click on the 'Create an Account' link and check if the correct page is loaded
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.accountCreation_xpath))).click()
        if self.driver.title == "Create New Customer Account":
            return True
        else:
            return False

    def signinCreateAccount(self):
        # Click on the 'Sign In' button and check if the correct page is loaded
        self.driver.find_element(By.XPATH, self.sign_in_page_creation_button_xpath).click()
        if self.driver.title == "Create New Customer Account":
            return True
        else:
            return False

    def inputNames(self, firstname, lastname):
        # Input first name and last name in respective input fields
        self.driver.find_element(By.ID, self.fristname_input_id).send_keys(firstname)
        self.driver.find_element(By.ID, self.lastname_input_id).send_keys(lastname)

    def inputEmail(self, email):
        # Input email in the email input field
        self.driver.find_element(By.XPATH, self.email_input_xpath).send_keys(email)

    def inputPasswords(self, password):
        # Input password and confirm password in their respective input fields
        self.driver.find_element(By.XPATH, self.password_input_xpath).send_keys(password)
        time.sleep(2)  # Wait for a few seconds before entering confirm password
        self.driver.find_element(By.XPATH, self.confirm_password_input_xpath).send_keys(password)

    def createButton(self):
        # Click on the 'Create an Account' button
        self.driver.find_element(By.XPATH, self.accountCreation_button_xpath).click()

    # Objects and their action definition for the sign-in process
    def path_to_signinButton(self):
        # Click on the 'Sign In' link
        self.driver.find_element(By.XPATH, self.sign_in_link_xpath).click()

    def emailSignin(self, email):
        # Input email in the sign-in email input field
        self.driver.find_element(By.XPATH, self.email_sign_in_input_xpath).send_keys(email)

    def passwordSignin(self, password):
        # Input password in the sign-in password input field
        self.driver.find_element(By.XPATH, self.password_sign_in_input_xpath).send_keys(password)

    def signinButton(self):
        # Click on the 'Sign In' button
        self.driver.find_element(By.NAME, self.sign_button_name).click()

    def log_dropdown(self, function):
        # Click on the logout dropdown and perform actions based on the provided function parameter
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.logout_drop_down_xpath))).click()
        if function == "my account":
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.My_account_xpath))).click()
        elif function == "my wish list":
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.wish_list_xpath))).click()
        else:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Logout_xpath))).click()

    def list_of_prompt_on_welcomepage(self):
        # Click on various links and return a list of displayed page titles
        list_of_items = [self.myorder_xpath, self.Downloadable_Products_xpath, self.mywish_list_xpath,
                         self.address_book_xpath, self.address_info_xpath, self.Stored_Payment_Methods_xpath,
                         self.product_review_xpath]
        displayed_list = [self.driver.title]
        for link in list_of_items:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, link)))
            element.click()
            displayed_list.append(self.driver.title)
        return displayed_list

    def email_generator(self):
        # Generate a random email address
        validchars = 'abcdefghijklmnopqrstuvwxyz1234567890'
        loginlen = random.randint(4, 15)
        login = ''
        for i in range(loginlen):
            pos = random.randint(0, len(validchars) - 1)
            login = login + validchars[pos]
        if login[0].isnumeric():
            pos = random.randint(0, len(validchars) - 10)
            login = validchars[pos] + login
        servers = ['@gmail', '@yahoo', '@redmail', '@hotmail', '@bing']
        servpos = random.randint(0, len(servers) - 1)
        email = login + servers[servpos]
        tlds = ['.com', '.in', '.gov', '.ac.in', '.net', '.org']
        tldpos = random.randint(0, len(tlds) - 1)
        email = email + tlds[tldpos]

        return email