from test.base import BaseCase
from ui.pages.leadfom import LeadformPage

TEXT_WITH_SHIFTS = "Вау\n\nТут два переноса"

class TestAudience(BaseCase):

    def test_decoration_required_fields(self, leadform_page: LeadformPage):
        leadform_page.open()
        leadform_page.click_create_button()
        elements = leadform_page.empty_required_fields()
        assert len(elements) == 5

    def test_too_long_description(self, audience_page):
        audience_page.open()
        audience_page.click_create_button()
        audience_page.enter_text(TEXT_WITH_SHIFTS)

        assert audience_page.find_text("Используйте перенос строки не больше 2 раз подряд")
