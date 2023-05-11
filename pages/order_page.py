from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OrderPage(BasePage):
    page_url = "https://qa-scooter.praktikum-services.ru/order"

    ORDER_PAGE_HEADER = [By.XPATH, "//div[text()='Для кого самокат']"]

    MAIN_PAGE_BADGE = [By.XPATH, "//img[@alt='Scooter']/parent::a"]
    MAIN_PAGE_HEADER = [By.XPATH, "//div/br/parent::div/div/br"]

    YANDEX_BADGE = [By.XPATH, "//img[@alt='Yandex']/parent::a"]
    YANDEX_PAGE_HEADER = [By.XPATH, "//a[@aria-label='Логотип Дзен']"]

    MENU_ORDER_BTN = [By.XPATH, "//div[@id='root']/div/div/div/div/button[text()='Заказать']"]
    BODY_ORDER_BTN = [By.XPATH, "//div[@id='root']/div/div/div/div/div/button[text()='Заказать']"]

    INPUT_NAME = [By.XPATH, "//input[@type='text'][@placeholder='* Имя']"]
    INPUT_FAMILY = [By.XPATH, "//input[@type='text'][@placeholder='* Фамилия']"]
    INPUT_ADDRESS = [By.XPATH, "//input[@type='text'][@placeholder='* Адрес: куда привезти заказ']"]
    INPUT_PHONE = [By.XPATH, "//input[@type='text'][@placeholder='* Телефон: на него позвонит курьер']"]
    INPUT_METRO = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    INPUT_DATE = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    CALENDAR_DATE = [By.XPATH, "//button[text()='Previous Month']/parent::div//div[text()='{date}']"]
    INPUT_RENT = [By.XPATH, "//div[text()='* Срок аренды']"]
    RENT_OPTION = [By.XPATH, "//div[@role='option'][text()='{days}']"]
    INPUT_COLOR_BLACK = [By.XPATH, "//label[@for='black']"]
    INPUT_COLOR_GRAY = [By.XPATH, "//label[@for='gray']"]
    INPUT_COMMENT = [By.XPATH, "//input[@type='text'][@placeholder='Комментарий для курьера']"]

    METRO_STATION = [By.XPATH, "//div[text()='{station}']/parent::button"]
    FIRST_PAGE_SUBMIT_BTN = [By.XPATH, "//button[text()='Далее']"]
    SECOND_PAGE_SUBMIT_BTN = [By.XPATH, "//div[text()='Про аренду']/parent::div//button[text()='Заказать']"]

    APPROVE_RENT_BTN = [By.XPATH, "//div[text()='Хотите оформить заказ?']/parent::div//button[text()='Да']"]

    def check_is_order_page(self):
        assert self.find(self.ORDER_PAGE_HEADER).is_displayed()

    def check_is_main_page(self):
        assert self.find(self.MAIN_PAGE_HEADER).is_displayed()

    def check_is_yandex_page(self):
        self.switch_tab()
        assert self.find(self.YANDEX_PAGE_HEADER).is_displayed()

    def go_main(self):
        self.find(self.MAIN_PAGE_BADGE).click()

    def go_yandex(self):
        self.find(self.YANDEX_BADGE).click()

    def go_order_by_menu(self):
        self.find(self.MENU_ORDER_BTN).click()

    def go_order_by_body(self):
        self.find(self.BODY_ORDER_BTN).click()

    def fill_name(self, text):
        element = self.find(self.INPUT_NAME)
        element.send_keys(text)

    def fill_family(self, text):
        element = self.find(self.INPUT_FAMILY)
        element.send_keys(text)

    def fill_address(self, text):
        element = self.find(self.INPUT_ADDRESS)
        element.send_keys(text)

    def fill_phone(self, text):
        element = self.find(self.INPUT_PHONE)
        element.send_keys(text)

    def fill_metro(self, text):
        element = self.find(self.INPUT_METRO)
        element.click()
        element.send_keys(text)
        station_btn = self.find(self.METRO_STATION, station=text)
        station_btn.click()

    def fill_date(self, date):
        element = self.find(self.INPUT_DATE)
        element.click()
        date_element = self.find(self.CALENDAR_DATE, date=date)
        date_element.click()

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

    def add_color_black(self):
        self.find(self.INPUT_COLOR_BLACK).click()

    def add_color_gray(self):
        self.find(self.INPUT_COLOR_GRAY).click()

    def fill_comment(self, text):
        element = self.find(self.INPUT_COMMENT)
        element.send_keys(text)


    def fill_form_first_page(self):
        self.fill_name("Елена")
        self.fill_family("Масленникова")
        self.fill_address("Кустанайская 5")
        self.fill_phone("+79998887766")
        self.fill_metro("Красногвардейская")

    def submit_form_first_page(self):
        self.find(self.FIRST_PAGE_SUBMIT_BTN).click()

    def fill_form_second_page(self):
        self.fill_date("11")
        self.fill_rent(2)
        self.add_color_black()
        self.fill_comment("Тащить без лифта на 13 этаж")

    def submit_form_second_page(self):
        self.find(self.SECOND_PAGE_SUBMIT_BTN).click()

    def approve_rent(self):
        self.find(self.APPROVE_RENT_BTN).click()

    def check_approve_popup(self):
        assert self.find(self.APPROVE_RENT_BTN).is_displayed()
