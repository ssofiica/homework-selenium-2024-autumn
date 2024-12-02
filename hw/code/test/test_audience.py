import pytest
from ui.pages.audience import AudiencePage
from test.base import BaseCase

class TestAudience(BaseCase):
    # authorize = True

    def test_open_creation_window(self, audience_page: AudiencePage):
        audience_page.open()
        audience_page.click_create_button()
        assert audience_page.find_text("Создать аудиторию")

        