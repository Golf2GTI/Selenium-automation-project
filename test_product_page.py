from pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_button()
    page.solve_quiz_and_get_code()
    page.correct_product_name_in_message()
    page.correct_price_in_basket()



