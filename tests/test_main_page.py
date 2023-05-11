import pytest

from pages.main_page import MainPage


@pytest.mark.parametrize("question, answer",[
    pytest.param(
        "Сколько это стоит? И как оплатить?",
        "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        id="payment",
    ),
    pytest.param(
        "Хочу сразу несколько самокатов! Так можно?",
        "Пока что у нас так: один заказ — один самокат. "
        "Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        id="count",
    ),
    pytest.param(
        "Как рассчитывается время аренды?",
        "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. "
        "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. "
        "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        id="rent",
    ),
    pytest.param(
        "Можно ли заказать самокат прямо на сегодня?",
        "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        id="today",
    ),
    pytest.param(
        "Можно ли продлить заказ или вернуть самокат раньше?",
        "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        id="duration",
    ),
    pytest.param(
        "Вы привозите зарядку вместе с самокатом?",
        "Самокат приезжает к вам с полной зарядкой. "
        "Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        id="charging",
    ),
    pytest.param(
        "Можно ли отменить заказ?",
        "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        id="cancel",
    ),
    pytest.param(
        "Я жизу за МКАДом, привезёте?",
        "Да, обязательно. Всем самокатов! И Москве, и Московской области.",
        id="regional",
    ),
])
def test_main_page_question_open_with_valid_text(web_driver, question, answer):
    page = MainPage(web_driver)
    page.check_question(question, answer)


def test_main_page_to_order_page_by_menu_btn_success(web_driver):
    page = MainPage(web_driver)
    page.open()
    page.go_order_by_menu()
    page.check_is_order_page()


def test_main_page_to_order_page_by_body_btn_success(web_driver):
    page = MainPage(web_driver)
    page.open()
    page.go_order_by_body()
    page.check_is_order_page()
