from pages.order_page import OrderPage


def test_open_order_page(web_driver):
    page = OrderPage(web_driver)
    page.open()
    page.check_is_order_page()
    page.fill_form_first_page()
    page.submit_form_first_page()
    page.fill_form_second_page()
    page.submit_form_second_page()
    page.check_approve_popup()


def test_go_main(web_driver):
    page = OrderPage(web_driver)
    page.open()
    page.go_main()
    page.wait(1)
    page.check_is_main_page()


def test_go_yandex(web_driver):
    page = OrderPage(web_driver)
    page.open()
    page.go_yandex()
    page.wait(1)
    page.check_is_yandex_page()