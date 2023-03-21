from pages.main_page import MainPage
from pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    When guest opens main page - the basket is empty.
    """
    page = MainPage(browser, link)
    page.open()
    page.guest_click_go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()


class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        """
        Guest is able to go to login page.
        """
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_link()

    def test_guest_should_see_login_link(self, browser):
        """
        Test guest should see login link on main page.
        """
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
