from selene import browser, have


class CartPage:
    def open_cart(self):
        browser.element('#shopping_cart_container').click()
        return self

    def should_contain_item(self, item_name):
        browser.element('.cart_item').should(have.text(item_name))
        return self

    def should_have_items_count(self, count):
        items = browser.all('.cart_item')
        items.should(have.size(count))
        return self

    def remove_item(self, item_name):
        item_id = item_name.lower().replace(' ', '-')
        browser.element(f'button[data-test="remove-{item_id}"]').click()
        return self