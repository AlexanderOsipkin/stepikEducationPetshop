from pathlib import Path
import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current url: {get_url}')

    """Method assert word"""
    def assertion_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")  # задаем переменную с текущим временем
        name_screenshot = f"screenshot_{now_date}.png"  # задаем название для скриншота
        project_path = Path(__file__).resolve().parent.parent # задаем путь для сохранения скрина
        screenshot_path = project_path / "screen" / name_screenshot # явно даем понять куда надо сохранить
        self.driver.save_screenshot(str(screenshot_path))
        print(f"Screenshot successfully saved: {screenshot_path}")

    """Method assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")
