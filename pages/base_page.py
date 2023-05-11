import allure
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import BasePageLocators


class BasePage(BasePageLocators):
    driver: WebDriver = ...
    page_url = "https://qa-scooter.praktikum-services.ru/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        with allure.step('Открываем страницу {self.page_url}'.format(self=self)):
            self.driver.get(self.page_url)
            self.accept_cookies()

    @allure.step('Запускаем ожидание на {seconds} секунд')
    def wait(self, seconds, condition=lambda _: False):
        try:
            WebDriverWait(self.driver, seconds).until(condition)
        except TimeoutException as ignore:
            pass

    def find(self, descriptor, **kwargs):
        result = self.driver.find_element(by=descriptor[0], value=descriptor[1].format(**kwargs))
        return result

    @allure.step('Принимаем работу с COOKIES')
    def accept_cookies(self):
        accept_btn = self.find(self.ACCEPT_COOKIES_BTN)
        accept_btn.click()

    @allure.step('Прокрутка страницы до самого низа')
    def scroll_to_bottom(self):
        # Прокрутка страницы до тех пор пока не станет виден блок вопросов
        body = self.find(self.BODY)
        for idx in range(10):
            body.send_keys(Keys.PAGE_DOWN)

    @allure.step('Переключение вкладки браузера')
    def switch_tab(self):
        for handle in self.driver.window_handles:
            if handle != self.driver.current_window_handle:
                self.driver.switch_to.window(handle)
                break
