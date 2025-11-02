import allure
from selene import browser, have


class CartPage:
    @allure.step("Verify cart page is loaded")
    def should_be_loaded(self):
        browser.element('.title').should(have.text('Your Cart'))
        return self

    @allure.step("Verify cart contains item '{item_name}'")
    def should_contain_item(self, item_name):
        browser.element('.cart_item').should(have.text(item_name))
        return self

    @allure.step("Verify cart has {count} items")
    def should_have_items_count(self, count):
        items = browser.all('.cart_item')
        items.should(have.size(count))
        return self