import pytest
import os
from selenium import webdriver
from ui.pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function', autouse=True)
def driver(config):
    url = config['url']
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    yield driver
    driver.quit()

@pytest.fixture()
def credentials():
    return (os.getenv("LOGIN"), os.getenv("PASSWORD"))

@pytest.fixture
def login_page(driver):
    driver.get(LoginPage.url)
    return LoginPage(driver=driver)

@pytest.fixture
def audience_page(login_page: LoginPage, credentials):
    page = login_page.login(credentials[0],credentials[1], 'a')
    page.open_audience_tab()
    return page

@pytest.fixture
def campaign_page(login_page: LoginPage, credentials):
    page = login_page.login(credentials[0],credentials[1], 'c')
    page.open()
    return page

@pytest.fixture
def leadform_page(login_page: LoginPage, credentials):
    page = login_page.login(credentials[0], credentials[1], 'l')
    page.open()
    return page
