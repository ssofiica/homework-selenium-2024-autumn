from ui.pages.base_page import BasePage
from ui.pages.consts import URLs
from ui.locators.audience import AudienceLocators

class AudiencePage(BasePage):
    url = URLs.audience
    locators = AudienceLocators

    def open(self):
        self.driver.get(self.url)

    def click_create_button(self):
        self.click(self.locators.CREATE_BUTTON, 50)


    