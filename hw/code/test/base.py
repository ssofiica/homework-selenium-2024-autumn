import pytest
import os
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage
from ui.pages.audience import AudiencePage
from ui.pages.login_page import LoginPage
from dotenv import load_dotenv, dotenv_values

load_dotenv()

class BaseCase:
    # authorize = False

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.login_page = LoginPage(driver)
        user, password = request.getfixturevalue('credentials')
        self.login_page.open()
        self.login_page.login(user, password)