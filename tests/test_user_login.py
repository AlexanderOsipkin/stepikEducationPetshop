from pages.login_page import LoginPage


def test_user_login(driver):
    # Авторизация
    login_page = LoginPage(driver)
    login_page.authorization()