import pytest
import os
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage
from ui.pages.audience import AudiencePage
from ui.pages.main_page import MainPage
from dotenv import load_dotenv, dotenv_values

load_dotenv()

class BaseCase:
    # authorize = False
    driver = None

    @pytest.fixture(scope='session', autouse=True)
    #def setup(self, driver, config, request: FixtureRequest):
    def setup(self, driver, config):
        self.driver = driver
        self.config = config

        self.base_page: BasePage = BasePage(driver)
        #self.login_page: LoginPage = LoginPage(driver)
        # if self.authorize:
        self.driver.get("https://ads.vk.com/hq/audience")
        env_variables = dotenv_values('.env')
        for key, value in env_variables.items():
            self.driver.add_cookie({'name': key, 'value': value})

        #login, password = request.getfixturevalue("credentials")
        #self.login_page.open()
        self.main_page: MainPage = MainPage(self.driver)
