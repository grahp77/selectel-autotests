from selenium.webdriver.common.by import By
from .base_page import BasePage

class RegistrationPage(BasePage):
    """Page Object для страницы регистрации"""
    
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    GENERATE_PASSWORD_BUTTON = (By.XPATH, "//button[contains(text(),'Сгенерировать')]")
    NEWSLETTER_CHECKBOX = (By.XPATH, "//label[contains(text(),'новостных рассылок')]/input")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Создать аккаунт')]")
    SUPPORT_LINK = (By.LINK_TEXT, "support@selectel.ru")
    LOGIN_LINK = (By.LINK_TEXT, "Войти")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://my.selectel.ru/registration"
    
    def open_registration_page(self):
        """Открыть страницу регистрации"""
        self.open(self.url)
    
    def enter_email(self, email: str):
        """Ввести email"""
        self.send_keys(self.EMAIL_FIELD, email)
    
    def enter_password(self, password: str):
        """Ввести пароль"""
        self.send_keys(self.PASSWORD_FIELD, password)
    
    def click_generate_password(self):
        """Нажать кнопку генерации пароля"""
        self.click(self.GENERATE_PASSWORD_BUTTON)
    
    def toggle_newsletter_checkbox(self):
        """Переключить чекбокс рассылки"""
        self.click(self.NEWSLETTER_CHECKBOX)
    
    def click_create_account(self):
        """Нажать кнопку создания аккаунта"""
        self.click(self.CREATE_ACCOUNT_BUTTON)
    
    def click_support_link(self):
        """Кликнуть на ссылку поддержки"""
        self.click(self.SUPPORT_LINK)
    
    def is_error_message_displayed(self) -> bool:
        """Проверить наличие сообщения об ошибке"""
        try:
            return self.find_element(self.ERROR_MESSAGE).is_displayed()
        except:
            return False
    
    def get_current_url(self) -> str:
        """Получить текущий URL"""
        return self.driver.current_url