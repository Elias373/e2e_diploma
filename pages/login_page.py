from selene import browser, have


class LoginPage:
    def open(self):
        browser.open('/')
        return self

    def login(self, username, password):
        browser.element('#user-name').type(username)
        browser.element('#password').type(password)
        browser.element('#login-button').click()
        return self

    def should_have_error(self, text):
        browser.element('[data-test="error"]').should(have.text(text))
        return self