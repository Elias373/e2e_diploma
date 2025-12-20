import allure
from pages.menu_page import MenuPage


@allure.suite("Navigation")
class TestNavigation:

    @allure.title("Burger menu full functionality")
    def test_burger_menu_full_functionality(self, logged_in_main_page):
        menu = MenuPage()
        with allure.step("Open menu and verify items"):
            menu.open() \
                .should_have_items_count(4) \
                .should_have_items('All Items', 'About', 'Logout', 'Reset App State')
        with allure.step("Close menu with cross button"):
            menu.close()
            assert menu.is_menu_closed(), "Menu should be closed after closing"

    @allure.title("Check price sorting low to high")
    def test_check_price_sorting(self, logged_in_main_page):
        logged_in_main_page.sort_price_low_to_high()
        prices = logged_in_main_page.get_prices()

        assert prices == sorted(prices), \
            f"Prices should be sorted ascending, but got: {prices}"
        print(f"Sorted prices: {sorted(prices)}")


