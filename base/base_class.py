from pathlib import Path
import datetime
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current url: {get_url}')

    """Method assert word"""
    def assert_value(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")  # задаем переменную с текущим временем
        name_screenshot = f"screenshot_{now_date}.png"  # задаем название для скриншота
        project_path = Path(__file__).resolve().parent.parent  # задаем путь для сохранения скрина
        screenshot_path = project_path / "screen" / name_screenshot  # явно даем понять куда надо сохранить
        self.driver.save_screenshot(str(screenshot_path))
        print(f"Screenshot successfully saved: {screenshot_path}")

    """Method assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    """Method close popup"""
    def close_popup(self):
        try:
            close_button = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='TutoringEcoTooltip_button__zhTqX']")))
            close_button.click()
            print("Popup closed")

        except TimeoutException:
            print("Popup not found")

    """Method assert text"""
    def assert_text_contains(self, element, expected_text):
        assert expected_text in element.text
        print("Text contains expected value")