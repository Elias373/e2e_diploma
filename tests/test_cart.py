import allure
import pytest
from selene import browser, have
from pages.main_page import MainPage
from pages.cart_page import CartPage



main = MainPage()
cart = CartPage()

@allure.suite("Cart")
class TestCart:

    @allure.title("Add Item to Cart")
    def test_add_item_to_cart(self, authorized_user):
        with allure.step("Perform Login"):
            main = authorized_user
        with allure.step("Add item to cart"):
            main.add_item_to_cart('add-to-cart-sauce-labs-backpack')
        with allure.step("Verify cart"):
            cart.open_cart()
            browser.element('.title').should(have.text('Your Cart'))
            cart.should_contain_item('Sauce Labs Backpack')
        with allure.step("Verify item count in cart"):
            cart.should_have_items_count(1)

    @allure.title("Remove Item from Cart")
    def test_remove_item_from_cart(self, authorized_user):
        with allure.step("Perform Login"):
            main = authorized_user
        with allure.step("Add item to cart"):
            main.add_item_to_cart('add-to-cart-sauce-labs-backpack')
        with allure.step("Remove item from cart"):
            main.remove_item_from_cart('remove-sauce-labs-backpack')
        with allure.step("Verify cart is empty"):
            cart.open_cart()
            cart.should_have_items_count(0)










