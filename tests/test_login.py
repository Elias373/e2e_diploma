import allure
from selene import browser, have, be
from pages.login_page import LoginPage
from pages.main_page import MainPage

login = LoginPage()
main = MainPage()


@allure.label("epic", "Authentication")
@allure.label("story", "Login")
@allure.title("Successful Login")
def test_successful_login(browser_setup):
    with allure.step("Open login page"):
        login.open()
    with allure.step("Enter valid credentials"):
        login.login('standard_user', 'secret_sauce')
    with allure.step("Verify user is logged in"):
        main.should_be_loaded()


@allure.label("epic", "Authentication")
@allure.label("story", "Login")
@allure.title("Failed Login")
def test_failed_login(browser_setup):
    with allure.step("Open login page"):
        login.open()
    with allure.step("Enter invalid credentials"):
        login.login('invalid_user', 'invalid_password')
    with allure.step("Verify error message is shown"):
        login.should_have_error('Epic sadface: Username and password do not match any user in this service')


@allure.label("epic", "Authentication")
@allure.label("story", "Logout")
@allure.title("Logout")
def test_logout(authorized_user):
    with allure.step("Perform Login"):
        main = authorized_user
    with allure.step("Perform logout"):
        main.logout()
    with allure.step("Verify user is logged out"):
        browser.element('#login-button').should(be.visible)