from pages.main_page import MainPage


def test_search_product(setup_browser):
    mp = MainPage(setup_browser)
    mp.search_product()
