import allure

from pages.order_page import OrderPage


@allure.title('Проверка позитивного сценария заполнения формы бронирования самоката')
@allure.description('Открываем страницу бронирования, заполняем сперва первую, а после вторую части формы заказа '
                    'а затем проверяем что всплывающее окно появилось')
def test_open_order_page(web_driver):
    page = OrderPage(web_driver)
    page.open()
    page.fill_form_first_page()
    page.submit_form_first_page()
    page.fill_form_second_page()
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
