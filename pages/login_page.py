from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'login not in url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"


class BasketPage(BasePage):
    def should_be_correct_information_about_book(self):
        self.name_book_in_basket_is_name_book_in_catalog()
        self.price_book_in_basket_is_price_book_in_catalog()
        self.print_text_name_book_in_basket()
        self.print_text_price_book_in_basket()

    def print_text_name_book_in_basket(self):
        print(self.text_of_locator(*LoginPageLocators.NAME_BOOK_IN_BASKET) + " added to basket")

    def name_book_in_basket_is_name_book_in_catalog(self):
        assert self.text_of_locator(*LoginPageLocators.NAME_BOOK_IN_BASKET) == self.text_of_locator(*LoginPageLocators.NAME_BOOK), "Добавлена неверная книга"

    def print_text_price_book_in_basket(self):
        print(self.text_of_locator(*LoginPageLocators.PRICE_BOOK_IN_BASKET) + " is prise the book")

    def price_book_in_basket_is_price_book_in_catalog(self):
        assert self.text_of_locator(*LoginPageLocators.PRICE_BOOK_IN_BASKET) == self.text_of_locator(*LoginPageLocators.PRICE_BOOK), "Price is not correct"



