from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_search_product(driver):
    # Логинимся
    login = LoginPage(driver)
    login.authorization()

    # Ищем продукт в поле поиска
    mp = MainPage(driver)
    mp.search_product()
