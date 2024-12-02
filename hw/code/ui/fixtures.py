import pytest
import os
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='session', autouse=True)
def driver(config):
    url = config['url']
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(chrome_options, Service(ChromeDriverManager().install()))
    driver.get(url)
    yield driver
    driver.quit()

@pytest.fixture()
def credentials():
    return (os.getenv("LOGIN"), os.getenv("PASSWORD"))