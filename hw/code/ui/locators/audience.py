from selenium.webdriver.common.by import By
from ui.locators.base import BasePageLocators

class AudienceLocators(BasePageLocators):
    CREATE_BUTTON = (By.XPATH, '//button[@data-testid="create-audience"]')
    CREATION_NAME_AUDITORY = (By.XPATH, '//*[@name="segmentName"]//input')
    ADD_SOURCE = (By.XPATH, '//*[contains(@class, "CreateSegmentModal")]//button')
    KEY_PHRASE_BUTTON = (By.XPATH, '//*[contains(text(), "Ключевые фразы")]')
    PERIOD_INPUT = (By.XPATH, '//input[@min="1"]')
    KEY_PHRASE_INPUT = (By.XPATH, '//textarea[@placeholder="Введите фразу и нажмите Enter"]')
    TEN_SAME_BUTTON = (By.XPATH, '//*[contains(text(), "Показать 10 похожих")]')
    KEY_SUGGEST = (By.CLASS_NAME, 'KeyPhrasesSuggesions_suggestionItem__zO7rL')
    SUBMUT_BUTTON = (By.XPATH, '//button[@data-testid="submit"]') 
    SAVED_SOURCE_PARAMETRS= (By.CLASS_NAME, 'InfoRow_content__LN5Bb')

    