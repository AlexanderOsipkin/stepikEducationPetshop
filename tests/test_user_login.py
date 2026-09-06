from pages.login_page import LoginPage


def test_user_login(driver):
    login = LoginPage(driver)
    login.authorization()