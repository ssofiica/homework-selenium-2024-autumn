import datetime
import time
import pytest
from test.base import BaseCase
from ui.pages.campaign import CampaignPage
from ui.locators.campaign import CampaignLocators

TOO_SMALL_BUDGET = "50"
TOO_BIG_BUDGET = "10000000000000"
NORM_BUDGET = "2000"
SMALL_BUDGET_ALERT = "Укажите бюджет не меньше 100₽"
DRAFT_SAVED = "Изменения сохранены"
LINK = "yandex.ru"
NAME = "Кампания "

class TestCampaign(BaseCase):

    # # ok
    def test_small_budget(self, campaign_page: CampaignPage):
        campaign_page.close_modal()
        campaign_page.click_campaign_creation()
        campaign_page.add_site(LINK)
        campaign_page.enter_budget(TOO_SMALL_BUDGET)
        campaign_page.click_enter()
        assert campaign_page.small_budget_alert() == SMALL_BUDGET_ALERT
    
    # # ok
    def test_big_budget(self, campaign_page: CampaignPage):
        campaign_page.close_modal()
        campaign_page.click_campaign_creation()
        campaign_page.add_site(LINK)
        el = campaign_page.enter_budget(TOO_BIG_BUDGET)
        value = el.get_attribute('value')
        assert value == "1\xa0000\xa0000\xa0000\xa0000 ₽"

    # # ok
    def test_save_campaign(self, campaign_page: CampaignPage):
        campaign_page.close_modal()
        campaign_page.click_campaign_creation()
        #campaign_page.open_app()
        campaign_page.add_site(LINK)
        campaign_page.enter_budget(NORM_BUDGET)
        campaign_page.click_enter()
        campaign_page.click_save_draft()
        assert campaign_page.is_draft_saved() == DRAFT_SAVED
    
    # #ok
    def test_check_saved_draft(self, campaign_page: CampaignPage):
        campaign_page.close_modal()
        campaign_page.select_drafts()
        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        name = NAME + formatted_date
        draft = campaign_page.find_draft(name)
        assert draft.text == name

    # ok
    def test_delete_draft(self, campaign_page: CampaignPage):
        campaign_page.close_modal()
        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        name = NAME + formatted_date
        campaign_page.select_drafts() # переключение на кампании-черновики
        campaign_page.select_draft(name) # выбор черновика с нужным названием
        campaign_page.click_delete() # удаление черновика
        campaign_page.select_all()
        campaign_page.select_drafts()
        res = campaign_page.find(CampaignLocators.DRAFT(self, name), 2) # чек того, что его нет
        assert res is False
        