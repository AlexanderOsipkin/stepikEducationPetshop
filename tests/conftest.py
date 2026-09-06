import pytest
from selenium import webdriver

from utilities.attach import add_screenshot, add_logs, add_html


@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--guest")

    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)

    yield driver

    add_screenshot(driver)
    add_logs(driver)
    add_html(driver)

    driver.quit()