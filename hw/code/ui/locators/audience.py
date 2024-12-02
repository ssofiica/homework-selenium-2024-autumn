from selenium.webdriver.common.by import By
from ui.locators.base import BasePageLocators

class AudienceLocators(BasePageLocators):
    CREATE_BUTTON = (By.XPATH, '//button[@data-testid="create-audience"]')

    