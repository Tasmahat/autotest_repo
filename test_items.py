from selenium.webdriver.common.by import By


def test(browser):
    try:
        browser.get("https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")

        button = browser.find_elements(By.CSS_SELECTOR, 'button.btn-add-to-basket')

        assert len(button) > 0, "Site has no button"

    finally:
        browser.quit()


