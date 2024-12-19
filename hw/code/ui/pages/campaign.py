from ui.pages.base_page import BasePage
from ui.pages.consts import URLs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from ui.locators.campaign import CampaignLocators

LINK = "https://apps.apple.com/ru/app/orange-game/id1668760195"

class CampaignPage(BasePage):
    url = URLs.campaign
    locators = CampaignLocators

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.click(self.locators.TAB_CAMPAIGN, 10)

    def close_modal(self):
        if self.find(self.locators.CLOSE_MODAL_BUTTON, 100):
            self.click(self.locators.CLOSE_MODAL_BUTTON, 100)

    def click_campaign_creation(self):
        self.click(self.locators.CREATE_BUTTON, 1000)

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
    
    def add_site(self, link):
        self.click(self.locators.CREATE_SITE, 50)
        el = self.fill(self.locators.SITE_INPUT, link, 50)
        el.send_keys(Keys.RETURN) 

    def enter_budget(self, value):
        return self.fill(self.locators.BUDGET_INPUT, value, 50)

    def click_enter(self):
        self.click(self.locators.CONTINUE_BUTTON, 100)

    def click_save_draft(self):
        self.click(self.locators.SAVE_DRAFT_BUTTON, 1000)
    
    def small_budget_alert(self):
        el = self.find(self.locators.SMALL_BUDGET_ALERT, 30)
        return el.text

    def is_draft_saved(self):
        el = self.wait(2000).until(EC.presence_of_element_located(self.locators.CHANGES_SAVED))
        return el.get_attribute('textContent')
    
    def select_all(self):
        self.click(self.locators.SELECT_CAMP_TYPE_BUTTON)
        self.click(self.locators.ALL_CAMP)

    def select_drafts(self):
        self.click(self.locators.SELECT_CAMP_TYPE_BUTTON)
        self.click(self.locators.DRAFT_CAMP)

    def find_draft(self, name):
        return self.find(self.locators.CONTAINS_ANY_TEXT(self, name), 1000)
    
    def select_draft(self, name):
        row = self.find(self.locators.DRAFT_ROW_BY_NAME(self, name), 1000)
        checkbox = row.find_element(*self.locators.DRAFT_CHECKBOX)
        checkbox.click()
    
    def click_delete_selected(self):
        self.click(self.locators.DELETE_BUTTON)
        self.click(self.locators.ACCEPT_DELETE)
        