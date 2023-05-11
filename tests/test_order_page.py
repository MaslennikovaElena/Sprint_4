import allure

from pages.order_page import OrderPage


@allure.title('Проверка позитивного сценария заполнения формы бронирования самоката')
@allure.description('Открываем страницу бронирования, заполняем сперва первую, а после вторую части формы заказа '
                    'а затем проверяем что всплывающее окно появилось')
def test_order_page_make_order(web_driver):
    page = OrderPage(web_driver)
    page.open()
    page.fill_form_first_page(
        name="Елена",
        family="Масленникова",
        address="Кустанайская",
        phone="+78887776655",
        metro="Зябликово",
    )
    page.submit_form_first_page()
    page.fill_form_second_page(
        rent=2,
        date="11",
        is_black=True,
        comment="Тащить без лифта на 13 этаж"
    )
    page.submit_form_second_page()
    page.check_approve_popup()


@allure.title('Проверка альтернативного позитивного сценария заполнения формы бронирования самоката')
@allure.description('Открываем страницу бронирования, заполняем сперва первую, а после вторую части формы заказа '
                    'а затем проверяем что всплывающее окно появилось')
def test_order_page_make_alternate_order(web_driver):
    page = OrderPage(web_driver)
    page.open()
    page.fill_form_first_page(
        name="Даня",
        family="Масленников",
        address="Декабристов",
        phone="+79991112233",
        metro="Отрадное",
    )
    page.submit_form_first_page()
    page.fill_form_second_page(
        rent=6,
        date="18",
        is_black=False,
        comment="Домофон, сучтите три раза"
    )
    page.submit_form_second_page()
    page.check_approve_popup()


@allure.title('Проверка что нажатие на логотип самоката ведет на главную страниц')
@allure.description('Открываем страницу заказа, после чего нажимаем на логотип самоката, '
                    'и проверяем перешли ли на главную страницу')
def test_go_main(web_driver):
    page = OrderPage(web_driver)
    page.open()
    page.go_main()
    page.wait(1)
    page.check_is_main_page()


@allure.title('Проверка что нажатие на логотип яндекса ведет на главную страниц яндекса')
@allure.description('Открываем страницу заказа, после чего нажимаем на логотип яндекса, '
                    'и проверяем перешли ли на главную страницу яндекса')
def test_go_yandex(web_driver):
    page = OrderPage(web_driver)
    page.open()
    page.go_yandex()
    page.wait(1)
    page.check_is_yandex_page()
