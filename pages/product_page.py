from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_product_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()


    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()


    def should_be_correct_product_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        success_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name == success_name, f"Expected '{product_name}' in success message, got '{success_name}'"


    def should_be_correct_price_in_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price == basket_total, f"Expected basket total '{product_price}', got '{basket_total}'"