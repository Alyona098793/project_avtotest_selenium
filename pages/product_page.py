from .base_page import BasePage
from .locators import LoginPageLocators
from .login_page import LoginPage


class ProductPage(BasePage):

    def add_product_to_basket(self):
        basket_link = self.browser.find_element(*LoginPageLocators.ADD_FORM)
        basket_link.click()
        #return LoginPage(browser=self.browser, url=self.browser.current_url)

    #def should_be_login_link(self):
       # assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"