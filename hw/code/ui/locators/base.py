from selenium.webdriver.common.by import By

class BasePageLocators:
    CONTAINS_ANY_TEXT = lambda self, text: (
        By.XPATH,
        f"//*[contains(text(), '{text}')]",
    )