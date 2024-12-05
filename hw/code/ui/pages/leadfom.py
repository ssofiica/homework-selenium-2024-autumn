import time
from ui.pages.base_page import BasePage
from ui.pages.consts import URLs
from ui.locators.leadform import LeadformLocators

class LeadformPage(BasePage):
    url = URLs.leadform
    locators = LeadformLocators

    def open(self):
        self.driver.get(self.url)

    def click_create_button(self):
        self.click(self.locators.CREATE_LEADFORM_BUTTON, 50)

    def empty_required_fields(self):
        self.fill(self.locators.NAME_INPUT, "", 50)
        self.click(self.locators.SUBBMIT_BUTTON, 50)
        return self.find_elements(self.locators.REQUIRED_FIELD, 30)
    
    def enter_long_description_field(self, text):
        self.click(self.locators.MORE_TEXT_BUTTON, 50)
        self.fill(self.locators.LONG_DESCRIPTION, text, 50)