import pytest
from dotenv import load_dotenv

load_dotenv()

class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config):
        self.driver = driver
        self.config = config
    