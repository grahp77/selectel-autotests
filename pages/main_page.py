from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPage(BasePage):
    """Page Object для главной страницы selectel.ru"""
    
    TITLE = (By.TAG_NAME, "title")
    LOGO = (By.CSS_SELECTOR, ".Logo_logo__u7oWZ")
    MENU_ITEMS = (By.CSS_SELECTOR, ".Header_navItem__UQn3b")
    CONTACT_PHONE = (By.CSS_SELECTOR, ".Header_phone__DfWkO")
    LOGIN_BUTTON = (By.LINK_TEXT, "Войти")
    REGISTRATION_BUTTON = (By.LINK_TEXT, "Регистрация")
    SEARCH_ICON = (By.CSS_SELECTOR, ".Header_searchIcon__L6PmZ")
    FOOTER_LINKS = (By.CSS_SELECTOR, ".Footer_footer__yJjgF a")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://selectel.ru"
    
    def open_main_page(self):
        """Открыть главную страницу"""
        self.open(self.url)
    
    def get_page_title(self) -> str:
        """Получить заголовок страницы"""
        return self.get_title()
    
    def is_logo_displayed(self) -> bool:
        """Проверить отображение логотипа"""
        return self.find_element(self.LOGO).is_displayed()
    
    def get_menu_items_count(self) -> int:
        """Получить количество пунктов меню"""
        return len(self.driver.find_elements(*self.MENU_ITEMS))
    
    def click_login_button(self):
        """Кликнуть на кнопку 'Войти'"""
        self.click(self.LOGIN_BUTTON)
    
    def click_registration_button(self):
        """Кликнуть на кнопку 'Регистрация'"""
        self.click(self.REGISTRATION_BUTTON)
    
    def get_footer_links_count(self) -> int:
        """Получить количество ссылок в футере"""
        return len(self.driver.find_elements(*self.FOOTER_LINKS))