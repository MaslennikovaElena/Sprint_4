from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    driver: WebDriver = ...
    page_url = "https://qa-scooter.praktikum-services.ru/"

    BODY = [By.TAG_NAME, "body"]
    ACCEPT_COOKIES_BTN = [By.XPATH, "//button[text()='да все привыкли']"]

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.page_url)
        self.accept_cookies()

    def wait(self, seconds, condition=lambda _: False):
        try:
            WebDriverWait(self.driver, seconds).until(condition)
        except TimeoutException as ignore:
            pass

    def find(self, descriptor, **kwargs):
        result = self.driver.find_element(by=descriptor[0], value=descriptor[1].format(**kwargs))
        return result

    def accept_cookies(self):
        accept_btn = self.find(self.ACCEPT_COOKIES_BTN)
        accept_btn.click()

    def scroll_to_bottom(self):
        # Прокрутка страницы до тех пор пока не станет виден блок вопросов
        body = self.find(self.BODY)
        for idx in range(10):
            body.send_keys(Keys.PAGE_DOWN)

    def switch_tab(self):
        for handle in self.driver.window_handles:
            if handle != self.driver.current_window_handle:
                self.driver.switch_to.window(handle)
                break