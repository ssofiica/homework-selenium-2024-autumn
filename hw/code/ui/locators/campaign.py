from selenium.webdriver.common.by import By
from ui.locators.base import BasePageLocators

class CampaignLocators(BasePageLocators):
    TAB_CAMPAIGN = (By.XPATH, '//*[@data-route="dashboardV2"]')
    CREATE_BUTTON = (By.XPATH, '//a[@data-testid="create-button"]')

    CREATE_MOBAPP = (By.XPATH, '//div[@data-id="mobapps"]') #создание кампании для приложения
    CREATE_SITE = (By.XPATH, '//div[@data-id="site_conversions"]') #создание кампании для сайта
    SITE_INPUT = (By.XPATH, '//input[@placeholder="Введите ссылку на сайт"]')

    SAVED_SOURCE_PARAMETRS= (By.XPATH, '//input[@data-testid="mob-app-select"]')
    ADD_APP = (By.XPATH, '//button[text()="Привязать новое приложение"]')
    APP_LINK_INPUT = (By.XPATH, '//input[@data-testid="app-link"]')
    ADD_APP_BUTTON = (By.XPATH, '//button[@data-testid="app-add"]')
    CLOSE_BUTTON = (By.XPATH, '//div[@aria-label="Закрыть"]') #вызвать два раза
    ADDED_APP = (By.XPATH, '//*[contains(text(), "orange (game)")]')
    BUDGET_INPUT = (By.XPATH, '//input[@data-testid="targeting-not-set"]')
    CONTINUE_BUTTON = (By.XPATH, '//*[contains(text(), "Продолжить")]')
    SMALL_BUDGET_ALERT = (By.XPATH, '//*[contains(text(), "Укажите бюджет не меньше 100₽")]')
    SAVE_DRAFT_BUTTON = (By.XPATH, '//*[contains(text(), "Сохранить как черновик")]')
    CHANGES_SAVED = (By.XPATH, '//div[contains(text(), "Изменения сохранены")]')
    REGION_INPUT = (By.XPATH, '//input[@data-testid="search"]')
    ROOT_BUTTON = (By.XPATH, '//button[@data-route="root"]')

    SELECT_CAMP_TYPE_BUTTON = (By.XPATH, '//button[@data-testid="tags-selector"]')
    ALL_CAMP = (By.XPATH, '//span[@data-testid="all"]')
    DRAFT_CAMP = (By.XPATH, '//span[@data-testid="drafts"]')


    DRAFT_ROW_BY_NAME = lambda self, text: (
        By.XPATH,
        f'//div[contains(@class, "BaseTable__row") and .//button[text()="{text}"]]',
    )
    DRAFT_CHECKBOX = (By.XPATH, './/label[input[starts-with(@id, "checkbox")]]')
    DELETE_BUTTON = (By.XPATH, '//button[@data-testid="delete-button"]')

    ACCEPT_DELETE = (By.XPATH, '//div[contains(@class, "vkuiModalPage")]//button[contains(., "Удалить")]')
    DRAFT = lambda self, text: (
        By.XPATH,
        f'//button[text()="{text}"]',
    )
