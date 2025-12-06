import allure
import pytest
from selene import browser, have
from pages.main_page import MainPage

@allure.suite("Navigation")
class TestNavigation:

    @allure.title("Menu")
    def test_navigation(self, authorized_user):
        with allure.step("Perform Login"):
            main = authorized_user
        with allure.step("Open about page via menu"):
            main.open_about_page()
        with allure.step("Verify about page opened"):
            browser.should(have.url_containing('saucelabs.com'))

    @allure.title("Product Filtering")
    def test_product_filtering(self, authorized_user):
        with allure.step("Perform Login"):
            main = authorized_user
        with allure.step("Apply price filter low to high"):
            browser.element('.product_sort_container').element('option[value="lohi"]').click()
        with allure.step("Verify filter is applied"):
            browser.element('.active_option').should(have.text('Price (low to high)'))
