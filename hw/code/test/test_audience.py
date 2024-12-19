import datetime
import time
from test.base import BaseCase
from ui.pages.audience import AudiencePage

NAME = "Аудитория "
MIN_PERIOD = "0"
MAX_PERIOD = "35"
PERIOD = "5"
KEY_PHRASE = "собака"
TOO_BIG_TEXT = """Аудитория 2024-12-03nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
        nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
        nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn"""

class TestAudience(BaseCase):

    # ok
    def test_open_creation_window(self, audience_page):
        audience_page.click_create_button()
        assert audience_page.find_text("Создать аудиторию")

    # ok
    def test_name_max_length(self, audience_page):
        audience_page.click_create_button()
        audience_page.enter_text(TOO_BIG_TEXT)
        assert audience_page.find_text("Напишите текст не больше 255 символов")

    # ok
    def test_source_period_length(self, audience_page: AudiencePage):
        audience_page.click_create_button()
        audience_page.click_add_source_button()
        audience_page.click_key_phrase()
        audience_page.add_period(MIN_PERIOD)
        assert audience_page.find_text("От 1 до 30 дней")
        audience_page.add_period(MAX_PERIOD)
        assert audience_page.find_text("От 1 до 30 дней")

    # ok
    def test_save_audience(self,  audience_page: AudiencePage):
        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        name = NAME + formatted_date
        audience_page.click_create_button()
        audience_page.click_add_source_button()
        audience_page.click_key_phrase()
        audience_page.enter_key_phrase(KEY_PHRASE)
        audience_page.add_period(PERIOD)
        audience_page.save_key_phrase()
        audience_page.save_audience()
        aud = audience_page.find_audience(name, 100)
        assert aud.text == name

    # ok
    def test_delete_audience(self,  audience_page: AudiencePage):
        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        name = NAME + formatted_date
        audience_page.select_audience(name) # выбор аудитории с нужным названием
        audience_page.click_delete()
        audience_page.select_users_tab()
        audience_page.select_aud_tab()
        res = audience_page.find_audience(name, 5) # чек того, что ее нет
        assert res is False
