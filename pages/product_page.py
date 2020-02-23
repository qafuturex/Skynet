from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_cart_button.click()

    def should_be_correct_product_name_in_message(self):
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        return product_name_in_message

    def should_be_correct_price_in_message(self):
        price_in_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text
        return price_in_message

    def should_be_message_product_added(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert self.should_be_correct_product_name_in_message() == product_name, "Wrong product name"

        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        assert self.should_be_correct_price_in_message() == price, "Wrong price"
