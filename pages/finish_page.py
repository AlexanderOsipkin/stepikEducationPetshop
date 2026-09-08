import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import Keys
from dotenv import load_dotenv

load_dotenv()

user_credentials = os.getenv("USER_NAME")
user_email = os.getenv("USER_EMAIL")
phone_number = os.getenv("PHONE_NUMBER")
city = os.getenv("USER_CITY")
pickup_name = os.getenv("PICKUP_NAME")

change_sum = 12345
order_comment = "test"


class FinishPage(Base):

    # LOCATORS
    add_recipient1_button = "(//button[@data-testid='add-recipient'])[1]"
    add_recipient2_button = "(//button[@data-testid='add-recipient'])[2]"
    user_name = "(//input[@data-testid='TextInput__Input'])[1]"
    user_phone = "//input[@data-testid='phone__Input']"
    user_email = "(//input[@data-testid='TextInput__Input'])[2]"
    save_button = "//button[@data-testid='Button-save-enable']"
    user_fio = "//div[@data-testid='fio']"
    user_phone_assert = "//div[@data-testid='phone']"
    user_mail_assert = "//div[@data-testid='mail']"
    delivery_method_button = "//div[@data-testid='root_deliveryMethod_city']"
    city_name = "//input[@data-testid='Autocomplete__input']"
    cart_order_button = "//button[@data-testid='cartOrderButton']"
    current_city = "//*[@id='root_deliveryMethod_city']/button/div/span"
    pickup_button = "(//div[@data-testid='Delivery__group_none-tile'])[2]"
    pickup_name = "(//input[@data-testid='Input__Input'])[2]"
    pickup_confirm = "//div[@data-testid='PickPointListElement']"
    pickup_ok_button = "//button[@data-testid='ok']"
    street_name = "//span[@data-testid='street']"
    change_sum = "//input[@data-testid='Input__Input']"
    sms_radio = "//input[@id='notify-1']"
    order_comment = "//textarea[@data-testid='textarea']"
    submit_button = "//button[@data-testid='Order__submit']"
    order_info = "//p[@data-testid='MainInfo__orderInfo']//span[contains(., 'Вся информация о заказе находится в Личном кабинете')]"

    # GETTERS
    def get_add_recipient1_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.add_recipient1_button)))

    def get_add_recipient2_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.add_recipient2_button)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.user_name)))

    def get_user_phone(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.user_phone)))

    def get_user_email(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.user_email)))

    def get_save_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.save_button)))

    def get_user_fio(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.user_fio)))

    def get_user_phone_assert(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.user_phone_assert)))

    def get_user_mail_assert(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.user_mail_assert)))

    def get_delivery_method_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.delivery_method_button)))

    def get_city_name(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.city_name)))

    def get_cart_order_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_order_button)))

    def get_current_city(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.current_city)))

    def get_pickup_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.pickup_button)))

    def get_pickup_name(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.pickup_name)))

    def get_pickup_confirm(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.pickup_confirm)))

    def get_pickup_ok_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.pickup_ok_button)))

    def get_street_name(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.street_name)))

    def get_change_sum(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.change_sum)))

    def get_sms_radio(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.sms_radio)))

    def get_order_comment(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.order_comment)))

    def get_submit_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.submit_button)))

    def get_order_info(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.order_info)))

    # ACTIONS
    def click_add_recipient1_button(self):
        self.get_add_recipient1_button().click()

    def click_add_recipient2_button(self):
        self.get_add_recipient2_button().click()

    def input_user_name(self, user_credentials):
        self.get_user_name().send_keys(user_credentials)
        print(f"Input user name: {user_credentials}")

    def input_user_phone(self, phone_number):
        self.get_user_phone().clear()
        self.get_user_phone().send_keys(phone_number)
        print(f"Input user phone: 7{phone_number}")

    def input_user_email(self, user_email):
        self.get_user_email().send_keys(user_email)
        print(f"Input user email: {user_email}")

    def click_save_button(self):
        self.get_save_button().click()
        print("Save recipient data")

    def input_city_name(self, city):
        self.get_city_name().send_keys(city)
        self.get_city_name().send_keys(Keys.ENTER)
        print(f"Input city: {city}")

    def click_cart_order_button(self):
        self.get_cart_order_button().click()

    def click_pickup_button(self):
        self.get_pickup_button().click()
        print("Select pickup delivery")

    def input_pickup_name(self, pickup_name):
        self.get_pickup_name().send_keys(pickup_name)
        print(f"Search pickup point: {pickup_name}")

    def click_pickup_ok_button(self):
        self.get_pickup_ok_button().click()

    def click_pickup_confirm(self):
        self.get_pickup_confirm().click()
        print("Select pickup point")

    def input_change_sum(self, change_sum):
        self.get_change_sum().send_keys(change_sum)
        print(f"Input change sum: {change_sum}")

    def click_sms_radio(self):
        element = self.get_sms_radio()

        self.driver.execute_script("arguments[0].click();", element)

        assert element.is_selected()
        print("SMS notification selected")

    def input_order_comment(self, order_comment):
        self.get_order_comment().send_keys(order_comment)
        print(f"Input order comment: {order_comment}")

    def click_submit_button(self):
        self.get_submit_button().click()
        print("Submit order")

    # METHODS
    def check_city(self):
        current_city = self.get_current_city().text

        print("Now city:", current_city)

        if current_city != city:
            print("Change city:", city)

            self.click_delivery_method_button()
            self.input_city_name(city)
            self.click_cart_order_button()

        else:
            print("City correct")

    def confirm_order(self):
        self.get_current_url()

        self.click_add_recipient1_button()
        self.click_add_recipient2_button()

        self.assert_url("https://www.petshop.ru/personal/order/make/")

        self.input_user_name(user_credentials)
        self.input_user_phone(phone_number)
        self.input_user_email(user_email)

        self.click_save_button()

        self.assert_value(self.get_user_fio(), user_credentials)
        self.assert_phone(self.get_user_phone_assert(), phone_number)
        self.assert_value(self.get_user_mail_assert(), user_email)
        print("Recipient data correct")

        self.check_city()

        self.click_pickup_button()

        self.input_pickup_name(pickup_name)
        self.click_pickup_confirm()
        self.click_pickup_ok_button()

        selected_pickup = self.get_street_name().text
        print(f"Selected pickup point: {selected_pickup}")
        print(f"Expected pickup point: {pickup_name}")

        self.assert_value(self.get_street_name(), pickup_name)
        print("Pickup point correct")

        self.input_change_sum(change_sum)

        self.click_sms_radio()

        self.input_order_comment(order_comment)

        # закомментил от случайного нажатия + ордер потом только через ТП отменить можно,
        # тест прогоняю без полного оформлнения
        # self.click_submit_button()
        # self.assert_value(self.get_order_info(), "успешно оформлен. Вся информация о заказе находится в Личном кабинете")

        self.get_screenshot()
        print("Order confirm")
