import allure
from selene import browser, have, be
from pages.cart_page import CartPage


@allure.suite("Cart")
class TestCart:

    @allure.title("Add item and verify on main page")
    def test_add_item_and_verify_on_main_page(self, logged_in_main_page):
        product_name = 'Sauce Labs Backpack'
        with allure.step("Verify cart is initially empty"):
            browser.element('.shopping_cart_badge').should(be.not_.visible)
        with allure.step(f"Add '{product_name}' to cart"):
            logged_in_main_page.add_item_to_cart(product_name)
        with allure.step("Verify cart badge shows '1'"):
            browser.element('.shopping_cart_badge').should(be.visible.and_(have.text('1'))
            )

    @allure.title("Remove item from cart page")
    def test_remove_item_from_cart_page(self, logged_in_main_page):
        cart_page = CartPage()
        product_name = 'Sauce Labs Backpack'
        with allure.step("Verify cart is initially empty"):
            browser.element('.shopping_cart_badge').should(be.not_.visible)
        with allure.step(f"Add '{product_name}' to cart"):
            logged_in_main_page.add_item_to_cart(product_name)
        with allure.step("Open shopping cart"):
            cart_page.open_cart()
            browser.element('.title').should(have.text('Your Cart'))
        with allure.step(f"Verify cart contains '{product_name}'"):
            cart_page.should_contain_item(product_name)
            cart_page.should_have_items_count(1)
        with allure.step(f"Remove '{product_name}' from cart page"):
            cart_page.remove_item(product_name)
        with allure.step("Verify cart is empty after removal"):
            cart_page.should_have_items_count(0)
            browser.all('.cart_item').should(have.size(0))







