from selenium.webdriver.chrome.webdriver import WebDriver
from ui.pages.consts import URLs
from ui.locators.base import BasePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from typing import List
import time

class PageNotOpenedExeption(Exception):
    pass

class BasePage:
    locators = BasePageLocators()
    url = URLs.base
    check_url = True
    
    def is_opened(self, timeout=15):
        if not self.check_url:
            return True

        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedExeption(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        # self.is_opened()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 20

        return WebDriverWait(self.driver, timeout=timeout)
    
    def find(self, locator, timeout=20):
        try:
            return self.wait(timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        except Exception as e:
            print(f"Error finding element with locator {locator}: {e}")
            raise
        
    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    def fill(self, locator, text, timeout=None) -> WebElement:
        elem = self.find(locator, timeout)
        # if not elem: 
        #     return
        elem.clear()
        elem.send_keys(text)
        return elem 

    def find_text(self, text):
        elem = self.wait(10).until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{text}')]")))
        return elem
    
    def find_elements(self, locator, timeout=None) -> List[WebElement]:
        elements = self.wait(timeout).until(EC.presence_of_all_elements_located(locator))
        return elements
    