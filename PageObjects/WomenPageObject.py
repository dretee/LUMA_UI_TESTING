import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class WomenPageObject:
    women_link_xpath = "//a[@id='ui-id-4']"
    top_xpath = "//div[@class='block filter']//li[1]"
    bottom_xpath = "//div[@class='block filter']//li[1]"
    hoodies_sweatshirt_xpath = "//a[contains(text(),'Hoodies & Sweatshirts')]"
    jackets_xpath = "//a[contains(text(),'Jackets')]"
    tees_xpath = "//a[contains(text(),'Tees')]"
    bras_tanks_xpath = "//a[contains(text(),'Bras & Tanks')]"
    pants_xpaths = "//a[contains(text(),'Pants')]"
    shorts_xpaths ="//a[contains(text(),'Shorts')]"


    # test the links
    # test adding to the cart
    # test removing from the cart
    # test the checking out process
    # test extreme cases of adding more quanties and seeing the response, both empty cart should be considered