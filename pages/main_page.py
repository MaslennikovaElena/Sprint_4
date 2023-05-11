
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    QUESTION = [By.XPATH, "//div[@data-accordion-component='AccordionItemButton'][text()='{message}']"]
    ANSWER_BOX = [By.XPATH, f"{QUESTION}/parent::div/parent::div/div[@data-accordion-component='AccordionItemPanel']"]
    ANSWER = [By.XPATH, "//p[text()='{message}']/parent::div"]

    MENU_ORDER_BTN = [By.XPATH, "//div[@id='root']/div/div/div/div/button[text()='Заказать']"]
    BODY_ORDER_BTN = [By.XPATH, "//div[@id='root']/div/div/div/div/div/button[text()='Заказать']"]
    ORDER_PAGE_HEADER = [By.XPATH, "//div[text()='Для кого самокат']"]

    def go_order_by_menu(self):
        self.find(self.MENU_ORDER_BTN).click()

    def go_order_by_body(self):
        self.find(self.BODY_ORDER_BTN).click()

    def check_is_order_page(self):
        assert self.find(self.ORDER_PAGE_HEADER).is_displayed()


    def get_answer(self, message):
        result = self.find(self.ANSWER, message=message)
        return result

    def scroll_to_bottom(self):
        # Прокрутка страницы до тех пор пока не станет виден блок вопросов
        body = self.find(self.BODY)
        for idx in range(10):
            body.send_keys(Keys.PAGE_DOWN)

    def click_question(self, question):
        element = self.find(self.QUESTION, message=question)
        element.click()
        self.wait(0.5)

    def check_question(self, text, expected):
        # Проверка что по нажатию на вопрос в аккардионе октрывается правильный текст
        self.open()
        self.scroll_to_bottom()
        self.click_question(text)

        assert self.get_answer(expected).is_displayed()
