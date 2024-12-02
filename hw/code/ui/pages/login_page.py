from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.locators.login import LoginLocators
from ui.pages.consts import URLs


class LoginPage(BasePage):
    locators = LoginLocators()
    url = URLs.login
    authorize = False

    # def __init__(self, set_driver):
    #     self.driver = set_driver

    def open(self):
        self.driver.get(self.url)

    def login(self, login, password):
        self.click(self.locators.MAIL_OAUTH_BUTTON)
        self.fill(self.locators.MAIL_LOGIN_INPUT, login)
        self.click(self.locators.NEXT_BUTTON)
        self.click(self.locators.OTHER_WAY)
        self.click(self.locators.PASSWORD_WAY)
        self.fill(self.locators.MAIL_PASSWORD_INPUT, password)
        self.click(self.locators.SUBMUT_BUTTON)
        self.click(self.locators.CAPTCHA_BUTTON)
        self.fill(self.locators.MAIL_PASSWORD_INPUT, password)
        # self.click(self.locators.CAPTCHA_CLICK)
        self.click(self.locators.SUBMUT_BUTTON)

        return MainPage(self.driver)
        