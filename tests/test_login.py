import pytest
import allure
from selene import browser, be
from pages.login_page import LoginPage
from pages.main_page import MainPage


login = LoginPage()
main = MainPage()

@allure.suite("Authentication")
class TestLogin:

    @allure.title("Successful Login")
    def test_successful_login(self, browser_setup):
        with allure.step("Open login page"):
            login.open()
        with allure.step("Enter valid credentials"):
            login.login('standard_user', 'secret_sauce')
        with allure.step("Verify user is logged in"):
            main.should_be_loaded()

    @allure.title("Failed Login")
    def test_failed_login(self, browser_setup):
        with allure.step("Open login page"):
            login.open()
        with allure.step("Enter invalid credentials"):
            login.login('invalid_user', 'invalid_password')
        with allure.step("Verify error message is shown"):
            login.should_have_error('Epic sadface: Username and password do not match any user in this service')

    @allure.title("Logout")
    def test_logout(self, authorized_user):
        with allure.step("User is already logged in"):
            main = authorized_user
        with allure.step("Perform logout"):
            main.logout()
        with allure.step("Verify user is logged out"):
            browser.element('#login-button').should(be.visible)


