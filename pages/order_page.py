import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage, OrderPageLocators):
    page_url = "https://qa-scooter.praktikum-services.ru/order"

    @allure.step('Проверяем является ли страница Главной')
    def check_is_main_page(self):
        assert self.find(self.MAIN_PAGE_HEADER).is_enabled()

    @allure.step('Проверяем является ли страница начальной страницей Яндекса')
    def check_is_yandex_page(self):
        self.switch_tab()
        assert self.find(self.YANDEX_PAGE_HEADER).is_displayed()

    @allure.step('Нажатие на логотип Самоката')
    def go_main(self):
        self.find(self.MAIN_PAGE_BADGE).click()

    @allure.step('Нажатие на логотип Яндекса')
    def go_yandex(self):
        self.find(self.YANDEX_BADGE).click()

    @allure.step('Заполнение поля Имя текстом: {text}')
    def fill_name(self, text):
        element = self.find(self.INPUT_NAME)
        element.send_keys(text)

    @allure.step('Заполнение поля Фамилия текстом: {text}')
    def fill_family(self, text):
        element = self.find(self.INPUT_FAMILY)
        element.send_keys(text)

    @allure.step('Заполнение поля Адрес текстом: {text}')
    def fill_address(self, text):
        element = self.find(self.INPUT_ADDRESS)
        element.send_keys(text)

    @allure.step('Заполнение поля Телефон текстом: {text}')
    def fill_phone(self, text):
        element = self.find(self.INPUT_PHONE)
        element.send_keys(text)

    @allure.step('Выбор станици метро: {text}')
    def fill_metro(self, text):
        element = self.find(self.INPUT_METRO)
        element.click()
        element.send_keys(text)
        station_btn = self.find(self.METRO_STATION, station=text)
        station_btn.click()

    @allure.step('Выбор даты в календаре: {date}')
    def fill_date(self, date):
        element = self.find(self.INPUT_DATE)
        element.click()
        date_element = self.find(self.CALENDAR_DATE, date=date)
        date_element.click()

    @allure.step('Заполнение поля Срок аренды на {days} суток')
    def fill_rent(self, days):
        element = self.find(self.INPUT_RENT)
        element.click()
        if days == 1:
            days_text = "сутки"
        elif days == 2:
            days_text = "двое суток"
        elif days == 3:
            days_text = "трое суток"
        elif days == 4:
            days_text = "четверо суток"
        elif days == 5:
            days_text = "пятеро суток"
        elif days == 6:
            days_text = "шестеро суток"
        else:
            days_text = "семеро суток"

        option = self.find(self.RENT_OPTION, days=days_text)
        option.click()

    @allure.step('Выбор черного цвета самоката')
    def add_color_black(self):
        self.find(self.INPUT_COLOR_BLACK).click()

    @allure.step('Выбор серого цвета самоката')
    def add_color_gray(self):
        self.find(self.INPUT_COLOR_GRAY).click()

    @allure.step('Заполнение поля Комментарий текстом: {text}')
    def fill_comment(self, text):
        element = self.find(self.INPUT_COMMENT)
        element.send_keys(text)

    @allure.step('Заполнение первой страницы формы')
    def fill_form_first_page(
            self,
            name,
            family,
            address,
            phone,
            metro,
    ):
        self.fill_name(name)
        self.fill_family(family)
        self.fill_address(address)
        self.fill_phone(phone)
        self.fill_metro(metro)

    @allure.step('Переход ко второй части формы')
    def submit_form_first_page(self):
        self.find(self.FIRST_PAGE_SUBMIT_BTN).click()

    @allure.step('Заполнение второй страницы формы')
    def fill_form_second_page(
            self,
            date,
            rent,
            is_black,
            comment,
    ):
        self.fill_date(date)
        self.fill_rent(rent)
        if is_black:
            self.add_color_black()
        else:
            self.add_color_gray()
        self.fill_comment(comment)

    @allure.step('Завершение заполнения формы')
    def submit_form_second_page(self):
        self.find(self.SECOND_PAGE_SUBMIT_BTN).click()

    @allure.step('Проверка наличия всплывающего окна')
    def check_approve_popup(self):
        assert self.find(self.APPROVE_RENT_BTN).is_displayed()
