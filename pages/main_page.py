from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    """Главная страница selectel.ru"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = "https://selectel.ru"
    
    def open(self):
        """Открыть главную страницу"""
        self.driver.get(self.url)
    
    def click_login_button(self):
        """Нажать на кнопку 'Войти'"""
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Войти"))
        )
        login_button.click()
    
    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url
