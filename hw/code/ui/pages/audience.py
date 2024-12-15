from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from ui.pages.consts import URLs
from ui.locators.audience import AudienceLocators

class AudiencePage(BasePage):
    url = URLs.audience
    locators = AudienceLocators

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def open_audience_tab(self):
        self.click(self.locators.TAB_AUDIENCE, 10)

    def click_create_button(self):
        self.click(self.locators.CREATE_BUTTON, 50)

    def click_add_source_button(self):
        self.click(self.locators.ADD_SOURCE, 50)

    def click_key_phrase(self):
        self.click(self.locators.KEY_PHRASE_BUTTON, 50)

    def add_period(self, text):
        self.fill(self.locators.PERIOD_INPUT, text, 50)

    def enter_text(self, text):
        self.fill(self.locators.CREATION_NAME_AUDITORY, text)

    def enter_key_phrase(self, text):
        self.fill(self.locators.KEY_PHRASE_INPUT, text, 50)

    def select_key(self):
        self.click(self.locators.TEN_SAME_BUTTON)
        items = self.find_elements(self.locators.KEY_SUGGEST, 1000)
        if items:
            v = items[0]
            value = v.get_attribute("data-suggest")
            v.click()
            return value
        else:
            print("Элементы не найдены.")

    def get_source_parameters(self):
        elements = self.find_elements(self.locators.SAVED_SOURCE_PARAMETRS)
        print(elements)
        params = elements[0].text
        print(params)
        keys = params.split(' • ')
        print(keys)
        period = elements[1].text
        print(period)
        return (keys, period)
    
    def save_key_phrase(self):
        buttons = self.find_elements(self.locators.SUBMUT_BUTTON, 100)
        print(buttons)
        b1 = buttons[1]
        b1.click()

    def save_audience(self):
        self.click(self.locators.SUBMUT_BUTTON, 50)

    def find_audience(self, name, timeout=100):
        return self.find(self.locators.FIND_AUD_NAME(self, name), timeout)
    
    def select_audience(self, name):
        row = self.find(self.locators.ROW_BY_NAME(self, name), 1000)
        checkbox = row.find_element(*self.locators.CHECKBOX)
        checkbox.click()
    
    def click_delete(self):
        self.click(self.locators.DELETE_BUTTON)
        self.click(self.locators.ACCEPT_DELETE)

    def select_users_tab(self):
        self.click(self.locators.USERS_TAB)
    
    def select_aud_tab(self):
        self.click(self.locators.AUD_TAB)
