from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".price_color")
    ALERT_ADDING_PRODUCT = (By.CSS_SELECTOR, "#messages .alertinner strong")
    ALERT_PRICE_BASKET = (By.CSS_SELECTOR, "#messages .alertinner p strong ")
