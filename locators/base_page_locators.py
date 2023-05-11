from selenium.webdriver.common.by import By


class BasePageLocators:
    BODY = [By.TAG_NAME, "body"]
    """Указание на тело HTML страницы"""
    ACCEPT_COOKIES_BTN = [By.XPATH, "//button[text()='да все привыкли']"]
    """Кнопка подтверждения использования COOKIES"""
