from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocator():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, '#messages > .alert:nth-child(1) > .alertinner strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, '#messages > .alert:nth-child(3) > .alertinner strong')
    PRICE = (By.CSS_SELECTOR, 'p.price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert-success:nth-child(1)')

