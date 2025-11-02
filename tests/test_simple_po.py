import allure
from selene import browser, have, be
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage

login = LoginPage()
main = MainPage()
cart = CartPage()

@allure.title("Successful Login")
def test_successful_login():
    with allure.step("Open login page"):
        login.open()
    with allure.step("Enter valid credentials"):
        login.login('standard_user', 'secret_sauce')
    with allure.step("Verify user is logged in"):
        main.should_be_loaded()

@allure.title("Add Item to Cart")
def test_add_item_to_cart():
    with allure.step("Login to application"):
        login.open().login('standard_user', 'secret_sauce')
    with allure.step("Add item to cart"):
        main.add_item_to_cart('add-to-cart-sauce-labs-backpack')
    with allure.step("Verify item count in cart"):
        main.cart_should_have_count(1)

@allure.title("Navigation")
def test_navigation():
    with allure.step("Login to application"):
        login.open().login('standard_user', 'secret_sauce')
    with allure.step("Open about page via menu"):
        main.open_about_page()
    with allure.step("Verify about page opened"):
        browser.should(have.url_containing('saucelabs.com'))

@allure.title("Logout")
def test_logout():
    with allure.step("Login to application"):
        login.open().login('standard_user', 'secret_sauce')
    with allure.step("Perform logout"):
        main.logout()
    with allure.step("Verify user is logged out"):
        browser.element('#login-button').should(be.visible)

@allure.title("Failed Login")
def test_failed_login():
    with allure.step("Open login page"):
        login.open()
    with allure.step("Enter invalid credentials"):
        login.login('invalid_user', 'invalid_password')
    with allure.step("Verify error message is shown"):
        login.should_have_error('Username and password do not match')