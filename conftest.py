import pytest
from selenium import webdriver


@pytest.fixture()
def web_driver():
    # Фикстура создания драйвера для работы в тестах
    chrome_options = webdriver.ChromeOptions()  # создали объект для опций
    chrome_options.add_argument('--headless')  # добавили настройку

    driver = webdriver.Chrome(options=chrome_options)

    yield driver

    # Закрытие браузера в конце теста
    driver.quit()
