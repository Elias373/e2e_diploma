import allure
from selene import browser, have

class MainPage:
    @allure.step("Verify main page is loaded")
    def should_be_loaded(self):
        browser.element('.title').should(have.text('Products'))
        return self

    @allure.step("Add item to cart with ID '{item_id}'")
    def add_item_to_cart(self, item_id):
        browser.element(f'#{item_id}').click()
        return self

    @allure.step("Verify cart has {count} items")
    def cart_should_have_count(self, count):
        browser.element('.shopping_cart_badge').should(have.text(str(count)))
        return self

    @allure.step("Go to cart")
    def go_to_cart(self):
        browser.element('.shopping_cart_link').click()
        return self

    @allure.step("Open about page")
    def open_about_page(self):
        browser.element('#react-burger-menu-btn').click()
        browser.element('#about_sidebar_link').click()
        return self

    @allure.step("Logout")
    def logout(self):
        browser.element('#react-burger-menu-btn').click()
        browser.element('#logout_sidebar_link').click()
        return self