from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    ADD_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    NAME_BOOK_IN_BASKET = (By.CSS_SELECTOR, "#messages strong")
    PRICE_BOOK_IN_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    PRICE_BOOK = (By.XPATH, '//div[@class = "col-sm-6 product_main"]/p')
    NAME_BOOK = (By.XPATH, '//div[@class = "col-sm-6 product_main"]/h1')
