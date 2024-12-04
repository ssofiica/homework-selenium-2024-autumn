import time
import pytest
from test.base import BaseCase
from ui.pages.audience import AudiencePage

PERIOD = 5
KEY_PHRASE = "собака"

class TestAudience(BaseCase):
    # authorize = True

    # ok
    def test_open_creation_window(self, audience_page):
        audience_page.open()
        audience_page.click_create_button()
        assert audience_page.find_text("Создать аудиторию")

    # ok
    def test_name_max_length(self, audience_page):
        audience_page.open()
        time.sleep(4)
        audience_page.click_create_button()
        text = """Аудитория 2024-12-03nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
        nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
        nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn"""
        audience_page.enter_text(text)
        assert audience_page.find_text("Напишите текст не больше 255 символов")

    # ok
    def test_source_period_min_length(self, audience_page):
        audience_page.open()
        audience_page.click_create_button()
        audience_page.click_add_source_button()
        audience_page.add_period("0")
        assert audience_page.find_text("От 1 до 30 дней")

    # ok
    def test_source_period_max_length(self, audience_page):
        audience_page.open()
        time.sleep(3)
        audience_page.click_create_button()
        audience_page.click_add_source_button()
        time.sleep(3)
        audience_page.add_period("35")
        assert audience_page.find_text("От 1 до 30 дней")

    # ok
    def test_add_key_phrase(self, audience_page: AudiencePage):
        audience_page.open()
        audience_page.click_create_button()
        audience_page.click_add_source_button()
        time.sleep(3)
        audience_page.enter_key_phrase(KEY_PHRASE)
        value = audience_page.select_key()
        audience_page.add_period("5")
        audience_page.save()
        keys, period = audience_page.get_source_parameters()
        entered_keys = [KEY_PHRASE, value]
        
        assert keys == entered_keys
        assert period == PERIOD

    















        