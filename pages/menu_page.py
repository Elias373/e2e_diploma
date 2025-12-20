from selene import browser, be, have


class MenuPage:

    def open(self):
        browser.element('#react-burger-menu-btn').click()
        browser.element('.bm-menu-wrap').should(be.visible)
        return self

    def close(self):
        browser.element('#react-burger-cross-btn').click()
        browser.element('.bm-menu-wrap').should(be.not_.visible)
        return self



    def should_have_items(self, *expected_items):
        browser.all('.bm-item-list a').should(have.exact_texts(*expected_items))
        return self

    def should_have_items_count(self, count):
        browser.all('.bm-item-list a').should(have.size(count))
        return self

    def click_item(self, item_text):
        browser.all('.bm-item-list a').element_by(have.text(item_text)).click()
        return self

    def logout(self):
        return self.open().click_item('Logout')
