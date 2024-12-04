import time
import pytest
from test.base import BaseCase
from ui.pages.campaign import CampaignPage

PERIOD = 5
KEY_PHRASE = "собака"

class TestCampaign(BaseCase):

    # ok
    def test_add_app(self, campaign_page: CampaignPage):
        campaign_page.open()
        campaign_page.click_campaign_creation()
        campaign_page.open_app()
        assert campaign_page.add_app()

    def test_small_budget(self, campaign_page: CampaignPage):
        campaign_page.click_campaign_creation()
        campaign_page.open_app()
        campaign_page.enter_budget("50")
        campaign_page.click_enter()
        assert campaign_page.small_budget_alert()

    def test_big_budget(self, campaign_page: CampaignPage):
        campaign_page.click_campaign_creation()
        campaign_page.open_app()
        el = campaign_page.enter_budget("10000000000000")
        value = el.get_attribute('value')
        assert value == "1 000 000 000 000 ₽"

    def test_save_campaign(self, campaign_page: CampaignPage):
        campaign_page.open()
        campaign_page.click_campaign_creation()
        campaign_page.open_app()
        campaign_page.add_app()
        campaign_page.enter_budget("2000")
        campaign_page.click_enter()
        campaign_page.click_save_draft()
        assert campaign_page.is_draft_saved()