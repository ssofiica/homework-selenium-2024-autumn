import time
from ui.pages.base_page import BasePage
from ui.pages.consts import URLs
from ui.locators.campaign import CampaignLocators

LINK = "https://apps.apple.com/ru/app/orange-game/id1668760195"

class CampaignPage(BasePage):
    url = URLs.campaign
    locators = CampaignLocators

    def open(self):
        self.driver.get(self.url)

    def click_campaign_creation(self):
        self.click(self.locators.CREATE_BUTTON, 50)

    def open_app(self):
        self.click(self.locators.CREATE_MOBAPP, 50)

    def add_app(self):
        self.click(self.locators.SAVED_SOURCE_PARAMETRS, 30)
        self.click(self.locators.ADD_APP, 30)
        self.fill(self.locators.APP_LINK_INPUT, LINK, 30)
        self.click(self.locators.ADD_APP_BUTTON, 30)
        self.click(self.locators.CLOSE_BUTTON, 30)
        self.click(self.locators.CLOSE_BUTTON, 30)
        return self.find(self.locators.ADDED_APP, 30)

    def enter_budget(self, value):
        return self.fill(self.locators.BUDGET_INPUT, value, 50)

    def click_enter(self):
        self.click(self.locators.CONTINUE_BUTTON, 30)

    def click_save_draft(self):
        self.click(self.locators.SAVE_DRAFT_BUTTON, 30)
    
    def small_budget_alert(self):
        self.find(self.locators.SMALL_BUDGET_ALERT, 30)

    def is_draft_saved(self):
        return self.find(self.locators.CHANGES_SAVED, 30)

    