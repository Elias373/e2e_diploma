import allure
from selene import browser, be
from pages.login_page import LoginPage
from pages.menu_page import MenuPage


@allure.suite("Authentication")
class TestLogin:

    @allure.title("Successful Login")
    def test_successful_login(self, browser_setup):
        login_page = LoginPage()
        with allure.step("Open login page"):
            login_page.open()
        with allure.step("Enter valid credentials"):
            login_page.login('standard_user', 'secret_sauce')
        with allure.step("Verify user is logged in"):
            from pages.main_page import MainPage
            MainPage().should_be_loaded()

    @allure.title("Failed Login")
    def test_failed_login(self, browser_setup):
        login_page = LoginPage()
        with allure.step("Open login page"):
            login_page.open()
        with allure.step("Enter invalid credentials"):
            login_page.login('invalid_user', 'invalid_password')
        with allure.step("Verify error message is shown"):
            login_page.should_have_error(
                'Epic sadface: Username and password do not match any user in this service'
            )


    @allure.title("Logout")
    def test_logout(self, logged_in_main_page):
        with allure.step("Perform logout"):
            MenuPage().logout()
        with allure.step("Verify user is logged out"):
            browser.element('#login-button').should(be.visible)

