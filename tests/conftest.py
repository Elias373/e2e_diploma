import os
import pytest
from selene import browser
from selenium import webdriver
from dotenv import load_dotenv
from utils.attach import add_screenshot, add_logs, add_html, add_video


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def browser_setup():
    browser.config.base_url = os.environ['BASE_URL']
    browser.config.window_width = int(os.environ['WINDOW_WIDTH'])
    browser.config.window_height = int(os.environ['WINDOW_HEIGHT'])
    browser.config.timeout = float(os.environ['TIMEOUT'])


    selenoid_login = os.environ['SELENOID_LOGIN']
    selenoid_password = os.environ['SELENOID_PASSWORD']


    browser_name = os.environ['BROWSER_NAME']
    browser_version = os.environ['BROWSER_VERSION']
    enable_vnc = os.environ['ENABLE_VNC'].lower() == 'true'
    enable_video = os.environ['ENABLE_VIDEO'].lower() == 'true'


    options = webdriver.ChromeOptions() if browser_name == 'chrome' else webdriver.FirefoxOptions()


    options.set_capability('goog:loggingPrefs', {
        'browser': 'ALL',
        'performance': 'ALL',
        'driver': 'ALL'
    })


    options.set_capability("browserName", browser_name)
    options.set_capability("browserVersion", browser_version)
    options.set_capability("selenoid:options", {
        "enableVNC": enable_vnc,
        "enableVideo": enable_video
    })


    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver

    yield


    add_screenshot(browser)
    add_logs(browser)
    add_html(browser)
    add_video(browser)

    browser.quit()


@pytest.fixture
def logged_in_main_page(browser_setup):

    from pages.login_page import LoginPage
    from pages.main_page import MainPage

    username = os.environ['VALID_USERNAME']
    password = os.environ['VALID_PASSWORD']

    login_page = LoginPage()
    login_page.open().login(username, password)

    return MainPage()