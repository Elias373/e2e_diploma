import allure
from selene import browser, have
from pages.cart_page import CartPage

cart = CartPage()

pytestmark = allure.epic("Test Cart")

@allure.title("Add Item to Cart")
def test_add_item_to_cart(authorized_user):
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
def test_remove_item_from_cart(authorized_user):
    main = authorized_user
    with allure.step("Add item to cart"):
        main.add_item_to_cart('add-to-cart-sauce-labs-backpack')
    with allure.step("Remove item from cart"):
        main.remove_item_from_cart('remove-sauce-labs-backpack')
    with allure.step("Verify cart is empty"):
        cart.open_cart()
        cart.should_have_items_count(0)