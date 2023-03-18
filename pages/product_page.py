from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart_button(self):
        add_to_cart_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart_btn.click()
    # def success_add_message(self):
    #     self.is_element_present(*ProductPageLocators.SUCCESS_ADD_MESSAGE)
    def correct_product_name_in_message(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
    def correct_price_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text




