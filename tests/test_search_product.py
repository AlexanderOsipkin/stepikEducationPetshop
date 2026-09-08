from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_search_product(driver):
    # Авторизация
    login_page = LoginPage(driver)
    login_page.authorization()

    # Ищем продукт в поле поиска
    main_page = MainPage(driver)
    main_page.search_product()
