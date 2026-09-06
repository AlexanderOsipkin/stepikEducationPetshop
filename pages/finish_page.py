from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class FinishPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    cart_order_button = "//button[@data-testid='cartOrderButton']"

    # GETTERS
    def get_cart_order_button(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.cart_order_button)))

    # ACTIONS
    def click_cart_order_button(self):
        self.get_cart_order_button().click()

    # METHODS
    def assert_product_in_cart(self):
        self.get_current_url()

        self.click_cart_order_button()

        self.assert_url("https://www.petshop.ru/personal/order/make/")

        self.get_screenshot()
        print("Order confirm")
