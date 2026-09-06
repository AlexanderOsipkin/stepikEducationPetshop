from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class CardPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    vitamins_card = "//a[.//span[@data-testid='productListCard__title']]"
    brand_card_header = "//a[@data-tesid='productDetails__titleBrand']"
    product_title = "//span[@data-testid='productDetails__titleName']"
    product_price = "(//span[@data-testid='priceWithNewPrice'])[1]"
    add_product_in_cart = "(//button[@data-testid='ButtonIconCounter_add'])[2]"

    # GETTERS
    def get_vitamins_card(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.vitamins_card)))

    def get_brand_card_header(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.brand_card_header)))

    def get_product_title(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_title)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.product_price)))

    def get_add_product_in_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_product_in_cart)))

    # ACTIONS
    def click_vitamins_card(self):
        self.get_vitamins_card().click()

    def click_add_product_in_cart(self):
        self.get_add_product_in_cart().click()

    # METHODS
    def vitamin_card(self):
        self.get_current_url()

        self.click_vitamins_card()
        self.assert_value(self.get_brand_card_header(), "Unitabs")
        self.assert_value(self.get_product_title(), "Витамины ArthroАctive с Q10 для собак, 100таб")
        self.assert_url(
            "https://www.petshop.ru/catalog/dogs/vet/vitaminy-dlya-sobak/dlya-kostey-i-sustavov-sobak/vitamins-arthroactive-with-q10-for-dogs-100tab/?oid=70291")

        # product_price = self.get_product_price().text

        self.click_add_product_in_cart()

        self.get_screenshot()
        print("Product correct")
