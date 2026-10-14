import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage


@allure.epic("Petshop")
@allure.feature("Search for products")
@allure.story("Search for a product by brand name")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Search for Royal Canin products")
@allure.description("Verifies that searching for Royal Canin returns results for the desired brand")
def test_search_product(driver):
    # Авторизация
    with allure.step("User authorization"):
        login_page = LoginPage(driver)
        login_page.authorization()

    # Ищем продукт в поле поиска
    with allure.step("Search for Royal Canin and check your results"):
        main_page = MainPage(driver)
        main_page.search_product()
