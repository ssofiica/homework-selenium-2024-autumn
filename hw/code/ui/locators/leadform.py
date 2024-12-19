from selenium.webdriver.common.by import By
from ui.locators.base import BasePageLocators

class LeadformLocators(BasePageLocators):
    TAB = (By.XPATH, '//*[@data-route="leadads"]')
    CREATE_LEADFORM_BUTTON = (By.XPATH, '//button[starts-with(@class, "LeadForms_createButton")]')
    SUBBMIT_BUTTON = (By.XPATH, '//button[@data-testid="submit"]')
    FIND_IN_FORM = lambda text: (
        By.XPATH,
        f'//div[starts-with(@class, "ModalSidebarPage_rightPlace")]//*[text()="{text}"]',
    )
    LEAD_ROW_BY_NAME = lambda text: (
        By.XPATH,
        f'//div[starts-with(@class, "ContextMenuWrapper_wrapper") and .//h5[text()="{text}"]]',
    )
    ARCHIVE_BUTTON = (By.XPATH, ".//span[text()='Архивировать']")
    TAB_OPROS = (By.XPATH, "//div[@data-testid='tabs-item']")
    TAB_LEAD = (By.XPATH, "//div[@data-testid='tabs-item']")


    # Раздел "Оформление"
    NAME_INPUT = (By.XPATH, '//input[@placeholder="Название лид-формы"]')
    REQUIRED_FIELD = (By.XPATH, '//*[contains(text(), "Обязательное поле")]')
    MORE_TEXT_BUTTON = (By.XPATH, "//span[text()='Больше текста']")
    LONG_DESCRIPTION = (By.XPATH, "//textarea[@placeholder='Расскажите о вашем предложении']")
    LID_MAGNIT_BUTTON = (By.XPATH, "//span[text()='Лид-магнит']")
    SALE_TYPE_PERCENT = (By.XPATH, "//label[input[@value='percent']]")

    UPLOAD_IMG_BUTTON = (By.XPATH, "//div[@data-testid='set-global-image']")
    LOGO = (By.XPATH, "//div[starts-with(@class, 'ImageItem_image')]")
    CROP_BOX = (By.CLASS_NAME, 'cropper-crop-box')
    APPLY_BUTTON = (By.XPATH, "//button[.//span[text()='Применить']]")
    SAVE_LOGO_BUTTON = (By.XPATH, "//button[.//span[text()='Сохранить']]")

    INPUT_COMPANY_NAME = (By.XPATH, "//input[@placeholder='Название компании']")
    INPUT_TITLE = (By.XPATH, "//input[@placeholder='Текст заголовка']")
    INPUT_DESCRIP = (By.XPATH, "//input[@placeholder='Введите описание']")

    # Раздел "Вопросы"
    ADD_QUEST_BUTTON = (By.XPATH, "//button[.//span[contains(text(), 'Добавить вопрос')]]")
    INPUT_QUEST= (By.XPATH, "//textarea[@placeholder='Напишите вопрос']")
    INPUT_ANSWER = (By.XPATH, "//input[@placeholder='Введите ответ']")
    DELETE_CONTACT_INFO_BUTTON = (By.XPATH, '//button[@aria-lebel="Delete"]')
    ADD_CONTACT_INFO_BUTTON = (By.XPATH, "//button[.//span[contains(text(), 'Добавить контактные данные')]]")
    EMAIL_CHECKBOX = (By.XPATH, '//label[input[@value="email"]]')
    ADD_BUTTON = (By.XPATH, "//button[contains(., 'Добавить')]")
    EMAIL_INPUT_IN_FORM = (By.XPATH, "//input[@placeholder='Введите email']")

    # Раздел "Результат"
    TITLE = (By.XPATH, "//div[h5[text()='Заголовок']]")
    ADD_SITE_BUTTON = (By.XPATH, '//div[@data-testid="add-site-btn"]')
    ADD_PHONE_BUTTON = (By.XPATH, '//div[@data-testid="add-phone-btn"]')
    INPUT_PHONE = (By.XPATH, "//input[@placeholder='+7......']")
    ADD_CODE_BUTTON = (By.XPATH, '//div[@data-testid="add-promo-code-btn"]')
    INPUT_CODE = (By.XPATH, "//input[@placeholder='Введите промокод']")
    FIND_CODE_IN_FORM = lambda text: (
        By.XPATH,
        f'//div[starts-with(@class, "ModalSidebarPage_rightPlace")]//input[@value="{text}"]',
    )

    # Раздел "Настройки"
    INPUT_UR_FACE = (By.XPATH, "//input[@placeholder='Введите название']")
    INPUT_UR_ADDRESS = (By.XPATH, "//input[@placeholder='Введите адрес']")
