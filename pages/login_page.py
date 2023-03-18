from .base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
    def should_be_login_url(self):
        # реализуйте проверку подстроки login в url
        assert "login" in self.url, "No 'login' string in URL"
    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "LOGIN_FORM is not present"
    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "REGISTER_FORM is not present"
    def register_new_user(self, email, password):
        self.go_to_login_page()
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()

