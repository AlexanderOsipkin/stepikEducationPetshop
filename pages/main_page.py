from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import Keys


class MainPage(Base):
    url = "https://www.petshop.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    search_field = "//input[@data-testid='search_field']"
    product_brand_name = "//span[@data-testid='productListCard__brandName']"

    # GETTERS
    def get_search_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.search_field)))

    def get_product_brand_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_brand_name)))

    # ACTIONS

    def input_text_in_search_field(self, text):
        self.get_search_field().send_keys(text)
        print("Input some text in search field")

    def accept_value_in_search_field(self):
        self.get_search_field().send_keys(Keys.ENTER)
        print("Accept enter value")

    # METHODS
    def search_product(self):
        self.driver.get(self.url)
        self.get_current_url()

        self.close_popup()

        self.input_text_in_search_field("Royal Canin")
        self.accept_value_in_search_field()

        self.assert_text_contains(self.get_product_brand_name(), "Royal Canin")
        print("Product correct")
