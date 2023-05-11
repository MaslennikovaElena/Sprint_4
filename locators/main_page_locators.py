from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION = [By.XPATH, "//div[@data-accordion-component='AccordionItemButton'][text()='{message}']"]
    """Шаблон локатора для поиска вопроса"""
    ANSWER_BOX = [By.XPATH, f"{QUESTION}/parent::div/parent::div/div[@data-accordion-component='AccordionItemPanel']"]
    """Шаблон локатора для поиска панели ответа"""
    ANSWER = [By.XPATH, "//p[text()='{message}']/parent::div"]
    """Шаблон локатора для поиска ответа"""

    MENU_ORDER_BTN = [By.XPATH, "//div[@id='root']/div/div/div/div/button[text()='Заказать']"]
    """Шаблон локатора для кнопки в меню страницы для прехода к оформлению заказа"""
    BODY_ORDER_BTN = [By.XPATH, "//div[@id='root']/div/div/div/div/div/button[text()='Заказать']"]
    """Шаблон локатора для кнопки в теле страницы для прехода к оформлению заказа"""
    ORDER_PAGE_HEADER = [By.XPATH, "//div[text()='Для кого самокат']"]
    """Заголовок соответсвующий странице заказа"""
