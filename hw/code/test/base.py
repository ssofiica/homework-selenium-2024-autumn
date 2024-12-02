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

    @pytest.fixture(scope='function', autouse=True)
    #def setup(self, driver, config, request: FixtureRequest):
    def setup(self, driver, config):
        self.driver = driver
        self.config = config

        self.base_page: BasePage = BasePage(driver)
        #self.login_page: LoginPage = LoginPage(driver)
        # if self.authorize:
        self.driver.get("https://ads.vk.com/hq/overview")
        device_id = os.getenv("device_id")
        self.driver.add_cookie({'name': 'device_id', 'value': device_id})
        session_id = os.getenv("session_id")
        self.driver.add_cookie({'name': 'session_id', 'value': session_id})
        referral_code = os.getenv("referral_code")
        self.driver.add_cookie({'name': 'referral_code', 'value': referral_code})
        NEXT_LOCALE = os.getenv("NEXT_LOCALE")
        self.driver.add_cookie({'name': 'NEXT_LOCALE', 'value': NEXT_LOCALE})
        remixstlid = os.getenv("remixstlid")
        self.driver.add_cookie({'name': 'remixstlid', 'value': remixstlid})
        remixlang = os.getenv("remixlang")
        self.driver.add_cookie({'name': 'remixlang', 'value': remixlang})
        remixua = os.getenv("remixua")
        self.driver.add_cookie({'name': 'remixua', 'value': remixua})
        remixstid = os.getenv("remixstid")
        self.driver.add_cookie({'name': 'remixstid', 'value': remixstid})
        remixscreen_width = os.getenv("remixscreen_width")
        self.driver.add_cookie({'name': 'remixscreen_width', 'value': remixscreen_width})
        remixscreen_height = os.getenv("remixscreen_height")
        self.driver.add_cookie({'name': 'remixscreen_height', 'value': remixscreen_height})
        remixscreen_depth = os.getenv("remixscreen_depth")
        self.driver.add_cookie({'name': 'remixscreen_depth', 'value': remixscreen_depth})
        remixscreen_orient = os.getenv("remixscreen_orient")
        self.driver.add_cookie({'name': 'remixscreen_orient', 'value': remixscreen_orient})
        remixsf = os.getenv("remixsf")
        self.driver.add_cookie({'name': 'remixsf', 'value': remixsf})
        remixgp = os.getenv("remixgp")
        self.driver.add_cookie({'name': 'remixgp', 'value': remixgp})
        remixuas = os.getenv("remixuas")
        self.driver.add_cookie({'name': 'remixuas', 'value': remixuas})
        remixsuc = os.getenv("remixsuc")
        self.driver.add_cookie({'name': 'remixsuc', 'value': remixsuc})
        remixdmgr = os.getenv("remixdmgr")
        self.driver.add_cookie({'name': 'remixdmgr', 'value': remixdmgr})
        remixuacck = os.getenv("remixuacck")
        self.driver.add_cookie({'name': 'remixuacck', 'value': remixuacck})
        vkads = os.getenv("vkads")
        self.driver.add_cookie({'name': 'vkads', 'value': vkads})
        login_sid = os.getenv("login_sid")
        self.driver.add_cookie({'name': 'login_sid', 'value': login_sid})
        remixscreen_dpr = os.getenv("remixscreen_dpr")
        self.driver.add_cookie({'name': 'remixscreen_dpr', 'value': remixscreen_dpr})
        remixsid = os.getenv("remixsid")
        self.driver.add_cookie({'name': 'remixsid', 'value': remixsid})
        remixpuad = os.getenv("remixpuad")
        self.driver.add_cookie({'name': 'remixpuad', 'value': remixpuad})
        httoken = os.getenv("httoken")
        self.driver.add_cookie({'name': 'httoken', 'value': httoken})
        remixrefkey = os.getenv("remixrefkey")
        self.driver.add_cookie({'name': 'remixrefkey', 'value': remixrefkey})
        #login, password = request.getfixturevalue("credentials")
        #self.login_page.open()
