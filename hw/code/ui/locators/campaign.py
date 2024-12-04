from selenium.webdriver.common.by import By
from ui.locators.base import BasePageLocators

class CampaignLocators(BasePageLocators):
    CREATE_BUTTON = (By.XPATH, '//button[@data-testid="create-button"]')
    CREATE_MOBAPP = (By.XPATH, '//button[@data-id="mobapps"]')
    SAVED_SOURCE_PARAMETRS= (By.CLASS_NAME, 'Select_modalWrapper__ArYWw')
    ADD_APP = (By.XPATH, '//button[text()="Привязать новое приложение"]')
    APP_LINK_INPUT = (By.XPATH, '//input[@data-testid="app-link"]')
    ADD_APP_BUTTON = (By.XPATH, '//button[@data-testid="app-add"]')
    CLOSE_BUTTON = (By.XPATH, '//button[@aria-label="close_button"]') #вызвать два раза
    ADDED_APP = (By.XPATH, '//*[contains(text(), "orange (game)")]')
    BUDGET_INPUT = (By.XPATH, '//input[@data-testid="targeting-not-set"]')
    CONTINUE_BUTTON = (By.XPATH, '//button[text()="Продолжить"]')
    SMALL_BUDGET_ALERT = (By.XPATH, '//*[contains(text(), "Укажите бюджет не меньше 100₽")]')
    SAVE_DRAFT_BUTTON = (By.XPATH, '//button[text()="Сохранить как черновик"]')
    CHANGES_SAVED = (By.XPATH, '//*[contains(text(), "Изменения сохранены")]')
    REGION_INPUT = (By.XPATH, '//input[@data-testid="search"]')
    ROOT_BUTTON = (By.XPATH, '//button[@data-route="root"]')
