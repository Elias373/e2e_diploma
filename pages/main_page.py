from selene import browser, have, query
from pages.menu_page import MenuPage


class MainPage:
    def __init__(self):
        self.menu = MenuPage()

    def should_be_loaded(self):
        browser.element('.title').should(have.text('Products'))
        return self

    def add_item_to_cart(self, product_name):
        item_id = product_name.lower().replace(' ', '-')
        browser.element(f'button[data-test="add-to-cart-{item_id}"]').click()
        return self

    def sort_price_low_to_high(self):
        browser.element('.product_sort_container').click()
        browser.element('option[value="lohi"]').click()
        return self

    def get_prices(self):

        price_elements = browser.all('.inventory_item_price')
        prices = []

        for price_el in price_elements:
            price_text = price_el.get(query.text).replace('$', '')
            prices.append(float(price_text))

        return prices

    def verify_prices_sorted_low_to_high(self):
        prices = self.get_prices()
        sorted_prices = sorted(prices)

        assert prices == sorted_prices, \
            f"Prices not sorted ascending. Actual: {prices}, Expected: {sorted_prices}"

        return self



