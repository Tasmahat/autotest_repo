import pytest

from .pages.product_page import PageObject


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"])
def test_guest_can_add_product_to_basket(browser, link):
    page = PageObject(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.send_message()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = PageObject(browser, "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = PageObject(browser, "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = PageObject(browser, "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
    page.open()
    page.add_to_cart()
    page.should_disappear()
