from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_PRODUCTS = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, ".content>#content_inner>p>a")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#register_form input[name='registration-email']")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#register_form input[name='registration-password1']")
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#register_form input[name='registration-password2']")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form button[name='registration_submit']")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".price_color")
    ALERT_ADDING_PRODUCT = (By.CSS_SELECTOR, "#messages .alertinner strong")
    ALERT_PRICE_BASKET = (By.CSS_SELECTOR, "#messages .alertinner p strong ")
