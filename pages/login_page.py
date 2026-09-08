import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from dotenv import load_dotenv


load_dotenv()

login = os.getenv("PETSHOP_LOGIN")
password = os.getenv("PETSHOP_PASSWORD")


class LoginPage(Base):
    # LOCATORS
    enter_button = "(//button[@data-testid='button'])[1]"
    login_button = "//button[@data-testid='PhoneAuthorization__clickableText-loginAuth']"
    user_name = "//input[@data-testid='TextInput__Input']"
    user_password = "//input[@name='root_password']"
    authorization_button = "//button[@data-testid='LoginAuthorization__btn-enabled']"
    user_info_after_login = "//button[@data-testid='UserInfo__name']"

    # GETTERS
    def get_enter_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_user_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.user_password)))

    def get_authorization_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.authorization_button)))

    def get_user_info_after_login(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.user_info_after_login)))

    # ACTIONS
    def click_enter_button(self):
        self.get_enter_button().click()

    def click_login_button(self):
        self.get_login_button().click()

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_user_password(self, password):
        self.get_user_password().send_keys(password)
        print("Input user password")

    def click_authorization_button(self):
        self.get_authorization_button().click()
        print("Click authorization button")

    # METHODS
    def authorization(self):
        self.driver.get(self.driver.base_url)
        self.get_current_url()

        self.close_popup()
        self.close_cookie()

        self.click_enter_button()
        self.click_login_button()

        self.input_user_name(login)
        self.input_user_password(password)

        self.click_authorization_button()

        time.sleep(1)

        self.driver.refresh()

        self.assert_value(self.get_user_info_after_login(), login)
        self.assert_url("https://www.petshop.ru/#popup=login-auth")
        self.get_screenshot()

        print("Login success")