from pages.login_page import LoginPage


def test_user_login(setup_browser):
    login = LoginPage(setup_browser)
    login.authorization()
