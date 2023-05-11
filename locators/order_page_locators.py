from selenium.webdriver.common.by import By


class OrderPageLocators:
    MAIN_PAGE_BADGE = [By.XPATH, "//img[@alt='Scooter']/parent::a"]
    """Логотип самока"""
    MAIN_PAGE_HEADER = [By.XPATH, "//div/br/parent::div/div/br"]
    """Заголовок на главной странице"""

    YANDEX_BADGE = [By.XPATH, "//img[@alt='Yandex']/parent::a"]
    """Логотип Яндекса"""
    YANDEX_PAGE_HEADER = [By.XPATH, "//a[@aria-label='Логотип Дзен']"]
    """Заголовок на главной странице яндекса"""

    INPUT_NAME = [By.XPATH, "//input[@type='text'][@placeholder='* Имя']"]
    """Поле ввода Имени"""
    INPUT_FAMILY = [By.XPATH, "//input[@type='text'][@placeholder='* Фамилия']"]
    """Поле ввода фамилии"""
    INPUT_ADDRESS = [By.XPATH, "//input[@type='text'][@placeholder='* Адрес: куда привезти заказ']"]
    """Поле ввода Адреса"""
    INPUT_PHONE = [By.XPATH, "//input[@type='text'][@placeholder='* Телефон: на него позвонит курьер']"]
    """Поле ввода номера телефона"""
    INPUT_METRO = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    """Поле ввода станции метро"""
    METRO_STATION = [By.XPATH, "//div[text()='{station}']/parent::button"]
    """Строчка в выпадающем списке с заданной станцией метро"""
    INPUT_DATE = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    """Поле ввода даты"""
    CALENDAR_DATE = [By.XPATH, "//button[text()='Previous Month']/parent::div//div[text()='{date}']"]
    """Шаблон локатора для поле соответсвтующего дате (без месяца) во всплывающем календаре"""
    INPUT_RENT = [By.XPATH, "//div[text()='* Срок аренды']"]
    """Поле ввода срока аренды"""
    RENT_OPTION = [By.XPATH, "//div[@role='option'][text()='{days}']"]
    """Шаблон локатора для поиска заданной строчки срока аренды"""
    INPUT_COLOR_BLACK = [By.XPATH, "//label[@for='black']"]
    """Локатор выбирающий строчку с Черным цветом самоката"""
    INPUT_COLOR_GRAY = [By.XPATH, "//label[@for='gray']"]
    """Локатор выбирающий строчку с Серым цветом самоката"""
    INPUT_COMMENT = [By.XPATH, "//input[@type='text'][@placeholder='Комментарий для курьера']"]
    """Поле ввода комментария"""

    FIRST_PAGE_SUBMIT_BTN = [By.XPATH, "//button[text()='Далее']"]
    """Кнопка подтверждения ввода данных первой страницы формы"""
    SECOND_PAGE_SUBMIT_BTN = [By.XPATH, "//div[text()='Про аренду']/parent::div//button[text()='Заказать']"]
    """Кнопка подтверждения ввода данных второй страницы формы"""

    APPROVE_RENT_BTN = [By.XPATH, "//div[text()='Хотите оформить заказ?']/parent::div//button[text()='Да']"]
    """Кнопка во всплывающем окне для подтверждения заказа"""
