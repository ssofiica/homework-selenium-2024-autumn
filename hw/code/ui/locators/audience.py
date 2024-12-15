from selenium.webdriver.common.by import By
from ui.locators.base import BasePageLocators

class AudienceLocators(BasePageLocators):
    TAB_AUDIENCE = (By.XPATH, "//*[@data-route='audience']")
    CREATE_BUTTON = (By.XPATH, '//button[@data-testid="create-audience"]')
    CREATION_NAME_AUDITORY = (By.XPATH, '//*[@name="segmentName"]//input')
    ADD_SOURCE = (By.XPATH, '//*[contains(@class, "CreateSegmentModal")]//button')
    KEY_PHRASE_BUTTON = (By.XPATH, '//div[@role="button" and contains(., "Ключевые фразы")]')
    PERIOD_INPUT = (By.XPATH, '//input[@min="1"]')
    KEY_PHRASE_INPUT = (By.XPATH, '//textarea[@placeholder="Введите фразу и нажмите Enter"]')
    TEN_SAME_BUTTON = (By.XPATH, '//*[contains(text(), "Показать 10 похожих")]')
    KEY_SUGGEST = (By.CLASS_NAME, 'KeyPhrasesSuggesions_suggestionItem__zO7rL')
    SUBMUT_BUTTON = (By.XPATH, '//button[@data-testid="submit"]') 
    SAVED_SOURCE_PARAMETRS= (By.CLASS_NAME, 'InfoRow_content__LN5Bb')

    ROW_BY_NAME = lambda self, text: (
        By.XPATH,
        f'//div[@class="BaseTable__row" and contains(., "{text}")]',
    )
    CHECKBOX = (By.XPATH, './/label[input[@type="checkbox"]]')
    DELETE_BUTTON = (By.XPATH, '//button[@data-testid="remove-items-button"]')
    ACCEPT_DELETE = (By.XPATH, '//div[contains(@class, "vkuiModalPage")]//button[contains(., "Удалить")]')

    USERS_TAB = (By.XPATH, '//div[@id="tab_audience.users_list"]')
    AUD_TAB = (By.XPATH, '//div[@id="tab_audience"]')
    FIND_AUD_NAME = lambda self, text: (
        By.XPATH,
        f'//h5[text()="{text}"]',
    )