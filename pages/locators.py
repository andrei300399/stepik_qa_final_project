from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_formm")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_formm")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".price_color")
    ALERT_ADDING_PRODUCT = (By.CSS_SELECTOR, "#messages .alertinner strong")
    ALERT_PRICE_BASKET = (By.CSS_SELECTOR, "#messages .alertinner p strong ")
