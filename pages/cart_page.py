import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class CartPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    cart_button = "//a[@data-testid='CartCounter_empty']"
    product_in_cart = "//p[@data-testid='cartListItemTitle']"
    product_price_in_cart = "//span[@data-testid='priceWithNewPrice']"
    cart_order_button = "//button[@data-testid='cartOrderButton']"

    # GETTERS
    def get_cart_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_product_in_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_in_cart)))

    def get_product_price_in_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.product_price_in_cart)))

    def get_cart_order_button(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.cart_order_button)))

    # ACTIONS
    def click_cart_button(self):
        self.get_cart_button().click()

    def click_cart_order_button(self):
        self.get_cart_order_button().click()

    # METHODS
    def assert_product_in_cart(self):
        self.get_current_url()

        self.click_cart_button()

        product = self.get_product_in_cart()
        print("Товар в корзине:", repr(product.text))

        self.assert_value(self.get_product_in_cart(), "Unitabs Витамины ArthroАctive с Q10 для собак, 100таб")
        self.assert_url("https://www.petshop.ru/personal/cart/")
        print("Product in cart correct")

        self.click_cart_order_button()

        time.sleep(3)

        self.assert_url("https://www.petshop.ru/personal/order/make/")
        print("Correct redirect on finish page")

        self.get_screenshot()