import pytest
from selenium import webdriver

BASE_URL = "https://www.petshop.ru/"


@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--guest")

    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)

    driver.base_url = BASE_URL

    yield driver

    # driver.quit()
