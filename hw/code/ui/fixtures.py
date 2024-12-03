import pytest
import os
# from selenium.webdriver.chrome.service import Service
# from selenium import webdriver
import undetected_chromedriver as uc
from ui.pages.audience import AudiencePage
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='function', autouse=True)
def driver(config):
    url = config['url']
    # chrome_options = webdriver.ChromeOptions()
    driver = uc.Chrome()
    driver.get(url)
    yield driver
    driver.quit()

@pytest.fixture()
def credentials():
    return (os.getenv("LOGIN"), os.getenv("PASSWORD"))

@pytest.fixture
def audience_page(driver):
    driver.get("https://ads.vk.com/hq/audience")
    return AudiencePage(driver)

