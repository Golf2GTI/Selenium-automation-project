import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.base_page import BasePage
from random_word import RandomWords

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_cant_see_success_message(browser):
    """
    Test guest can't see success message on product page.
    """
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    """
    Test guest can add product to cart, check that added product name and price is correct.
    """
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_button()
    page.correct_product_name_in_message()
    page.correct_price_in_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """
    Test guest can't see success message after adding product to cart.
    """
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_button()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    Test message disappeared after adding product to cart.
    """
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_button()
    page.is_message_dissappeared()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """
    Test guest can go to login page from product page.
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """
    Test guest can't see product in cart opened from product page.
    """
    page = ProductPage(browser, link)
    page.open()
    page.guest_click_go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()


def test_guest_should_see_login_link_on_product_page(browser):
    """
    Test guest should see login link on product page.
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        r = RandomWords()
        self.email = r.get_random_word() + "@fakemail.org"
        self.password = r.get_random_word() + "123"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(self.email, self.password)
        page = BasePage(browser, link)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        """
        Test user can't see success message on opened product page.
        """
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """
        Test user can add product to cart, check that added product name and price is correct.
        """
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart_button()
        page.correct_product_name_in_message()
        page.correct_price_in_basket()
