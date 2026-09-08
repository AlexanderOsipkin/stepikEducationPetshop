import re
import datetime

from pathlib import Path
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""
    def get_current_url(self):
        current_url = self.driver.current_url
        print(f"Current URL: {current_url}")

    """Method assert value"""
    def assert_value(self, word, result):
        actual_value = word.text

        assert actual_value == result, (f"Expected: '{result}', but got: '{actual_value}'")
        print(f"Good value: {actual_value}")

    """Method screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")  # задаем переменную с текущим временем
        name_screenshot = f"screenshot_{now_date}.png"  # задаем название для скриншота

        project_path = Path(__file__).resolve().parent.parent  # задаем путь для сохранения скрина
        screenshot_path = project_path / "screen" / name_screenshot  # явно даем понять куда надо сохранить
        screenshot_path.parent.mkdir(exist_ok=True)  # задаем на случай если папки нет

        self.driver.save_screenshot(str(screenshot_path))
        print(f"Screenshot successfully saved: {screenshot_path}")

    """Method assert url"""

    def assert_url(self, result):
        current_url = self.driver.current_url

        assert current_url == result, (f"Expected URL: '{result}', but got: '{current_url}'")
        print(f"Good URL: {current_url}")

    """Method close popup"""
    def close_popup(self):
        try:
            close_button = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='TutoringEcoTooltip_button__zhTqX']")))
            close_button.click()
            print("Popup closed")

        except TimeoutException:
            print("Popup not found")

    """Method close cookie"""
    def close_cookie(self):
        try:
            WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'CookieInformer_informer')]//button[@title='Закрыть']"))).click()

        except TimeoutException:
            print("Cookie popup not found")

    """Method assert phone number"""
    def assert_phone(self, word, result):
        actual_phone = re.sub(r"\D", "", word.text)
        expected_phone = re.sub(r"\D", "", result)

        assert actual_phone[-10:] == expected_phone[-10:], (f"Expected phone: '{result}', but got: '{word.text}'")