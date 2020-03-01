from .base_page import BasePage
from .locators import LoginPageLocator
import datetime


class LoginPage(BasePage):

    def system_time(self):
        sys_time = str(datetime.datetime.now().strftime('%H%M%S'))
        return sys_time

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "url is incorrect"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocator.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocator.REGISTER_FORM), "Register form is not present"

    def register_new_user(self, email, password):
        self.go_to_login_page()
        register_login = self.browser.find_element(*LoginPageLocator.REGISTER_EMAIL)
        email = email + self.system_time() + '.ru'
        register_login.send_keys(email)
        register_password = self.browser.find_element(*LoginPageLocator.REGISTER_PASSWORD)
        password = password + self.system_time()
        register_password.send_keys(password)
        register_password_confirm = self.browser.find_element(*LoginPageLocator.REGISTER_PASSWORD_CONFIRM)
        register_password_confirm.send_keys(password)
        confirm_button = self.browser.find_element(*LoginPageLocator.REGISTER_SUBMIT)
        confirm_button.click()




