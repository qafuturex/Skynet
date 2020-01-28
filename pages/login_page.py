from .base_page import BasePage
from .locators import LoginPageLocator
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login1' in self.browser.current_url, "url is incorrect"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocator.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocator.REGISTER_FORM), "Register form is not present"
