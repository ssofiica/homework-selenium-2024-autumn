import pytest
from ui.pages.audience import AudiencePage
from test.base import BaseCase

class TestAudience(BaseCase):
    # authorize = True

    def test_open_creation_window(self):
        self.audience_page = self.main_page.go_to_audience_page()
        self.driver.get("https://ads.vk.com/hq/audience")
        self.audience_page.click_create_button()
        assert self.audience_page.find_text("Создать аудиторию")

        