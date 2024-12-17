import time
from ui.pages.base_page import BasePage
from ui.pages.consts import URLs
from ui.locators.leadform import LeadformLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LeadformPage(BasePage):
    url = URLs.leadform
    locators = LeadformLocators

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.click(self.locators.TAB, 10)

    def click_create_button(self):
        self.click(self.locators.CREATE_LEADFORM_BUTTON, 50)

    def empty_required_fields(self):
        self.fill(self.locators.NAME_INPUT, " ", 50)
        self.click(self.locators.SUBBMIT_BUTTON, 50)
        return self.find_elements(self.locators.REQUIRED_FIELD, 30)
    
    def enter_long_description_field(self, text):
        self.click(self.locators.MORE_TEXT_BUTTON, 50)
        self.fill(self.locators.LONG_DESCRIPTION, text, 50)

    def click_continue(self):
        self.click(self.locators.SUBBMIT_BUTTON, 50)

    def select_lid_magnit(self):
        self.click(self.locators.LID_MAGNIT_BUTTON, 50)

    def enter_sale_percent(self):
        self.click(self.locators.SALE_TYPE_PERCENT, 50)

    def upload_logo(self):
        self.click(self.locators.UPLOAD_IMG_BUTTON, 100)
        el = self.find_elements(self.locators.LOGO, 100)
        el[0].click()
        crop = self.find(self.locators.CROP_BOX, 100)
        # Перемещение элемента (например, на 50 пикселей вправо и 0 вниз)
        action = ActionChains(self.driver)
        action.click_and_hold(crop).move_by_offset(2, 0).release().perform()
        self.click(self.locators.APPLY_BUTTON, 100)
        self.click(self.locators.SAVE_LOGO_BUTTON, 100)

    def fill_company_name(self, text):
        self.fill(self.locators.INPUT_COMPANY_NAME, text, 5000)
    
    def fill_title(self, text):
        self.fill(self.locators.INPUT_TITLE, text, 100)

    def fill_description(self, text):
        self.fill(self.locators.INPUT_DESCRIP, text, 100)

    def fill_ur_face(self, text):
        self.fill(self.locators.INPUT_UR_FACE, text, 100)

    def fill_ur_address(self, text):
        self.fill(self.locators.INPUT_UR_ADDRESS, text, 100)

    def find_form(self, text):
        return self.find(self.locators.CONTAINS_ANY_TEXT(self, text), 1000)

    def add_question(self, text):
        self.click(self.locators.ADD_QUEST_BUTTON, 50)
        self.fill(self.locators.INPUT_QUEST, text, 100)

    def add_answers(self, a1, a2):
        inputs = self.find_elements(self.locators.INPUT_ANSWER, 100)
        inputs[0].clear()
        inputs[0].send_keys(a1)
        inputs[1].clear()
        inputs[1].send_keys(a2)

    def find_in_form(self, text):
        return self.find(self.locators.FIND_IN_FORM(text), 100)

    def delete_contact_info(self):
        btns = self.find_elements(self.locators.DELETE_CONTACT_INFO_BUTTON, 100)
        print(btns)
        for button in btns:
            button.click()

    def add_email(self):
        self.click(self.locators.ADD_CONTACT_INFO_BUTTON)
        self.click(self.locators.EMAIL_CHECKBOX)
        self.click(self.locators.ADD_BUTTON)

    def find_email_input(self):
        return self.find(self.locators.EMAIL_INPUT_IN_FORM, 100)

    def add_phone(self, phone):
        self.click(self.locators.ADD_PHONE_BUTTON, 100)
        self.fill(self.locators.INPUT_PHONE, phone, 100)

    def add_code(self, code):
        self.click(self.locators.ADD_CODE_BUTTON, 100)
        self.fill(self.locators.INPUT_CODE, code, 100)

    def find_code_in_form(self, code):
        return self.find(self.locators.FIND_CODE_IN_FORM(code), 100)

    def fill_title_result(self, text):
        div = self.find(self.locators.TITLE)
        input = div.find_element(By.XPATH, ".//input")
        input.clear()
        input.send_keys(text)

    def find_empty_required_fields(self):
        return self.find_elements(self.locators.REQUIRED_FIELD, 30)
    
    def archive_lead(self, name):
        div = self.find(self.locators.LEAD_ROW_BY_NAME(name), 1000)
        actions = ActionChains(self.driver)
        actions.move_to_element(div).perform()
        button = div.find_element(By.XPATH, ".//span[text()='Архивировать']")
        button.click()
        
    def switch_to_opros(self):
        self.click(self.locators.TAB_OPROS, 100)

    def switch_to_lead(self):
        self.click(self.locators.TAB_LEAD, 100)