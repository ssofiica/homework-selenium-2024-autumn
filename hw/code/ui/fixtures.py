import pytest
import os
from ui.pages.consts import URLs
# from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import undetected_chromedriver as uc
from ui.pages.audience import AudiencePage
from ui.pages.login_page import LoginPage
from ui.pages.campaign import CampaignPage
from ui.pages.leadfom import LeadformPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

USER_DATA_DIR = '/Users/svalo/AppData/Local/Google/Chrome/'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'


@pytest.fixture(scope='function', autouse=True)
def driver(config):
    url = config['url']
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=chrome_options)
    #options = uc.ChromeOptions()
    #options = webdriver.ChromeOptions()
    # options.add_argument(f'--user-data-dir={USER_DATA_DIR}')
    # options.add_argument(f'--user-agent={USER_AGENT}')
    # options.add_argument('--profile-directory=Default')
    # driver = uc.Chrome(options=options, port=0)
    driver.get(url)
    yield driver
    driver.quit()

@pytest.fixture()
def credentials():
    return (os.getenv("LOGIN"), os.getenv("PASSWORD"))

# @pytest.fixture
# def audience_page(driver):
#     driver.get(URLs.audience)
#     return AudiencePage(driver)

@pytest.fixture
def leadform_page(driver):
    driver.get(URLs.leadform)
    return LeadformPage(driver)

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