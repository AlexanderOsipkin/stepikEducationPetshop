import allure
from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from pages.card_page import CardPage
from pages.cart_page import CartPage
from pages.finish_page import FinishPage


@allure.epic("Petshop")
@allure.feature("Buy product")
@allure.story("Adding an item to your cart and proceeding to checkout")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Checking the purchase scenario before confirming the order")
@allure.description(
    "Verifies authorization, vitamin searches through the catalog, product card, "
    "cart, and data entry on the checkout page. "
    "Final order submission is disabled to prevent accidental placement of a real order"
)
def test_buy_product(driver):
    # Авторизация
    with allure.step("User authorization"):
        login_page = LoginPage(driver)
        login_page.authorization()

    # Поиск витаминов через меню
    with allure.step("Search for vitamins using the catalog and filters"):
        menu_page = MenuPage(driver)
        menu_page.search_vitamins()

    # Просматриваем карточку товара
    with allure.step("Checking the product card and adding it to the cart"):
        card_page = CardPage(driver)
        card_page.vitamin_card()

    # Проверяем товар в корзине
    with allure.step("Checking the item in the cart"):
        cart_page = CartPage(driver)
        cart_page.assert_product_in_cart()

    # Оформление заказа
    with allure.step("Filling in the details on the checkout page"):
        finish_page = FinishPage(driver)
        finish_page.confirm_order()