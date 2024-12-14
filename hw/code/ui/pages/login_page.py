# from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from ui.pages.base_page import BasePage
from ui.pages.audience import AudiencePage
from ui.pages.campaign import CampaignPage
from ui.locators.login import LoginLocators
from ui.pages.consts import URLs


class LoginPage(BasePage):
    locators = LoginLocators()
    url = URLs.login

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def login(self, login, password, type):
        self.click(self.locators.MAIL_OAUTH_BUTTON)
        self.fill(self.locators.MAIL_LOGIN_INPUT, login)
        self.click(self.locators.NEXT_BUTTON)
        self.click(self.locators.OTHER_WAY)
        self.click(self.locators.PASSWORD_WAY)
        self.fill(self.locators.MAIL_PASSWORD_INPUT, password)
        #time.sleep(5)
        self.click(self.locators.SUBMUT_BUTTON)
        # if self.find(self.locators.CAPTCHA_BUTTON, 10):
        #     self.click(self.locators.CAPTCHA_BUTTON)
        # #time.sleep(20)
        # self.fill(self.locators.MAIL_PASSWORD_INPUT, password)
        # if self.find(self.locators.SUBMUT_BUTTON, 10):
        #     self.click(self.locators.SUBMUT_BUTTON)

        if type == 'a':
            return AudiencePage(self.driver)
        if type == 'c':
            return CampaignPage(self.driver)
        