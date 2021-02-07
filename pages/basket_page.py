from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS), "Basket has products"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), "Not message about empty basket"
