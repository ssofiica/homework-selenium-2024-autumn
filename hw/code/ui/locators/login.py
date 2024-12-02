from selenium.webdriver.common.by import By
from ui.locators.base import BasePageLocators

class LoginLocators(BasePageLocators):
    MAIL_OAUTH_BUTTON = (By.XPATH, '//button[@data-test-id="oAuthService_mail_ru"]')
    MAIL_LOGIN_INPUT = (By.NAME, 'username') 
    NEXT_BUTTON = (By.XPATH, '//button[@data-test-id="next-button"]')
    OTHER_WAY = (By.XPATH, '//a[@data-test-id="auth-problems"]')
    PASSWORD_WAY = (By.XPATH, '//li[@data-test-id="auth-by-password"]//a[text()="Использовать пароль для входа"]')
    MAIL_PASSWORD_INPUT = (By.NAME, 'password')
    SUBMUT_BUTTON = (By.XPATH, '//button[@data-test-id="submit-button"]') 
    CAPTCHA_BUTTON = (By.XPATH, '//button[@data-test-id="recaptcha-inter-next"]')
    CAPTCHA_CLICK = (By.ID, 'recaptcha-anchor')