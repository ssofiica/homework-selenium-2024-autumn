import pytest
import os
from ui.pages.consts import URLs
# from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import undetected_chromedriver as uc
from ui.pages.audience import AudiencePage
from ui.pages.campaign import CampaignPage
from ui.pages.leadfom import LeadformPage
from webdriver_manager.chrome import ChromeDriverManager

USER_DATA_DIR = '/Users/svalo/AppData/Local/Google/Chrome/'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'


@pytest.fixture(scope='function', autouse=True)
def driver(config):
    url = config['url']
    #driver = webdriver.Chrome()
    options = uc.ChromeOptions()
    #options = webdriver.ChromeOptions()
    options.add_argument(f'--user-data-dir={USER_DATA_DIR}')
    options.add_argument(f'--user-agent={USER_AGENT}')
    options.add_argument('--profile-directory=Default')
    driver = uc.Chrome(options=options, port=0)
    driver.get(url)
    yield driver
    driver.quit()

@pytest.fixture()
def credentials():
    return (os.getenv("LOGIN"), os.getenv("PASSWORD"))

@pytest.fixture
def audience_page(driver):
    driver.get(URLs.audience)
    return AudiencePage(driver)

@pytest.fixture
def campaign_page(driver):
    driver.get(URLs.campaign)
    return CampaignPage(driver)

@pytest.fixture
def leadform_page(driver):
    driver.get(URLs.leadform)
    return LeadformPage(driver)