import allure
from selene import browser, have
from pages.main_page import MainPage


@allure.label("epic", "Navigation")
@allure.label("story", "Menu")
@allure.title("Menu")
def test_navigation(authorized_user):
    with allure.step("Perform Login"):
        main = authorized_user
    with allure.step("Open about page via menu"):
        main.open_about_page()
    with allure.step("Verify about page opened"):
        browser.should(have.url_containing('saucelabs.com'))


@allure.label("epic", "Navigation")
@allure.label("story", "Product Filtering")
@allure.title("Product Filtering")
def test_product_filtering(authorized_user):
    with allure.step("Perform Login"):
        main = authorized_user
    with allure.step("Apply price filter low to high"):
        browser.element('.product_sort_container').element('option[value="lohi"]').click()
    with allure.step("Verify filter is applied"):
        browser.element('.active_option').should(have.text('Price (low to high)'))
