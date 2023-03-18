from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart_button(self):
        add_to_cart_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart_btn.click()
    def correct_product_name_in_message(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
    def correct_price_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ADD_MESSAGE), \
            "Success message is presented, but should not be"
    def is_message_dissappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ADD_MESSAGE), \
            "Success message is not disappeared, but should"




