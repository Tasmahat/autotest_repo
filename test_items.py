from selenium.webdriver.common.by import By
import time


def test_has_add_to_cart_button(browser):
    try:
        browser.get("https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")

        button = browser.find_elements(By.CSS_SELECTOR, 'button.btn-add-to-basket')

        assert len(button) > 0, "Site has no button"

    finally:
        time.sleep(5)
        browser.quit()
