from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import Keys


class MenuPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    menu_vitamins = "//a[@href='/catalog/dogs/vitamins/']"
    vitamins_header = "//h1[@data-testid='ps-page-title-header']"
    brand_button = "//button[@data-group-id='-1']"
    search_brand = "//div[@aria-label='Поиск по списку']//input[@data-testid='search_field']"
    vitamins_checkbox = "//label[@data-testid='ps-checkbox-wrap']"
    apply_button = "//button[@data-testid='filterDropdownContent__applyBtn']"
    age_button = "//button[@data-group-id='2']"
    age_checkbox = "//label[.//span[text()='Пожилые (7+)']]"
    vitamins_card = "//div[@data-testid='ProductListCard']"
    brand_card_header = "//a[@data-tesid='productDetails__titleBrand']"
    product_title = "//span[@data-testid='productDetails__titleName']"
    product_price = "(//span[@data-testid='priceWithNewPrice'])[1]"
    product_price_in_cart = "//span[@data-testid='priceWithNewPrice']"
    add_product_in_cart = "(//button[@data-testid='ButtonIconCounter_add'])[2]"
    cart_button = "//a[@data-testid='CartCounter_empty']"
    product_in_cart = "//img[@data-testid='cartListItemImage']"
    cart_order_button = "//button[@data-testid='cartOrderButton']"

    # GETTERS
    def get_menu_vitamins(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.menu_vitamins)))

    def get_vitamins_header(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.vitamins_header)))

    def get_brand_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.brand_button)))

    def get_search_brand(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.search_brand)))

    def get_vitamins_checkbox(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.vitamins_checkbox)))

    def get_apply_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.apply_button)))

    def get_age_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.age_button)))

    def get_age_checkbox(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.age_checkbox)))

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

    def get_cart_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_product_in_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_in_cart)))

    def get_product_price_in_cart(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.product_price_in_cart)))

    def get_cart_order_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.cart_order_button)))

    # ACTIONS
    def click_menu_vitamins(self):
        self.get_menu_vitamins().click()
        print("Click on vitamins in menu")

    def click_brand_button(self):
        self.get_brand_button().click()
        print("Click on brands button")

    def input_search_brand(self, text):
        self.get_brand_button().send_keys(text)
        print("Search vitamins brand")

    def click_vitamins_checkbox(self):
        self.get_vitamins_checkbox().click()

    def click_apply_button(self):
        self.get_apply_button().click()

    def click_age_button(self):
        self.get_age_button().click()

    def click_age_checkbox(self):
        self.get_age_checkbox().click()

    def click_vitamins_card(self):
        self.get_vitamins_card().click()

    def click_add_product_in_cart(self):
        self.get_add_product_in_cart().click()

    def click_cart_button(self):
        self.get_cart_button().click()

    def click_cart_order_button(self):
        self.get_cart_order_button().click()

    # METHODS
    def search_vitamins(self):
        self.driver.get(self.driver.base_url)
        self.get_current_url()

        self.close_popup()

        self.click_menu_vitamins()
        self.assert_value(self.get_vitamins_header(), "Витамины и добавки для собак")

        self.input_search_brand("Unitabs")
        self.click_vitamins_checkbox()
        self.click_apply_button()
        self.click_age_button()
        self.click_age_checkbox()
        self.click_apply_button()
        self.click_vitamins_card()
        self.assert_value(self.get_brand_card_header(), "Unitabs")
        self.assert_value(self.get_product_title(), "Витамины ArthroАctive с Q10 для собак, 100таб")
        self.assert_url(
            "https://www.petshop.ru/catalog/dogs/vet/vitaminy-dlya-sobak/dlya-kostey-i-sustavov-sobak/vitamins-arthroactive-with-q10-for-dogs-100tab/?oid=70291")

        product_price = self.get_product_price().text

        self.click_add_product_in_cart()
        self.click_cart_button()
        self.assert_value(self.get_product_in_cart(), "Витамины ArthroАctive с Q10 для собак, 100таб")
        self.assert_url("https://www.petshop.ru/personal/cart/")
        self.click_cart_order_button()

        self.get_screenshot()
        print("Product correct")
