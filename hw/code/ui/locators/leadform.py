from selenium.webdriver.common.by import By
from ui.locators.base import BasePageLocators

class LeadformLocators(BasePageLocators):
    CREATE_LEADFORM_BUTTON = (By.XPATH, '//button[@test-id="create-leadform-button"]')
    NAME_INPUT = (By.XPATH, '//input[@placeholder="Название лид-формы"]')
    SUBBMIT_BUTTON = (By.XPATH, '//button[@data-testid="submit"]')
    REQUIRED_FIELD = (By.XPATH, '//*[contains(text(), "Обязательное поле")]')
    MORE_TEXT_BUTTON = (By.XPATH, "//span[text()='Больше текста']")
    LONG_DESCRIPTION = (By.XPATH, "//textarea[@placeholder='Расскажите о вашем предложении']")
