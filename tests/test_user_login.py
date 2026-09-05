from selenium import webdriver

from pages.login_page import LoginPage


def test_user_login():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--guest")
    driver = webdriver.Chrome(options=options)

    login = LoginPage(driver)
    login.authorization()

    print("Login success")