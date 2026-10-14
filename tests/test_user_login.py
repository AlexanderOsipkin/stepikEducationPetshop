import allure
from pages.login_page import LoginPage


@allure.epic("Petshop")
@allure.feature("Authorization")
@allure.story("Successful user login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("User authorization in Petshop")
@allure.description("Checks login with credentials from environment variables")
def test_user_login(driver):
    # Авторизация
    with allure.step("User authorization"):
        login_page = LoginPage(driver)
        login_page.authorization()
