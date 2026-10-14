import pytest
import allure
import os

from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")


@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()

    options.add_experimental_option("detach", True)
    options.add_argument("--guest")

    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)

    driver.base_url = BASE_URL

    yield driver

    # driver.quit() оставлен закомментированным, чтобы браузер не закрывался
    # автоматически после тестов. Для обычного CI-прогона лучше включить driver.quit().


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """При падении теста прикладывает скриншот и URL в Allure."""
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    driver = item.funcargs.get("driver")
    if driver is None:
        return

    try:
        allure.attach(
            driver.get_screenshot_as_png(),
            name=f"Failure screenshot - {item.name}",
            attachment_type=allure.attachment_type.PNG,
        )
        allure.attach(
            driver.current_url,
            name="URL at failure",
            attachment_type=allure.attachment_type.TEXT,
        )
    except Exception as error:
        # Ошибка создания вложения не должна маскировать исходную ошибку теста.
        print(f"Could not attach failure details to Allure: {error}")
