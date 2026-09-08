from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from pages.card_page import CardPage
from pages.cart_page import CartPage
from pages.finish_page import FinishPage


def test_buy_product(driver):
    # Авторизация
    login_page = LoginPage(driver)
    login_page.authorization()

    # Поиск витаминов через меню
    menu_page = MenuPage(driver)
    menu_page.search_vitamins()

    # Просматриваем карточку товара
    card_page = CardPage(driver)
    card_page.vitamin_card()

    # Проверяем товар в корзине
    cart_page = CartPage(driver)
    cart_page.assert_product_in_cart()

    # Оформление заказа
    finish_page = FinishPage(driver)
    finish_page.confirm_order()

