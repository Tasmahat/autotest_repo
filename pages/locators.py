from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_OF_PRODUCT_ACTUAL = (By.CSS_SELECTOR, "div.alertinner strong")
    NAME_OF_PRODUCT_EXPECTED = (By.CSS_SELECTOR, "div.product_main h1")
    COST_OF_PRODUCT_ACTUAL = (By.CSS_SELECTOR, "#messages div.alert.alert-safe.alert-noicon.alert-info.fade.in div p:nth-child(1) strong")
    COST_OF_PRODUCT_EXPECTED = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alertinner ")