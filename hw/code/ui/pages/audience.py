import time
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

    def click_add_source_button(self):
        self.click(self.locators.ADD_SOURCE, 50)

    def add_period(self, text):
        self.click(self.locators.KEY_PHRASE_BUTTON, 50)
        self.fill(self.locators.PERIOD_INPUT, text, 50)
        time.sleep(3)

    def enter_text(self, text):
        self.fill(self.locators.CREATION_NAME_AUDITORY, text)

    def enter_key_phrase(self, text):
        self.click(self.locators.KEY_PHRASE_BUTTON, 50)
        self.fill(self.locators.KEY_PHRASE_INPUT, text, 50)

    def select_key(self):
        self.click(self.locators.TEN_SAME_BUTTON)
        time.sleep(3)
        items = self.find_elements(self.locators.KEY_SUGGEST)
        print(type(items), len(items))
        # if items:
        #     print(type(items))
        #     # items[0].click()
        #     # value = items[0].get_attribute("data-suggest")
        #     # print(value)
        #     # return value
        # else:
        #     print("Элементы не найдены.")

    def get_key_values(self):
        textarea = self.find(self.locators.KEY_PHRASE_INPUT)
        value = textarea.get_attribute("value")
        return value
    
    def save(self):
        self.click(self.locators.SUBMUT_BUTTON, 50)