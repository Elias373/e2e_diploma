import allure
from selene import have, browser, be

from pages.login_page import LoginPage
from pages.main_page import MainPage

login = LoginPage()
main = MainPage()


@allure.title("Successful login")
def test_successful_login():
    with allure.step("Open and login"):
        login.open().login('standard_user', 'secret_sauce')

    with allure.step("Verify main page loaded"):
        main.should_be_loaded()


@allure.title("Add item to cart")
def test_add_to_cart():
    with allure.step("Login to application"):
        login.open().login('standard_user', 'secret_sauce')

    with allure.step("Add item and verify cart"):
        main.add_item_to_cart('add-to-cart-sauce-labs-backpack')
        main.cart_should_have_count(1)


@allure.title("Navigation to about page")
def test_navigation():
    with allure.step("Login and open about page"):
        login.open().login('standard_user', 'secret_sauce')
        main.open_about_page()

    with allure.step("Verify navigation worked"):
        browser.should(have.url_containing('saucelabs.com'))


@allure.title("User logout")
def test_logout():
    with allure.step("Login and logout"):
        login.open().login('standard_user', 'secret_sauce')
        main.logout()

    with allure.step("Verify logout successful"):
        browser.element('#login-button').should(be.visible)


@allure.title("Failed login")
def test_login_fail():
    with allure.step("Attempt login with invalid credentials"):
        login.open().login('invalid_user', 'invalid_password')

    with allure.step("Verify error message"):
        login.should_have_error('Username and password do not match')