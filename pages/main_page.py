import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage, MainPageLocators):

    @allure.step('Переход к заказу по кнопке в меню')
    def go_order_by_menu(self):
        self.find(self.MENU_ORDER_BTN).click()

    @allure.step('Переход к заказу по кнопке в теле основной страницы')
    def go_order_by_body(self):
        self.find(self.BODY_ORDER_BTN).click()

    @allure.step('Проверка, является ли страница, страницей заказа')
    def check_is_order_page(self):
        assert self.find(self.ORDER_PAGE_HEADER).is_displayed()

    @allure.step('Получение текста ответа по заданному вопросу: {message}')
    def get_answer(self, message):
        result = self.find(self.ANSWER, message=message)
        return result

    @allure.step('Нажатие на строку вопроса: {question}')
    def click_question(self, question):
        element = self.find(self.QUESTION, message=question)
        element.click()
        self.wait(1)

    @allure.step('Проверка, что заданному вопросу ({text}) соответствует ответ ({expected})')
    def check_question(self, text, expected):
        # Проверка что по нажатию на вопрос в аккардионе октрывается правильный текст
        self.open()
        self.scroll_to_bottom()
        self.click_question(text)

        assert self.get_answer(expected).is_displayed()
