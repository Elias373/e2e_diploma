import allure
from selene import browser, have

class LoginPage:
    @allure.step("Open login page")
    def open(self):
        browser.open('/')
        return self

    @allure.step("Login with username '{username}' and password '{password}'")
    def login(self, username, password):
        browser.element('#user-name').type(username)
        browser.element('#password').type(password)
        browser.element('#login-button').click()
        return self

    @allure.step("Verify error message contains '{text}'")
    def should_have_error(self, text):
        browser.element('[data-test="error"]').should(have.text(text))
        return self