from selenium import webdriver

from pages.main_page import MainPage


def test_search_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--guest")
    driver = webdriver.Chrome(options=options)

    mp = MainPage(driver)
    mp.search_product()
